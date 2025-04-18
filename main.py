from grid_paths import count_paths, count_paths_no_cache
import os
import time

def show_menu():
    print("\nCaminhos em uma Grade (Recursão)")
    print("-" * 50)
    print("Escolha uma opção:")
    print("1. Usar tamanhos padrões")
    print("2. Digitar um tamanho personalizado")
    print("3. Sair")

def choose_execution_mode():
    print("\nModo de execução:")
    print("a. Com cache (memoization)")
    print("b. Sem cache (recursão pura)")
    print("c. Ambos (comparar tempos)")
    while True:
        mode = input("Escolha o modo: ").strip().lower()
        if mode in ("a", "b", "c"):
            return mode
        print("Opção inválida. Tente novamente.")

def run_default_sizes():
    sizes = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (10, 10)]
    mode = choose_execution_mode()

    print("\nResultados:")
    for m, n in sizes:
        print(f"\nTamanho: {m} x {n}")
        if mode in ("a", "c"):
            if m > 15 or n > 15:
                print("⚠️ Sem cache: valores muito grandes podem causar lentidão ou erro.")
                continue
            start = time.time()
            result = count_paths(m, n)
            elapsed = time.time() - start
            print(f"✅ Com cache: {result} caminhos (tempo: {elapsed:.6f}s)")

        if mode in ("b", "c"):
            if m > 15 or n > 15:
                print("⚠️ Sem cache: valores muito grandes podem causar lentidão ou erro.")
                continue
            start = time.time()
            result = count_paths_no_cache(m, n)
            elapsed = time.time() - start
            print(f"🚫 Sem cache: {result} caminhos (tempo: {elapsed:.6f}s)")

def run_custom_size():
    try:
        m = int(input("Informe o número de linhas (m): "))
        n = int(input("Informe o número de colunas (n): "))
        mode = choose_execution_mode()

        print(f"\nGrade: {m} x {n}")
        if mode in ("a", "c"):
            start = time.time()
            result = count_paths(m, n)
            elapsed = time.time() - start
            print(f"✅ Com cache: {result} caminhos (tempo: {elapsed:.6f}s)")

        if mode in ("b", "c"):
            if m > 15 or n > 15:
                print("⚠️ Sem cache: valores muito grandes podem causar lentidão ou erro. Execução cancelada.")
            else:
                start = time.time()
                result = count_paths_no_cache(m, n)
                elapsed = time.time() - start
                print(f"🚫 Sem cache: {result} caminhos (tempo: {elapsed:.6f}s)")

    except ValueError:
        print("Entrada inválida. Use apenas números inteiros.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_terminal()
        show_menu()
        option = input("Digite sua opção: ").strip()

        if option == "1":
            run_default_sizes()
        elif option == "2":
            run_custom_size()
        elif option == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

main()
