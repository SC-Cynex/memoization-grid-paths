# 📌 Caminhos em uma Grade (Grid Paths)

## 📖 Descrição do Problema

Dado um grid (grade) de tamanho `m x n`, o objetivo é contar quantos caminhos distintos existem do canto superior esquerdo até o canto inferior direito, podendo mover-se **apenas para a direita ou para baixo** a cada passo.

Este problema é um clássico exemplo de sobreposição de subproblemas, ideal para ser resolvido com **recursividade** e **memoization** (programação dinâmica com cache).

## 🎯 Estratégia Utilizada

A solução foi implementada de forma **recursiva**, de cima para baixo, com as seguintes decisões estratégicas:

- A função `count_paths(m, n)` calcula o número de caminhos possíveis a partir das dimensões da grade.
- O problema possui **subproblemas repetidos**: por exemplo, `count_paths(3, 2)` será chamado diversas vezes ao longo da recursão.
- A estratégia de memoization foi aplicada para armazenar os resultados já computados em um **cache** (hashtable).

## ⚙️ Implementação da Memoization

Utilizamos um **dicionário (`dict`) do Python**, que funciona como uma hashtable para armazenar resultados intermediários:

```python
memo = {}
```

Antes de qualquer chamada recursiva, o algoritmo verifica se o resultado do subproblema já está armazenado no cache:

```python
if (m, n) in memo:
    return memo[(m, n)]
```

Caso não esteja, o valor é calculado recursivamente e armazenado no cache:

```python
memo[(m, n)] = count_paths(m - 1, n, memo) + count_paths(m, n - 1, memo)
```

Assim, cada subproblema é resolvido no máximo uma única vez, reduzindo significativamente o tempo de execução.

## 💡 Comparação: Com e Sem Cache

O projeto também oferece a opção de executar o algoritmo:

✅ Com memoization (otimizado)

🚫 Sem memoization (recursivo puro)

🔄 Ambos, permitindo a comparação de desempenho com tempos de execução.

Isso demonstra na prática como a otimização com cache melhora a eficiência do algoritmo para tamanhos maiores de grade.

## 🧪 Exemplos de Execução

| Tamanho da Grade | Com Cache (tempo) | Sem Cache (tempo)               |
| ---------------- | ----------------- | ------------------------------- |
| 3 x 3            | 0.000002 s        | 0.000015 s                      |
| 10 x 10          | 0.000005 s        | ⚠️ Muito lento ou estoura pilha |

## ✅ Conclusão

Este projeto demonstra na prática como programação dinâmica e memoization são técnicas essenciais para otimizar algoritmos recursivos, reduzindo complexidade de tempo e evitando recomputações desnecessárias.

## 👨‍💻 Desenvolvedores

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/humberto-peres"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/118866895?s=400&u=a12412e21705d58ab604be67c1e1431c80174b64&v=4" width="100px;" alt=""/><br /><sub><b>Humberto Peres</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/WesllyHn"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/117309594?v=4" width="100px;" alt=""/><br /><sub><b>Weslly Neres</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/Pellegr1n1"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/119978954?v=4" width="100px;" alt=""/><br /><sub><b>Leandro Pellegrini</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/v0cs"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104214178?v=4" width="100px;" alt=""/><br /><sub><b>Vítor Celestino</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">🚀</a></td>
  </tr>
</table>
