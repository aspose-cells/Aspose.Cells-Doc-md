---
title: AIプラグイン連携
type: docs
weight: 35
url: /ja/python-net/ai-plugin-integration/
description: Aspose.Cells for Python via .NET をAIツールに統合します。
keywords: MarkItDown、Marker、Docling、ExcelをJSON、MD、HTMLに変換。
---

# AIプラグイン連携

このドキュメントは、[MarkItDown](https://github.com/microsoft/markitdown)、 [Marker](https://github.com/datalab-to/marker)、 [Docling](https://github.com/docling-project/docling) の3つのAI支援ドキュメント処理ツールの概要と、それらが [Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) のプラグインを通じてどのように統合されているかを強調しています。

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

## 2. Aspose.Cells for Python via .NETプラグイン連携

これらのAIドキュメント処理ツールとExcelデータを連携させるために、それぞれのツール用に専用のプラグインを開発しました。

| プラグイン | リポジトリ | 機能 |
|--------|------------|---------------|
| MarkItDownプラグイン | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | ExcelファイルをMarkdown形式に変換。 |
| Markerプラグイン | [markerプラグイン](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | ExcelファイルをMarker対応形式（Markdown、JSON、HTML）に変換し、MarkerのLLMモードを活用して表を改善。 |
| Doclingプラグイン | [doclingプラグイン](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Excelファイルを `DoclingDocument` オブジェクトに変換し、Markdown、JSON、HTMLにエクスポートして多modal分析をサポート。 |

### 2.1 プラグインの利点

1. **迅速なExcel変換**：Excel内容を迅速にMarkdown、JSON、HTMLに変換し、AI処理に適用。  
2. **表とフォーマット情報の保持**：元の表データを基本的に保持し、データの完全性を確保。  
3. **AIツールとの互換性**： MarkItDown、Marker、Doclingの入力として直接使用可能で、高度な解析機能を活用。  
4. **簡単インストール**：Aspose.Cells for Python via .NET（aspose-cells-python）の追加インストールとプラグインディレクトリのREADME指示に従うだけ。

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
インストールを確認してください：
```bash
markitdown --list-plugins
```
プラグインを使用してXLSXファイルを変換：
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 マーカープラグイン

Python 3.10以上と[PyTorch](https://pytorch.org/get-started/locally/)が必要です。

```
pip install marker-pdf
```
非PDFドキュメントには完全な依存関係をインストールしてください：
```
pip install marker-pdf[full]
```

単一ファイルの変換：
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 Doclingプラグイン

Doclingをインストール：
```
pip install -e .
```

Excelファイルを異なる形式に変換：
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

詳細な[インストール手順](https://docling-project.github.io/docling/installation/)はドキュメントにあります。

### 3.4 Asposeライセンスの設定

Aspose.Cellsを使用する前に、ライセンスを設定してください：

Windows (PowerShell)：
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD)：
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Unix系システム：
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. 要約

#### AI機能：
これら3つのツールは、AIドキュメント解析、構造化出力、多モーダル対応、生成AIフレームワークとの連携において共通の利点を持っています。

#### Aspose.Cellsプラグイン：
ExcelデータをMarkdown、JSON、HTMLにシームレスに変換し、表や数式を保持し、MarkItDown、Marker、Doclingと直接連携します。

#### 利用ケース：
インテリジェント文書処理、ナレッジベース構築、RAGシステム、レポート解析、学術文書変換、その他のAI駆動ワークフローに最適です。

{{< app/cells/assistant language="python-net" >}}
