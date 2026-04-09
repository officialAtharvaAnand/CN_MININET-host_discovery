# Host Discovery Service - SDN Project
# Name: Atharva Anand | SRN: PES1UG24CS092

from pox.core import core
from pox.lib.util import dpid_to_str
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, arp, ipv4
import time, datetime

log = core.getLogger()

class HostDiscovery(object):
    def __init__(self, connection):
        self.connection = connection
        self.host_db = {}      # mac -> info
        self.mac_to_port = {}  # mac -> port
        connection.addListeners(self)
        log.info("Switch %s connected", dpid_to_str(connection.dpid))

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if not packet.parsed:
            return

        src_mac = str(packet.src)
        dst_mac = str(packet.dst)
        in_port = event.port
        now = time.time()

        # Learn MAC → port
        self.mac_to_port[src_mac] = in_port

        # Extract IP
        src_ip = None
        arp_pkt = packet.find('arp')
        ip_pkt  = packet.find('ipv4')

        if arp_pkt:
            src_ip = str(arp_pkt.protosrc)
        elif ip_pkt:
            src_ip = str(ip_pkt.srcip)

        # -----------------------------
        # HOST DISCOVERY LOGIC
        # -----------------------------
        is_new = src_mac not in self.host_db

        if is_new:
            self.host_db[src_mac] = {
                'ip': src_ip or 'unknown',
                'port': in_port,
                'first_seen': now,
                'last_seen': now,
                'count': 1
            }

            log.info("")
            log.info("*** [NEW HOST DETECTED] ***")
            log.info(" MAC  : %s", src_mac)
            log.info(" IP   : %s", src_ip or 'unknown')
            log.info(" Port : %s", in_port)
            log.info(" Time : %s",
                datetime.datetime.fromtimestamp(now).strftime('%H:%M:%S'))

            self.print_table()

        else:
            e = self.host_db[src_mac]
            e['last_seen'] = now
            e['count'] += 1

            if src_ip and e['ip'] == 'unknown':
                e['ip'] = src_ip

        # -----------------------------
        # FLOW RULE INSTALLATION (FIXED)
        # -----------------------------
        if dst_mac in self.mac_to_port:
            out_port = self.mac_to_port[dst_mac]

            # INSTALL FLOW RULE
            fm = of.ofp_flow_mod()
            fm.match.in_port = in_port
            fm.match.dl_dst = packet.dst
            fm.idle_timeout = 10
            fm.hard_timeout = 30
            fm.priority = 1
            fm.actions.append(of.ofp_action_output(port=out_port))

            self.connection.send(fm)

            # ALSO SEND CURRENT PACKET
            po = of.ofp_packet_out()
            po.data = event.ofp
            po.actions.append(of.ofp_action_output(port=out_port))
            po.in_port = in_port
            self.connection.send(po)

        else:
            # FLOOD
            po = of.ofp_packet_out()
            po.data = event.ofp
            po.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
            po.in_port = in_port
            self.connection.send(po)

    def print_table(self):
        log.info("  +------------------+---------------+------+-------+")
        log.info("  | MAC              | IP            | Port | Pkts  |")
        log.info("  +------------------+---------------+------+-------+")

        for mac, i in self.host_db.items():
            log.info("  | %-16s | %-13s | %-4s | %-5s |",
                     mac[-17:], i['ip'], i['port'], i['count'])

        log.info("  +------------------+---------------+------+-------+")
        log.info("  Total hosts discovered: %d", len(self.host_db))


class HostDiscoveryLauncher(object):
    def __init__(self):
        log.info("=" * 50)
        log.info(" Host Discovery Service - POX Controller")
        log.info(" Atharva Anand | PES1UG24CS092")
        log.info("=" * 50)

        core.openflow.addListenerByName(
            "ConnectionUp", self._handle_ConnectionUp)

    def _handle_ConnectionUp(self, event):
        HostDiscovery(event.connection)


def launch():
    core.registerNew(HostDiscoveryLauncher)
