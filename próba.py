def podkreslanie(lancuch):
    snake=""
    for element in lancuch:
        if element==" ":
            snake+="_"
        else:
            snake+=element
    return snake

print('Wpisz dowolne zdanie:')
zdanie=input()
print('Jesteś pewien, że to ma być to zdanie? Może coś innego???? ')
odpowiedz=input()
if odpowiedz=="tak":
    print(podkreslanie(zdanie))
elif odpowiedz == "coś innego":
    print("jabłuszko")
else:
    print('banan')

# zdanie="wlazł kotek na płotek"
# print(podkreslanie(zdanie))
