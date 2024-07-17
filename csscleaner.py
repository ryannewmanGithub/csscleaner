giantstring = ""


output_f = open('outputfile.css', 'w')

with open('inputfile.css', 'r') as f:
    lines = f.readlines()
    for line in lines:
        for char in line:
            if char not in list("{};"):
                giantstring += char
                continue
            if char == "{":
                giantstring += " "
                giantstring += char
                giantstring += "\n"
                giantstring += "\t"
            if char == ";":
                giantstring += char
                giantstring += "\n"
                giantstring += "\t"
            if char == "}":
                giantstring += "\n"
                giantstring += char
                giantstring += "\n"
            

output_f.write(giantstring)
output_f.close()



    