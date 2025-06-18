from PIL import Image

def encrypt_decrypt_image(input_path, output_path, key):
    # Open image
    img = Image.open(input_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    # Manipulate each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # XOR each channel with the key
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save the image
    img.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    key = 123  # Secret key (0–255)
    
    # Encrypt
    encrypt_decrypt_image("input_image.jpg", "encrypted_image.jpg", key)
    
    # Decrypt (run again with same key)
    encrypt_decrypt_image("encrypted_image.jpg", "decrypted_image.jpg", key)
