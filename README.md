# 🔢 Teste de Primalidade Miller-Rabin
Este repositório contém uma implementação do Teste de Miller-Rabin, um algoritmo probabilístico essencial na teoria dos números e criptografia moderna. Desenvolvido como projeto para a disciplina de Fundamentos de Matemática para Ciência da Computação 2 (FMCC 2) na UFCG.

## 💡 Sobre o Projeto
O Teste de Miller-Rabin é utilizado para determinar se um número é provavelmente primo. Diferente de métodos de divisão por tentativa, ele consegue lidar com números extremamente grandes em tempo polinomial, sendo uma peça fundamental no algoritmo.

### Por que Miller-Rabin?

- **Eficiência:** Muito mais rápido que testes determinísticos como o Crivo de Eratóstenes para números de centenas de dígitos.

- **Confiabilidade:** O erro do algoritmo é controlado pelo número de iterações ($k$). A probabilidade de um número composto ser declarado primo é menor que $4^{-k}$.
  
- **Aplicação Real:** É a base para a geração de chaves no algoritmo **RSA**.

---

## 🧬 Fundamentos Matemáticos

O teste baseia-se na decomposição de um número ímpar $n-1$ na forma:
$$n - 1 = 2^s \cdot d$$
Onde $d$ é ímpar. Para um número ser considerado primo em relação a uma base $a$ (testemunha), uma das seguintes condições de congruência deve ser satisfeita:

1.  $a^d \equiv 1 \pmod{n}$
2.  $a^{2^r \cdot d} \equiv -1 \pmod{n}$ para algum $0 \le r < s$

### Créditos
Gabriela Ramalho
Lara Soares
Murilo Jadson
Rebeca Medeiros
Stefany Alves

Disciplina: FMCC2
Professor: Tiago Massoni
Instituição: Universidade Federal de Campina Grande (UFCG) 
