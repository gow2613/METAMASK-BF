from mnemonic import Mnemonic

# Create an instance of the Mnemonic class
mnemo = Mnemonic("english")  # Specify the language for the mnemonic (e.g., "english")

# Generate a 12-word mnemonic sentence
mnemonic_sentence = mnemo.generate(strength=128)  # Strength of 128 bits generates a 12-word phrase

print(mnemonic_sentence)
