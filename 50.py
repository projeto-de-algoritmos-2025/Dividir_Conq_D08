class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. Tratar o caso de expoente negativo
        # Se n for negativo, calculamos para -n e invertemos o resultado no final.
        if n < 0:
            x = 1 / x
            # Usamos -n para o cálculo. Note que -n pode exceder o limite
            # de int se n for o valor mínimo (e.g., -2^31), mas Python lida
            # com inteiros grandes automaticamente.
            n = -n
        
        # O resultado será armazenado em 'ans'
        ans = 1.0
        
        # 'current_product' armazena as potências de x (x^1, x^2, x^4, x^8, ...)
        current_product = x
        
        # 2. Loop principal usando o algoritmo de Exponenciação Rápida
        # O loop continua enquanto houver bits em n a serem processados.
        while n > 0:
            # Se o bit menos significativo de n for 1 (n é ímpar),
            # multiplicamos a resposta atual por 'current_product'.
            # Isso corresponde à parte "x" na fórmula: x^n = x * x^(n-1)
            if n % 2 == 1:
                ans *= current_product
            
            # Elevamos a potência do 'current_product' ao quadrado: x^k -> x^(2k)
            # Isso corresponde a dobrar a potência que estamos considerando.
            current_product *= current_product
            
            # Deslocamos n para a direita (n //= 2).
            # Isso move para o próximo bit da representação binária de n.
            n //= 2
            
        return ans