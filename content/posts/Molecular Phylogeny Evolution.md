---
title: Evolução filogenética e Molecular
created: 2026-08-16
tags:
  - Biomol
  - Filogenia
  - Evolução
  - Bioinformatica
---

![Type|126x20](https://img.shields.io/badge/Type-Bioinformatica-2ea44f?style=flat-square)
![Subject](https://img.shields.io/badge/Subject-Filogenia%20e%20Evolução-8a2be2?style=flat-square)
![Evolução filogenética e Molecular](/images/Molecular%20Phylogenyand%20Evolution-1786991207974.webp)

_Nothing in biology makes sense except in the light of evolution. —Theodosius Dobzhansky (1973)_

Disclaimer: Esse Blog foi escrito a partir do livro bioinformatcs and functional genomics e existem trechos e imagens que foram copiadas diretamente do livro
<!--more-->
# ✅ Checklist 
- [ ] describe the molecular clock hypothesis and explain its significance; 
- [x] define positive and negative selection and test its presence in sequences of interest;
- [ ] describe the types of phylogenetic trees and their parts (branches, nodes, roots);
- [ ] create phylogenetic trees using distance-based and character-based methods; and
- [ ] create phylogenetic trees using distance-based and character-based methods; and

# Compreensões sobre evolução

	É a teoria de que grupos de organismos mudam com o passar do tempo no passo que seus descendentes diferem estruturalmente e funcionamente de seus ancestrais, ou seja, você não é definido pelos seus pais! (frase minha)
	Também pode ser definida como um processo biologico nno qual os organismos herdam caracteristicas/features morfológicos e fisiológicos que definem as espécies.
	Evolução é um processo de mudança. A hereditariedade é geralmente conservada,a prole se assemelha os pais e ainda sim a sua estrutura e função corporal muda ao passar das gerações, então você pode dar meia razão para o Belchior pois ainda somos os mesmo e vivemos como os nossos pais, apesar de termos a capacidade de seguir e nos desenvolver por outros caminhos.        Existem 3 principais mecanismos que podem gerar mudanças (Simpson, 1952):
	- **Condições para o crescimento afetam o desenvolvimento** : Fatores             ambiêntais como acidentes e infecções causadoras de doenças não são herdadas     (apesar que a resposta para tais circunstâncias são controladas geneticamente     até certa medida, mas os dinossauros não conseguiriam sobreviver aos meteóros     de qualquer forma)
	- **Mecanismos de reprodução sexual**: A reprodução sexual garante mudânças       com o passar das gerações.A sequência de DNA e genes são "embaralhadas" via       recombinação gênica e os desendentes herdam essas novas características.
	- **Mutações** : Mutações específicas, assim como a deriva genética onde          afrequência dos alelos em uma população muda de geração para geração por puro     acaso e sorte, pode produzir mudanças em genes e nos cromossomos.
	 Ao nível molecular, evolução é o processo de mutação e seleção, evolução molecular é o estudo da mudança dos genes e proteínas entre diferentes ramos da árvore da vida
	 A filogenia é a inferência das relaçõe evolutivas. As primeiras ideias sobre filogenia foi concebida lá na Grécia antiga, tendo Aristóteles como o primeiro a desenvolver um pensamento nessa linha. Tradicionalmente, a filogenia era avaliada comparando-se características morfológicas entre organismos de diversas espécies (Mayr, 1982).


# Princípios de filogenia molecular e evolução

	Todas formas vivas possuem uma origem em comum e fazem parte da árvore da vida, mais de 99% das espécies que hora existiram, hoje estão extintas (Wilson, 1992), bizarro. Em princípio, deve existir uma única árvore da vida que precisamente descreve a evolução das espécies. O objetivo da filogenia é deduzir as árvores corretas e também inferir a janela de tempo entre a diferenciação entre organismo a partir do ancestral comum.
	Vale ressaltar, que a definição de evolução não é baseada no predicato de que existe uma única árvore, na verdade, a mutação é compreendida exclusivamente pelo processo de seleção e mutação. Uma árvore verdadeira representa os eventos históricos reais que ocorreram na evolução. É essencialmente impossível gerar uma árvore verdadeira. Em vez disso, geramos árvores inferidas, que representam.
	A árvore da vida possui 3 principais ramificações, bacteria, archea e eucariotos, que juntas reúnem todas as formas de vida conhecidas no planeta a partir de um ancestral comum.
	Na Bioinformática, um dos usos mais corriqueiros da filogenia é a descrição de proteínas e de DNA homológos em uma familía. Qualquer um desses grupos pode ser representado em uma árvore filogenética.
# Contexto Histórico: Globinas, Insulina e os Primeiros Passos da Evolução Molecular

	Duas proteínas são consideradas homologas se elas compartilharem um ancestral comum, ferramentas como o alinhamento BLAST registram os resultados de semelhança ou diferença entre diversos tipos de proteínas, que possivelmente tem uma função semelhante entre indivíduos diferentes. Também é utilizada para a visualização de ortólogos e parólogos, que são genes homólogos, mas se diferenciam pelo modo como divergiram. Ortólogos são dois genes em duas espécies diferentes que compartilham um ancestral comum, enquanto parólogos são dois genes no mesmo genoma que são resultado de um evento de duplicação do gene original.
	Em outra postagem irei mostrar como podemos aplicar uma variedade de abordagens para estudar essas relações entre as proteíans, como a metrica e pontuaçãp  de Dayhoff's, BLAST searching e multiplo alinhamento de sequencias. Será abordado a identificação de dobras de proteínas relacionadas a partir de modelos evolucionarios 

![Filogenia das globinas](/images/Molecular%20Phylogenyand%20Evolution-1786994823567.webp)

<small> Figura 1. Na década de 1960, vários grupos realizaram estudos pioneiros sobre a filogenia das globinas. Esta árvore foi modificada a partir de Dayhoff et al. (1972), que utilizaram a análise de máxima parcimônia para inferir as relações e a história de 13 globinas. A diferença percentual observada entre as sequências foi corrigida utilizando-se os dados das matrizes PAM apresentados na Tabela 3.3. A seta 1 indica um nó correspondente ao último ancestral comum do grupo das globinas de vertebrados, enquanto a seta 2 indica o ancestral das globinas de insetos e vertebrados. Fonte: Dayhoff et al. (1972) </small>

Historicamente, as globinas estão entre as familias de proteínas mais importantes para a compreensão da evolução bioquimica e molecular, desde a identificação da hemoglobina em 1830, da mioglobina em 1860 até a sua cristalização no século 19. As globinas estiveram entre as primeiras proteínas a serem sequenciadas e analisadas por meio de cristalografia de raios X. 
Dando sequência a trabalhos anteriores de Ingram (1961) e outros para determinar as sequências de proteínas globinas, Eck e Dayhoff (1966) utilizaram análise de parcimônia (definida em “Inferência Filogenética: Parcimônia Máxima”, abaixo) para gerar árvores da família das globinas.
A figura abaixo demonstra uma sequência de eventos no qual os genes das Globina foram duplicados e de especiação


![Subfamílias de globinas no tempo evolutivo](/images/Molecular%20Phylogenyand%20Evolution-1786994780823.webp)

Figure 7.2 Dayhoff <small> Figura 2. Dayhoff et al. (1972) resumiram a relação entre as subfamílias de globinas no contexto do tempo evolutivo. As datas dos eventos de especiação foram inferidas a partir de estudos baseados em fósseis. </small>


Estos acerca da insulina no começo dos anos 1950s, foram primordias para a compreensão da visão molecular. 
A insulina é uma pequena proteína secretada por células das ilhotas pancreáticas que estimula a captação de glicose ao ligar-se a um receptor de insulina em células musculares e hepáticas. *Frederick Sanger* e seus colegas em 1953 determinaram a sequência primearia dos aminoacidos da insulina, sendo a primeira proteina na historia a passar por esse feito. Também foram sequênciadas proteínas de outras 5 espécies (Vaca, Ovelha, Porco, Cavalo e Baleia). diferenças de aminoácidos foram restritas a três resíduos dentro de uma região de “alça” dissulfeto da cadeia A (Fig. 7.3b, sombreado em turquesa). Isso sugeriu que as substituições de aminoácidos ocorrem de forma não aleatória, algumas mudanças afetando a atividade biológica de forma drástica e outras tendo efeitos insignificantes (Anfinsen, 1959).

# Teoria do Relógio Molecular

Durante a década de 1960, um grande volume de dados sobre sequências de aminoácidos já havia sido acumulado a partir de diferentes proteínas. Observou-se que proteínas distintas apresentavam diferentes taxas de substituições de aminoácidos ao longo da evolução: enquanto algumas, como os citocromos c, evoluíam mais lentamente, outras acumulavam um número maior de substituições. A partir dessas observações, Emil Zuckerkandl e Linus Pauling (1962), assim como Emanuel Margoliash (1963), propuseram o conceito de relógio molecular. Essa hipótese estabelece que, para um determinado gene ou proteína, a taxa de evolução molecular é aproximadamente constante ao longo do tempo. Em um estudo pioneiro, Zuckerkandl e Pauling compararam as sequências de globinas humanas e observaram diferentes números de substituições de aminoácidos entre as cadeias α, β, γ e δ. Ao comparar as globinas humanas com as de gorilas, foram identificadas apenas duas diferenças na globina α e uma na globina β. Considerando evidências fósseis que indicavam que humanos e gorilas divergiram de um ancestral comum há aproximadamente 11 milhões de anos, essa divergência pôde ser utilizada como ponto de calibração para estimar o tempo de eventos evolutivos anteriores, incluindo duplicações gênicas que deram origem às diferentes famílias de globinas.

![Relógio molecular - proteínas vs tempo](/images/Molecular%20Phylogenyand%20Evolution-1786994404340.webp)

<small> Figura 3. Uma comparação entre o número de alterações de aminoácidos que ocorrem nas proteínas (eixo y) e o tempo decorrido desde a divergência das espécies (eixo x) revela que diferentes famílias de proteínas evoluem a taxas distintas. Algumas proteínas, como os citocromos c de diversos organismos, evoluem muito lentamente; outras, como a hemoglobina, evoluem a uma taxa intermediária; e proteínas como os fibrinopeptídeos sofrem substituições rapidamente. Esse comportamento é descrito pela hipótese do relógio molecular, proposta por Zuckerkandl e Pauling (1962), Margoliash (1963) e outros na década de 1960. O tempo de
divergência de vários organismos (setas) é estimado principalmente com base em evidências fósseis. Abreviação: MY, milhões de anos no passado. </small>

Um estudo fundamental sobre a existência do relógio molecular foi realizado por Richard Dickerson em 1971 (Fig. 7.5). Ele analisou três proteínas com grande quantidade de dados de sequência disponíveis: citocromos _c_, hemoglobinas e fibrinopeptídeos. Para cada uma, Dickerson traçou a relação entre o número de diferenças de aminoácidos entre dois organismos e o tempo de divergência evolutiva estimado por registros paleontológicos. Contudo, ao comparar sequências, tornou-se evidente a necessidade de um modelo estatístico para descrever o processo de substituição, uma vez que mutações múltiplas ou reversões podem ocorrer no mesmo sítio. Consequentemente, o número de eventos mutacionais que realmente ocorreram desde a divergência de um ancestral comum pode ser significativamente maior do que a diferença observada nas sequências atuais.

Para corrigir essa saturação evolutiva e estimar a verdadeira distância entre sequências ($m$) a partir da divergência observada ($n$), utiliza-se o modelo de Dickerson, expresso pela equação:

$$\frac{m}{100} = -\ln\left(1 - \frac{n}{100}\right) \quad \iff \quad \frac{n}{100} = 1 - e^{-\frac{m}{100}}$$
onde m é o número total de alterações de aminoácidos ocorridas em um segmento de 100 aminoácidos de uma proteína, e n é o número observado de alterações de aminoácidos por 100 resíduos. Essa correção compensa as alterações de aminoácidos que ocorrem, mas não são diretamente observadas, como duas ou mais alterações ocorrendo na mesma posição.  
Os resultados deste gráfico (Fig. 4) permitem várias conclusões (Dickerson, 1971):
 - Para cada proteína, os dados situam-se sobre uma linha reta. Isso sugere que a taxa de alteração	da sequência de aminoácidos permaneceu constante para cada proteína.
-  As taxas médias de alteração são distintamente diferentes para cada proteína. Por exemplo,	os fibrinopeptídeos evoluem com uma taxa de substituição muito mais elevada. O tempo (em milhões
   de anos) para que ocorra uma alteração de 1% na sequência de aminoácidos entre duas linhagens	evolutivas divergentes é de 20,0 milhões de anos para o citocromo c, 5,8 milhões de anos para a hemoglobina e 1,1 milhão de anos para os fibrinopeptídeos.
- As variações observadas na taxa de alteração entre famílias de proteínas refletem restrições  funcionais impostas pela seleção natural.

![Taxas de substituição de aminoácidos](/images/Molecular%20Phylogenyand%20Evolution-1786998603226.webp)

<small>Tabela 1. Taxas de substituição de aminoácidos por sítio de aminoácido a cada $10^9$ anos
(λ × 10⁹) em várias proteínas. Dayhoff (1978) expressou essas taxas como mutações pontuais
aceitas (PAMs) por 100 resíduos de aminoácidos que se estima terem ocorrido em
100 milhões de anos de evolução (compare com o Quadro 3.4). A taxa de aceitação de mutação
para a albumina sérica é de 19 PAMs a cada 100 milhões de anos. </small>

Isso é análogo à datação de espécimes geológicos utilizando o decaimento radioativo. Um
exemplo de como o relógio molecular pode ser utilizado é apresentado no Quadro 7.1.
A hipótese do relógio molecular não se aplica a todas as proteínas, e diversas exceções
e ressalvas foram observadas:
 - A taxa de evolução molecular varia entre diferentes organismos. Por exemplo,
   algumas sequências virais tendem a sofrer alterações extremamente rápidas em
   comparação com outras formas de vida.
 - O relógio varia entre diferentes genes (ver Tabela 7.1) e ao longo de diferentes partes
   de um mesmo gene (p. ex., Fig. 7.3; ver também a discussão sobre o parâmetro gama
   em “Etapa 3: Modelos de Substituição de DNA e Aminoácidos”, mais adiante). A
   principal força que rege o relógio molecular é a seleção. Roedores tendem a apresentar
   um relógio molecular mais rápido do que os primatas; isso pode ocorrer porque seus
   tempos de geração são mais curtos e eles possuem taxas metabólicas elevadas.
- O relógio só é aplicável quando o gene em questão mantém sua função ao longo do
  tempo evolutivo. Genes podem tornar-se não funcionais (p. ex., pseudogenes),
  levando a uma rápida alterações na sequência de nucleotídeos (e de aminoácidos). A taxa de evolução, por vezes, acelera-se após a ocorrência da duplicação gênica. Por exemplo, após a duplicação gênica
  ter gerado as hemoglobinas α e β, ocorreram altas taxas de substituição de aminoácidos que,
  presumivelmente, alteraram a função do gene, permitindo que algumas proteínas globinas
  fossem expressas em estágios de desenvolvimento altamente específicos.


# Seleção positiva e negativa

A teoria da evolução de Darwin sugere que, em nível fenotípico, características de uma população
que favorecem a sobrevivência são selecionadas (seleção positiva), enquanto características que reduzem a aptidão são selecionadas contra (seleção negativa). Por exemplo, em um grupo de girafas que viveu há milhões de anos, aquelas que possuíam pescoços mais longos conseguiam alcançar folhagens mais altas e tiveram mais sucesso reprodutivo do que os membros do grupo com pescoços mais curtos; ou seja, houve seleção positiva para a altura.
Em nível molecular, a perspectiva evolutiva convencional é que a seleção positiva e a negativa também atuam sobre as sequências de DNA. Um gene que codifica uma enzima pode sofrer duplicação e, posteriormente, alterações nos nucleotídeos podem permitir que um dos genes duplicados codifique uma enzima com uma nova função, a qual se mostra vantajosa e, portanto, é favorecida pela seleção. Acredita-se que esse processo de seleção positiva tenha ocorrido em duas ocasiões na evolução da lisozima, uma enzima que rompe as ligações do peptideoglicano bacteriano e, assim, atua como proteína antimicrobiana em secreções como leite, saliva e lágrimas. Há cerca de 25 milhões de anos, o gene da lisozima duplicou-se e assumiu uma nova função digestiva no estômago do ancestral de cabras, vacas e cervos. O surgimento dessa nova função ocorreu de forma independente em macacos folívoros, como o langur, há cerca de 15 milhões de anos (Jollès et al., 1990). Em cada um desses casos, a taxa de substituição de aminoácidos aumentou devido à seleção positiva, à medida que a lisozima assumia uma nova função.
Existem várias maneiras de avaliar se ocorreu seleção em dados de sequência.
Uma abordagem baseia-se no fato de que a porção do DNA que codifica uma proteína pode
apresentar tanto substituições sinônimas quanto não sinônimas. No caso de uma alteração
nucleotídica em um determinado códon, uma substituição sinônima não resulta em mudança
no aminoácido especificado. 
![Alinhamento beta-globina](/images/Molecular%20Phylogeny%20Evolution-1787001746703.webp)

<small>Figura 4. Árvores filogenéticas podem ser construídas usando dados de sequências de DNA, RNA ou proteínas. Frequentemente, a sequência de DNA é mais informativa do que a proteína na análise filogenética. Como exemplo, as sequências de beta-globina de três espécies são alinhadas na extremidade 5′ do DNA (com as terminações amino correspondentes das proteínas). Nas regiões não traduzidas 5′ e 3′, onde nenhuma proteína é codificada, normalmente há menos pressão seletiva para manter resíduos de nucleotídeos específicos. (Alguns elementos regulatórios podem ser altamente conservados.) Aqui, apenas uma posição de nucleotídeo varia (seta). Dentro da região codificadora de proteínas, existem resíduos de aminoácidos variantes nas posições 6, 7 e 11 (veja as pontas de seta verdes). Essas variantes podem ser informativas na realização da filogenia. No entanto, há um número ainda maior de alterações de nucleotídeos informativas, restringindo nossa atenção à região codificadora. Existem seis posições com alterações nucleotídicas sinônimas (nucleotídeos sombreados em azul; veja os códons 3, 7 e 10–12) que não resultam na especificação de um aminoácido diferente. Existem também seis posições com alterações não sinônimas que causam uma mudança no aminoácido (pontas de seta e nucleotídeos vermelhos). Para uma delas (códon 6 da sequência canina), uma alteração de um único nucleotídeo, C→G, em relação às sequências de primatas, é responsável pela mudança no aminoácido. Para outros três códons não sinônimos, dois nucleotídeos são alterados em relação às sequências de primatas. As sequências de beta-globina são de humanos (acesso GenBank NM_000518.4) e chimpanzés (Pan troglodytes; XM_5082).</small>

Por exemplo, considere um alinhamento das sequências de DNA
da beta-globina de humanos, chimpanzés, camundongos e cães em suas extremidades 5′
(terminais amino das proteínas; Fig. 7.7). No terceiro códon, os nucleotídeos CAT nas
sequências de humanos e cães codificam uma histidina. A alteração da terceira posição
para CAC nas sequências de chimpanzés e camundongos não altera o aminoácido codificado.
Outras alterações sinônimas são evidentes (Fig. 7.7, nucleotídeos em vermelho). Uma
substituição não sinônima altera o aminoácido especificado. Por exemplo, a beta-globina
de humanos e chimpanzés possui um códon CCT que especifica uma prolina, mas a
sequência canina correspondente apresenta uma única substituição que resulta em um
códon (GCT) especificando uma alanina (Fig. 7.7, códon 6). A comparação das taxas de substituição não sinônima por sítio não sinônimo (d̂N) versus substituição sinônima por sítio sinônimo (d̂S) pode revelar evidências de seleção positiva ou negativa. Se d̂S for maior que d̂N, isso sugere que a sequência de DNA está sob seleção negativa ou purificadora. A seleção negativa limita a mudança em uma sequência de aminoácidos correspondente; isso ocorre quando algum aspecto da estrutura e/ou função de uma proteína é crítico e não tolera substituições. Quando d̂N é maior que d̂S, isso ...sugere que ocorre seleção positiva. Um exemplo de seleção positiva é um gene duplicado que está sob pressão para evoluir novas funções. 

Em 1978, 500 mulheres foram inadvertidamente infectadas pelo vírus da hepatite C (HCV). Stuart Ray e colegas (2005) sequenciaram
uma porção de 5,2 quilobases do genoma do HCV proveniente do inóculo original e de
22 mulheres, cerca de 20 anos após a infecção. Eles demonstraram a existência de *loci*
sob seleção tanto positiva quanto negativa, refletindo a evolução do vírus para
otimizar sua aptidão (*fitness*) em cada hospedeiro. Por exemplo, substituições de
aminoácidos em epítopos conhecidos divergiram da sequência consenso em indivíduos
que possuíam o alelo do antígeno leucocitário humano (HLA) para aquele epítopo,
indicando um mecanismo de seleção imune. Em outro estudo, Cox *et al.* (2005) estudaram a variação de sequência do HCV antes, durante e após a infecção pelo vírus. Eles demonstraram que as substituições de aminoácidos refletem o escape do reconhecimento por células T; nos indivíduos com infecção persistente, houve pressões seletivas sobre epítopos que resultaram em alterações não sinônimas. Os resultados de Ray et al. (2005) e Cox et al. (2005) exemplificam a utilidade de estudos longitudinais na filogenia e revelam mecanismos pelos quais a seleção positiva e a seleção natural moldam a aptidão dos vírus.

