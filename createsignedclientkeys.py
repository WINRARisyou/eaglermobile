from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate a 2048-bit private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Extract the modulus and private exponent (secret)
private_numbers = private_key.private_numbers()
modulus = private_numbers.public_numbers.n
private_exponent = private_numbers.d

# Print the modulus and secret in decimal format
print("Modulus:", modulus)
print("Secret:", private_exponent)

# Now you can create your own Signed Eaglercraft Client (it'll show up as unsigned in game, but you can make custom client bundles this way)