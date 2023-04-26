def podkreslanie(lancuch):
    snake=""
    for element in lancuch:
        if element==" ":
            snake+="_"
        else:
            snake+=element
    return snake

# print('Wpisz dowolne zdanie:')
# zdanie=input()
# print(podkreslanie(zdanie))

zdanie="wlazł kotek na płotek"
print(podkreslanie(zdanie))
