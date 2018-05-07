# P1.1
## 1
A vulnerabilidade presente é o facto de se poder alocar a quantidade de chars corresponde à multiplicação do número de linhas e colunas da matriz, assim sendo possível alocar um número ilimitado de chars, o que não deve ser possível.
## 2
Basta chamar a função com valores de size_t muito grandes.
## 3
Segmentation Fault

# P1.2
## 1
A vulnerabilidade encontra-se no facto de que se passarmos o valor 0 como o tamanho então o tamanho real vai passar a ser -1, e isso leva a que se tente alocar a memória num sítio fora(antes????) do buffer.

## 2
Basta chamar a função com tamanho igual 0.
O erro ocorre quando é feita a tentativa de copiar a memoria para o endereço fora do buffer.

## 3
Segmentation Fault

# P1.3
## 1
A vulnerabilidade deve-se ao facto de a variável tamanho ser um size_t (que uma vez que é um unsigned int não se importa com o sinal) ao passo que a variável tamanho_real é um int. Isto faz com que se passarmos um inteiro negativo à função ele vai passar no primeiro if e vai fazer com que o tamanho_real seja negativo e aloque memoria fora(antes????) do buffer.

## 2
Basta chamar a função com tamanho menor do que 0.
O erro ocorre quando é feita a tentativa de copiar a memoria para o endereço fora do buffer.

## 3
Segmentation Fault
