'''
Os exercícios:

1. Modele e implemente um método recursivo que calcule o fatorial de um número n passado como parâmetro.

2. Modele e implemente um método recursivo que calcule o somatório de um número n (passado como parâmetro) até 0.

3. Modele e implemente um método recursivo que calcule o n-ésimo número da sequência de fibonacci.

4. Modele e implemente um método recursivo que calcule o somatório dos números inteiros entre os números k e j, passados como parâmetro.

5. Modele e implemente um método recursivo que recebe um String em retorna true se este String for um palíndrome, false caso contrário.
    ``` 
         boolean isPal(String s) 
    ```
6. Modele e implemente um método recursivo que recebe um inteiro zero ou positivo e retorna um String com o número em binário.
    ``` 
         String convBase2(int n) 
    ``` 
7. Modele e implemente um método recursivo que calcule o somatório dos números contidos em um ArrayList de inteiros, passado como parâmetro.

8. Modele e implemente um método recursivo para encontrar o maior elemento de um ArrayList.
   ``` 
         int findBiggest(ArrayList<Integer> ar) 
    ``` 

9. Implemente um método recursivo para determinar se um string ocorre dentro de outro.
	  ``` 
         boolean findSubStr(String str, String match)
	  ``` 
10. Faça um método recursivo que determina o número de dígitos de um inteiro.
	  ``` 
         int nroDigit(int n)
	  ``` 
11. Implemente um métodos que recebe um String e retorna um ArrayList com todas as permutações deste String.
	  ``` 
         ArrayList<String> permutations(String s)
	  ``` 

'''

def ex1(n):
    if n < 2:
        return 1
    else: return n * ex1(n-1)





def ex2(n):
    if n < 1 : 
        return 0
    else: return n + ex2(n-1)


def ex3(n):
    if n < 1:
        return 1
    else: return ex3(n-1) + ex3(n-2)

def ex4(k,j):
    if k >= j:
        return k 
    else: return k + ex4(k+1,j)

def ex5(string, size1=0):
    
    if size1 == len(string)/2 and string[size1] == string[len(string)-size1-1]:
        return True
    elif string[size1] == string[len(string)-size1-1]:
        return ex5(string, size1+1)
    else:
        return False

def ex6(n):
    if n <= 1:
        return "1"
    # elif n == 2:
        # return "0"
    elif n % 2  == 0:
        return  ex6(n/2) + "0" 
    else: return ex6(n/2) + "1"

def ex7(arr, idx=0, sum = 0):
    if idx > len(arr)-1:
        return sum
    else:
        return ex7(arr, idx+1, sum+arr[idx])

def ex8(arr, idx=0, biggest=0):
    if idx > len(arr)-1:
        return biggest
    else:
        return ex8(arr, idx+1, arr[idx] if arr[idx] > biggest else biggest) 

def ex9(string, match, idx1 = 0, idx2 = 0, value = False):
    if len(string) - 1 > idx1:
        if(len(string)-1 > idx2) and string[idx1] == match[idx2] and value:
            return True
        elif(string[idx1] == match[idx2]):
            return ex9(string,match, idx1+1, idx2+1, True)
        else: return ex9(string,match,idx1+1)
    else: return False

def ex10(n,digit=0):
    if n / 10 < 1:
        return digit
    else: return ex10(n/10,digit+1)

def ex11(s):
    if len(s) == 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in ex11(remaining):
            result.append(char + perm)
    
    return result


print(ex1(3))

print(ex2(3))

print(ex3(5))

print(ex4(5, 10))

print(ex5("abba"))

print(ex6(16))

print(ex7([1,2,3]))

print(ex8([1,2,3]))


print(ex9("abcddabc", "dd"))


print(ex10(900))

print(ex11("abc"))