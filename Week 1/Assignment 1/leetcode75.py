def gcdOfStrings(str1, str2):
    
        if len(set(str2)) != len(str2):
            # process repeated str2
            print(len(str1)%len(str2))
            if len(str1)%len(str2) != 0:

                print(str2.find(str2[0]))
                while str2[1:].find(str2[0]) > 0:
                    print("str[1:]", str2[1:])
                    print("str2[1:].find(str2[0])", str2[1:].find(str2[0]))
                    print("str2[str2[1:].find(str2[0]):]", str2[str2[1:].find(str2[0]):])

                    # check for duplicate char
                    
                    str2 = str2[(str2[1:].find(str2[0]) + 1):]
                    # str2 = str2(str2[0].index())
            
        # finds difference between the strings
        newString = [x for x in str1 if x not in str2]

        print("new string: ", newString)

        if len(newString) == 0:
            # if NO foreign char not in str2 
            print("ret str2:", str2)
            return str2
        else:
            # if foreign char not in str2
            print("ret null")
            return ""

# gcdOfStrings("ABCABC", "ABC")
# gcdOfStrings("ABABAB", "ABAB")
# gcdOfStrings("LEET", "CODE")

gcdOfStrings("ABABABAB", "ABAB")
