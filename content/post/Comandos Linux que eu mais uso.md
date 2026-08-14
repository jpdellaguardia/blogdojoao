


ffmpeg -i video.mp4 -an -vf "scale=1280:-2:flags=lanczos" -c:v libx264 -profile:v high -level 4.0 -pix_fmt yuv420p -crf 22 -movflags +faststart output.mp4

python -m venv venv
source venv/bin/activate

---

title: "{{ replace .Name "-" " " | title }}"  
date: {{ .Date }}  
draft: true

description: "Uma breve descrição do que este post aborda."

categories:

- "Pessoal"
    

tags:

- ""
    

## subject: ""

## Introdução

Escreva aqui uma introdução curta e pessoal sobre o assunto.

Explique rapidamente **o que aconteceu**, **por que isso chamou sua atenção** ou **por que você decidiu escrever sobre isso**.

---

## O que aconteceu?

Conte a história ou apresente o assunto.

Prefira escrever de maneira natural, como se estivesse contando para alguém o que descobriu.

Você pode inserir imagens normalmente:

<img src="/images/exemplo.webp" style="max-width: 100% !important; height: auto !important; max-height: 450px !important; object-fit: contain !important; display: block !important; margin: 1rem auto !important; border-radius: 6px !important;" />

---

## Algumas coisas que achei interessantes

- Primeiro ponto interessante
    
- Segundo ponto interessante
    
- Terceiro ponto interessante
    

Ou simplesmente continue escrevendo em parágrafos quando uma lista não fizer sentido.

> **Uma observação pessoal:** coloque aqui uma conclusão, curiosidade ou comentário que você queira destacar.

---

## Mais sobre isso

Desenvolva aqui a parte mais interessante do post.

Você pode adicionar:

- imagens;
    
- vídeos;
    
- gráficos;
    
- código;
    
- links;
    
- tabelas;
    
- citações;
    
- referências.
    

### Um detalhe interessante

Use subtítulos menores quando precisar dividir uma seção.

---

## Minha opinião

Aqui entra a parte mais pessoal do texto.

O que você achou?

O que mudou sua percepção?

Você faria algo diferente?

---

## Conclusão

Finalize o texto de maneira natural.

Não precisa necessariamente fazer uma conclusão acadêmica. Para um blog pessoal, pode ser simplesmente uma última observação, uma reflexão ou algo que você pretende fazer depois.

> **Nota:** caso exista alguma informação importante que precise de contexto ou ressalva, coloque-a aqui.

---

**Publicado em:** {{ .Date.Format "02/01/2006" }}