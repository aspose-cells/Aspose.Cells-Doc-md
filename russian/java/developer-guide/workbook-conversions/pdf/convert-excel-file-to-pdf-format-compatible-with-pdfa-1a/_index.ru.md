---
title: Преобразование файла Excel в формат PDF, совместимый с PDFA-1a.
type: docs
weight: 80
url: /ru/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **Возможные сценарии использования**

PDF/А — уникальный ароматизатор PDF, предназначенный для долговременного хранения документов. PDF/A — это стандартизованная по ISO версия Portable Document Format (PDF), представляющая собой архивный формат PDF, который включает все шрифты, используемые в документе, в файл PDF. PDF/A отличается от PDF тем, что запрещает такие функции, как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Aspose.Cells позволяет сохранять файлы Excel в файлы PDF, совместимые с PDF/A (поддерживаются как PdfA1a, так и PdfA1b). В этом разделе описывается, как сохранить книгу Excel в файл, совместимый с PDF/A (PdfA1a) PDF.

## **Преобразование файла Excel в формат PDF, совместимый с PDFA-1a.**

Разработчики могут использовать**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**класс для установки различных атрибутов для преобразования. Установка различных свойств**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class дает вам контроль над настройками печати, шрифта, безопасности и сжатия для вывода PDF. Наиболее важным свойством является**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**это позволяет сохранять файлы Excel в файлы PDF/A, совместимые с PDF.

В следующем примере кода показано, как преобразовать файл Excel в формат PDF, совместимый с PDFA-1a. Пожалуйста, посмотрите его[вывод PDF](outputCompliancePdfA1a.pdf) а также скриншот для справки.

## **Скриншот**

![дело:изображение_альтернативный_текст](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
