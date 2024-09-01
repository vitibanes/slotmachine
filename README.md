<h2>🎰 Descrição do Código</h2>
<p>Este código é uma simulação simples de uma máquina caça-níqueis (slot machine) em Python. Ele permite que o jogador deposite dinheiro, defina o número de linhas em que deseja apostar, escolha o valor da aposta e, em seguida, "gire" a máquina para ver se ganhou ou perdeu dinheiro.</p>

<h3>🛠️ Estrutura do Código</h3>
<ul>
  <li><strong>🔧 Constantes Definidas:</strong>
    <ul>
      <li><code>MAX_LINES</code>, <code>MAX_BET</code>, <code>MIN_BET</code>: Estes valores definem o número máximo de linhas que podem ser apostadas, o valor máximo de aposta por linha e o valor mínimo de aposta por linha, respectivamente.</li>
      <li><code>ROWS</code>, <code>COLS</code>: Definem o número de linhas e colunas da slot machine.</li>
      <li><code>symbol_count</code>, <code>symbol_value</code>: Dicionários que armazenam a quantidade de cada símbolo na máquina e o valor de cada símbolo, respectivamente.</li>
    </ul>
  </li>
  <li><strong>✨ Funções Principais:</strong>
    <ul>
      <li><code>check_winnings(columns, lines, bet, values)</code>: Verifica quais linhas são vencedoras e calcula os ganhos com base nos símbolos presentes nessas linhas.</li>
      <li><code>get_slot_machine_spin(rows, cols, symbols)</code>: Gera uma nova "rotação" da slot machine, retornando os símbolos em cada coluna.</li>
      <li><code>print_slot_machine(columns)</code>: Imprime o resultado da rotação da slot machine em um formato visual amigável.</li>
      <li><code>deposit()</code>: Solicita ao usuário um valor de depósito inicial.</li>
      <li><code>get_number_of_lines()</code>: Solicita ao usuário o número de linhas que ele gostaria de apostar.</li>
      <li><code>get_bet()</code>: Solicita ao usuário o valor da aposta por linha.</li>
      <li><code>spin(balance)</code>: Realiza uma rotação completa da slot machine, ajustando o saldo do jogador com base no resultado.</li>
    </ul>
  </li>
  <li><strong>🎯 Função Principal:</strong>
    <ul>
      <li><code>main()</code>: Controla o fluxo principal do jogo. Solicita o depósito inicial, permite que o jogador continue jogando até que escolha sair, e exibe o saldo final do jogador.</li>
    </ul>
  </li>
</ul>

<h3>🎮 Como Jogar</h3>
<ol>
  <li><strong>💰 Depósito:</strong> O jogador começa depositando um valor para jogar.</li>
  <li><strong>🔢 Escolha das Linhas:</strong> O jogador escolhe quantas linhas deseja apostar (de 1 a 3).</li>
  <li><strong>💸 Valor da Aposta:</strong> O jogador escolhe quanto deseja apostar por linha, dentro dos limites estabelecidos.</li>
  <li><strong>🎲 Girar:</strong> A slot machine é girada, e o resultado é mostrado na tela. O saldo do jogador é atualizado com base nos ganhos ou perdas.</li>
  <li><strong>↩️ Continuar ou Sair:</strong> O jogador pode optar por continuar jogando até que decida sair, momento em que o saldo final é exibido.</li>
</ol>

<h3>📝 Exemplo de Uso</h3>
<pre><code> Seu saldo é de $100
Pressione enter para jogar ou 'q' para sair: 
Quantas linhas gostaria de apostar (1-3)? 2
Quanto você gostaria de apostar em cada linha? $10
Você está apostando $10 em 2 linhas. Aposta total é de $20.
A | B | A
A | A | C
A | A | A
 Você ganhou $20.
 Linhas ganhas: 3
 Seu saldo é de $100
</code></pre>
