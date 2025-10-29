---
title: AI 插件集成
type: docs
weight: 35
url: /zh/python-net/ai-plugin-integration/
description: 将Aspose.Cells for Python via .NET集成到AI工具中。
keywords: MarkItDown、Marker和Docling，转换Excel为JSON、MD和HTML。
---

# AI插件集成

本文总结了三种基于AI的文档处理工具—[MarkItDown](https://github.com/microsoft/markitdown)、[Marker](https://github.com/datalab-to/marker)和[Docling](https://github.com/docling-project/docling)，介绍它们的共同AI特性及与[Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/)的插件集成。

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

## 2. Aspose.Cells for Python via .NET插件集成

为了将Excel数据与这些AI文档处理工具结合，我们为每个工具开发了专用插件：

| 插件 | 仓库 | 功能 |
|--------|------------|---------------|
| MarkItDown插件 | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | 将Excel文件转换为Markdown格式。 |
| Marker插件 | [marker插件](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | 将Excel文件转换为Marker支持的格式（Markdown、JSON或HTML），利用Marker的LLM模式提升表格效果。 |
| Docling插件 | [docling插件](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | 将Excel文件转换为`DoclingDocument`对象，然后导出为Markdown、JSON或HTML，用于多模态分析。 |

### 2.1 插件优势

1. **快速Excel转换**：快速将Excel内容转换为Markdown、JSON或HTML，便于AI处理。  
2. **保留表格和格式信息**：基本保留原始表格数据，确保数据完整性。  
3. **兼容AI工具**：可直接作为MarkItDown、Marker或Docling的输入，利用其高级解析功能。  
4. **易于安装**：只需额外安装Aspose.Cells for Python via .NET（aspose-cells-python）并遵循插件目录中的README说明。

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
验证安装：
```bash
markitdown --list-plugins
```
使用插件转换XLSX文件：
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 标记插件

你需要Python 3.10+和 [PyTorch](https://pytorch.org/get-started/locally/)。

```
pip install marker-pdf
```
对于非PDF文件，请安装完整依赖：
```
pip install marker-pdf[full]
```

转换单个文件：
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 Docling插件

安装Docling：
```
pip install -e .
```

将Excel文件转换为不同格式：
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

更详细的[安装指南](https://docling-project.github.io/docling/installation/)可在文档中找到。

### 3.4 设置Aspose许可证

在任何插件中使用Aspose.Cells之前，设置许可证：

Windows（PowerShell）：
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows（CMD）：
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

类Unix系统：
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4.总结

#### AI功能：
这三个工具在AI文档解析、结构化输出、多模态支持和与生成式AI框架的集成方面具有共同优势。

#### Aspose.Cells插件：
实现Excel数据无缝转换为Markdown、JSON或HTML，保留表格、公式，并与MarkItDown、Marker或Docling直接集成。

#### 使用案例：
非常适合智能文档处理、知识库构建、RAG系统、报告解析、学术文档转换和其他基于AI的工作流程。

{{< app/cells/assistant language="python-net" >}}
