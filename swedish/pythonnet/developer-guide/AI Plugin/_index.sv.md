---
title: AI Plugin Integration
type: docs
weight: 35
url: /sv/python-net/ai-plugin-integration/
description: Integrera Aspose.Cells för Python via .NET med AI verktyg.
keywords: MarkItDown, Marker och Docling, konvertera Excel till JSON, MD och HTML.
---

# AI-Plugin-Integration

Detta dokument sammanfattar tre AI-drivna dokumenthanteringsverktyg—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker), och [Docling](https://github.com/docling-project/docling)—med fokus på deras gemensamma AI-funktioner och integrationen med [Aspose.Cells för Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) via plugins.

---

## 1. Common AI Features

### 1.1 Multi-format Document Parsing and Structured Representation
All three projects support parsing multiple document formats, including PDF, DOCX, PPTX, XLSX, HTML, etc., and converting them into structured formats (Markdown, JSON, or HTML) suitable for AI processing.

- **MarkItDown**: Converts documents into Markdown format, easily integrated with LLMs and text analysis pipelines.  
- **Marker**: Supports Markdown, JSON, and HTML output while preserving tables, formulas, and other content.  
- **Docling**: Provides a unified `DoclingDocument` representation, supporting multi-format document parsing and structured export.

### 1.2 Integration with Generative AI Frameworks
All three tools support integration with generative AI frameworks to enhance document processing capabilities:

- **MarkItDown**: Integrates with Azure OpenAI to improve document and image processing.  
- **Marker**: Supports leveraging large language model (LLM) technology to improve the accuracy of document processing.  
- **Docling**: Compatible with frameworks like LangChain, LlamaIndex, and Haystack for agentic AI applications.

---

## 2. Aspose.Cells för Python via .NET Plugin-Integration

För att kombinera Excel-data med dessa AI-dokumenthanteringsverktyg utvecklade vi dedicated-plugins för varje verktyg:

| Plugin | Repository | Funktionalitet |
|--------|------------|---------------|
| MarkItDown Plugin | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Konverterar Excel-filer till Markdown-format. |
| Marker-plugin | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Konverterar Excel-filer till Marker-stödda format (Markdown, JSON eller HTML), med hjälp av Markers LLM-läge för förbättrad tabell. |
| Docling Plugin | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Konverterar Excel-filer till `DoclingDocument`-objekt, och exporterar sedan Markdown, JSON eller HTML för multimodal analys. |

### 2.1 Plugin-fördelar

1. **Snabb Excel-konvertering**: Konverterar snabbt Excel-innehåll till Markdown, JSON eller HTML för AI-behandling.  
2. **Bevara tabell- och formatinformation**: Bevarar i stort sett den ursprungliga tabellinformationen för att säkerställa dataintegritet.  
3. **Kompatibel med AI-verktyg**: Kan användas direkt som input för MarkItDown, Marker eller Docling, med avancerade parsningsegenskaper.  
4. **Lätt att installera**: Kräver endast ytterligare installation av Aspose.Cells för Python via .NET (aspsoe-cells-python) och att följa README-instruktionerna i plugin-mapparna.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Verifiera installation:
```bash
markitdown --list-plugins
```
Konvertera en XLSX-fil med hjälp av plugin:
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 Marker Plugin

Du behöver Python 3.10+ och [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
För icke-PDF-dokument, installera fulla beroenden:
```
pip install marker-pdf[full]
```

Konvertera en fil:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 Docling Plugin

Installera Docling:
```
pip install -e .
```

Konvertera Excel-filer till olika format:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Mer [detaljerade installationsinstruktioner](https://docling-project.github.io/docling/installation/) finns tillgängliga i dokumentationen.

### 3.4 Sätt Aspose-licens

Innan du använder Aspose.Cells i något plugin, sätt licensen:

Windows (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Unix-baserade system:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. Sammanfattning

#### AI-funktioner:
De tre verktygen delar vanliga fördelar inom AI-dokumentanalys, strukturerad output, multimodal support och integration med generativa AI-ramverk.

#### Aspose.Cells Plugins:
Aktivera smidig konvertering av Excel-data till Markdown, JSON eller HTML, bevara tabeller, formler och integrera direkt med MarkItDown, Marker eller Docling.

#### Användningsområden:
Ideal för intelligent dokumentbehandling, kunskapsbasuppbyggnad, RAG-system, rapportanalys, konvertering av akademiska dokument och andra AI-drivna arbetsflöden.

{{< app/cells/assistant language="python-net" >}}
