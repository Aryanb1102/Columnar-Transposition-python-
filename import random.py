import random
import string

def generate_random_key(length):
    # Generate a random key of the given length
    letters = string.ascii_uppercase
    key = ''.join(random.choice(letters) for _ in range(length))
    return key

def get_numeric_key(key):
    # Assign numerical values to key letters based on their order in the sorted key
    key_upper = key.upper()
    key_indices = list(range(len(key_upper)))
    key_chars_with_indices = list(zip(key_upper, key_indices))
    # Sort the key letters alphabetically, maintaining original indices for duplicates
    sorted_key = sorted(key_chars_with_indices)
    numeric_assignments = {}
    num = 1
    for char, original_idx in sorted_key:
        numeric_assignments[original_idx] = num
        num += 1
    # Build the numeric key based on original positions
    numeric_key = [numeric_assignments[idx] for idx in key_indices]
    return numeric_key

def encrypt(plaintext, key):
    key_length = len(key)
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    num_rows = -(-len(plaintext) // key_length)  # Ceiling division
    # Fill the grid with characters
    grid = ['' for _ in range(key_length * num_rows)]
    for idx, char in enumerate(plaintext):
        grid[idx] = char
    # Convert the grid into rows
    rows = [grid[i:i+key_length] for i in range(0, len(grid), key_length)]
    # Get numeric key for column ordering
    numeric_key = get_numeric_key(key)
    # Determine the order to read columns
    col_order = sorted(range(len(numeric_key)), key=lambda k: numeric_key[k])
    # Create ciphertext by reading columns in order
    ciphertext = ''
    for col_idx in col_order:
        for row in rows:
            if col_idx < len(row) and row[col_idx]:
                ciphertext += row[col_idx]
    return ciphertext

def decrypt(ciphertext, key):
    key_length = len(key)
    num_rows = -(-len(ciphertext) // key_length)  # Ceiling division
    # Get numeric key for column ordering
    numeric_key = get_numeric_key(key)
    col_order = sorted(range(len(numeric_key)), key=lambda k: numeric_key[k])
    # Calculate the number of filled cells in each column
    num_full_cols = len(ciphertext) % key_length
    col_lengths = [num_rows] * key_length
    if num_full_cols != 0:
        for i in range(key_length - num_full_cols):
            col_lengths[col_order[-(i+1)]] -= 1
    # Build the columns
    cols = {}
    index = 0
    for col_idx in col_order:
        col_length = col_lengths[col_idx]
        cols[col_idx] = ciphertext[index:index+col_length]
        index += col_length
    # Reconstruct the plaintext from the columns
    plaintext = ''
    for row_idx in range(num_rows):
        for col_idx in range(key_length):
            col = cols.get(col_idx, '')
            if row_idx < len(col):
                plaintext += col[row_idx]
    return plaintext

def main():
    choice = input("Do you want to input the key? (y/n): ")
    if choice.lower() == 'y':
        key = input("Enter the key: ").replace(" ", "").upper()
    else:
        key_length = int(input("Enter the key length: "))
        key = generate_random_key(key_length)
        print(f"Generated key: {key}")

    plaintext = input("Enter the plaintext: ")
    ciphertext = encrypt(plaintext, key)
    print(f"\nEncrypted Ciphertext:\n{ciphertext}")

    decrypted_text = decrypt(ciphertext, key)
    print(f"\nDecrypted Plaintext:\n{decrypted_text}")

if __name__ == "__main__":
    main()
