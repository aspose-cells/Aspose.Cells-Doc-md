---
title: Yapay Zeka Eklenti Entegrasyonu
type: docs
weight: 35
url: /tr/python-net/ai-plugin-integration/
description: Aspose.Cells for Python via .NET yi Yapay Zeka araçlarına entegre edin.
keywords: MarkItDown, Marker ve Docling,Excel i JSON,MD ve HTML ye dönüştürür.
---

# Yapay Zeka Eklenti Entegrasyonu

Bu belge, üç Yapay Zeka destekli belge işleme aracını—[MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker), ve [Docling](https://github.com/docling-project/docling)—özetler ve bunların ortak Yapay Zeka özelliklerini ve [Aspose.Cells for Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) ile eklentiler aracılığıyla entegrasyonunu vurgular.

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

## 2. Aspose.Cells for Python via .NET Eklenti Entegrasyonu

Excel verilerini bu Yapay Zeka belge işleme araçlarıyla birleştirmek için her araç için özel eklentiler geliştirdik:

| Eklenti | Depo | İşlevsellik |
|--------|------------|---------------|
| MarkItDown Eklentisi | [markitdown-aspose-cells-eklenti](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Excel dosyalarını Markdown formatına dönüştürür. |
| Marker Eklentisi | [marker eklentisi](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Excel dosyalarını Marker destekli formatlara (Markdown, JSON veya HTML) dönüştürür, Marker’in LLM modunu kullanarak daha gelişmiş tablo sağlar. |
| Docling Eklentisi | [docling eklentisi](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Excel dosyalarını `DoclingDocument` nesnelerine dönüştürür, ardından Markdown, JSON veya HTML olarak dışa aktarır, çok modlu analiz için. |

### 2.1 Eklenti Avantajları

1. **Hızlı Excel Dönüşümü**: Excel içeriğini hızla Markdown, JSON veya HTML'e dönüştürerek Yapay Zeka işlemleri için hazır hale getirir.  
2. **Tablo ve Biçim Bilgisini Koruma**: Temelde orijinal tablo verilerini koruyarak veri bütünlüğünü sağlar.  
3. **Yapay Zeka Araçlarıyla Uyumluluk**: MarkItDown, Marker veya Docling'e doğrudan giriş olarak kullanılabilir, gelişmiş çözümleme özelliklerinden yararlanır.  
4. **Kolay Kurulum**: Ek olarak, Aspose.Cells for Python via .NET(aspose-cells-python) kurulumu ve eklenti dizinlerindeki README talimatlarının izlenmesi yeterlidir.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Kurulumu doğrula:
```bash
markitdown --list-plugins
```
Bir XLSX dosyasını eklenti kullanarak dönüştürün:
```bash
markitdown --use-plugins test.xlsx
```
### 3.2 Marker Eklentisi

Python 3.10+ ve [PyTorch](https://pytorch.org/get-started/locally/) gerekebilir.

```
pip install marker-pdf
```
PDF olmayan belgeler için tam bağımlılıkları yükleyin:
```
pip install marker-pdf[full]
```

Tek bir dosya dönüştür:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### 3.3 Docling Eklentisi

Docling'i yükleyin:
```
pip install -e .
```

Excel dosyalarını farklı formatlara dönüştürün:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Daha fazla [ayrıntılı yükleme talimatları](https://docling-project.github.io/docling/installation/) belgelerde bulunmaktadır.

### 3.4 Aspose Lisansını Ayarla

Herhangi bir eklentide Aspose.Cells kullanmadan önce lisansı ayarlayın:

Windows (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Unix tabanlı sistemler:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. Özet

#### Yapay Zeka Özellikleri:
Üç araç, yapay zeka belge ayrıştırma, yapılandırılmış çıktı, çok modlu destek ve üretici yapay zeka çerçeveleriyle entegrasyonda ortak avantajlar paylaşır.

#### Aspose.Cells Eklentileri:
Excel verilerinin Markdown, JSON veya HTML'ye sorunsuz dönüştürülmesini sağlar, tabloları, formülleri koruyarak ve doğrudan MarkItDown, Marker veya Docling ile entegre edilir.

#### Kullanım Durumları:
Akıllı belge işleme, bilgi tabanı oluşturma, RAG sistemleri, rapor çözümleme, akademik belge dönüştürme ve diğer AI güdümlü iş akışları için idealdir.

{{< app/cells/assistant language="python-net" >}}
