def task_0(q:int, w:float, e:str, r:list, t:bool) -> str:
    return ((q, '=', type(q)) +
            (w, '=', type(w))+
            (e, '=', type(e))+
            (r, '=', type(r))+
            (t, '=', type(t)))
print("Некрасивая версия:")
print((task_0(4, 3.6, 'hello', [4, 7], True)), '\n')


print('Первый вариант выглядит не красиво. Я не смогла придумать как его улучшить, поэтому сделала ещё другим способом:')
def task_1(a:int, b:float, c:str, d:list, h:bool) -> str:
    if a and b and c and d and h:
        print(a, '=', type(a))
        print(b, '=', type(b))
        print(c, '=', type(c))
        print(d, '=', type(d))
        print(h, '=', type(h))
print(task_1(4, 3.6, 'hello', [4, 7], True), '\n')


def task_2(x=[1, 2, 3, 5, 8, 13, 21]) ->list:
    return  x[0:3]
print('Cписок:', task_2(), '\n')


def task_3(y: int) -> int:
    return y**2
print('a^2 =', task_3(5))
#Не поняла что означает пункт: "c. распечатайте в консоль вызов функции".