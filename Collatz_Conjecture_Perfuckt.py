set_results = [0]
e = 0
f = 1
while f == 1:
    n = input("우박수 여부를 확인할 숫자:")
    if str.isdigit(n) == True and int(n) >= 1:
        k = int(n)
        while k > 1:
            if k % 2 == 0:
                k = k / 2
                e = e + 1
                set_results.append(k)
            else:
                k = 3 * k + 1
                e = e + 1
                set_results.append(k)
            if k == 1:
                f = 0
                break
    else:
        print("옳지 않은 문자 형식. 자연수를 아라비아 숫자로 입력해주십시오.")
        n = 0
        continue
    if f == 0:
        break
a = "결과값:"
b = "\n"
c = "은 우박수입니다. 정지시간 : "
d = "최대값 : "
print(a + str(k) + b + n + c + str(e) + b + d + str(max(set_results)))

set_results.remove(0)

print(set_results)
set_results.clear