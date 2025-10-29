---
title: Конвертация файла Excel в формат PDF, совместимый с PDFA 1a, с помощью Golang через C++
linktitle: Преобразование файла Excel в формат PDF, совместимый с PDFA 1a
type: docs
weight: 130
url: /ru/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Узнайте, как конвертировать файлы Excel в PDF формат, соответствующий стандарту PDF/A 1a, с помощью Aspose.Cells и Golang через C++.
---

## **Возможные сценарии использования**

PDF/A — это особая разновидность PDF, предназначенная для долгосрочного хранения документов. PDF/A — это стандартизированная ISO-версия Portable Document Format (PDF), являющаяся архивным форматом PDF, который встраивает все используемые шрифты в файл PDF. PDF/A отличается от PDF возможностью запрета некоторых функций, таких как связывание шрифтов (в отличие от внедрения шрифтов) и шифрование. Aspose.Cells позволяет сохранять файлы Excel в PDF-файлах, совместимых с PDF/A (поддерживаются PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u). В этой теме описано, как сохранять рабочую книгу Excel в PDF-файл, совместимый с PDF/A-1a.

## **Преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a**

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) для установки различных атрибутов для преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) дает контроль над настройками печати, шрифтов, безопасности и сжатия для создаваемого PDF. Самым важным свойством является [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), позволяющее сохранять файлы Excel в архивные PDF-файлы.

В следующем примере кода объясняется, как преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a. См. его [выходной PDF](outputCompliancePdfA1a.pdf) а также скриншот для справки.

## **Снимок экрана**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
