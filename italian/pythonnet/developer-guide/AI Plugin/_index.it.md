---
title: Integrazione del plugin AI
type: docs
weight: 35
url: /it/python-net/ai-plugin-integration/
description: Integra Aspose.Cells for Python via .NET negli strumenti AI.
keywords: MarkItDown, Marker e Docling, convertono Excel in JSON, MD e HTML.
---

# Integrazione del plugin AI

Questo documento riassume tre strumenti di elaborazione documenti supportati dall'IA—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker), e [Docling](https://github.com/docling-project/docling)—sottolineando le loro caratteristiche comuni di IA e la loro integrazione con [Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) tramite plugin.

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

## 2. Integrazione del plugin Aspose.Cells for Python via .NET

Per combinare i dati di Excel con questi strumenti di elaborazione documenti basati su IA, abbiamo sviluppato plugin dedicati per ciascun strumento:

| Plugin | Repository | Funzionalità |
|--------|------------|---------------|
| Plugin MarkItDown | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Converte file Excel in formato Markdown. |
| Plugin Marker | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Converte file Excel in formati supportati da Marker (Markdown, JSON o HTML), sfruttando la modalità LLM di Marker per tabelle migliorate. |
| Plugin Docling | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Converte file Excel in oggetti `DoclingDocument`, quindi esporta in Markdown, JSON o HTML per analisi multimodale. |

### 2.1 Vantaggi del plugin

1. **Conversione Rapida di Excel**: Converte rapidamente il contenuto di Excel in Markdown, JSON o HTML per l'elaborazione IA.  
2. **Preserva le Informazioni di Tavola e Formato**: Preserva fondamentalmente i dati originali della tabella per garantire l'integrità dei dati.  
3. **Compatibilità con gli Strumenti IA**: Può essere utilizzato direttamente come input per MarkItDown, Marker o Docling, sfruttando le funzionalità di parsing avanzato.  
4. **Installazione Facile**: Richiede solo l'installazione aggiuntiva di Aspose.Cells for Python via .NET (aspsoe-cells-python) e seguire le istruzioni README nelle directory dei plugin.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Verifica dell'installazione:
```bash
markitdown --list-plugins
```
Converti un file XLSX utilizzando il plugin:
```bash
markitdown --use-plugins test.xlsx
```
### Plugin Marker 3.2

Avrai bisogno di Python 3.10+ e [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
Per documenti non PDF, installa le dipendenze complete:
```
pip install marker-pdf[full]
```

Converti un singolo file:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### Plugin Docling 3.3

Installa Docling:
```
pip install -e .
```

Converti file Excel in formati diversi:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Per ulteriori [istruzioni dettagliate sull'installazione](https://docling-project.github.io/docling/installation/) sono disponibili nella documentazione.

### Set license Aspose 3.4

Prima di utilizzare Aspose.Cells in qualsiasi plugin, imposta la licenza:

Windows (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Sistemi Unix-based:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## Riepilogo 4

#### Caratteristiche AI:
I tre strumenti condividono vantaggi comuni nell'analisi di documenti AI, output strutturato, supporto multi-modale e integrazione con framework di AI generativa.

#### Plugins Aspose.Cells:
Abilita la conversione senza soluzione di continuità dei dati Excel in Markdown, JSON o HTML, preservando tabelle, formule e integrandosi direttamente con MarkItDown, Marker o Docling.

#### Casi d'uso:
Ideale per l'elaborazione intelligente dei documenti, costruzione di basi di conoscenza, sistemi RAG, analisi dei rapporti, conversione di documenti accademici e altri flussi di lavoro basati su AI.

{{< app/cells/assistant language="python-net" >}}
