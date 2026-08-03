# 🤠 Pow-Pow

Um duelo de cowboys por turnos, jogado direto no terminal.

## Sobre o jogo

Você e a máquina começam cada um com vidas, balas no tambor, esquivas e a possibilidade de recarregar. A cada rodada, os dois escolhem em segredo entre três ações — **atirar**, **defender** ou **recarregar** — sem saber o que o adversário escolheu. Só depois que ambos decidem é que as jogadas são reveladas e o confronto é resolvido.

## Como funciona cada confronto

| Jogada do jogador | Jogada do oponente | Resultado |
|---|---|---|
| Atirar | Atirar | Ambos perdem uma bala |
| Atirar | Defender | Atirador perde uma bala, defensor perde uma esquiva |
| Defender | Defender | Ambos perdem uma esquiva |
| Recarregar | Recarregar | Esquivas voltam ao máximo e cada um ganha uma bala extra |
| Recarregar | Defender | Quem recarregou recupera esquivas e ganha bala extra; defensor perde uma esquiva |
| Recarregar | Atirar | Quem recarregou perde uma vida (mas recupera esquivas e ganha bala extra); atirador perde uma bala |

Vidas só são perdidas nesse último caso — recarregar contra um tiro certeiro. Todo o resto afeta apenas munição e esquivas.

Recarregar é a jogada mais arriscada: deixa você exposto a um tiro, mas é a única forma de repor balas e esquivas ao longo da partida. Sem balas você não pode atirar; sem esquivas você não pode defender — mas recarregar está sempre disponível.

## O oponente

A máquina não joga de forma totalmente aleatória. Ela acompanha o histórico de jogadas do adversário ao longo da partida e ajusta as probabilidades de cada ação com base nesse padrão, ficando mais difícil de prever conforme a partida avança.

## Fim de jogo

A partida termina quando um dos dois perde todas as vidas primeiro.

## Como jogar

Baixe o 'pow_pow.py' mais recente nas releases, e execute o arquivo.

## Requisitos

- Uma máquina capaz de interpretar python
- Um monitor no qual seja possível enxergar texto
- Um teclado funcional (apenas as teclas '1', '2', '3', '0' e 'enter' são necessárias)

> Caso os "gráficos" do jogo não pareçam formar desenho nenhum, há três causas possíveis:
>  - A largura da janela pode estar pequena demais.
>  - A sua fonte ou o ambiente em que o arquivo está sendo executado pode não se dar bem com o design
>  - A sua interpretação artística de caracteres ASCII pode ser diferente da do designer do jogo

