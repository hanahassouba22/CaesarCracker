def crack_caesar(ciphertext):
    results = []
    print("🔓 Trying all shifts...\n")
    
    for shift in range(26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                result += char
        results.append(f"Shift {shift}: {result}")
    
    # Most English-like (has common words)
    common_words = ['the', 'and', 'for', 'are', 'but', 'not']
    for r in results:
        if any(word in r.lower() for word in common_words):
            print(f"🎯 BEST MATCH: {r}")
            return r
    return results[0]

# Test it!
secret = input("Enter encoded message: ")
print(crack_caesar(secret))
