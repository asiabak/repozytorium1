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
print('Jesteś pewien, że to ma być to zdanie?')
odpowiedz=input()
if odpowiedz=="tak":
    print(podkreslanie(zdanie))
else:
    print('zła odpowiedź')

# zdanie="wlazł kotek na płotek"
# print(podkreslanie(zdanie))
