def bitwise_and_or_xor(s1, s2):
    and_result = ""
    or_result = ""
    xor_result = ""
    for i in range(len(s1)):
        if s1[i] == "1" and s2[i] == "1":
            and_result += "1"
        else:
            and_result += "0"
        if s1[i] == "1" or s2[i] == "1":
            or_result += "1"
        else:
            or_result += "0"
        if s1[i] == s2[i]:
            xor_result += "0"
        else:
            xor_result += "1"
    return and_result, or_result, xor_result

def main():
    s1 = input("Enter the first bit string: ")
    s2 = input("Enter the second bit string: ")
    print("The bitwise AND, OR, and XOR of the two strings are: ", bitwise_and_or_xor(s1, s2))

if __name__ == "__main__":
    main()