---
title: تكامل إضافات الذكاء الاصطناعي
type: docs
weight: 35
url: /ar/python-net/ai-plugin-integration/
description: دمج Aspose.Cells لـ Python via .NET مع أدوات الذكاء الاصطناعي.
keywords: MarkItDown و Marker و Docling، تحويل Excel إلى JSON وMD و HTML.
---

# تكامل إضافات الذكاء الاصطناعي

يلخص هذا المستند ثلاثة أدوات معالجة المستندات المدعومة بالذكاء الاصطناعي—[MarkItDown](https://github.com/microsoft/markitdown)، [Marker](https://github.com/datalab-to/marker)، و [Docling](https://github.com/docling-project/docling)—ويبرز ميزاتها المشتركة من حيث الذكاء الاصطناعي وتكاملها مع [Aspose.Cells لـ Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) من خلال الإضافات.

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

## 2. دمج إضافة Aspose.Cells لـ Python via .NET

لدمج بيانات Excel مع أدوات معالجة المستندات المدعومة بالذكاء الاصطناعي، طورنا إضافات مخصصة لكل أداة:

| الإضافة | المستودع | الوظيفة |
|--------|------------|---------------|
| إضافة MarkItDown | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | تحويل ملفات Excel إلى صيغة ماركداون. |
| إضافة Marker | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | تحويل ملفات Excel إلى صيغ يدعمها Marker (ماركداون، JSON، أو HTML)، مع الاستفادة من وضع LLM الخاص بـ Marker لتحسين الجدول. |
| إضافة Docling | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | تحويل ملفات Excel إلى كائنات `DoclingDocument`، ثم تصديرها إلى JSON أو Markdown أو HTML للتحليل متعدد الوسائط. |

### 2.1 مزايا الإضافة

1. **تحويل Excel بسرعة**: يحول بسرعة محتوى Excel إلى صيغة ماركداون أو JSON أو HTML لمعالجة الذكاء الاصطناعي.  
2. **الحفاظ على معلومات الجدول والتنسيق**: يحافظ بشكل أساسي على بيانات الجدول الأصلية لضمان سلامة البيانات.  
3. **متوافق مع أدوات الذكاء الاصطناعي**: يمكن استخدامه مباشرة كمدخلات لـ MarkItDown، Marker، أو Docling، مع الاستفادة من ميزات التحليل المتقدمة.  
4. **سهولة التثبيت**: يتطلب فقط تثبيت Aspose.Cells لـ Python via .NET (aspsoe-cells-python) واتباع تعليمات README في أدلة الإضافة.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
تحقق من التثبيت:
```bash
markitdown --list-plugins
```
تحويل ملف XLSX باستخدام الملحق:
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 ملحق العلامة التجارية

ستحتاج إلى بايثون 3.10+ و [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
للملفات غير PDF، قم بتثبيت الاعتمادات الكاملة:
```
pip install marker-pdf[full]
```

تحويل ملف واحد:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 ملحق Docling

تثبيت Docling:
```
pip install -e .
```

تحويل ملفات Excel إلى صيغ مختلفة:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

توفر المستندات مزيدًا من [تعليمات التثبيت المفصلة](https://docling-project.github.io/docling/installation/).

### 3.4 تعيين ترخيص Aspose

قبل استخدام Aspose.Cells في أي ملحق، قم بتعيين الترخيص:

ويندوز (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

ويندوز (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

أنظمة المستندات المبنية على Unix:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. ملخص

#### ميزات الذكاء الاصطناعي:
تشترك الأدوات الثلاث في مزايا مشتركة في تحليل المستندات بالذكاء الاصطناعي، والإخراج المنسق، ودعم الوسائط المتعددة، والتكامل مع أُطُر الذكاء الاصطناعي التوليدي.

#### ملحقات Aspose.Cells:
تمكين تحويل سلس لبيانات Excel إلى Markdown أو JSON أو HTML، مع الحفاظ على الجداول والصيغ ودمجها مباشرة مع MarkItDown أو Marker أو Docling.

#### حالات الاستخدام:
مثالي لمعالجة المستندات الذكية، وبناء قواعد المعرفة، وأنظمة RAG، وتحليل التقارير، وتحويل المستندات الأكاديمية، وغيرها من سير العمل المدفوعة بالذكاء الاصطناعي.

{{< app/cells/assistant language="python-net" >}}
