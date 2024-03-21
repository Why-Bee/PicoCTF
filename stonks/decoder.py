s = "ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3��}"

# Create a loop to convert this to a LE format

out = ""

for i in range(0, len(s)-3, 4):
	out += s[i+3] + s[i+2] + s[i+1] + s[i]

print(out)