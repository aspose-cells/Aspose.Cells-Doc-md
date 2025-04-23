---
title: Преобразовать Excel в Pdf, изображение и другие форматы
linktitle: Преобразования рабочих книг
type: docs
weight: 65
url: /ru/net/convert-workbook-to-different-formats/
description: Преобразование файлов Excel в Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML и многие другие.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает конвертацию между множеством форматов. Технически, конвертация означает загрузку книги в одном формате файла и сохранение ее в другом.

{{% /alert %}}

## **Конвертировать книгу Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Преобразовать рабочую книгу Excel в JPG**
Aspose.Cells поддерживает преобразование файлов Excel в JPG.
Приведенный ниже пример кода показывает, как сохранить рабочую книгу в формате JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Преобразование рабочей книги Excel в изображение**
Aspose.Cells поддерживает преобразование файлов Excel в изображения.
Приведенный ниже пример кода показывает, как сохранить рабочую книгу в виде изображений.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Преобразование рабочей книги Excel в XPS**

Формат документа XPS состоит из структурированной разметки XML, которая определяет макет документа и визуальное оформление каждой страницы, а также правила отображения для распределения, архивирования, отображения, обработки и печати документов.

Язык разметки для XPS является подмножеством XAML, что позволяет ему включать элементы векторной графики в документы, используя XAML для разметки примитивов Windows Presentation Foundation (WPF). Используемые элементы описаны в терминах путей и других геометрических примитивов.

Файл XPS, на самом деле, является файлом UNICODE ZIP-архива с использованием упаковочных соглашений Open Packaging Conventions, содержащий файлы, из которых состоит документ. Эти включают XML-файл разметки для каждой страницы, текст, встроенные шрифты, растровые изображения, 2D векторную графику, а также информацию о цифровом управлении правами. Содержимое файла XPS можно изучить, просто открыв его в приложении, которое поддерживает ZIP-файлы.

Начиная с Aspose.Cells 6.0.0, поддерживается преобразование Microsoft Excel в XPS.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Преобразовать Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells поддерживает преобразование файлов Excel в файлы Ods, Sxc и Fods. Приведенный ниже пример кода показывает, как преобразовать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Преобразование книги Excel в файлы MHTML**

MHTML объединяет обычный HTML с внешними ресурсами (то есть контентом, который обычно ссылается, таким как изображения, анимации, звук и т. д.) в один файл. Они используются для электронных писем с расширением файла .mht.

Aspose.Cells поддерживает чтение и запись файлов MHTML.

В приведенном ниже примере кода показано, как сохранить книгу в формате MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Преобразование книги Excel в HTML**

API Aspose.Cells предоставляет поддержку экспорта электронных таблиц в формат HTML. Для этой цели Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions) для обеспечения гибкости управления несколькими аспектами выходного HTML.

Приведенный ниже пример кода демонстрирует, как сохранить рабочую книгу в файл HTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Установка параметров изображения для HTML**

Начиная с версии 8.0.2, Aspose.Cells предлагает [**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) для класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions), что позволяет разработчикам указывать предпочтения изображения при сохранении электронных таблиц в формат HTML.

Ниже приведены подробности некоторых настроек изображения, которые могут быть применены,

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype): указывает тип изображения. Обратите внимание, что все формы, включая диаграммы, отображаются как изображения в выходном HTML.
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): указывает сглаживание линий, кривых и краев заполненных областей.
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): указывает качество отображения текста.
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality): указывает качество изображения от 0 до 100, когда [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) указан как Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): получает или задает вертикальное разрешение изображения в точках на дюйм.
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): получает или задает горизонтальное разрешение изображения в точках на дюйм.
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): получает или задает тип сжатия для изображений, когда [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) указан как Tiff.
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent): указывает, должен ли фон изображения быть прозрачным, когда указан формат изображения как Png.

Ниже приведен пример кода, демонстрирующий использование [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) для указания различных предпочтений.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Преобразование электронной таблицы Excel в Markdown**

API Aspose.Cells предоставляет поддержку экспорта электронных таблиц в формат Markdown. Для экспорта активного листа в формат Markdown, передайте [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Вы также можете использовать класс [**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions), чтобы указать дополнительные параметры для экспорта листа в формат Markdown.

Приведенный ниже пример кода демонстрирует экспорт активного листа в формат Markdown с использованием элемента перечисления [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Пожалуйста, обратитесь к [выходному файлу Markdown](md_sample.txt), созданному кодом, в качестве справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Конвертировать книгу Excel в JSON**

Aspose.Cells поддерживает преобразование книги в файл JSON (JavaScript Object Notation).

Ниже приведен пример кода, демонстрирующий экспорт активного листа в Json с использованием [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) члена перечисления. Пожалуйста, см. код для преобразования [исходного файла](Book1.xlsx) в [выходной файл Json](Book1.Json), созданный кодом для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Преобразовать Excel в XML**
Aspose.Cells поддерживает преобразование книги Excel в XML документ электронной таблицы Excel 2003 и обычные данные XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Преобразовать книгу Excel в TIFF**
Aspose.Cells поддерживает конвертацию книги в файл TIFF.

Ниже приведен фрагмент кода, показывающий, как преобразовать Excel в TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Преобразовать книгу Excel в DOCX**

API Aspose.Cells поддерживает конвертацию электронных таблиц в формат DOCX. Чтобы экспортировать книгу в формат DOCX, укажите [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) вторым параметром метода [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Вы также можете использовать класс [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) для указания дополнительных параметров экспорта листа в формат DOCX.

Приведенный ниже пример кода демонстрирует экспорт активного листа в формат DOCX с использованием элемента перечисления [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Пожалуйста, посмотрите [файл DOCX](Book1.docx), сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Преобразовать книгу Excel в PPTX**

API Aspose.Cells поддерживает конвертацию электронных таблиц в формат PPTX. Чтобы экспортировать книгу в формат PPTX, укажите [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) вторым параметром метода [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Вы также можете использовать класс [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) для указания дополнительных параметров экспорта листа в формат PPTX.

Приведенный ниже пример кода демонстрирует экспорт активного листа в формат PPTX с использованием элемента перечисления [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Пожалуйста, посмотрите [файл PPTX](Book1.pptx), сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Преобразовать рабочую книгу Excel в EPUB**

API Aspose.Cells поддерживает преобразование таблиц в формат EPUB. Чтобы экспортировать рабочую книгу в EPUB, передайте [**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) как второй параметр метода [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Вы также можете использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions) для задания дополнительных настроек при экспорте листа в EPUB.

Следующий пример кода демонстрирует экспорт активного листа в EPUB с помощью перечисления [**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToEPUB-1.cs" >}}

## **Преобразовать рабочую книгу Excel в AZW3**

API Aspose.Cells поддерживает преобразование таблиц в формат AZW3. Чтобы экспортировать рабочую книгу в AZW3, передайте [**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) как второй параметр метода [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Вы также можете использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions) для задания дополнительных настроек при экспорте листа в AZW3.

Следующий пример кода демонстрирует экспорт активного листа в AZW3 с помощью перечисления [**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToAZW3-1.cs" >}}

## **Продвинутые темы**
- [Преобразование версии XLSB в XLSM](/cells/ru/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ru/net/convert-excel-to-html/)
- [Изображение](/cells/ru/net/convert-excel-to-image/)
- [Json](/cells/ru/net/convert-workbook-to-json/)
- [Преобразовать книгу Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice calc).](/cells/ru/net/convert-excel-to-ods/)
- [Pdf](/cells/ru/net/convert-excel-workbook-to-pdf/)
- [Преобразовать Excel в CSV, TSV и Txt](/cells/ru/net/convert-excel-to-csv-tsv-and-txt/)
- [Отслеживание прогресса конвертации документов](/cells/ru/net/track-document-conversion-progress/)
- [Преобразование CSV, TSV и TXT в Excel](/cells/ru/net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="csharp" >}}
