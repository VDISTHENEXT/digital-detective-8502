def main():
    print("=== Decimal to Binary and Hexadecimal Converter ===")
    user_input = input("Enter a positive decimal number: ")
    decimal_number = int(user_input)
    
    binary_result = bin(decimal_number)
    hex_result = hex(decimal_number)
    
    print(f"Decimal value:     {decimal_number}")
    print(f"Binary value:      {binary_result}")
    print(f"Hexadecimal value: {hex_result}")

if __name__ == "__main__":
    main()
