lista_precos = [100, 2000, 6000, 8000]
reajuste_total = 0.05
reajuste_faixa1 = 0.2
reajuste_faixa2 = 0.05
meta = 5000
#======================================
lista_reajustada = []
lista_reajustada2 = []
#======================================
for preco in lista_precos:
    novo_preco = preco * (1 + reajuste_total)
    novo_preco5 = preco * (1 + reajuste_faixa1) 
    novo_preco10 = preco * (1 + reajuste_faixa2)
    lista_reajustada.append(novo_preco)
    if preco <= meta:   
        lista_reajustada2.append(novo_preco5)
    else:   
        lista_reajustada2.append(novo_preco10)
   
print(f"\nReajuste geral de {reajuste_total * 100}%: ", lista_reajustada)
print(f"Reajuste escalonado de {reajuste_faixa2 * 100}% e {reajuste_faixa1 * 100}%: ", lista_reajustada2, "\n")
