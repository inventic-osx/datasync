import os

def generate_random_bytes_512():
  return os.urandom(512)  # Generate 512 random bytes using os.urandom

random_bytes = generate_random_bytes_512()
print(random_bytes)  # Output: b'\xbf\xf3\xb6\x95...'
