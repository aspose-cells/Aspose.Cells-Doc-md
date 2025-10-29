---
title: Интеграция AI плагина
type: docs
weight: 35
url: /ru/python-net/ai-plugin-integration/
description: Интегрировать Aspose.Cells для Python via .NET с AI инструментами.
keywords: MarkItDown, Marker и Docling, преобразование Excel в JSON, MD и HTML.
---

# Интеграция AI-плагина

Этот документ подытоживает три инструмента обработки документов на базе ИИ — [MarkItDown](https://github.com/microsoft/markitdown), [Marker](https://github.com/datalab-to/marker) и [Docling](https://github.com/docling-project/docling), выделяя их общие функции ИИ и их интеграцию с [Aspose.Cells для Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/) через плагины.

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

## 2. Интеграция плагина Aspose.Cells для Python via .NET

Чтобы объединить данные Excel с этими инструментами обработки документов на базе ИИ, мы разработали специально предназначенные плагины для каждого инструмента:

| Плагин | Репозиторий | Функциональность |
|--------|------------|---------------|
| Плагин MarkItDown | [markitdown-aspose-cells-plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/markitdown-aspose-cells-plugin) | Преобразует файлы Excel в формат Markdown. |
| Плагин Marker | [marker plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/marker) | Преобразует файлы Excel в поддерживаемые Marker форматы (Markdown, JSON или HTML), используя режим LLM Marker для улучшенной таблицы. |
| Плагин Docling | [docling plugin](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Plugin/docling) | Преобразует файлы Excel в объекты `DoclingDocument`, затем экспортирует в Markdown, JSON или HTML для многомодального анализа. |

### 2.1 Преимущества плагина

1. **Быстрое преобразование Excel**: Быстро преобразует содержимое Excel в Markdown, JSON или HTML для обработки ИИ.  
2. **Сохранение информации о таблицах и форматировании**: В основном сохраняет исходные данные таблицы для обеспечения целостности данных.  
3. **Совместимость с инструментами ИИ**: Может быть использован непосредственно как входные данные для MarkItDown, Marker или Docling, используя расширенные функции парсинга.  
4. **Легкая установка**: Требует только дополнительной установки Aspose.Cells для Python via .NET(aspsoe-cells-python) и следовать инструкциям README в каталогах плагинов.

---

## 3. Installation and Usage

### 3.1 MarkItDown Plugin

Install the plugin from the current directory:

```bash
pip install -e .
```
Проверьте установку:
```bash
markitdown --list-plugins
```
Конвертация файла XLSX с помощью плагина:
```bash
markitdown --use-plugins test.xlsx
```
### Плагин Marker 3.2

Вам понадобится Python 3.10+ и [PyTorch](https://pytorch.org/get-started/locally/).

```
pip install marker-pdf
```
Для документов без PDF установите все зависимости:
```
pip install marker-pdf[full]
```

Конвертировать один файл:
```
marker_single /path/to/test.xlsx
marker_single /path/to/test.xlsx --output_format html
```
### Плагин Docling 3.3

Установите Docling:
```
pip install -e .
```

Конвертация Excel-файлов в разные форматы:
```
docling /path/test.xlsx --to html
docling /path/test.xlsx --to md
docling /path/test.xlsx --to json
```

Более [подробных инструкций по установке](https://docling-project.github.io/docling/installation/) доступно в документации.

### 3.4 Настройка лицензии Aspose

Перед использованием Aspose.Cells в любом плагине установите лицензию:

Windows (PowerShell):
```
$env:ASPOSE_LICENSE_PATH = "C:\path\to\license"
```

Windows (CMD):
```
set ASPOSE_LICENSE_PATH=C:\path\to\license
```

Системы на базе Unix:
```
export ASPOSE_LICENSE_PATH="/path/to/license"
```
## 4. Итоги

#### Возможности AI:
Три инструмента обладают общими преимуществами в распознавании AI-документов, структурированном выводе, мультимодальной поддержке и интеграции с генеративными AI-фреймворками.

#### Плагины Aspose.Cells:
Обеспечивают плавную конвертацию данных Excel в Markdown, JSON или HTML, сохраняя таблицы, формулы и интеграцию с MarkItDown, Marker или Docling.

#### Примеры использования:
Идеально подходит для обработки интеллектуальных документов, построения базы знаний, систем RAG, анализа отчетов, преобразования академических документов и других рабочих процессов на базе ИИ.

{{< app/cells/assistant language="python-net" >}}
