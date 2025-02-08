def compress_string(text):
    # If the string is empty or has only one character, return it as is
    if len(text) <= 1:
        return text
    
    # Initialize variables
    compressed = ""  # Store the compressed string
    count = 1       # Count of current character
    current_char = text[0]  # Start with first character
    
    # Loop through the string starting from second character
    for i in range(1, len(text)):
        # If current character is same as previous
        if text[i] == current_char:
            count += 1
        else:
            # Add current character and its count to result
            compressed += current_char + str(count)
            # Reset count and update current character
            current_char = text[i]
            count = 1
    
    # Add the last character and its count
    compressed += current_char + str(count)
    
    # Return shorter string
    if len(compressed) < len(text):
        return compressed
    return text


# Test cases
def run_tests():
    # Test 1: Basic compression
    print("Test 1:", compress_string("aabcccccaaa"))  # Should print "a2b1c5a3"
    
    # Test 2: No compression needed
    print("Test 2:", compress_string("ab"))  # Should print "ab"
    
    # Test 3: Single character
    print("Test 3:", compress_string("a"))  # Should print "a"
    
    # Test 4: Empty string
    print("Test 4:", compress_string(""))  # Should print ""
    
    # Test 5: All same characters
    print("Test 5:", compress_string("aaaa"))  # Should print "a4"


# Run the tests if this file is run directly
if __name__ == "__main__":
    run_tests()

