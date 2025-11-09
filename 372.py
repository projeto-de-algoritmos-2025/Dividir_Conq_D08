class Solution(object):
    def superPow(self, a, b):
        MOD = 1337

        if not b:
            return 1
        
        # pega o último dígito
        last = b.pop()
        
        # (a^rest)^10 % MOD
        part1 = pow(self.superPow(a, b), 10, MOD)
        # a^last % MOD
        part2 = pow(a, last, MOD)
        
        return (part1 * part2) % MOD