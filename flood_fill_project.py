import sys
from collections import deque

DEFAULT_GRID = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0],
]
DEFAULT_START = (0, 0)
DEFAULT_EXPECTED = [
    [2, 2, 1, 3, 3],
    [2, 1, 1, 3, 3],
    [2, 2, 1, 1, 1],
    [1, 1, 4, 4, 4],
]

TEST2_GRID = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]
TEST2_START = (0, 0)
TEST2_EXPECTED = [
    [2, 1, 3],
    [1, 4, 1],
    [5, 1, 6],
]


def ler_inteiros(msg):
    try:
        return [int(x) for x in input(msg).strip().split()]
    except (OSError, EOFError):
        raise RuntimeError("Entrada não disponível neste ambiente.")


def imprimir_grade(grade):
    for linha in grade:
        print(" ".join(map(str, linha)))


def dentro(l, c, n, m):
    return 0 <= l < n and 0 <= c < m


def preencher_regiao(grade, inicio, cor):
    n, m = len(grade), len(grade[0])
    il, ic = inicio
    if not dentro(il, ic, n, m) or grade[il][ic] != 0:
        return
    fila = deque([(il, ic)])
    grade[il][ic] = cor
    while fila:
        l, c = fila.popleft()
        for dl, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nl, nc = l + dl, c + dc
            if dentro(nl, nc, n, m) and grade[nl][nc] == 0:
                grade[nl][nc] = cor
                fila.append((nl, nc))


def proxima_zero(grade):
    for i, linha in enumerate(grade):
        for j, val in enumerate(linha):
            if val == 0:
                return i, j
    return None


def flood_fill(grade, inicio):
    cor = 2
    preencher_regiao(grade, inicio, cor)
    cor += 1
    while True:
        nz = proxima_zero(grade)
        if nz is None:
            break
        preencher_regiao(grade, nz, cor)
        cor += 1


def copiar_grade(g):
    return [linha[:] for linha in g]


def executar_padrao():
    grade = copiar_grade(DEFAULT_GRID)
    print("Grade inicial (padrão):")
    imprimir_grade(grade)
    flood_fill(grade, DEFAULT_START)
    print("\nGrade preenchida:")
    imprimir_grade(grade)


def modo_interativo():
    linhas, colunas = ler_inteiros("Digite número de linhas e colunas (ex: 4 5): ")
    grade = []
    print("Digite cada linha da grade usando 0 para área livre e 1 para obstáculo")
    for i in range(linhas):
        linha = ler_inteiros(f"L{i} > ")
        if len(linha) != colunas:
            raise ValueError(f"Esperado {colunas} valores, obtido {len(linha)}.")
        grade.append(linha)
    li, ci = ler_inteiros("Digite a posição inicial (linha coluna, 0-based): ")
    print("\nGrade inicial:")
    imprimir_grade(grade)
    flood_fill(grade, (li, ci))
    print("\nGrade preenchida:")
    imprimir_grade(grade)


def rodar_testes():
    print("Executando suite de testes…")

    g1 = copiar_grade(DEFAULT_GRID)
    flood_fill(g1, DEFAULT_START)
    if g1 != DEFAULT_EXPECTED:
        raise AssertionError("Teste 1 falhou")

    g2 = copiar_grade(TEST2_GRID)
    flood_fill(g2, TEST2_START)
    if g2 != TEST2_EXPECTED:
        raise AssertionError("Teste 2 falhou")

    print("Todos os testes passaram!")


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--padrao":
            executar_padrao()
            return
        if arg == "--teste":
            rodar_testes()
            return

    try:
        if sys.stdin is None or sys.stdin.closed or not sys.stdin.isatty():
            raise RuntimeError
        modo_interativo()
    except RuntimeError:
        print("Entrada padrão indisponível. Executando caso padrão…")
        executar_padrao()


if __name__ == "__main__":
    main()
