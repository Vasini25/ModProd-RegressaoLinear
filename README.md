# ModProd Regressão Linear

## Previsão de ponto futuro em série temporal não estacionária.

#### Programa em Python para calcular, dada um conjunto de pontos de uma série temporal não estacionária, a previsão do próximo ponto, calculada utilizando regressão linear.

Ao estudar Modelagem da Produção e as respectivas atividades de Planejamento e Controle da Produção (PCP), um dos<br>
primeiros conceitos com o qual nos defrontamos é o planejamento da demanda futura.<br>
Para tal, há métodos para predição, onde se tenta estimar qual será a demanda do seu produto produzido ou serviço<br>
oferecido no primeiro período de todos, quando não há dados históricos aos quais se comparar e analisar.

Quando a empresa possui algum tempo de operação e venda, ela coleta dados da quantidade de produtos demandada ao<br>
longo de períodos de tempo, que podem ser definidos pela própria empresa da maneira que for mais adequado a ela<br>
(anos, meses, semanas ou até dias). O mais comum é pensar em um período de um mês, mas, de novo, isto varia de <br>
acordo com a empresa, seu porte, seu tempo de operação, seu produto e até sua estrutura de operação em si.

Prever a demanda é fundamental para tomar decisões de alto nível dentro da empresa e definir outras atividades<br>
com as quais nos depararemos ao avançar dos estudos em PCP.

Em se tratando da previsão, podemos nos apoiar em dados (gráficos e/ou tabelas da demanda com o passar de peíodos <br>
de tempo, aos quais damos o nome de "Séries Temporais") que são separados em duas categorias:

**- Séries Temporais Estacionárias:**
	Séries em que não há aumento ou diminuição considerável ao logo do tempo, ou seja, em que a tendência da<br>
	demanda é flutuar em torno de uma reta de tendẽncia bem definida.<br>
	Para este tipo de série, o mais comum é utilizar alguns métodos, em especial, os diferentes métodos de<br>
	médias móveis, aplicando-se os diferentes tipos de cálculos de Erro a cada uma delas, verificando qual<br>
	pode ter um resultado mais preciso e confiável.<br>
	Também são comuns de entrarem nesta classificação séries temporais com poucos dados.

**- Séries Temporais Não Estácionárias:**
	Necessitam de uma quantidade minimamente considerável de dados de demanda em períodos passados.
	Caracterizam-se por apresentar ascenção ou declíneo no "nível médio" (tendência) das vendas.
	Neste caso a reta de tendência será bem definida, inclusive porque, definí-la faz parte do processo<br>
	para tentar prever a demanda no próximo período.
	Utiliza-se os dados num plano cartesiano períodoXdemanda ("com período" no eixo das abcissas e "demanda"<br>
	no eixo das ordenadas) e utiliza-se o método da Regressão Linear, que, por sua vez, utiliza o método<br>
	dos Mínimos Quadrados para definir uma equação de reta y = a + bx que esteja o mais próximo possível<br> 
	de todos os pontos que será a reta T (tendência). *Caso este método seja adotado para séries<br>
	estacionárias, o valor obtido ao calcular "b" tenderá a 0 (será 0 ou muito próximo dele).
	Ao definir os valores de "a" e "b", basta substituir o "x" na equação encontrada pelo valor do próximo<br>
	ponto do eixo das abcissas, ou seja, o número cardinal do´ponto que representa o próximo período<br>
	(período a ser previsto).
	Pode-se calcular o coeficiente de correlação "r", que indicará uma valor entre 0 e 1, o qual quanto<br>
	mais próximo de 1, melhor a reta encontrada reflitirá o local dos pontos no gráfico, ou seja, maior<br>
	sua acurácia ao representá-los, já que eles dificilmente estariam todos alinhados.
	Mais 3 aspectos podem influenciar uma série temporal não estacionária: Sazonalidade, Ciclo e Aleatoriedade.
	A Tendência não apresentar um valor de "r" satisfatório indica que ela pode apresentar, ao menos, <br>
	uma destas 3 caracterísicas, sendo a sazonalidade a mais provável e a que define as outras duas.
	A sazonalidade, apenas, também śerá aqui abordada quando necessário.
	A sazonalidade é um pico de demanda devido a algum fator externo que ocorre de tempos em tempos.
	Como por exemplo, a venda de picolés, que apresenta maior demanda nos primeiros meses do ano (no <br>
	hemisfério sul) devido à estação do verão.
	Todos os períodos compreendidos entre dois pontos de sazonalidade são chamados de "Ciclos".
	Por fim, os demais ruídos que podem ocorrer nos períodos que não são afetados pela sazonalidade<br>
	são chamados de "Aleatoriedade"
	

### Neste programa, abordaremos o método da regressão linear, com uma função que demanda uma lista de valores de 
demandas anteriores de quantidade variável, e o valor numérico do ponto para p qual se deseja encontrar 
a previsão da demanda. Caso haja fator de sazonalidade, ele é calculado (feature funcionando perfeitamente, mas 
não devidamente implementada para uso a partir da main, pois necessita de um preset).
