import time
import random
import sympy
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from teste_primalidade.teste_primalidade_miller_rabin import miller_rabin

def benchmark_miller_rabin(tempo_limite_segundos=10.0):
    """
    Vai aumentando os bits até o tempo por teste
    ultrapassar o limite definido.
    """
    print(f"Limite por teste: {tempo_limite_segundos}s")
    print(f"{'Bits':>8} | {'Dígitos':>8} | {'Tempo/teste':>12} | {'Testes/min':>11} | Status")
    print("-" * 65)

    faixas = [
        64, 128, 256, 512,
        1024, 2048, 4096, 8192,
        16384, 32768, 65536, 131072
    ]

    ultimo_viavel = None

    for bits in faixas:
        digitos = int(bits * 0.30103)  # bits → dígitos decimais

        # Gera 5 amostras e tira a média
        tempos = []
        for _ in range(5):
            n = sympy.randprime(2**(bits-1), 2**bits)
            inicio = time.perf_counter()
            miller_rabin(n, k=40)
            tempos.append(time.perf_counter() - inicio)

        tempo_medio = sum(tempos) / len(tempos)
        testes_por_min = 60 / tempo_medio if tempo_medio > 0 else float('inf')

        status = "✓ viável"
        if tempo_medio > tempo_limite_segundos:
            status = "✗ muito lento"

        print(f"{bits:>8} | {digitos:>8} | {tempo_medio:>10.4f}s | "
              f"{testes_por_min:>10.1f} | {status}")

        if tempo_medio <= tempo_limite_segundos:
            ultimo_viavel = bits
        else:
            print(f"\n→ Limite prático encontrado: {ultimo_viavel} bits "
                  f"({int(ultimo_viavel * 0.30103)} dígitos decimais)")
            break

    return ultimo_viavel


print(benchmark_miller_rabin(tempo_limite_segundos=30.0))
