---
title: KI Plugin Integration
type: docs
weight: 35
url: /de/python-net/ai-plugin-integration/
description: Integrieren Sie Aspose.Cells für Python via .NET in KI Tools.
keywords: MarkItDown, Marker und Docling, Excel in JSON, MD und HTML konvertieren.
---

# KI-Plugin-Integration

Dieses Dokument fasst drei KI-gestützte Dokumentenverarbeitungstools zusammen—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker) und [Docling](https://github.com/docling-project/docling)—hervorhebt ihre gemeinsamen KI-Funktionen und ihre Integration mit [Aspose.Cells für Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) durch Plugins.

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

## 2. Aspose.Cells für Python via .NET Plugin-Integration

Um Excel-Daten mit diesen KI-Dokumentenverarbeitungs-Tools zu kombinieren, entwickelten wir spezielle Plugins für jedes Tool:

| Plugin | Repository | Funktionalität |
|--------|------------|---------------|
| MarkItDown Plugin | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Konvertiert Excel-Dateien in Markdown-Format. |
| Marker Plugin | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Konvertiert Excel-Dateien in Marker-kompatible Formate (Markdown, JSON oder HTML) und nutzt den LLM-Modus von Marker für verbesserte Tabellen. |
| Docling Plugin | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Konvertiert Excel-Dateien in `DoclingDocument`-Objekte und exportiert dann Markdown, JSON oder HTML für multimodale Analysen. |

### 2.1 Plugin-Vorteile

1. **Schnelle Excel-Konvertierung**: Konvertiert Excel-Inhalte schnell in Markdown, JSON oder HTML für die KI-Verarbeitung.  
2. **Tabellen- und Formatinformationen bewahren**: Bewahrt im Wesentlichen die ursprünglichen Tabellendaten, um die Datenintegrität zu gewährleisten.  
3. **Kompatibel mit KI-Tools**: Kann direkt als Eingabe für MarkItDown, Marker oder Docling verwendet werden, mit fortschrittlichen Parsing-Funktionen.  
4. **Einfache Installation**: Erfordert nur die zusätzliche Installation von Aspose.Cells für Python via .NET (aspsoe-cells-python) und das Befolgen der README-Anweisungen in den Plugin-Verzeichnissen.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Installationsüberprüfung:
```bash
markitdown --list-plugins
```
Konvertiere eine XLSX-Datei mit dem Plugin:
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 Marker Plugin

Du benötigst Python 3.10+ und [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
Für Nicht-PDF-Dokumente, installiere vollständige Abhängigkeiten:
```
pip install marker-pdf[full]
```

Konvertiere eine einzelne Datei:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 Docling Plugin

Installiere Docling:
```
pip install -e .
```

Konvertiere Excel-Dateien in verschiedene Formate:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Weitere [detaillierte Installationsanleitungen](https://docling-project.github.io/docling/installation/) sind in der Dokumentation verfügbar.

### 3.4 Setze Aspose-Lizenz

Bevor du Aspose.Cells in einem beliebigen Plugin verwendest, setze die Lizenz:

Windows (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Unix-basierte Systeme:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. Zusammenfassung

#### KI-Funktionen:
Die drei Tools teilen gemeinsame Vorteile bei der KI-Dokumentenparsing, strukturiertem Output, Multi-Modal-Unterstützung und Integration in generative KI-Frameworks.

#### Aspose.Cells Plugins:
Ermögliche nahtlose Konvertierung von Excel-Daten in Markdown, JSON oder HTML, wobei Tabellen, Formeln erhalten bleiben und direkte Integration mit MarkItDown, Marker oder Docling möglich ist.

#### Anwendungsfälle:
Ideal für intelligente Dokumentenverarbeitung, Wissensdatenbankaufbau, RAG-Systeme, Berichtsparsing, Konvertierung wissenschaftlicher Dokumente und andere KI-gesteuerte Workflows.

{{< app/cells/assistant language="python-net" >}}
