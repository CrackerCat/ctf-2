table=[0x37,0x34,0x35,0x32,0x33,0x30,0x31,0x3E,0x3F,0x3C,0x3D,0x3A,0x3B,0x38,0x39,0x26,0x27,0x24,0x25,0x22,0x23,0x20,0x21,0x2E,0x2F,0x2C,0x17,0x14,0x15,0x12,0x13,0x10,0x11,0x1E,0x1F,0x1C,0x1D,0x1A,0x1B,0x18,0x19,0x6, 0x7,0x4,0x5,0x2,0x3,0x0,0x1,0x0E,0x0F,0x0C,0x46,0x47,0x44,0x45,0x42,0x43,0x40,0x41,0x4E,0x4F,0x5D,0x59]

shoudbe="reverse+"
output=[]

for i in shoudbe:
    output.append(table.index(ord(i)^0x76))
# [43, 30, 47, 30, 43, 44, 30, 62]
# [0x2b,0x1e,0x2f,0x1e,0x2b,0x2c,0x1e,0x3e]
'''
v17 = Dst >> 2;
v18 = (v15 >> 4) + 16 * (Dst & 3);
v19 = (v16 >> 6) + 4 * (v15 & 0xF);
i = v16 & 0x3F;
'''

print(output)

'''
flag1=0xad
flag2=0xeb
flag3=0xde

flag4=0xae
flag5=0xc7
flag6=0xbe
ADEBDEAEC7BE
'''
