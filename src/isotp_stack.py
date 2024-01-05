"""
setup_isotp(): Configure la pile ISOTP.
send_isotp_message(message): Envoie un message en utilisant le protocole ISOTP.
receive_isotp_message(): Réceptionne un message ISOTP.
isotp_error_handler(error): Gère les erreurs liées à ISOTP.

classe qui gère la pile ISOTP (ISO-TP, ISO 15765-2) pour la transmission de données sur le réseau CAN. ISO-TP permet de transmettre des messages plus longs que les 8 octets maximum autorisés par le standard CAN
"""
import can
import isotp


class IsoTpStack:
    def __init__(self, can_interface):
        """
        Configure la pile ISOTP en utilisant une interface CAN existante.

        Args:
            can_interface (can.interface.Bus): Interface CAN initialisée.
        """
        self.can_interface = can_interface
        self.isotp_stack = isotp.CanStack(self.can_interface)

    def setup_isotp(self, tx_id, rx_id):
        """
        Configure les identifiants d'émission et de réception pour la pile ISOTP.

        Args:
            tx_id (int): Identifiant CAN pour les messages transmis.
            rx_id (int): Identifiant CAN pour les messages reçus.
        """
        self.isotp_stack.set_general_options(
            txid=tx_id,
            rxid=rx_id,
            stmin=5,  # Temps minimal de séparation entre les frames, en ms
            blocksize=8,  # Nombre maximal de frames avant l'acquittement
        )
        print("Configuration ISOTP terminée.")

    def send_isotp_message(self, message):
        """
        Envoie un message en utilisant la pile ISOTP.

        Args:
            message (bytes): Message à envoyer.
        """
        self.isotp_stack.send(message)
        print("Message ISOTP envoyé.")

    def receive_isotp_message(self):
        """
        Réceptionne un message ISOTP.

        Returns:
            bytes: Message reçu ou None si aucun message.
        """
        if self.isotp_stack.available():
            message = self.isotp_stack.recv()
            print("Message ISOTP reçu.")
            return message
        else:
            print("Aucun message ISOTP disponible.")
            return None


# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une interface CAN (assurez-vous d'avoir configuré correctement)
    can_interface = can.interface.Bus(
        bustype="PCAN", channel="PCAN_USBBUS1", bitrate=500000
    )

    # Créer et configurer la pile ISOTP
    isotp_stack = IsoTpStack(can_interface)
    isotp_stack.setup_isotp(tx_id=0x123, rx_id=0x456)

    # Envoyer et recevoir un message ISOTP
    isotp_stack.send_isotp_message(b"Hello ISOTP")
    received_message = isotp_stack.receive_isotp_message()
    if received_message:
        print(f"Reçu: {received_message}")

    # Fermer l'interface CAN
    can_interface.shutdown()
