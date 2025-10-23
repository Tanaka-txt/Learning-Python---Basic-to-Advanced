#Ordem de execução de prioridade aritmética
# 1. (n+n)      - Parentese
# 2. **         - Expo
# 3. * / // %   - mult e div
# 4. + -        - Soma e Sub

conta_1 = 1 + 1 ** 5 + 5 # 7
conta_2 = ((1 + 1) ** 5) + 5 # 7
print(conta_1)