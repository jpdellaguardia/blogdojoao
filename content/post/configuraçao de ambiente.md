---
title: Como Configurar um Ambiente de Bioinformática com Python ,Docker e R
draft: false
date: 2026-08-18
---
<img src="/images/configura-ao-de-ambiente-1787097824922.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />
# Neste Tutorial você vai

-  Instalar os softwares necessários com Anaconda
-  Instalar os softwares necessários com Docker
-  Criar interface com **R* ** via **rpy2**

#Python #Bioinformatica #DNA #RNA #Sequenciamento

<!--more-->
# Configuração do Python e Ecosistema de Desenvolvimeto

Nesta publicação vou orientar como você pode configurar o seu ambiênte de desenvolvimento para dar seus primeiros passos no mundo da Bioinformática através da distribuição **Python**.  Aqui, também estará incluso uma breve demonstração de como você pode integrar a linguagem **R** ao **rpy2**, que é outra poderosa ferramenta de desenvolviimento no campo da Bioinformática e Ciências Biológicas em geral.

*Disclaimer 01*. Existem diversas formas que você pode utilizar para performar essas análises, nesta postagem, vou ensinar 2 abordagens diferentes, uma utilizando o **Anaconda Python** (http://docs.continuum.io/anaconda/) e outra utilizando abordagem insntalar o software via *Docker* (Um servidor que permite fazer virtualização que trás uma série de beneficios, principalmente se você pretender compartilhar o seu código) em geral, um notebook simples com no mínimo 4GB de RAM deve ser capaz de reproduzir integralmente este tutorial.

*Disclairme 02.* Se você usa Windows, deixe de usar, fim de tutorial. Brincadeira, considere instalar o Linux na sua maquina, seja por dual boot, ou se você quiser insistir com o Windows, use o Linux através do terminal do **WSL2**, pois não vou abordar as configurações específicas para o Windows, apesar de que todo o passo a passo seja básicamente o mesmo e você quebrando um pouco a cabeça deve ser capaz de deduzir. Enfatizando, este tutorial será voltado para um âmbiente de desenvolvimento através dos comandos Linux que é o padrão utilizado para análises avançadas. **Sequênciamento de nova Geração (NGS)**, Análise de Dados e Machine Learning são mais performáticos em cluster Linuxs. Para os usuários de MACos, os comandos e os passos são os mesmos.

# Dependências

Antes de instalar o Python propriamente dito, você tera que instalar softwares externos ao Python que irão atuar em conjunto, a lista varia de acordo com qual atividade específica você está buscando, seja um alinhamento de sequências BLAST de RNA, DNA, Proteína, sejá a produção de gráficos estatísticos, Machine Learning. Fortuitamente, a maioria desses softwares estão disponíveis via projeto *Bioconda*, facilitando assim a nossa vida.
Antes de tudo, no seu sistema Linux será necessária a intalação de compiladores e bibliotecas, principalmente para aqueles que estão usando via WSL2, considere instalar o build-essential package (sudo apt-get install build-essential), para macOS utilize Xcode (https://developer.apple.com/xcode/)
Na tabela abaixo você encontrará a lista com os softwares mais importantes para aprender bioinformatica com Python.

| **Biblioteca** | **Foco/Uso**                       | **URL**                                                                                | **Descrição**                      |
| -------------- | ---------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------- |
| pandas         | Análise e Manipulação de Dados     | [https://pandas.pydata.org/](https://pandas.pydata.org/)                               | Data processing                    |
| NumPy          | Computação Numérica Fundamental    | [http://www.numpy.org/](http://www.numpy.org/)                                         | Array/matrix processing            |
| SciPy          | Computação Científica Avançada     | [http://www.scipy.org/](http://www.scipy.org/)                                         | Scientific computing               |
| Biopython      | Bioinformática de Uso Geral        | [https://biopython.org/](https://biopython.org/)                                       | Bioinformatics library             |
| seaborn        | Visualização de Dados Estatísticos | [http://seaborn.pydata.org/](http://seaborn.pydata.org/)                               | Statistical chart library          |
| R              | Bioinformatics and Statistics      | [https://www.r-project.org/](https://www.r-project.org/)                               | Language for statistical computing |
| rpy2           | R connectivity                     | [https://rpy2.readthedocs.io](https://rpy2.readthedocs.io/)                            | R interface                        |
| PyVCF          | NGS                                | [https://pyvcf.readthedocs.io](https://pyvcf.readthedocs.io/)                          | VCF processing                     |
| Pysam          | NGS                                | [https://github.com/pysam-developers/pysam](https://github.com/pysam-developers/pysam) | SAM/BAM processing                 |
| HTSeq          | NGS/Genomes                        | [https://htseq.readthedocs.io](https://htseq.readthedocs.io/)                          | NGS processing                     |
| DendroPY       | Phylogenetics                      | [https://dendropy.org/](https://dendropy.org/)                                         | Phylogenetics                      |
| PyMol          | Proteomics                         | [https://pymol.org](https://pymol.org/)                                                | Molecular visualization            |
| scikit-learn   | Machine learning                   | [http://scikit-learn.org](http://scikit-learn.org/)                                    | Machine learning library           |
| Cython         | Big data                           | [http://cython.org/](http://cython.org/)                                               | High performance                   |
| Dask           | Big data                           | [http://dask.pydata.org](https://www.google.com/search?q=http://dask.pydata.org)       | Parallel processing                |
<small> Figura 1.1 - Tabela mostrando vários pacotes de software úteis na Bioinformática </small>

# Primeiros passos - Anaconda

1. Começe fazendo o dowload da distribuição Anaconda

text [https://www.anaconda.com/download](https://www.anaconda.com/download)  abra o terminal na pasta onde o instalador (.sh) foi baixado, execute o comando Testarei utilizando a versão xx.xx



