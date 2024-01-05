"""
connect_debugger(): Établit une connexion avec l'interface de débogage.
send_debug_command(command): Envoie une commande de débogage.
get_debug_data(): Récupère les données de débogage depuis le bootloader.
disconnect_debugger(): Déconnecte l'interface de débogage.
"""

import can
import isotp
from can_interface import CANInterface
from isotp_stack import IsoTpStack


class DebuggerInterface:
    def __init__(self, can_bus_type, can_channel, can_bitrate, tx_id, rx_id):
        """
        Initialise l'interface de débogage.

        Args:
            can_bus_type (str): Type de bus CAN (ex. 'PCAN' ou 'SocketCAN').
            can_channel (str): Canal du bus CAN à utiliser.
            can_bitrate (int): Taux de transmission pour le bus CAN.
            tx_id (int): Identifiant CAN pour les messages transmis (débogage).
            rx_id (int): Identifiant CAN pour les messages reçus (débogage).
        """
        self.can_interface = CANInterface(can_bus_type, can_channel, can_bitrate)
        self.isotp_stack = IsoTpStack(self.can_interface)
        self.isotp_stack.setup_isotp(tx_id, rx_id)

    def connect_debugger(self):
        """
        Établit une connexion avec l'interface de débogage.
        """
        print("Connexion avec l'interface de débogage établie.")

    def send_debug_command(self, command):
        """
        Envoie une commande de débogage.

        Args:
            command (bytes): Commande de débogage à envoyer.
        """
        self.isotp_stack.send_isotp_message(command)
        print("Commande de débogage envoyée.")

    def get_debug_data(self):
        """
        Récupère les données de débogage depuis le dispositif.

        Returns:
            bytes: Données de débogage reçues.
        """
        data = self.isotp_stack.receive_isotp_message()
        if data:
            print("Données de débogage reçues.")
        else:
            print("Aucune donnée de débogage disponible.")
        return data

    def disconnect_debugger(self):
        """
        Déconnecte l'interface de débogage.
        """
        self.can_interface.shutdown()
        print("Interface de débogage déconnectée.")


# Exemple d'utilisation
if __name__ == "__main__":
    debugger = DebuggerInterface("PCAN", "PCAN_USBBUS1", 500000, 0x123, 0x456)
    debugger.connect_debugger()
    debugger.send_debug_command(b"CheckStatus")
    debug_data = debugger.get_debug_data()
    if debug_data:
        print(f"Debug Data: {debug_data}")
    debugger.disconnect_debugger()
