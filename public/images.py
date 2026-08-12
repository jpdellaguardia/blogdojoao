import os
import re
import shutil
from urllib.parse import quote

# 1. Diretórios configurados
posts_dir = "/home/aquila/projetos/blogdojoao/content/post/"
attachments_dir = "/home/aquila/Documentos/Obsidian Vault/images/"
static_images_dir = "/home/aquila/projetos/blogdojoao/static/images/"

# Garante que a pasta static/images exista
os.makedirs(static_images_dir, exist_ok=True)

# Regex para capturar tanto ![[imagem.png]] quanto ![[imagem.png|largura]]
image_regex = r'!\[\[(.*?\.(?:png|jpg|jpeg|gif|svg|webp))(?:\|.*?)?\]\]'

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        images = re.findall(image_regex, content, re.IGNORECASE)

        for img in images:
            src_img = os.path.join(attachments_dir, img)
            dst_img = os.path.join(static_images_dir, img)

            # Copia a imagem da pasta de anexos do Obsidian para a pasta static do Hugo
            if os.path.exists(src_img):
                shutil.copy(src_img, dst_img)
                print(f"📷 Imagem copiada: {img}")
            else:
                print(f"⚠️ Imagem não encontrada na pasta de anexos: {src_img}")

            # Codifica os espaços da URL (ex: 'Pasted image.png' -> 'Pasted%20image.png')
            encoded_img = quote(img)
            markdown_image = f'![{img}](/images/{encoded_img})'
            
            # Substitui a tag do Obsidian pela sintaxe nativa do Markdown do Hugo
            content = re.sub(rf'!\[\[{re.escape(img)}(?:\|.*?)?\]\]', markdown_image, content)

        # Atualiza a nota do Hugo
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("✅ Processamento de imagens concluído com sucesso!")