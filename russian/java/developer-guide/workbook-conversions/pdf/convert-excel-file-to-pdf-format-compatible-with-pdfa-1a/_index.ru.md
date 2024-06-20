---
title: Преобразование файла Excel в формат PDF, совместимый с PDFA 1a
type: docs
weight: 80
url: /ru/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Возможные сценарии использования**

PDF/A - это уникальный вариант PDF, созданный для долгосрочного сохранения документов. PDF/A - это стандартизированная версия формата Portable Document Format (PDF), который является архивным форматом PDF, включающим все используемые шрифты в документе внутри файла PDF. PDF/A отличается от PDF тем, что запрещает такие возможности, как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Aspose.Cells позволяет вам сохранять файлы Excel в файлы PDF/A, соответствующие стандарту PDF (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u поддерживаются). Эта тема описывает, как сохранить книгу Excel в файл PDF/A с соблюдением стандарта (PDF/A-1a) PDF.

## **Преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a**

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) для установки различных атрибутов для конвертации. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) дает вам контроль над параметрами печати, шрифтом, настройками безопасности и сжатия для выходного PDF. Самое важное свойство - это [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance), которое позволяет сохранять файлы Excel в форматах PDF/A совместимых файлов PDF.

В следующем примере кода объясняется, как преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a. См. его [выходной PDF](outputCompliancePdfA1a.pdf) а также скриншот для справки.

## **Снимок экрана**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
