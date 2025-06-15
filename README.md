# Integrantes

Lucas Ribeiro do Nascimento

# Flood Fill Project

Implementação em **Python 3** do algoritmo *Flood Fill* para identificação e colorização de regiões ortogonalmente conectadas em uma grade 2‑D.

---

## 1 • Objetivo

Colorir automaticamente todas as células livres (`0`) de uma grade, atribuindo um identificador incremental (`2, 3, 4…`) a cada região isolada, preservando obstáculos (`1`).

---


## 2 • Pré‑requisitos

- **Python ≥ 3.8**  (Não são necessárias bibliotecas de terceiros.)

Verifique a versão:

```bash
python --version
```

---

## 3 • Instalação

1. Clone ou faça download dos arquivos.
2. Navegue para o diretório `flood_fill_project`.

```bash
git clone <repo>
cd flood_fill_project
```

---

## 4 • Modos de Execução

| Modo                | Comando                         | Descrição                                  |
| ------------------- | ------------------------------- | ------------------------------------------ |
| **Interativo**      | `python flood_fill.py`          | Solicita parâmetros via teclado            |
| **Caso padrão**     | `python flood_fill.py --padrao` | Executa um cenário embutido sem entradas   |
| **Suite de testes** | `python flood_fill.py --teste`  | Valida o algoritmo com dois casos de teste |

---

## 5 • Formato de Entrada (modo interativo)

1. **Dimensões** `linhas colunas` — números inteiros separados por espaço.
2. **Conteúdo da grade** um linha por vez contendo `0` ou `1`.
3. **Posição inicial** `linha coluna` (índices base 0).

### Exemplo

```
Digite número de linhas e colunas (ex: 4 5): 4 5
Digite cada linha da grade usando 0 para área livre e 1 para obstáculo
L0 > 0 0 1 0 0
L1 > 0 1 1 0 0
L2 > 0 0 1 1 1
L3 > 1 1 0 0 0
Digite a posição inicial (linha coluna, 0-based): 0 0
```

---

## 6 • Saída

A grade é impressa antes e depois do preenchimento, com cada região numerada.

---

## 7 • Complexidade

- **Tempo:** `O(n × m)` — cada célula é visitada no máximo uma vez.
- **Memória:** `O(n × m)` — fila de BFS na pior hipótese.

---

## 8 • Validação Automática

```
python flood_fill.py --teste
```

Ambos os testes devem exibir **“Todos os testes passaram!”**. Altere ou acres-  cente testes conforme necessário, mantendo os existentes.

---
