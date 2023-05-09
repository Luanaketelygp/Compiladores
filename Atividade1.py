class AF:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def contar_padroes(self, padroes):
        count = 0
        for padrao in padroes:
            if self.verificar_padrao(padrao):
                count += 1
        return count

    def verificar_padrao(self, padrao):
        estado_atual = self.estado_inicial
        for simbolo in padrao:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                return False
        return estado_atual in self.estados_finais

af_estados = {'q0', 'q1', 'q2'}
af_estado_inicial = 'q0'
af_estados_finais = {'q2'}
af_transicoes = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q1',
    ('q1', '1'): 'q2',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q2'
}

automato = AF(af_estados, af_estado_inicial, af_estados_finais, af_transicoes)
padroes = ['010', '0110', '100', '110', '101']

qtd_padroes = automato.contar_padroes(padroes)
print(f"A quantidade de padrões é: {qtd_padroes}")
