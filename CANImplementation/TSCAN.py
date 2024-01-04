"""
Containts all the functions relate to the CAN BUS 
"""
from enum import Enum
import can










# ***********************************************************************************************************
# *	                          ENUM
# ************************************************************************************************************
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

class Comtype(Enum):
    ONE_TO_ONE = "ONE_TO_ONE"
    ONE_TO_N   = "ONE_TO_N"



# ***********************************************************************************************************
# *	                               Functions
# ************************************************************************************************************
def crc16_calculate(p_src):
    """
    Function to calculate the 16-bit CRC (Cyclic Redundancy Check) for the input bytes.

    Parameters:
        p_src (bytes): The bytes for which the CRC is to be calculated.

    Returns:
        int: The 16-bit CRC.
    """
    # Initialize CRC to 0
    crc = 0

    # Iterate over each byte in the data sourc
    for byte_value in p_src:

        # Perform XOR between the current CRC and the data byte shifted 8 bits to the left
        crc ^= byte_value << 8

        # Repeat the following operation 8 times
        for _ in range(8):

            # Shift the CRC one bit to the left
            temp = crc << 1

            # If the most significant bit of the CRC is 1
            if crc & 0x8000:

                # Perform XOR between temp and the polynomial
                temp ^= 0x1021

            # Update the CRC with the value of temp, keeping only the least significant 16 bits    
            crc = temp & 0xFFFF

    # Return the computed CRC        
    return crc


def send_can_message(bus:can.bus,arbitration_id, data):
   
    arbitration_id = int(arbitration_id, 16)

    # Créez un message CAN
    msg = can.Message(arbitration_id = arbitration_id,
                      data=data,
                      is_extended_id=True)

    # Envoyez le message
    try:
        bus.send(msg)
        print("Message envoyé")
    except can.CanError:
        print("Erreur lors de l'envoi du message")
    bus.shutdown()    




def generate_arbitration_id(source_address, target_address, comm_type: Comtype):


    # Convert addresses to hexadecimal
    source_address_hex = format(source_address, '02x')
    target_address_hex = format(target_address, '02x')

    # Build the arbitration ID based on the communication type
    if comm_type == Comtype.ONE_TO_ONE:
        arbitration_id = "18DA" + target_address_hex + source_address_hex
    elif comm_type == Comtype.ONE_TO_N:
        arbitration_id = "18DB" + target_address_hex + source_address_hex
    else:
        return None  # Return None if the communication type is not recognized

    return arbitration_id


def Hosthello_BootloaderHello