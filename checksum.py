class ChecksumCalculator:
    @staticmethod
    def decimal_to_binary(decimal, bits):
        return format(decimal, '0{}b'.format(bits))
    @staticmethod
    def binary_to_decimal(binary):
        return int(binary, 2)
    @staticmethod
    def wrap_up_to_8_bits(value):
        wrapped_value = (value & 0xFF) + (value >> 8)
        return wrapped_value & 0xFF
    @staticmethod
    def calculate_checksum(data):
        total_sum = sum(data)
        print(f"Sum of the data packet: {total_sum}")
        binary_sum = ChecksumCalculator.decimal_to_binary(total_sum, 16)
        print(f"Binary representation of the sum: {binary_sum}")
        wrapped_sum = ChecksumCalculator.wrap_up_to_8_bits(total_sum)
        print(f"Wrapped up 8-bit sum: {ChecksumCalculator.decimal_to_binary(wrapped_sum, 8)}")
        checksum = (~wrapped_sum) & 0xFF
        print(f"Complemented checksum (8 bits): {ChecksumCalculator.decimal_to_binary(checksum, 8)}")
        return checksum
    @staticmethod
    def verify_checksum(data_with_checksum):
        total_sum = sum(data_with_checksum)
        print(f"\nReceiver's total sum: {total_sum}")
        binary_sum = ChecksumCalculator.decimal_to_binary(total_sum, 16)
        print(f"Binary representation of the receiver's sum: {binary_sum}")
        wrapped_sum = ChecksumCalculator.wrap_up_to_8_bits(total_sum)
        print(f"Receiver's wrapped up 8-bit sum: {ChecksumCalculator.decimal_to_binary(wrapped_sum, 8)}")
        final_complement = (~wrapped_sum) & 0xFF
        print(f"Final complement at receiver's end: {ChecksumCalculator.decimal_to_binary(final_complement, 8)}")
        return final_complement == 0
if __name__ == '__main__':
    data = [93, 21, 88, 92, 61]
    print("Original Data Packet: ")
    print(" ".join(map(str, data)))
    checksum = ChecksumCalculator.calculate_checksum(data)
    transmitted_data = data + [checksum]
    print("\nTransmitted Data Packet: ")
    print(" ".join(map(str, transmitted_data)))
    is_valid = ChecksumCalculator.verify_checksum(transmitted_data)
    print("\nIs the received data valid?")
    if is_valid:
        print("Yes\nThere is no Error")
    else:
        print("No\nError Found in data")