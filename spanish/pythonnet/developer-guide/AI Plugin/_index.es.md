---
title: Integración de Plugins de IA
type: docs
weight: 35
url: /es/python-net/ai-plugin-integration/
description: Integra Aspose.Cells para Python via .NET con herramientas de IA.
keywords: MarkItDown, Marker y Docling, convierten Excel a JSON, MD y HTML.
---

# Integración de Plugins de IA

Este documento resume tres herramientas de procesamiento de documentos impulsadas por IA—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker) y [Docling](https://github.com/docling-project/docling)—destacando sus características comunes de IA y su integración con [Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) a través de plugins.

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

## 2. Integración del Plugin Aspose.Cells para Python via .NET

Para combinar datos de Excel con estas herramientas de procesamiento de documentos de IA, desarrollamos plugins dedicados para cada herramienta:

| Plugin | Repositorio | Funcionalidad |
|--------|------------|---------------|
| Plugin MarkItDown | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Convierte archivos Excel a formato Markdown. |
| Plugin Marker | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Convierte archivos Excel en formatos compatibles con Marker (Markdown, JSON o HTML), aprovechando el modo LLM de Marker para mejorar las tablas. |
| Plugin Docling | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Convierte archivos Excel en objetos `DoclingDocument`, y luego exporta en Markdown, JSON o HTML para análisis multimodal. |

### 2.1 Ventajas del plugin

1. **Conversión rápida de Excel**: Convierte rápidamente el contenido de Excel en Markdown, JSON o HTML para procesamiento de IA.  
2. **Preservar información de tablas y formatos**: Preserva básicamente los datos originales de las tablas para garantizar la integridad de los datos.  
3. **Compatible con herramientas de IA**: Puede usarse directamente como entrada para MarkItDown, Marker o Docling, aprovechando sus funciones avanzadas de análisis.  
4. **Instalación sencilla**: Solo requiere la instalación adicional de Aspose.Cells para Python via .NET (aspsoe-cells-python) y seguir las instrucciones del README en los directorios de plugins.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Verificar la instalación:
```bash
markitdown --list-plugins
```
Convertir un archivo XLSX usando el plugin:
```bash
markitdown --use-plugins test.xlsx
```
### Plugin de Marcador 3.2

Necesitarás Python 3.10+ y [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
Para documentos que no sean PDF, instala todas las dependencias:
```
pip install marker-pdf[full]
```

Convierte un solo archivo:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### Plugin Docling 3.3

Instalar Docling:
```
pip install -e .
```

Convertir archivos de Excel a diferentes formatos:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Hay instrucciones de instalación [más detalladas](https://docling-project.github.io/docling/installation/) disponibles en la documentación.

### 3.4 Configurar Licencia Aspose

Antes de usar Aspose.Cells en cualquier plugin, configura la licencia:

Windows (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Sistemas basados en Unix:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. Resumen

#### Funciones de IA:
Las tres herramientas comparten ventajas comunes en el análisis de documentos con IA, salida estructurada, soporte multimodal e integración con marcos de IA generativa.

#### Plugins de Aspose.Cells:
Permite una conversión fluida de datos de Excel a Markdown, JSON o HTML, conservando tablas, fórmulas e integrándose directamente con MarkItDown, Marker o Docling.

#### Casos de Uso:
Ideal para procesamiento inteligente de documentos, construcción de bases de conocimiento, sistemas RAG, análisis de informes, conversión de documentos académicos y otros flujos de trabajo impulsados por IA.

{{< app/cells/assistant language="python-net" >}}
