import os
import re

WORKSPACE_DIR = r"D:\onedrive\outros\workspace_book"
CAPITULOS_DIR = os.path.join(WORKSPACE_DIR, "capitulos")
OUTPUT_HTML = os.path.join(WORKSPACE_DIR, "docs", "index.html")

def format_markdown_to_html(content):
    # Processar dividindo o conteúdo em blocos de código e blocos comuns
    blocks = re.split(r'(```[\s\S]*?```)', content)
    formatted_blocks = []
    
    in_diary = False
    diary_buffer = []

    for block in blocks:
        if block.startswith('```'):
            code = block.strip('`').strip()
            lines = code.split('\n')
            if lines and lines[0].strip() in ['python', 'cpp', 'assembly', 'c++', 'asm', 'diagram']:
                block_type = lines[0].strip()
                lines = lines[1:]
            else:
                block_type = ''
            
            clean_code = '\n'.join(lines)
            clean_code = clean_code.replace('<', '&lt;').replace('>', '&gt;')
            
            if block_type == 'diagram':
                diagram_html = """
<div class="register-diagram">
  <div class="diagram-title">Gavetas do Processador (Registradores)</div>
  <div class="diagram-grid">
    <div class="register-card active">
      <span class="reg-name">Reg A</span>
      <span class="reg-desc">Acumulador</span>
    </div>
    <div class="register-card">
      <span class="reg-name">Reg B</span>
      <span class="reg-desc">Auxiliar</span>
    </div>
    <div class="register-card">
      <span class="reg-name">Reg C</span>
      <span class="reg-desc">Geral</span>
    </div>
    <div class="register-card">
      <span class="reg-name">Reg D</span>
      <span class="reg-desc">Geral</span>
    </div>
  </div>
</div>
"""
                formatted_blocks.append(diagram_html)
            else:
                formatted_blocks.append(f'<pre><code>{clean_code}</code></pre>')
            # Processar bloco de equações centralizado ($$) antes do inline ($)
            def convert_latex_to_html_local(math_text):
                math_text = math_text.replace(r'\approx', '≈')
                math_text = math_text.replace(r'\times', '×')
                math_text = math_text.replace(r'\cdot', '·')
                math_text = re.sub(r'\\vec\{(.*?)\}', r'\1', math_text)
                math_text = math_text.replace(r'\vec', '')
                math_text = math_text.replace(r'\text{ m/s}', ' m/s')
                math_text = math_text.replace(r'\text{m/s}', ' m/s')
                math_text = math_text.replace(r'\text', '')
                math_text = re.sub(r'\\frac\{(.*?)\}\{(.*?)\}', r'(\1) / \2', math_text)
                math_text = re.sub(r'\^\{(.*?)\}', r'<sup>\1</sup>', math_text)
                math_text = re.sub(r'\^(.)', r'<sup>\1</sup>', math_text)
                def italicize_vars(m):
                    var = m.group(0)
                    if var.lower() in ['m', 's', 'sec']:
                        return var
                    return f"<i>{var}</i>"
                math_text = re.sub(r'\b(PC|Efe|[a-zA-BD-Z])\b', italicize_vars, math_text)
                return math_text

            block = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', block)
            block = re.sub(r'\*(.*?)\*', r'<em>\1</em>', block)
            
            # Converter equações em bloco: $$equation$$ -> <div class="html-equation">equation</div>
            block = re.sub(r'\$\$(.*?)\$\$', lambda m: f'<div class="html-equation">{convert_latex_to_html_local(m.group(1))}</div>', block)
            # Converter equações inline: $equation$ -> <span class="html-math">equation</span>
            block = re.sub(r'\$(.*?)\$', lambda m: f'<span class="html-math">{convert_latex_to_html_local(m.group(1))}</span>', block)
            
            
            lines = block.split('\n')
            for line in lines:
                line_str = line.strip()
                if not line_str:
                    if in_diary:
                        formatted_blocks.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                        in_diary = False
                        diary_buffer = []
                    continue
                
                is_diary = line_str.startswith('*“') or line_str.startswith('“') or line_str.startswith('>') or in_diary
                
                if line_str.startswith('# '):
                    if in_diary:
                        formatted_blocks.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                        in_diary = False
                        diary_buffer = []
                    formatted_blocks.append(f'<h1 class="chapter-title">{line_str[2:]}</h1>')
                elif line_str.startswith('## '):
                    if in_diary:
                        formatted_blocks.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                        in_diary = False
                        diary_buffer = []
                    formatted_blocks.append(f'<h2>{line_str[3:]}</h2>')
                elif line_str.startswith('### '):
                    if in_diary:
                        formatted_blocks.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                        in_diary = False
                        diary_buffer = []
                    formatted_blocks.append(f'<h3>{line_str[4:]}</h3>')
                elif line_str.startswith('* ') or line_str.startswith('- '):
                    if in_diary:
                        formatted_blocks.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                        in_diary = False
                        diary_buffer = []
                    formatted_blocks.append(f'<li>{line_str[2:]}</li>')
                elif line_str.startswith('*“') or line_str.startswith('“') or line_str.startswith('>'):
                    in_diary = True
                    diary_buffer.append(line_str.lstrip('>').strip())
                elif in_diary:
                    diary_buffer.append(line_str)
                else:
                    formatted_blocks.append(f'<p class="narrative-p">{line_str}</p>')
            
            if in_diary:
                formatted_blocks.append(f'<div class="discovery-box"><span class="box-tag">[Diário de Bordo]</span><br/>{"<br/>".join(diary_buffer)}</div>')
                in_diary = False
                diary_buffer = []
                
    return '\n'.join(formatted_blocks)

def main():
    print("Iniciando compilação do livro em formato HTML Mobile-First...")
    
    html_start = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>A Rebeldia da Mecatrônica - Romance Instrutivo</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🤖</text></svg>">
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

        html {
            scroll-behavior: smooth;
            scroll-padding-top: 80px; /* Alinha o scroll para não ficar por baixo do cabeçalho fixo */
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

        .header-download-btn {
            background-color: var(--primary);
            color: #ffffff;
            text-decoration: none;
            padding: 0.35rem 0.75rem;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 4px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: background 0.2s;
            margin-right: 8px;
        }

        .header-download-btn:hover {
            background-color: #f97316;
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

        /* Capítulos e Seções em Formato de Livro (Paginação) */
        .chapter-section, .cover-section {
            display: none;
        }

        .chapter-section.active-page, .cover-section.active-page {
            display: block;
            animation: pageFadeIn 0.35s ease-out;
        }

        @keyframes pageFadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .chapter-section {
            margin-bottom: 2rem;
        }

        .page-navigation-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 3.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-color);
        }

        .nav-page-btn {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .nav-page-btn:hover:not(:disabled) {
            background-color: var(--primary);
            border-color: var(--primary);
            transform: translateY(-1px);
        }

        .nav-page-btn:disabled {
            opacity: 0.35;
            cursor: not-allowed;
        }

        .page-progress-text {
            font-size: 0.85rem;
            color: var(--text-muted);
            font-family: 'Outfit', sans-serif;
            font-weight: 500;
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
            text-indent: 18px; /* Recuo padrão do romance para os parágrafos subsequentes */
        }

        /* O primeiro parágrafo após qualquer título ou lista não deve ter recuo na primeira linha */
        .chapter-title + .narrative-p,
        h2 + .narrative-p,
        h3 + .narrative-p,
        li + .narrative-p,
        .discovery-box + .narrative-p,
        pre + .narrative-p,
        .html-equation + .narrative-p,
        .chapter-image + .narrative-p,
        .register-diagram + .narrative-p {
            text-indent: 0 !important;
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

        /* Blocos de Código Responsivos - Lousa Verde */
        pre {
            background: linear-gradient(135deg, #112919 0%, #153520 100%);
            border: 6px solid #4a2f13; /* Moldura de madeira */
            padding: 1.1rem;
            border-radius: 6px;
            overflow-x: auto;
            margin: 1.8rem 0;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5), inset 0 0 25px rgba(0,0,0,0.8);
            outline: 1px solid rgba(255, 255, 255, 0.05);
        }

        code {
            font-family: 'Fira Code', monospace;
            font-size: 0.82rem;
            color: #e2f3e8; /* Texto de giz esverdeado */
        }

        /* Equações e Expressões Matemáticas no HTML */
        .html-equation {
            background: linear-gradient(135deg, #112919 0%, #153520 100%);
            border: 5px solid #4a2f13; /* Moldura de madeira */
            border-radius: 6px;
            padding: 1.1rem;
            text-align: center;
            margin: 1.8rem auto;
            color: #fffae0; /* Texto cor de giz */
            font-family: 'Fira Code', monospace;
            font-size: 0.95rem;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5), inset 0 0 25px rgba(0,0,0,0.8);
            max-width: 100%;
            overflow-x: auto;
            outline: 1px solid rgba(255, 255, 255, 0.05);
        }

        .html-math {
            font-family: 'Fira Code', monospace;
            color: #fffae0;
            background-color: #1a3c26;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.88rem;
            border: 1px dashed rgba(255, 250, 224, 0.3);
        }

        /* Imagens dos Capítulos */
        .chapter-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin-bottom: 1.8rem;
            border: 1px solid var(--border-color);
        }

        /* Diagramas de registradores - Lousa Verde */
        .register-diagram {
            background: linear-gradient(135deg, #132e1c 0%, #1a3e26 100%);
            border: 6px solid #4a2f13; /* Moldura de madeira */
            border-radius: 6px;
            padding: 1.2rem;
            margin: 1.8rem 0;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5), inset 0 0 25px rgba(0,0,0,0.8);
            font-family: 'Verdana', sans-serif;
            outline: 1px solid rgba(255, 255, 255, 0.05);
        }
        .diagram-title {
            font-family: 'Outfit', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            color: #fffae0; /* Giz amarelo claro */
            letter-spacing: 1.5px;
            margin-bottom: 1.2rem;
            text-align: center;
            border-bottom: 2px dashed rgba(255,250,224,0.3);
            padding-bottom: 0.6rem;
        }
        .diagram-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        .register-card {
            background: rgba(255, 255, 255, 0.05);
            border: 2px dashed rgba(255, 255, 255, 0.3); /* Tracejado giz */
            border-radius: 4px;
            padding: 10px;
            text-align: center;
            transition: all 0.3s ease;
        }
        .register-card.active {
            border: 2px solid #fffae0; /* Giz amarelo contínuo */
            box-shadow: 0 0 10px rgba(255, 250, 224, 0.2);
        }
        .reg-name {
            display: block;
            font-family: 'Fira Code', monospace;
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 4px;
        }
        .register-card.active .reg-name {
            color: #fffae0;
        }
        .reg-desc {
            display: block;
            font-size: 0.78rem;
            color: rgba(255, 255, 255, 0.7);
        }
    </style>
</head>
<body>

    <div class="mobile-header">
        <span class="header-title">A Rebeldia da Mecatrônica</span>
        <div style="display: flex; align-items: center;">
            <a href="romance_instrutivo.pdf" class="header-download-btn" download>📥 PDF</a>
            <button class="menu-button" id="menuBtn">☰</button>
        </div>
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
        
        # Determinar Slug, Label e nome de imagem com base no tipo de título
        if "Capítulo" in first_line:
            match = re.search(r'Capítulo\s+(\d+)', first_line)
            num = int(match.group(1)) if match else idx
            slug = f"cap{num}"
            label = f"Cap. {num}: {clean_title}"
            img_name = f"cap{num}.png"
        elif "Apêndice" in first_line:
            match = re.search(r'Apêndice\s+([A-Z])', first_line)
            letra = match.group(1) if match else "A"
            slug = f"apendice-{letra.lower()}"
            label = f"Apêndice {letra}: {clean_title}"
            img_name = None
        else:
            if "Estudar" in first_line:
                slug = "como-estudar"
            elif "Prólogo" in first_line:
                slug = "prologo"
            else:
                slug = cap.replace('.md', '').replace('00_', '').replace('_', '-')
            label = first_line
            img_name = None
        
        menu_items.append(f'            <li><a href="#{slug}">{label}</a></li>')
        
        with open(cap_path, 'r', encoding='utf-8') as f:
            body = f.read()
            
        formatted_body = format_markdown_to_html(body)
        
        img_html = ""
        if img_name and os.path.exists(os.path.join(WORKSPACE_DIR, "imagens", img_name)):
            img_html = f'<img src="imagens/{img_name}" alt="Ilustração do Capítulo {slug.replace("cap", "")}" class="chapter-image">'
            if "</h1>" in formatted_body:
                parts = formatted_body.split("</h1>", 1)
                formatted_body = parts[0] + "</h1>\n" + img_html + parts[1]
            else:
                formatted_body = img_html + formatted_body
            
        chapter_html = f"""
        <div id="{slug}" class="chapter-section">
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
        <!-- Rodapé de Navegação do Livro -->
        <div class="page-navigation-footer">
            <button id="prevPageBtn" class="nav-page-btn">⬅️ Anterior</button>
            <span id="pageProgressIndicator" class="page-progress-text">Carregando...</span>
            <button id="nextPageBtn" class="nav-page-btn">Próximo ➡️</button>
        </div>
    </div>

    <script>
        // Menu Drawer Logic
        const menuBtn = document.getElementById('menuBtn');
        const drawer = document.getElementById('drawer');
        const overlay = document.getElementById('overlay');
        const links = document.querySelectorAll('.nav-drawer a');
        
        // Selecionar apenas seções válidas: a capa e os capítulos
        const sections = document.querySelectorAll('.content-container > .cover-section, .content-container > .chapter-section');
        const prevPageBtn = document.getElementById('prevPageBtn');
        const nextPageBtn = document.getElementById('nextPageBtn');
        const pageProgressIndicator = document.getElementById('pageProgressIndicator');

        const sectionsArray = Array.from(sections);

        function toggleMenu() {
            drawer.classList.toggle('open');
            overlay.classList.toggle('show');
        }

        menuBtn.addEventListener('click', toggleMenu);
        overlay.addEventListener('click', toggleMenu);

        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href').replace('#', '');
                showChapter(targetId);
                drawer.classList.remove('open');
                overlay.classList.remove('show');
            });
        });

        function showChapter(targetId) {
            if (!targetId) targetId = 'cover';
            
            let activeSection = document.getElementById(targetId);
            if (!activeSection) targetId = 'cover';
            
            // Ocultar todas as seções e mostrar apenas a ativa
            sections.forEach(sec => {
                sec.classList.remove('active-page');
            });
            
            activeSection = document.getElementById(targetId);
            activeSection.classList.add('active-page');
            
            // Atualizar classes 'active' no menu lateral
            links.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${targetId}`) {
                    link.classList.add('active');
                }
            });
            
            // Atualizar botões de anterior / próximo e o progresso
            updateNavButtons(targetId);
            
            // Rolagem instantânea para o topo da página ao trocar de capítulo
            window.scrollTo({ top: 0, behavior: 'instant' });
            
            // Atualizar hash na barra de endereços de forma amigável
            if (window.location.hash !== '#' + targetId) {
                history.pushState(null, null, '#' + targetId);
            }
        }

        function updateNavButtons(targetId) {
            const currentIndex = sectionsArray.findIndex(sec => sec.id === targetId);
            if (currentIndex === -1) return;
            
            // Botão Anterior
            if (currentIndex > 0) {
                prevPageBtn.disabled = false;
                prevPageBtn.onclick = () => showChapter(sectionsArray[currentIndex - 1].id);
            } else {
                prevPageBtn.disabled = true;
                prevPageBtn.onclick = null;
            }
            
            // Botão Próximo
            if (currentIndex < sectionsArray.length - 1) {
                nextPageBtn.disabled = false;
                nextPageBtn.onclick = () => showChapter(sectionsArray[currentIndex + 1].id);
            } else {
                nextPageBtn.disabled = true;
                nextPageBtn.onclick = null;
            }
            
            // Indicador de Progresso (Capa é considerada índice 0)
            if (currentIndex === 0) {
                pageProgressIndicator.textContent = "Início";
            } else {
                // Total de capítulos reais
                const totalChapters = sectionsArray.length - 1;
                pageProgressIndicator.textContent = `Página ${currentIndex} de ${totalChapters}`;
            }
        }

        // Carregar capítulo correto no carregamento inicial da página com base no hash
        window.addEventListener('load', () => {
            const hash = window.location.hash.replace('#', '');
            showChapter(hash || 'cover');
        });

        // Suporte a botões Voltar / Avançar do navegador
        window.addEventListener('popstate', () => {
            const hash = window.location.hash.replace('#', '');
            showChapter(hash || 'cover');
        });
    </script>
</body>
</html>
"""
    
    # Gravar o arquivo final
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_start + html_menu + html_middle + html_chapters_joined + html_end)

    # Copiar as imagens da pasta imagens/ raiz para docs/imagens/ para evitar erro 404
    import shutil
    docs_imagens_dir = os.path.join(WORKSPACE_DIR, "docs", "imagens")
    os.makedirs(docs_imagens_dir, exist_ok=True)
    imagens_dir = os.path.join(WORKSPACE_DIR, "imagens")
    if os.path.exists(imagens_dir):
        for item in os.listdir(imagens_dir):
            s_file = os.path.join(imagens_dir, item)
            d_file = os.path.join(docs_imagens_dir, item)
            if os.path.isfile(s_file):
                shutil.copy2(s_file, d_file)
                print(f"Copiada imagem: {item} para docs/imagens/")
        
    print(f"Livro em formato HTML Mobile-First compilado com sucesso em: {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
