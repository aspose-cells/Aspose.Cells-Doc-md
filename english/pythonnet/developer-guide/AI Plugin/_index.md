---
title: AI Plugin Integration
type: docs
weight: 35
url: /python-net/ai-plugin-integration/
description: Integrate Aspose.Cells for Python via .NET to AI tools.
keywords: MarkItDown, Marker, and Docling, convert Excel to JSON, MD, and HTML.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# AI Plugin Integration

This document summarizes three AI‑powered document processing tools—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker), and [Docling](https://github.com/docling-project/docling)—highlighting their common AI features and their integration with [Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) through plugins.

---

## 1. Common AI Features

### 1.1 Multi‑format Document Parsing and Structured Representation
All three projects support parsing multiple document formats, including PDF, DOCX, PPTX, XLSX, HTML, etc., and converting them into structured formats (Markdown, JSON, or HTML) suitable for AI processing.

- **MarkItDown**: Converts documents into Markdown format, easily integrated with LLMs and text analysis pipelines.  
- **Marker**: Supports Markdown, JSON, and HTML output while preserving tables, formulas, and other content.  
- **Docling**: Provides a unified `DoclingDocument` representation, supporting multi‑format document parsing and structured export.

### 1.2 Integration with Generative AI Frameworks
All three tools support integration with generative AI frameworks to enhance document processing capabilities:

- **MarkItDown**: Integrates with Azure OpenAI to improve document and image processing.  
- **Marker**: Supports leveraging large language model (LLM) technology to improve the accuracy of document processing.  
- **Docling**: Compatible with frameworks like LangChain, LlamaIndex, and Haystack for agentic AI applications.

---

## 2. Aspose.Cells for Python via .NET Plugin Integration

To combine Excel data with these AI document processing tools, we developed dedicated plugins for each tool:

| Plugin | Repository | Functionality |
|--------|------------|---------------|
| MarkItDown Plugin | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Converts Excel files to Markdown format. |
| Marker Plugin | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Converts Excel files into Marker‑supported formats (Markdown, JSON, or HTML), leveraging Marker’s LLM mode for improved table handling. |
| Docling Plugin | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Converts Excel files into `DoclingDocument` objects, then exports Markdown, JSON, or HTML for multi‑modal analysis. |

### 2.1 Plugin Advantages

1. **Fast Excel Conversion**: Quickly converts Excel content into Markdown, JSON, or HTML for AI processing.  
2. **Preserve Table and Format Information**: Effectively preserve the original table data to ensure data integrity.  
3. **Compatible with AI Tools**: Can be directly used as input for MarkItDown, Marker, or Docling, leveraging advanced parsing features.  
4. **Easy Installation**: Only requires additional installation of Aspose.Cells for Python via .NET (aspose-cells-python) and following the README instructions in the plugin directories.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```

Verify installation:

```bash
markitdown --list-plugins
```

Convert an XLSX file using the plugin:

```bash
markitdown --use-plugins test.xlsx
```

### 3.2 Marker Plugin

You'll need Python 3.10+ and [PyTorch](https://pytorch.org/get-started/locally/).

```bash
pip install marker-pdf
```

For non‑PDF documents, install full dependencies:

```bash
pip install marker-pdf[full]
```

Convert a single file:

```bash
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```

### 3.3 Docling Plugin

Install Docling:

```bash
pip install -e .
```

Convert Excel files to different formats:

```bash
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

More [detailed installation instructions](https://docling-project.github.io/docling/installation/) are available in the docs.

### 3.4 Set Aspose License

Before using Aspose.Cells in any plugin, set the license:

**Windows (PowerShell):**

```powershell
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

**Windows (CMD):**

```cmd
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

**Unix‑based systems:**

```bash
export ASPOSE_LICENSE_PATH="/path/to/license"
```

## 4. Summary

#### AI Features:
The three tools share common advantages in AI document parsing, structured output, multi‑modal support, and integration with generative AI frameworks.

#### Aspose.Cells Plugins:
Enable seamless conversion of Excel data into Markdown, JSON, or HTML, preserving tables, formulas, and integrating directly with MarkItDown, Marker, or Docling.

#### Use Cases:
Ideal for intelligent document processing, knowledge‑base construction, RAG systems, report parsing, academic document conversion, and other AI‑driven workflows.

{{< app/cells/assistant language="python-net" >}}
