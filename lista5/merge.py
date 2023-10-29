def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
    return nums



def apenas_numeros(nuns):
    numeros = []
    for c in nuns:
        num = ''
        for x in range(len(c)):
            if c[x].isdigit():
                num += c[x]
            elif num:
                numeros.append(int(num))
                num = ''
        if num:
            numeros.append(int(num))
    return merge_sort(numeros)


def partir(entradas):
    numeros = apenas_numeros(entradas)
    string = ' '.join(map(str, numeros))
    print(string,end='')


def main():
    entradas = []
    try:
        while True:
            x = input()
            entradas.append(x)
    except EOFError:
        partir(entradas)


if __name__ == '__main__':
    main()

# def apenas_numeros(nuns):
#     numeros = []
#     for c in nuns:
#         try:
#             numeros.append(int(c))
#         except:
#             pass
#     return merge_sort(numeros)

# def partir(entradas):
#     numeros = []
#     for c in entradas:
#         string_num = ''
#         for x in range(0,len(c)):
#             if x < len(c)-1:
#                 try:
#                     string_num = string_num + str(int(c[x]))
#                 except:
#                     numeros.append(string_num)
#                     string_num = ''
#             else:
#                 try:
#                     string_num = string_num + str(int(c[x]))
#                     numeros.append(string_num)
#                 except:
#                     pass
#     saida(apenas_numeros(numeros))

# def saida(numeros):
#     string = ''
#     for c in range(0,len(numeros)):
#         if c < len(numeros)-1:
#             string = string + str(numeros[c])+' '
#         else:
#             string = string + str(numeros[c])

#     print(string)

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) // 2
#     left_half = nums[:mid]
#     right_half = nums[mid:]
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#     i = j = 0
#     merged = []
#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:
#             merged.append(left_half[i])
#             i += 1
#         else:
#             merged.append(right_half[j])
#             j += 1
#     merged.extend(left_half[i:])
#     merged.extend(right_half[j:])
#     return merged




# nuns = []
# entradas = []
# try:
#     while True:
#         x = input()
#         entradas.append(x)
# except:
#     pass
# partir(entradas)
