#!/usr/bin/env python

"""
This module tests :class:`can.MessageSync`.
"""

import can.bus 
import CANImplementation.TSCAN
import pytest

def test_crc16_calculate():
    """
    Tests the :func:`can.bus.crc16_calculate` function.
    """

    # Given: A string of data
    input_data = [ord(c) for c in "123456789"] 

    # And: The expected CRC value for this data
    expected_crc = 0x31C3  

    # When: Calculating the CRC for the given data
    calculated_crc = CANImplementation.TSCAN.crc16_calculate(input_data)

    # Then: The calculated CRC should match the expected CRC
    assert calculated_crc == expected_crc, f"Le CRC calculé ({calculated_crc}) ne correspond pas au résultat attendu ({expected_crc})"


def test_generate_arbitration_id():
    # Test case for 1-to-1 communication
    arbitration_id = CANImplementation.TSCAN.generate_arbitration_id(source_address=0x55, target_address=0xAA, comm_type=CANImplementation.TSCAN.Comtype.ONE_TO_ONE)
    assert arbitration_id == '18DAaa55', f"Expected '18daaa55', but got {arbitration_id}"

    # Test case for 1-to-n communication
    arbitration_id = CANImplementation.TSCAN.generate_arbitration_id(source_address=0x55, target_address=0xAA, comm_type=CANImplementation.TSCAN.Comtype.ONE_TO_N)
    assert arbitration_id == '18DBaa55', f"Expected '18dbaa55', but got {arbitration_id}"

    # Test case for invalid communication type
    arbitration_id = CANImplementation.TSCAN.generate_arbitration_id(source_address=0x55, target_address=0xAA, comm_type='INVALID')
    assert arbitration_id is None, f"Expected None, but got {arbitration_id}"

    print("All test cases passed")


if __name__ == "__main__":
    pytest.main()