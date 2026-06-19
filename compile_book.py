import os
import re
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A5
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, Flowable
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Configurações de caminhos
WORKSPACE_DIR = r"D:\onedrive\outros\workspace_book"
CAPITULOS_DIR = os.path.join(WORKSPACE_DIR, "capitulos")
IMAGENS_DIR = os.path.join(WORKSPACE_DIR, "imagens")
OUTPUT_PDF = os.path.join(WORKSPACE_DIR, "docs", "romance_instrutivo.pdf")
COVER_IMAGE = os.path.join(WORKSPACE_DIR, "capa.png")

os.makedirs(IMAGENS_DIR, exist_ok=True)

# Margem profissional para formato A5
MARGIN = 0.6 * inch

# Copiar a capa do diretório de assets para o workspace se existir
assets_cover = r"C:\Users\chmul\.gemini\antigravity\brain\2e7ab392-633d-4a68-88d1-9d8c2ac47b9f\book_cover_tech_noir_1781823173853.png"
if os.path.exists(assets_cover) and not os.path.exists(COVER_IMAGE):
    import shutil
    shutil.copy(assets_cover, COVER_IMAGE)

# Registro da Fonte Verdana a partir do Windows Fonts
FONT_NAME = "Verdana"
FONT_BOLD = "Verdana-Bold"
FONT_ITALIC = "Verdana-Italic"
FONT_BI = "Verdana-BoldItalic"

try:
    pdfmetrics.registerFont(TTFont(FONT_NAME, 'C:\\Windows\\Fonts\\verdana.ttf'))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, 'C:\\Windows\\Fonts\\verdanab.ttf'))
    pdfmetrics.registerFont(TTFont(FONT_ITALIC, 'C:\\Windows\\Fonts\\verdanai.ttf'))
    pdfmetrics.registerFont(TTFont(FONT_BI, 'C:\\Windows\\Fonts\\verdanaz.ttf'))
    print("Fonte Verdana registrada com sucesso.")
except Exception as e:
    print(f"Aviso: Não foi possível carregar a fonte Verdana ({e}). Usando Helvetica como fallback.")
    FONT_NAME = "Helvetica"
    FONT_BOLD = "Helvetica-Bold"
    FONT_ITALIC = "Helvetica-Oblique"
    FONT_BI = "Helvetica-BoldOblique"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            super().showPage()
        super().save()

    def draw_page_elements(self, page_count):
        if self._pageNumber <= 3:
            return

        self.saveState()
        self.setFont(FONT_ITALIC, 8)
        self.setFillColor(colors.HexColor("#555555"))

        page_w, page_h = self._pagesize

        # Linha fina do cabeçalho
        self.setStrokeColor(colors.HexColor("#dddddd"))
        self.setLineWidth(0.5)
        self.line(MARGIN, page_h - 0.45 * inch, page_w - MARGIN, page_h - 0.45 * inch)

        book_page = self._pageNumber - 3

        if self._pageNumber % 2 == 0:
            self.drawString(MARGIN, 0.4 * inch, f"{book_page}")
            self.drawRightString(page_w - MARGIN, page_h - 0.4 * inch, "A Rebeldia da Mecatrônica")
        else:
            self.drawRightString(page_w - MARGIN, 0.4 * inch, f"{book_page}")
            self.drawString(MARGIN, page_h - 0.4 * inch, "Romance Instrutivo")

        self.restoreState()

def format_text(text):
    # Formatação de negrito e itálico adaptado para as tags <b> e <i> interpretadas pelo ReportLab
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = text.replace("“", '"').replace("”", '"').replace('*"', '"').replace('"*', '"')
    return text

def parse_markdown_to_story(file_path, cap_index, styles):
    story = []
    
    image_name = f"cap{cap_index}.png"
    image_path = os.path.join(IMAGENS_DIR, image_name)
    image_inserted = False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'(```[\s\S]*?```)', content)
    
    for block in blocks:
        if block.startswith('```'):
            code_lines = block.strip('`').strip().split('\n')
            block_type = code_lines[0].strip() if code_lines else ''
            if block_type == 'diagram':
                story.append(create_pdf_register_diagram(styles))
                story.append(Spacer(1, 10))
                continue
                
            if code_lines and code_lines[0] in ['python', 'cpp', 'assembly', 'c++', 'asm']:
                code_lines = code_lines[1:]
            code_text = "<br/>".join(code_lines).replace(" ", "&nbsp;").replace("<", "&lt;").replace(">", "&gt;")
            
            p_code = Paragraph(code_text, styles['CodeStyle'])
            t = Table([[p_code]], colWidths=[A5[0] - 2 * MARGIN])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#132e1c")), # Fundo lousa verde
                ('TOPPADDING', (0,0), (-1,-1), 8),
                ('BOTTOMPADDING', (0,0), (-1,-1), 8),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
                ('BOX', (0,0), (-1,-1), 4, colors.HexColor("#4a2f13")), # Moldura de madeira
            ]))
            story.append(t)
            story.append(Spacer(1, 10))
        else:
            lines = block.split('\n')
            diary_lines = []
            
            for line in lines:
                line_str = line.strip()
                if not line_str:
                    if diary_lines:
                        story.append(create_discovery_box(diary_lines, styles))
                        diary_lines = []
                    story.append(Spacer(1, 6))
                    continue
                
                is_diary_line = line_str.startswith('*“') or line_str.startswith('“') or line_str.startswith('>') or (diary_lines and not line_str.startswith('#'))
                
                if line_str.startswith('# ') or line_str.startswith('## ') or line_str.startswith('### '):
                    if diary_lines:
                        story.append(create_discovery_box(diary_lines, styles))
                        diary_lines = []
                    
                    if line_str.startswith('# '):
                        story.append(Paragraph(line_str[2:], styles['BookTitleStyle']))
                        story.append(Spacer(1, 10))
                        # Inserir imagem logo após o título principal do capítulo
                        if os.path.exists(image_path) and not image_inserted:
                            img = PILImage.open(image_path)
                            orig_w, orig_h = img.size
                            aspect = orig_h / orig_w
                            
                            max_w = A5[0] - 2 * MARGIN
                            max_h = 240  # Limite máximo de altura para não empurrar muito o texto
                            
                            if max_w * aspect <= max_h:
                                img_w = max_w
                                img_h = max_w * aspect
                            else:
                                img_h = max_h
                                img_w = max_h / aspect
                                
                            story.append(Image(image_path, width=img_w, height=img_h))
                            story.append(Spacer(1, 15))
                            image_inserted = True
                    elif line_str.startswith('## '):
                        story.append(Paragraph(line_str[3:], styles['SectionHeaderStyle']))
                        story.append(Spacer(1, 8))
                    elif line_str.startswith('### '):
                        story.append(Paragraph(line_str[4:], styles['SubSectionHeaderStyle']))
                        story.append(Spacer(1, 6))
                
                elif line_str.startswith('* ') or line_str.startswith('- '):
                    if diary_lines:
                        story.append(create_discovery_box(diary_lines, styles))
                        diary_lines = []
                    formatted_line = format_text(line_str[2:])
                    story.append(Paragraph(f"• {formatted_line}", styles['ListItemStyle']))
                
                elif is_diary_line:
                    clean_line = line_str.lstrip('>').strip()
                    diary_lines.append(clean_line)
                
                else:
                    if diary_lines:
                        story.append(create_discovery_box(diary_lines, styles))
                        diary_lines = []
                    formatted_line = format_text(line_str)
                    story.append(Paragraph(formatted_line, styles['NarrativeStyle']))
                    story.append(Spacer(1, 6))
            
            if diary_lines:
                story.append(create_discovery_box(diary_lines, styles))
                
    return story

def create_discovery_box(lines, styles):
    full_text = "<br/>".join([format_text(l) for l in lines])
    intro_label = "<font color='#d95d14'><b>[Descoberta e Anotação do Diário]</b></font><br/>"
    p_diary = Paragraph(intro_label + full_text, styles['DiaryStyle'])
    
    t = Table([[p_diary]], colWidths=[A5[0] - 2 * MARGIN])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fdfaf6")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('LINELEFT', (0,0), (0,-1), 3, colors.HexColor("#d95d14")),
        ('BOX', (0,0), (-1,-1), 0.2, colors.HexColor("#e6dcd3")),
    ]))
    return t

def create_pdf_register_diagram(styles):
    p_title = Paragraph("<font size='9' color='#fffae0'><b>GAVETAS DO PROCESSADOR (REGISTRADORES)</b></font>", styles['NormalStyle'])
    
    cell_a = Paragraph("<font color='#fffae0'><b>Reg A</b></font><br/><font size='8' color='#e2f3e8'>Acumulador</font>", styles['NormalStyle'])
    cell_b = Paragraph("<font color='#ffffff'><b>Reg B</b></font><br/><font size='8' color='#e2f3e8'>Auxiliar</font>", styles['NormalStyle'])
    cell_c = Paragraph("<font color='#ffffff'><b>Reg C</b></font><br/><font size='8' color='#e2f3e8'>Geral</font>", styles['NormalStyle'])
    cell_d = Paragraph("<font color='#ffffff'><b>Reg D</b></font><br/><font size='8' color='#e2f3e8'>Geral</font>", styles['NormalStyle'])
    
    t_cards = Table([[cell_a, cell_b], [cell_c, cell_d]], colWidths=[(A5[0] - 2 * MARGIN - 40) / 2] * 2)
    t_cards.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#163623")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (0,0), 1.5, colors.HexColor("#fffae0")), # Destaque em giz amarelo
        ('BOX', (1,0), (1,0), 0.5, colors.HexColor("#ffffff")), # Giz branco
        ('BOX', (0,1), (0,1), 0.5, colors.HexColor("#ffffff")),
        ('BOX', (1,1), (1,1), 0.5, colors.HexColor("#ffffff")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    
    container = Table([[p_title], [t_cards]], colWidths=[A5[0] - 2 * MARGIN])
    container.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#132e1c")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOX', (0,0), (-1,-1), 4, colors.HexColor("#4a2f13")), # Moldura de madeira escura
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return container

chapter_pages = {}

class PageTracker(Flowable):
    def __init__(self, key):
        Flowable.__init__(self)
        self.key = key
        self.width = 0
        self.height = 0
        
    def draw(self):
        chapter_pages[self.key] = self.canv._pageNumber

def build_story(styles, page_map=None):
    story = []

    # 1. Página de Capa
    if os.path.exists(COVER_IMAGE):
        print("Inserindo capa...")
        img = PILImage.open(COVER_IMAGE)
        orig_w, orig_h = img.size
        aspect = orig_h / orig_w
        
        max_w = A5[0] - 2 * MARGIN
        max_h = A5[1] - 2 * MARGIN - 60
        
        if max_w * aspect <= max_h:
            img_w = max_w
            img_h = max_w * aspect
        else:
            img_h = max_h
            img_w = max_h / aspect
            
        story.append(Spacer(1, 15))
        story.append(Image(COVER_IMAGE, width=img_w, height=img_h))
        story.append(PageBreak())

    # 2. Página de Dedicatória
    print("Inserindo dedicatória...")
    story.append(Spacer(1, 100))
    dedicatoria_text = (
        "<i>Dedicado à minha família, cujo apoio silencioso e inabalável estruturou "
        "o caminho para que este projeto de vida ganhasse o mundo.<br/><br/>"
        "E a todos os jovens engenheiros e mentes inquietas que, diante de estradas de barro "
        "ou algoritmos complexos, escolhem o caminho da persistência técnica e do "
        "despertar lúdico como ferramentas reais de emancipação.</i>"
    )
    story.append(Paragraph(dedicatoria_text, styles['DedicationStyle']))
    story.append(PageBreak())

    # 3. Página de Índice
    print("Inserindo sumário...")
    story.append(Paragraph("Sumário", styles['BookTitleStyle']))
    story.append(Spacer(1, 10))
    
    toc_data = []
    capitulos_files = sorted([f for f in os.listdir(CAPITULOS_DIR) if f.endswith('.md')])
    
    for idx, cap in enumerate(capitulos_files):
        cap_path = os.path.join(CAPITULOS_DIR, cap)
        with open(cap_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip().lstrip('#').strip()
        
        if page_map and cap in page_map:
            pg = str(page_map[cap] - 3)
        else:
            pg = ""
            
        p_title = Paragraph(first_line, styles['TOCStyle'])
        toc_data.append([p_title, pg])
    
    t_toc = Table(toc_data, colWidths=[295, 38])
    t_toc.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), FONT_NAME),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#2a2b2d")),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#eeeeee")),
    ]))
    story.append(t_toc)
    story.append(PageBreak())
 
    # 4. Ler capítulos
    for idx, cap in enumerate(capitulos_files):
        cap_path = os.path.join(CAPITULOS_DIR, cap)
        story.append(PageTracker(cap))
        story.extend(parse_markdown_to_story(cap_path, idx, styles))
        story.append(PageBreak())
        
    return story

def main():
    print("Iniciando compilação do livro em A5 com fonte Verdana...")
    
    styles = getSampleStyleSheet()
    
    # Configurações de estilo com fonte linear Verdana 12 e leading condensado (compacto)
    styles.add(ParagraphStyle(
        name='BookTitleStyle',
        parent=styles['Heading1'],
        fontName=FONT_BOLD,
        fontSize=16,
        leading=19,
        textColor=colors.HexColor("#0f2a4a"),
        spaceAfter=10,
        keepWithNext=True
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHeaderStyle',
        parent=styles['Heading2'],
        fontName=FONT_BOLD,
        fontSize=12.5,
        leading=15,
        textColor=colors.HexColor("#1b4b7a"),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    ))
    
    styles.add(ParagraphStyle(
        name='SubSectionHeaderStyle',
        parent=styles['Heading3'],
        fontName=FONT_BOLD,
        fontSize=11,
        leading=13,
        textColor=colors.HexColor("#d95d14"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    ))
    
    styles.add(ParagraphStyle(
        name='NormalStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=12,         # Fonte Verdana tamanho 12 conforme pedido
        leading=14.5,        # Leading condensado e compacto para otimizar espaço de leitura
        textColor=colors.HexColor("#2a2b2d"),
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='NarrativeStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=12,
        leading=15.5,        # Espaçamento ligeiramente maior para o ritmo narrativo
        textColor=colors.HexColor("#1a1b1d"),
        firstLineIndent=12,  # Indentação clássica de parágrafo literário
        spaceAfter=5
    ))

    styles.add(ParagraphStyle(
        name='DiaryStyle',
        parent=styles['Normal'],
        fontName=FONT_ITALIC,
        fontSize=11.5,
        leading=13.5,
        textColor=colors.HexColor("#3a3b3d")
    ))

    styles.add(ParagraphStyle(
        name='DedicationStyle',
        parent=styles['Normal'],
        fontName=FONT_ITALIC,
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#333333"),
        alignment=1
    ))
    
    styles.add(ParagraphStyle(
        name='ListItemStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=12,
        leading=14.5,
        textColor=colors.HexColor("#2a2b2d"),
        leftIndent=15,
        spaceAfter=3
    ))
    
    styles.add(ParagraphStyle(
        name='CodeStyle',
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#e2f3e8")
    ))
    
    styles.add(ParagraphStyle(
        name='TOCStyle',
        parent=styles['Normal'],
        fontName=FONT_NAME,
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor("#2a2b2d")
    ))

    # --- Passo 1: Primeira compilação para descobrir as páginas ---
    print("Passo 1: Detectando número das páginas dos capítulos...")
    doc_temp = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A5,
        rightMargin=MARGIN, leftMargin=MARGIN,
        topMargin=MARGIN + 0.2 * inch, bottomMargin=MARGIN
    )
    story_temp = build_story(styles, page_map=None)
    doc_temp.build(story_temp, canvasmaker=NumberedCanvas)
    
    # --- Passo 2: Segunda compilação com o Sumário preenchido corretamente ---
    print("Passo 2: Gerando versão final do PDF com Sumário atualizado...")
    doc_final = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A5,
        rightMargin=MARGIN, leftMargin=MARGIN,
        topMargin=MARGIN + 0.2 * inch, bottomMargin=MARGIN
    )
    story_final = build_story(styles, page_map=chapter_pages)
    doc_final.build(story_final, canvasmaker=NumberedCanvas)
    
    print(f"Livro compilado com sucesso em: {OUTPUT_PDF}")

if __name__ == "__main__":
    main()
