import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import random
from teste_primalidade.preteste import pre_teste
from teste_primalidade.decomposicao import decomposicao
from teste_primalidade.teste_eh_testemunha import eh_testemunha

def miller_rabin_estatistico(n, k=40):
   s, d = decomposicao(n)

   for _ in (range(k)):
      a = random.randint(2, n - 2)
      if eh_testemunha(a, n, s, d):
         return f"O número {n} é composto - verificado pelo teste de Miller-Rabin"

   prob_acerto = (1 - ((1/4) ** k)) * 100
   return f"O número {n} é provavelmente primo - Nível de certeza: {prob_acerto:.10f}%"
