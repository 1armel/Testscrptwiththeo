import pytest
import calculator.operation 
from enum import Enum
import CANImplementation.TSCAN
import can

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





 # Créez une instance de Bus pour l'interface 'pcan'
bus = can.interface.Bus(bustype = eBusType.PCAN.value, channel= Channel.PCAN_USBBUS1.value, bitrate= BitRate.BPS_250K.value)


arbitration_id = CANImplementation.TSCAN.generate_arbitration_id(source_address=0x55, target_address=0xAA, comm_type = CANImplementation.TSCAN.Comtype.ONE_TO_ONE)
CANImplementation.TSCAN.send_can_message(bus,arbitration_id, [0, 25, 0, 1, 3, 1, 4, 10])



