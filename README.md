# 🔐 Image Encryption Using Pixel Manipulation

This is a simple image encryption and decryption tool built using Python. It manipulates the RGB pixel values of an image using a basic XOR operation with a secret key. The encrypted image becomes unreadable to humans, and the original can be recovered using the same key.

## 📌 Features

- Encrypts images by scrambling pixel values
- Decrypts back to the original image using the same key
- Lightweight and beginner-friendly Python code
- Uses the `Pillow` library for image processing

---

## 🛠️ Technologies Used

- Python 3.x
- [Pillow](https://python-pillow.org/) (Python Imaging Library fork)

---

## 🔧 How It Works

Each image pixel is made of RGB values. The program applies a simple XOR operation on each pixel with a secret key like this:

```python
encrypted_pixel = (R ^ key, G ^ key, B ^ key)
To decrypt, the same XOR is applied again:
```
python
Copy code
decrypted_pixel = (encrypted_R ^ key, encrypted_G ^ key, encrypted_B ^ key)

How to Run
Install Pillow if not already installed:

bash
Copy code
pip install Pillow
Save the script as img_encryp.py

Place your input image (e.g., photo.jpg) in the same folder

Run the script:

bash
Copy code
```
python img_encryp.py
```
Edit the script to use your file name:

python
Copy code
encrypt_decrypt_image("photo.jpg", "encrypted_image.jpg", key)
encrypt_decrypt_image("encrypted_image.jpg", "decrypted_image.jpg", key)
