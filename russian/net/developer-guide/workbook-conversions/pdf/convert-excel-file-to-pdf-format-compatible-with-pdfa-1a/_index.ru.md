---
title: Преобразование файла Excel в формат PDF, совместимый с PDFA 1a
type: docs
weight: 130
url: /ru/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Возможные сценарии использования**

PDF/A - это уникальный вариант PDF, созданный для долгосрочного сохранения документов. PDF/A - это стандартизированная версия формата Portable Document Format (PDF), который является архивным форматом PDF, включающим все используемые шрифты в документе внутри файла PDF. PDF/A отличается от PDF тем, что запрещает такие возможности, как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Aspose.Cells позволяет вам сохранять файлы Excel в файлы PDF/A, соответствующие стандарту PDF (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u поддерживаются). Эта тема описывает, как сохранить книгу Excel в файл PDF/A с соблюдением стандарта (PDF/A-1a) PDF.

## **Преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a**

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) для установки различных атрибутов преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) дает вам контроль над параметрами печати, шрифта, безопасности и сжатия для выходных PDF. Самое важное свойство - [**PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance), позволяющее сохранять файлы Excel в файлы PDF/A, соответствующие стандарту PDF.

В следующем примере кода объясняется, как преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a. См. его [выходной PDF](outputCompliancePdfA1a.pdf) а также скриншот для справки.

## **Снимок экрана**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
{{< app/cells/assistant language="csharp" >}}
