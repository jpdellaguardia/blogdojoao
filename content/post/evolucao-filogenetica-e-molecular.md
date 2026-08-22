---
title: "Evolução filogenética e molecular"
date: 2026-08-17
draft: false
author: "João Pedro Della Guardia"
type: "Curiosidade"
subject: "Evolução filogenética e molecular"
categories: ["Biomol", "Filogenia", "Evolução", "Bioinformática"]
---
<img src="/images/evolucao-filogenetica-e-molecular-1787428764387.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />

> *“Nothing in biology makes sense except in the light of evolution.”*  
> — Theodosius Dobzhansky, 1973

## Objetivos de aprendizagem

Ao final deste estudo, você deverá ser capaz de:

- Descrever a hipótese do relógio molecular e explicar sua importância.
- Definir seleção positiva e negativa e reconhecer seus efeitos em sequências biológicas.
- Descrever os principais tipos de árvores filogenéticas e seus componentes.
- Construir árvores filogenéticas utilizando métodos baseados em distância e em caracteres.
- Interpretar relações evolutivas entre genes, proteínas e organismos.

## 1. Compreendendo a evolução

A evolução biológica pode ser entendida como o processo pelo qual as características das populações se modificam ao longo das gerações. Embora a hereditariedade preserve grande parte das características entre pais e descendentes, novas variantes podem surgir e alterar a composição genética das populações.

Entre os principais mecanismos associados à mudança evolutiva estão a **mutação**, a **recombinação genética**, a **seleção natural** e a **deriva genética**. Na reprodução sexuada, a recombinação reorganiza variantes presentes nos genomas parentais, produzindo novas combinações genéticas. As mutações, por sua vez, introduzem novas variantes de sequência.

No nível molecular, a evolução pode ser estudada por meio das alterações acumuladas em sequências de DNA, RNA e proteínas. A **evolução molecular** investiga justamente essas mudanças, enquanto a **filogenia** busca inferir as relações de ancestralidade e descendência entre diferentes organismos, genes ou proteínas.

## 2. Princípios de filogenia molecular e evolução

A filogenia molecular parte do princípio de que organismos, genes e proteínas podem compartilhar ancestrais comuns. O objetivo é utilizar características observáveis — especialmente sequências moleculares — para inferir uma história evolutiva plausível.

Uma árvore filogenética representa uma hipótese sobre essas relações. Os **nós internos** representam ancestrais comuns hipotéticos, enquanto as **ramificações** representam linhagens evolutivas. A raiz, quando presente, indica a direção temporal da evolução.

Na prática, a chamada “árvore verdadeira”, isto é, a representação exata de todos os eventos históricos que ocorreram durante a evolução, não pode ser observada diretamente. O que produzimos são **árvores inferidas**, obtidas a partir de modelos e métodos estatísticos ou de otimização.

A filogenia molecular possui diversas aplicações na bioinformática, incluindo a análise de famílias de proteínas, a identificação de genes homólogos e o estudo das relações entre sequências.

### 2.1 Homologia, ortologia e paralogia

Duas proteínas ou sequências são consideradas **homólogas** quando compartilham um ancestral evolutivo comum. A homologia não é uma medida de similaridade: duas sequências são ou não homólogas, enquanto a similaridade é uma propriedade que pode ser quantificada.

Entre os genes homólogos, é importante distinguir:

- **Ortólogos:** genes presentes em espécies diferentes que descendem de um ancestral comum separado por um evento de especiação.
- **Parálogos:** genes originados por um evento de duplicação gênica, podendo posteriormente adquirir funções distintas.

Ferramentas como o **BLAST** podem ser utilizadas para identificar sequências semelhantes e auxiliar na investigação dessas relações. Em análises filogenéticas mais aprofundadas, alinhamentos múltiplos, modelos de substituição e métodos de reconstrução de árvores permitem investigar a história evolutiva dessas sequências.

## 3. Contexto histórico: globinas, insulina e os primeiros estudos moleculares

As globinas estão entre as famílias de proteínas mais importantes para o desenvolvimento da biologia molecular evolutiva. A hemoglobina começou a ser investigada no século XIX, seguida pela mioglobina e, posteriormente, pela determinação de suas estruturas e sequências.

Trabalhos pioneiros de Ingram (1961) e de outros pesquisadores contribuíram para a determinação das sequências de proteínas globinas. Posteriormente, Eck e Dayhoff (1966) utilizaram métodos de análise filogenética, incluindo a **parcimônia**, para investigar as relações evolutivas entre diferentes globinas.
<img src="/images/evolucao-filogenetica-e-molecular-1787429342152.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />
![Relações filogenéticas entre globinas]

**Figura 1 —** Relações filogenéticas entre globinas. A árvore foi adaptada de Dayhoff et al. (1972), que utilizaram máxima parcimônia para inferir as relações entre 13 globinas. As diferenças observadas entre as sequências foram corrigidas utilizando dados das matrizes PAM. A seta 1 indica o nó correspondente ao último ancestral comum das globinas de vertebrados, enquanto a seta 2 indica o ancestral comum das globinas de insetos e vertebrados.  
**Fonte:** Adaptado de Dayhoff et al. (1972).

As análises das globinas permitiram reconstruir uma sequência de eventos envolvendo **duplicações gênicas** e **eventos de especiação**, oferecendo uma das primeiras demonstrações de como sequências proteicas poderiam ser utilizadas para investigar a história evolutiva.
<img src="/images/evolucao-filogenetica-e-molecular-1787429377615.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />
**Figura 2 —** Relações entre subfamílias de globinas no contexto do tempo evolutivo. As datas dos eventos de especiação foram estimadas com base em evidências paleontológicas.  
**Fonte:** Adaptado de Dayhoff et al. (1972). Reproduzido com permissão da National Biomedical Research Foundation.

Outro marco importante ocorreu no início da década de 1950, quando **Frederick Sanger e colaboradores determinaram, em 1953, a sequência primária de aminoácidos da insulina**, estabelecendo um importante precedente para o estudo molecular das proteínas.

Sequências de insulina de diferentes espécies — incluindo vaca, ovelha, porco, cavalo e baleia — também foram determinadas. As diferenças observadas estavam concentradas em poucos resíduos de aminoácidos, particularmente em uma região da cadeia A. Esses resultados contribuíram para demonstrar que as substituições de aminoácidos não ocorrem de maneira aleatória: algumas alterações podem comprometer fortemente a função de uma proteína, enquanto outras possuem efeitos funcionais relativamente pequenos.

## 4. A hipótese do relógio molecular

Durante a década de 1960, um grande volume de dados sobre sequências de aminoácidos já havia sido acumulado a partir de diferentes proteínas. Observou-se que proteínas distintas apresentavam diferentes taxas de substituição ao longo da evolução: algumas, como os citocromos *c*, evoluíam lentamente, enquanto outras famílias acumulavam um número maior de substituições.

A partir dessas observações, **Emil Zuckerkandl e Linus Pauling (1962)**, assim como **Emanuel Margoliash (1963)**, propuseram o conceito de **relógio molecular**. A hipótese estabelece que, para um determinado gene ou proteína, a taxa de evolução molecular pode permanecer aproximadamente constante ao longo do tempo.

Em um estudo pioneiro, Zuckerkandl e Pauling compararam sequências de globinas humanas e observaram diferentes números de substituições de aminoácidos entre as cadeias α, β, γ e δ.

Ao comparar as globinas humanas com as de gorilas, foram identificadas apenas duas diferenças na globina α e uma na globina β. Considerando evidências fósseis que indicavam uma divergência entre humanos e gorilas a partir de um ancestral comum há aproximadamente 11 milhões de anos, essa divergência pôde ser utilizada como **ponto de calibração** para estimar o tempo de eventos evolutivos anteriores, incluindo duplicações gênicas que deram origem a diferentes famílias de globinas.

## 5. Evidências experimentais do relógio molecular

Um estudo fundamental sobre a existência do relógio molecular foi realizado por **Richard Dickerson em 1971**. O pesquisador analisou três proteínas para as quais havia grande quantidade de dados de sequência disponíveis: **citocromos *c*, hemoglobinas e fibrinopeptídeos**.

Para cada proteína, Dickerson relacionou o número de diferenças de aminoácidos entre dois organismos ao tempo de divergência evolutiva estimado a partir de evidências paleontológicas.
<img src="/images/evolucao-filogenetica-e-molecular-1787429474060.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />
**Figura 3 —** Relação entre o número de alterações de aminoácidos e o tempo decorrido desde a divergência entre espécies. Diferentes famílias de proteínas apresentam diferentes taxas de evolução molecular. Citocromo *c* apresenta evolução relativamente lenta, hemoglobina apresenta taxa intermediária e fibrinopeptídeos apresentam uma taxa de substituição mais elevada.  
**Fonte:** Adaptado de Dickerson (1971).

Os resultados apresentaram uma relação aproximadamente linear para cada proteína, sugerindo que a taxa de alteração da sequência de aminoácidos poderia ser relativamente constante dentro de cada família proteica.

Entretanto, uma dificuldade importante surge quando tentamos estimar o número real de substituições a partir das diferenças observadas entre duas sequências. Uma mesma posição pode sofrer **múltiplas substituições** ao longo do tempo, e algumas dessas alterações deixam de ser observáveis na comparação final. Assim, o número de eventos evolutivos efetivamente ocorridos pode ser maior que o número de diferenças atualmente observadas.

Esse problema, conhecido como **saturação de substituições**, exige a utilização de modelos matemáticos para corrigir a distância observada.

### 5.1 Correção para múltiplas substituições

Para estimar a distância evolutiva corrigida, Dickerson utilizou uma relação originalmente proposta por Margoliash e Smith (1965) e por Zuckerkandl e Pauling (1965):

$$
\frac{m}{100}
=
-\ln\left(1-\frac{n}{100}\right)
$$

ou, equivalentemente,

$$
\frac{n}{100}
=
1-e^{-m/100}
$$

onde:

- $m$ representa o número total estimado de alterações de aminoácidos ocorridas em um segmento de 100 resíduos;
- $n$ representa o número de diferenças de aminoácidos efetivamente observadas por 100 resíduos.

A correção permite considerar alterações que ocorreram, mas não podem ser observadas diretamente na sequência atual, como duas ou mais substituições ocorrendo no mesmo sítio.

## 6. Diferentes proteínas possuem diferentes relógios

Os resultados de Dickerson (1971) permitiram estabelecer três observações importantes.

**Primeiro**, para cada proteína, os dados apresentavam aproximadamente uma relação linear entre divergência molecular e tempo. Isso é compatível com a ideia de uma taxa de evolução relativamente constante.

**Segundo**, as taxas médias de substituição eram diferentes entre as famílias de proteínas. Para uma alteração de aproximadamente 1% na sequência de aminoácidos entre duas linhagens divergentes, foram estimados cerca de:

| Proteína         | Tempo aproximado para 1% de alteração |
| ---------------- | ------------------------------------: |
| Citocromo *c*    |                  20,0 milhões de anos |
| Hemoglobina      |                   5,8 milhões de anos |
| Fibrinopeptídeos |                    1,1 milhão de anos |

Os fibrinopeptídeos, portanto, apresentavam uma taxa de substituição muito superior à observada para o citocromo *c*.

**Terceiro**, essas diferenças nas taxas de evolução refletem, em parte, as **restrições funcionais impostas pela seleção natural**. Proteínas essenciais para funções altamente conservadas tendem a tolerar menos alterações, enquanto proteínas submetidas a menores restrições funcionais podem acumular substituições com maior frequência.

## 7. Mutação, substituição e seleção natural

É importante distinguir **mutação** de **substituição**.

A mutação corresponde ao processo que produz uma alteração na sequência de DNA ou RNA. A substituição, por outro lado, corresponde à alteração de sequência que é observada e pode eventualmente ser fixada em uma população.

Assim, a taxa de substituição não depende exclusivamente da taxa de mutação. Ela também é influenciada pela **seleção natural**.

Uma mutação pode ser:

- **Deletéria:** reduz a aptidão do organismo e tende a ser eliminada pela seleção negativa.
- **Neutra ou aproximadamente neutra:** apresenta pouco ou nenhum efeito relevante sobre a aptidão.
- **Vantajosa:** aumenta a aptidão em determinado contexto e pode ser favorecida pela seleção positiva.

Isso ajuda a explicar por que algumas proteínas, como **histonas e ubiquitina**, apresentam taxas de substituição extremamente baixas. Alterações nessas proteínas podem ser fortemente prejudiciais porque suas funções são altamente conservadas.

Portanto, dizer que uma proteína “evolui lentamente” não significa necessariamente que ela sofre poucas mutações. Significa que poucas das alterações que surgem são toleradas e permanecem como substituições observáveis ao longo da evolução.
<img src="/images/evolucao-filogenetica-e-molecular-1787429508859.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />**Tabela 1 —** Taxas de substituição de aminoácidos por sítio em diferentes proteínas. As taxas são expressas como $\lambda \times 10^9$ substituições por sítio por ano. Dayhoff (1978) também expressou essas taxas em unidades PAM, correspondentes ao número de mutações pontuais aceitas por 100 resíduos de aminoácidos durante 100 milhões de anos de evolução.  
**Fonte:** Adaptado de Dayhoff (1978).

## 8. Limitações da hipótese do relógio molecular

Embora o relógio molecular seja uma ferramenta importante, sua aplicação exige cautela. A hipótese de uma taxa constante de evolução não é universal.

A taxa de evolução molecular pode variar:

- entre diferentes organismos;
- entre diferentes genes;
- entre diferentes regiões de um mesmo gene;
- antes e depois de eventos de duplicação gênica;
- de acordo com as pressões seletivas atuantes sobre determinada sequência.

Por exemplo, algumas sequências virais apresentam taxas de evolução extremamente elevadas. Da mesma forma, roedores podem apresentar taxas moleculares diferentes das observadas em primatas, possivelmente relacionadas, entre outros fatores, aos seus tempos de geração e às suas taxas metabólicas.

Outro problema ocorre quando um gene perde sua função. Genes que se tornam **pseudogenes**, por exemplo, podem acumular alterações de sequência muito mais rapidamente porque deixam de estar submetidos às mesmas restrições funcionais.

A duplicação gênica também pode alterar a dinâmica evolutiva. Após a duplicação que originou as hemoglobinas α e β, diferentes linhagens de globinas puderam acumular substituições e, posteriormente, adquirir padrões distintos de expressão e função.

## 9. Importância do relógio molecular para a filogenia

Uma das principais implicações da hipótese do relógio molecular é a possibilidade de utilizar diferenças acumuladas em sequências moleculares para **estimar o tempo de divergência entre linhagens**.

Quando uma taxa de substituição pode ser estimada e calibrada utilizando um evento evolutivo cuja idade seja conhecida — por exemplo, um evento de divergência apoiado por evidências fósseis — as sequências de DNA, RNA ou proteínas podem ser utilizadas como marcadores temporais.

Dessa maneira, o relógio molecular conecta duas dimensões da evolução:

**divergência de sequência → distância evolutiva → estimativa de tempo → reconstrução filogenética**

A abordagem tornou-se fundamental para a filogenia molecular e para a compreensão da história evolutiva dos organismos, permitindo investigar eventos que dificilmente poderiam ser reconstruídos apenas por meio do registro fóssil.

---

## Referências principais

- Dayhoff, M. O. et al. (1972). Estudos pioneiros sobre filogenia de globinas.
- Dayhoff, M. O. (1978). *Atlas of Protein Sequence and Structure*.
- Dickerson, R. E. (1971). Estudos sobre a relação entre divergência de proteínas e tempo evolutivo.
- Margoliash, E. (1963). Estudos sobre a evolução molecular de proteínas.
- Margoliash, E.; Smith, E. L. (1965). Estudos sobre diferenças observadas e substituições efetivas.
- Zuckerkandl, E.; Pauling, L. (1962). Estudos pioneiros sobre o relógio molecular.
- Zuckerkandl, E.; Pauling, L. (1965). Estudos sobre evolução molecular e substituições.
