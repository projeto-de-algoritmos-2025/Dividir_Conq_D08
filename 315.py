from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        # 1. Inicializa a matriz de contagens e o array de pares (valor, índice)
        counts = [0] * n
        # O array 'indexed_nums' armazena (valor, índice_original)
        indexed_nums = [(nums[i], i) for i in range(n)]

        # Função de mesclagem (Merge) modificada
        def merge(left_half, right_half):
            # i e j são ponteiros para as metades esquerda e direita, respectivamente
            i, j = 0, 0
            merged = []
            
            # smallers_count rastreia quantos elementos da metade direita
            # já foram adicionados ao 'merged' e são MENORES que o elemento atual da esquerda.
            smaller_count = 0 

            while i < len(left_half) or j < len(right_half):
                # Caso 1: A metade esquerda está esgotada
                if i == len(left_half):
                    merged.append(right_half[j])
                    j += 1
                
                # Caso 2: A metade direita está esgotada
                elif j == len(right_half):
                    # Adiciona a contagem acumulada ao elemento restante
                    original_index = left_half[i][1]
                    counts[original_index] += smaller_count
                    merged.append(left_half[i])
                    i += 1
                    
                # Caso 3: Elemento da esquerda é <= Elemento da direita
                # O elemento da esquerda é estável em relação à contagem de smallers_count.
                # Todos os 'smaller_count' são menores do que ele E estão à sua direita.
                elif left_half[i][0] <= right_half[j][0]:
                    original_index = left_half[i][1]
                    counts[original_index] += smaller_count
                    merged.append(left_half[i])
                    i += 1
                    
                # Caso 4: Elemento da esquerda é > Elemento da direita
                # O elemento da direita é MENOR que o elemento da esquerda.
                # Ele deve ser contado.
                else:
                    merged.append(right_half[j])
                    # Incrementa o contador de elementos menores
                    smaller_count += 1
                    j += 1
            
            return merged

        # Função principal do Merge Sort (Divide)
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Mescla as duas metades, realizando a contagem
            return merge(left, right)

        # Inicia o processo de ordenação e contagem
        merge_sort(indexed_nums)
        
        return counts