"""
initialize_can_interface(): Initialise l'interface CAN avec les paramètres requis.
send_can_message(message): Envoie un message via le bus CAN.
receive_can_message(): Réceptionne un message du bus CAN.
can_error_handling(error): Gère les erreurs spécifiques à l'interface CAN.
"""

import can


class CANInterface:
    def __init__(self, bus_type, channel, bitrate):
        """
        Initialise l'interface CAN.

        Args:
            bus_type (str): Type du bus CAN (ex. 'PCAN' ou 'SocketCAN').
            channel (str): Canal du bus CAN à utiliser.
            bitrate (int): Taux de transmission pour le bus CAN.
        """
        self.bus = can.interface.Bus(bustype=bus_type, channel=channel, bitrate=bitrate)
        print("Interface CAN initialisée.")

    def send_message(self, arbitration_id, data, is_extended_id=False):
        """
        Envoie un message via le bus CAN.

        Args:
            arbitration_id (int): Identifiant d'arbitrage du message CAN.
            data (list[int]): Données à envoyer.
            is_extended_id (bool): Indique si l'identifiant d'arbitrage est étendu.
        """
        message = can.Message(
            arbitration_id=arbitration_id, data=data, is_extended_id=is_extended_id
        )
        try:
            self.bus.send(message)
            print("Message envoyé sur le bus CAN.")
        except can.CanError as e:
            print(f"Erreur lors de l'envoi du message : {e}")

    def receive_message(self, timeout=None):
        """
        Réceptionne un message du bus CAN.

        Args:
            timeout (float): Temps d'attente maximal en secondes pour recevoir un message.

        Returns:
            can.Message: Le message CAN reçu, ou None si aucun message n'est reçu.
        """
        try:
            message = self.bus.recv(timeout)
            if message:
                print("Message reçu du bus CAN.")
                return message
            else:
                print("Aucun message reçu dans le délai imparti.")
                return None
        except can.CanError as e:
            print(f"Erreur lors de la réception du message : {e}")
            return None

    def shutdown(self):
        """
        Ferme l'interface CAN.
        """
        self.bus.shutdown()
        print("Interface CAN fermée.")


# Exemple d'utilisation
if __name__ == "__main__":
    can_interface = CANInterface("PCAN", "PCAN_USBBUS1", 250000)
    can_interface.send_message(0x123, [0x11, 0x22, 0x33])
    message = can_interface.receive_message(5)  # Attendre 5 secondes
    if message:
        print(f"Message reçu : {message}")
    can_interface.shutdown()
