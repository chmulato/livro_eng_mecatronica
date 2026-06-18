import os
import re

WORKSPACE_DIR = r"D:\onedrive\outros\workspace_book"
CAPITULOS_DIR = os.path.join(WORKSPACE_DIR, "capitulos")
OUTPUT_HTML = os.path.join(WORKSPACE_DIR, "romance_instrutivo.html")

def format_markdown_to_html(content):
    # Formata negrito e itálico básico
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
    
    # Processar equações LaTeX inline simples
    content = content.replace("$$", "").replace("$", "")
    
    # Processar blocos de código
    def code_repl(match):
        code = match.group(1).strip()
        lines = code.split('\n')
        if lines and lines[0] in ['python', 'cpp', 'assembly', 'c++', 'asm']:
            lines = lines[1:]
        clean_code = '\n'.join(lines)
        clean_code = clean_code.replace('<', '&lt;').replace('>', '&gt;')
        return f'<pre><code>{clean_code}</code></pre>'
    
    content = re.sub(r'```([\s\S]*?)```', code_repl, content)
    
    lines = content.split('\n')
    formatted_lines = []
    in_diary = False
    diary_buffer = []
    
    for line in lines:
        line_str = line.strip()
        if not line_str:
            if in_diary:
                formatted_lines.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                in_diary = False
                diary_buffer = []
            continue
            
        is_diary = line_str.startswith('*“') or line_str.startswith('“') or line_str.startswith('>') or in_diary
        
        if line_str.startswith('# '):
            if in_diary:
                formatted_lines.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                in_diary = False
                diary_buffer = []
            formatted_lines.append(f'<h1 class="chapter-title">{line_str[2:]}</h1>')
        elif line_str.startswith('## '):
            if in_diary:
                formatted_lines.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                in_diary = False
                diary_buffer = []
            formatted_lines.append(f'<h2>{line_str[3:]}</h2>')
        elif line_str.startswith('### '):
            if in_diary:
                formatted_lines.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                in_diary = False
                diary_buffer = []
            formatted_lines.append(f'<h3>{line_str[4:]}</h3>')
            
        elif line_str.startswith('* ') or line_str.startswith('- '):
            if in_diary:
                formatted_lines.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                in_diary = False
                diary_buffer = []
            formatted_lines.append(f'<li>{line_str[2:]}</li>')
            
        elif line_str.startswith('*“') or line_str.startswith('“') or line_str.startswith('>'):
            in_diary = True
            diary_buffer.append(line_str.lstrip('>').strip())
            
        elif in_diary:
            diary_buffer.append(line_str)
            
        else:
            if line_str.startswith('<pre>') or line_str.endswith('</pre>'):
                formatted_lines.append(line_str)
            else:
                # Se for um parágrafo de texto normal, adicionamos uma classe para estilizá-lo
                # com as diretrizes do modo narrativo (ritmo literário, legibilidade).
                # Para diferenciar tecnicismo e prosa, aplicamos narrative-p por padrão.
                formatted_lines.append(f'<p class="narrative-p">{line_str}</p>')
                
    if in_diary:
        formatted_lines.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
        
    return '\n'.join(formatted_lines)

def main():
    print("Iniciando compilação do livro em formato HTML Mobile-First...")
    
    html_start = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>A Rebeldia da Mecatrônica - Romance Instrutivo</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0f172a;
            --header-bg: #1e293b;
            --text-color: #f1f5f9;
            --text-muted: #94a3b8;
            --primary: #d95d14;
            --primary-glow: rgba(217, 93, 20, 0.15);
            --secondary: #3b82f6;
            --card-bg: rgba(30, 41, 59, 0.7);
            --border-color: #334155;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: 'Verdana', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.55;
            padding-top: 60px; /* Espaço para o header fixo */
        }

        /* Top Bar Fixo para Celulares */
        .mobile-header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 60px;
            background-color: var(--header-bg);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 1rem;
            z-index: 100;
        }

        .header-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 0.5px;
        }

        .menu-button {
            background: none;
            border: none;
            color: var(--text-color);
            font-size: 1.5rem;
            cursor: pointer;
            padding: 5px;
            display: flex;
            align-items: center;
        }

        /* Menu de Navegação Drawer (Slide-in) */
        .nav-drawer {
            position: fixed;
            top: 60px;
            bottom: 0;
            left: -100%;
            width: 85%;
            max-width: 300px;
            background-color: var(--header-bg);
            border-right: 1px solid var(--border-color);
            z-index: 99;
            transition: left 0.3s ease;
            overflow-y: auto;
            padding: 1.5rem;
        }

        .nav-drawer.open {
            left: 0;
        }

        .nav-drawer h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.2rem;
            color: var(--primary);
            margin-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
        }

        .nav-drawer ul {
            list-style: none;
        }

        .nav-drawer li {
            margin-bottom: 0.6rem;
        }

        .nav-drawer a {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.9rem;
            display: block;
            padding: 0.5rem;
            border-radius: 6px;
            transition: background 0.2s;
        }

        .nav-drawer a.active, .nav-drawer a:hover {
            color: #ffffff;
            background-color: var(--bg-color);
            border-left: 3px solid var(--primary);
            padding-left: 0.7rem;
        }

        /* Overlay escuro quando o menu estiver aberto */
        .overlay {
            position: fixed;
            top: 60px;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0,0,0,0.5);
            z-index: 98;
            display: none;
        }

        .overlay.show {
            display: block;
        }

        /* Container de Conteúdo (Mobile-First) */
        .content-container {
            width: 100%;
            max-width: 650px;
            margin: 0 auto;
            padding: 1.2rem;
        }

        /* Capa lúdica responsiva */
        .cover-section {
            text-align: center;
            padding: 2rem 0;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 3rem;
        }

        .cover-image {
            width: 100%;
            max-width: 240px;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5), 0 0 20px var(--primary-glow);
            margin-bottom: 1.5rem;
            border: 1px solid var(--border-color);
        }

        .cover-title {
            font-family: 'Outfit', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #ffffff;
        }

        .cover-subtitle {
            font-size: 1rem;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }

        /* Botão CTA para Download do PDF */
        .download-cta-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: var(--primary);
            color: #ffffff;
            text-decoration: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 700;
            margin: 1rem 0;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(217, 93, 20, 0.4);
            border: 1px solid rgba(255,255,255,0.1);
        }

        .download-cta-btn:hover {
            background-color: #f97316;
            box-shadow: 0 6px 20px rgba(217, 93, 20, 0.6);
            transform: translateY(-2px);
        }

        /* Dedicatória */
        .dedication {
            font-style: italic;
            font-size: 1rem;
            color: var(--text-muted);
            text-align: center;
            margin: 2rem auto;
            line-height: 1.6;
            padding: 0 10px;
        }

        /* Capítulos e Seções */
        .chapter-section {
            margin-bottom: 4rem;
            scroll-margin-top: 80px;
        }

        .chapter-title {
            font-family: 'Verdana', sans-serif;
            font-size: 1.5rem;
            color: #ffffff;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 0.5rem;
            font-weight: bold;
        }

        h2 {
            font-family: 'Verdana', sans-serif;
            color: var(--secondary);
            font-size: 1.2rem;
            margin-top: 1.8rem;
            margin-bottom: 0.8rem;
            font-weight: bold;
        }

        h3 {
            font-family: 'Verdana', sans-serif;
            color: var(--primary);
            font-size: 1.05rem;
            margin-top: 1.4rem;
            margin-bottom: 0.6rem;
            font-weight: bold;
        }

        p {
            margin-bottom: 0.9rem;
            color: #cbd5e1;
            font-size: 0.95rem;
            line-height: 1.6;
            text-align: left;
        }

        /* Estilização para o Modo Narrativo */
        .narrative-p {
            font-family: 'Verdana', sans-serif;
            color: #e2e8f0;
            line-height: 1.65;
            letter-spacing: 0.2px;
            margin-bottom: 1.1rem;
        }

        li {
            margin-left: 1.2rem;
            margin-bottom: 0.5rem;
            color: #cbd5e1;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        /* Caixas de Descoberta lúdicas (Diário) - Mobile-First */
        .discovery-box {
            background-color: rgba(30, 41, 59, 0.4);
            border-left: 4px solid var(--primary);
            border-right: 1px solid var(--border-color);
            border-top: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
            padding: 14px 16px;
            border-radius: 4px 12px 12px 4px;
            margin: 1.8rem 0;
            font-style: italic;
            color: #f8fafc;
            font-size: 0.92rem;
            line-height: 1.6;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .box-tag {
            font-style: normal;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--primary);
            letter-spacing: 1.5px;
            display: inline-block;
            margin-bottom: 6px;
            border-bottom: 1px solid var(--primary-glow);
            padding-bottom: 2px;
        }

        /* Blocos de Código Responsivos */
        pre {
            background-color: #090d16;
            border: 1px solid var(--border-color);
            padding: 1.1rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.8rem 0;
            box-shadow: inset 0 2px 8px rgba(0,0,0,0.6);
        }

        code {
            font-family: 'Fira Code', monospace;
            font-size: 0.8rem;
            color: #38bdf8;
        }

        /* Imagens dos Capítulos */
        .chapter-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin-bottom: 1.8rem;
            border: 1px solid var(--border-color);
        }
    </style>
</head>
<body>

    <div class="mobile-header">
        <span class="header-title">A Rebeldia da Mecatrônica</span>
        <button class="menu-button" id="menuBtn">☰</button>
    </div>

    <div class="overlay" id="overlay"></div>

    <div class="nav-drawer" id="drawer">
        <h2>Capítulos</h2>
        <ul>
            <li><a href="#cover" class="active">Capa & Dedicatória</a></li>
"""
    
    # 2. Ler os capítulos para criar o menu na barra lateral
    capitulos = sorted([f for f in os.listdir(CAPITULOS_DIR) if f.endswith('.md')])
    
    menu_items = []
    chapters_content = []
    
    for idx, cap in enumerate(capitulos, start=1):
        cap_path = os.path.join(CAPITULOS_DIR, cap)
        
        with open(cap_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip().lstrip('#').strip()
            
        clean_title = first_line.split(':')[-1].strip() if ':' in first_line else first_line
        
        menu_items.append(f'            <li><a href="#cap{idx}">Cap. {idx}: {clean_title}</a></li>')
        
        with open(cap_path, 'r', encoding='utf-8') as f:
            body = f.read()
            
        formatted_body = format_markdown_to_html(body)
        
        img_html = ""
        img_name = f"cap{idx}.png"
        if os.path.exists(os.path.join(WORKSPACE_DIR, "imagens", img_name)):
            img_html = f'<img src="imagens/{img_name}" alt="Ilustração do Capítulo {idx}" class="chapter-image">'
            
        chapter_html = f"""
        <div id="cap{idx}" class="chapter-section">
            {img_html}
            {formatted_body}
        </div>
        """
        chapters_content.append(chapter_html)
        
    html_menu = "\n".join(menu_items)
    
    html_middle = """
        </ul>
    </div>
 
    <div class="content-container">
        <div id="cover" class="cover-section">
            <img src="capa.png" alt="Capa: A Rebeldia da Mecatrônica" class="cover-image" onerror="this.style.display='none'">
            <h1 class="cover-title">A Rebeldia da Mecatrônica</h1>
            <p class="cover-subtitle">Romance Instrutivo de Tecnologia e Sociedade</p>
            
            <a href="romance_instrutivo.pdf" class="download-cta-btn" download>📥 Baixar Livro em PDF (Leitura Offline)</a>
            
            <div class="dedication">
                Dedicado à minha família, cujo apoio silencioso e inabalável estruturou
                o caminho para que este projeto de vida ganhasse o mundo.<br/><br/>
                E a todos os jovens engenheiros e mentes inquietas que, diante de estradas de barro
                ou algoritmos complexos, escolhem o caminho da persistência técnica e do
                despertar lúdico como ferramentas reais de emancipação.
            </div>
        </div>
    """
    
    html_chapters_joined = "\n".join(chapters_content)
    
    html_end = """
    </div>

    <script>
        // Menu Drawer Logic
        const menuBtn = document.getElementById('menuBtn');
        const drawer = document.getElementById('drawer');
        const overlay = document.getElementById('overlay');
        const links = document.querySelectorAll('.nav-drawer a');
        const sections = document.querySelectorAll('.content-container > div, .content-container > .chapter-section');

        function toggleMenu() {
            drawer.classList.toggle('open');
            overlay.classList.toggle('show');
        }

        menuBtn.addEventListener('click', toggleMenu);
        overlay.addEventListener('click', toggleMenu);

        links.forEach(link => {
            link.addEventListener('click', () => {
                drawer.classList.remove('open');
                overlay.classList.remove('show');
            });
        });

        // Active Link Selection on Scroll
        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (pageYOffset >= sectionTop - 120) {
                    current = section.getAttribute('id');
                }
            });

            links.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });
    </script>
</body>
</html>
"""
    
    # Gravar o arquivo final
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_start + html_menu + html_middle + html_chapters_joined + html_end)
        
    print(f"Livro em formato HTML Mobile-First compilado com sucesso em: {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
