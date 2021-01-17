class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):            #sum product
        if len(self.vec) == len(vec2):  #checking the length of the both list.
            newList = []
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
            return Vector(newList)
        else:
            print("Length dosen't match with another list")
    def __mul__(self, vec2):            #dot product
        if len(self.vec) == len(vec2):  #checking the length of the both list.
            sum = 0
            for i in range(len(self.vec)):
                sum += (self.vec[i] * vec2.vec[i])
            return sum
        else:
            print("Length dosen't match with another list")

    def __len__(self):                  # returning the length of the list.
        return len(self.vec)


v1 = Vector([1, 5, 6])
v2 = Vector([1, 4, 3])

print("Sum product of the vector is",v1+v2)
print("Dot product of the vector is",v1 * v2)
print(len(v1))
print(len(v2))
