---
title: Преобразование файла Excel в формат PDF, совместимый с PDFA 1a
type: docs
weight: 130
url: /ru/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Узнайте, как конвертировать файл Excel в формат PDF, совместимый с PDFA 1a, с помощью Aspose.Cells для Python via .NET API.
keywords: Python конвертировать файл Excel в формат PDF, совместимый с PDFA 1a, PDFA 1a, PDFA 1b, PDF14, PDF15, PDF16, PDF17
---

## **Возможные сценарии использования**

PDF/A - это уникальный вариант PDF, разработанный для долгосрочного сохранения документов. PDF/A - это стандартизированная версия формата Portable Document Format (PDF), который является архивным форматом PDF, в который встраиваются все используемые в документе шрифты. PDF/A отличается от PDF тем, что запрещает функции, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Aspose.Cells для Python via .NET позволяет сохранять файлы Excel в соответствующие стандарту PDF/A файлы PDF (поддерживаются PdfA1a и PdfA1b). В этой теме описано, как сохранить книгу Excel в формате PDF/A с соблюдением стандарта (PdfA1a).

## **Преобразовать файл Excel в формат PDF, совместимый с PDFA-1а**

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) для установки различных атрибутов преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) дает вам контроль над параметрами печати, шрифта, безопасности и сжатия для выходных PDF. Самое важное свойство - [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/), позволяющее сохранять файлы Excel в файлы PDF/A, соответствующие стандарту PDF.

В следующем примере кода объясняется, как преобразовать файл Excel в формат PDF, совместимый с PDFA-1а. Пожалуйста, ознакомьтесь с [выходным PDF](outputCompliancePdfA1a.pdf), а также скриншотом для справки.

## **Снимок экрана**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertExcelFileToPDFA_1a.py" >}}
