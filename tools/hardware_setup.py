#!/usr/bin/env python
# hardware_setup.py
# Script de configuration du matériel pour les tests du bootloader IDS CAN

import can
import PyLink
import sys
from enum import Enum


class eBusType(Enum):
    """
    Enum for different bus types.
    """
    PCAN      = 'pcan'
    SOCKETCAN = 'socketcan'
    SERIAL    = 'serial'

   

class Channel(Enum):
    """
    Enum for different channels on the Vector Bus Type devices.
    """
    PCAN_USBBUS1    = 'PCAN_USBBUS1'
    PCAN_USBBUS2    = 'PCAN_USBBUS2'
    PCAN_USBPROBUS1 = 'PCAN_USBPROBUS'



class BitRate(Enum):
    """
    Enum for different bit rates.
    """
    BPS_100K = 100000
    BPS_150K = 150000
    BPS_200K = 200000
    BPS_250K = 250000
    BPS_300K = 300000
    BPS_350K = 350000
    BPS_400K = 400000
    BPS_450K = 450000
    BPS_500K = 500000




def initialize_can_interface(channel, bustype):
    """
    Initialise et configure l'interface CAN.
    """
    try:
        can_interface = can.interface.Bus(channel=channel, bustype=bustype)
        print(f"Interface CAN initialisée sur le canal {channel} avec le type de bus {bustype}.")
        return can_interface
    except Exception as e:
        print(f"Erreur lors de l'initialisation de l'interface CAN : {e}")
        return None

def connect_to_actuator(target_id):
    """
    Connecte le debugger/programmeur à l'actionneur cible.
    """
    try:
        debugger = PyLink.JLink()
        debugger.open()
        if not debugger.connected():
            debugger.connect(target_id)
        print(f"Connecté à l'actionneur {target_id} via le débogueur.")
        return debugger
    except Exception as e:
        print(f"Erreur lors de la connexion au débogueur : {e}")
        return None

def setup_hardware(channel, bustype, target_id):
    """
    Effectue la configuration globale du matériel nécessaire pour les tests.
    """
    can_interface = initialize_can_interface(channel, bustype)
    if not can_interface:
        print("Impossible de poursuivre sans une interface CAN fonctionnelle.")
        return False

    debugger = connect_to_actuator(target_id)
    if not debugger:
        print("Impossible de poursuivre sans une connexion débogueur fonctionnelle.")
        return False

    return True

if __name__ == "__main__":
    # Extraction des paramètres à partir des arguments de ligne de commande
    if len(sys.argv) != 4:
        print("Usage: python hardware_setup.py <channel> <bustype> <target_id>")
        sys.exit(1)

    channel = sys.argv[1]
    bustype = sys.argv[2]
    target_id = sys.argv[3]

    if setup_hardware(channel, bustype, target_id):
        print("Configuration du matériel réussie.")
    else:
        print("Échec de la configuration du matériel.")
