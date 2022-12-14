---
title: Преобразование Excel в Pdf, изображение и другие форматы
linktitle: Преобразования книг
type: docs
weight: 65
url: /ru/net/convert-workbook-to-different-formats/
description: Преобразование файлов Excel в Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML и другие форматы.
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование между многими форматами. Технически преобразование означает загрузку книги в одном формате файла и сохранение ее в другом.

{{% /alert %}}

## **Конвертировать книгу Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и отдельными лицами. Это стандартный формат документов, и разработчиков программного обеспечения часто просят найти способ конвертировать Microsoft файлы Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и обеспечивает высокую визуальную точность преобразования.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Конвертировать книгу Excel в JPG**
Aspose.Cells поддерживает преобразование файлов Excel в JPG.
В приведенном ниже примере кода показано, как сохранить книгу в формате JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Преобразование книги Excel в изображение**
Aspose.Cells поддерживает преобразование файлов Excel в изображения.
В приведенном ниже примере кода показано, как сохранить книгу в виде изображений.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Преобразование книги Excel в XPS**

Формат документа XPS состоит из структурированной XML-разметки, которая определяет макет документа и внешний вид каждой страницы, а также правила рендеринга для распространения, архивирования, рендеринга, обработки и печати документов.

Язык разметки для XPS — это подмножество XAML, которое позволяет включать элементы векторной графики в документы, используя XAML для разметки примитивов Windows Presentation Foundation (WPF). Используемые элементы описываются в терминах путей и других геометрических примитивов.

Файл XPS фактически представляет собой ZIP-архив в формате Unicode, использующий Open Packaging Conventions и содержащий файлы, из которых состоит документ. К ним относятся файл разметки XML для каждой страницы, текст, встроенные шрифты, растровые изображения, двумерная векторная графика, а также информация об управлении цифровыми правами. Содержимое файла XPS можно проверить, просто открыв его в приложении, поддерживающем файлы ZIP.

Начиная с Aspose.Cells 6.0.0, Microsoft поддерживается преобразование Excel в XPS.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Преобразование Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells поддерживает преобразование файлов Excel в файлы Ods, Sxc и Fods. В приведенном ниже примере кода показано, как преобразовать[темп](book1.xlsx) в файл Ods, Sxc и Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Преобразование книги Excel в файлы MHTML**

MHTML объединяет обычный HTML с внешними ресурсами (то есть контентом, на который обычно ссылаются, таким как изображения, анимация, аудио и т. д.) в один файл. Они используются для электронных писем с расширением файла .mht.

Aspose.Cells поддерживает чтение и запись файлов MHTML.

В приведенном ниже примере кода показано, как сохранить книгу в виде файла MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Преобразование книги Excel в HTML**

 Aspose.Cells API обеспечивает поддержку экспорта электронных таблиц в формат HTML. Для этого Aspose.Cells использует**[HtmlSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**class, чтобы обеспечить гибкость управления несколькими аспектами выходного HTML.

В приведенном ниже примере кода показано, как сохранить книгу в виде HTML-файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Настройка параметров изображения для HTML**

 Начиная с 8.0.2, Aspose.Cells выставил**[Параметры изображения] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** для**[HtmlSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**class, позволяющий разработчикам указывать предпочтения изображения при сохранении электронных таблиц в формате HTML.

Ниже приведены сведения о некоторых параметрах изображения, которые можно применить.

- **[ImageType] (https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: указывает тип изображения. Обратите внимание, что все фигуры, включая диаграммы, отображаются в виде изображений в выходном HTML-коде.
- **[Режим сглаживания] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: задает сглаживание линий, кривых и краев заполненных областей.
- **[TextRenderingHint] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: определяет качество рендеринга текста.
- **[Качество](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)** : Указывает качество изображения от 0 до 100, когда**[ImageType] (https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**указывается как Jpeg.
- **[Вертикальное разрешение] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: получает или задает разрешение изображения по вертикали в точках на дюйм.
- **[Горизонтальное разрешение] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**: получает или задает разрешение изображения по горизонтали в точках на дюйм.
- **[TiffCompression] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)** : Получает или задает тип сжатия для изображений, когда**[ImageType] (https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**указывается как Tiff.
- **[Прозрачный] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**Указывает, должен ли фон изображения быть прозрачным, если ImageFormat указан как Png.

 В приведенном ниже коде показано, как использовать**[HtmlSaveOptions.ImageOptions] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**для указания различных предпочтений.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Преобразование книги Excel в Markdown**

Aspose.Cells API обеспечивает поддержку экспорта электронных таблиц в формат Markdown. Чтобы экспортировать активный рабочий лист в Markdown, передайте**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** в качестве второго параметра**[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** метод. Вы также можете использовать**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)** класс, чтобы указать дополнительные параметры для экспорта рабочего листа в Markdown.

 В следующем примере кода демонстрируется экспорт активного рабочего листа в Markdown с помощью**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** член перечисления. Пожалуйста, смотрите[выходной файл уценки](md_sample.txt)сгенерированный кодом для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Конвертировать книгу Excel в JSON**

Aspose.Cells поддерживает преобразование книги в файл Json (нотация объектов JavaScript).

 В следующем примере кода демонстрируется экспорт активного рабочего листа в Json с помощью[**СохранитьФормат.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) член перечисления. Пожалуйста, посмотрите код для преобразования[исходный файл](Book1.xlsx) к[выходной JSON-файл](Book1.Json)сгенерированный кодом для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Преобразование Excel в XML**
Aspose.Cells поддерживает преобразование книги в электронную таблицу Excel 2003 XML и простые данные XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Конвертировать книгу Excel в TIFF**
Aspose.Cells поддерживает преобразование книги в файл TIFF.

Фрагмент кода ниже показывает, как преобразовать Excel в TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Конвертировать книгу Excel в DOCX**

Aspose.Cells API обеспечивает поддержку преобразования электронных таблиц в формат DOCX. Чтобы экспортировать книгу в DOCX, передайте[**СохранитьФормат.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) в качестве второго параметра[**Книга. Сохранить**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) метод. Вы также можете использовать[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) класс, чтобы указать дополнительные параметры для экспорта рабочего листа в DOCX.

 В следующем примере кода демонстрируется экспорт активного рабочего листа в DOCX с помощью[**СохранитьФормат.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) член перечисления. Пожалуйста, смотрите[выходной файл DOCX](Book1.docx)сгенерированный кодом для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Преобразование книги Excel в PPTX**

Aspose.Cells API обеспечивает поддержку преобразования электронных таблиц в формат PPTX. Чтобы экспортировать книгу в PPTX, передайте[**СохранитьФормат.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) в качестве второго параметра[**Книга. Сохранить**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) метод. Вы также можете использовать[**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) class, чтобы указать дополнительные настройки для экспорта рабочего листа в PPTX.

 В следующем примере кода демонстрируется экспорт активного рабочего листа в PPTX с помощью[**СохранитьФормат.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) член перечисления. Пожалуйста, смотрите[выходной файл PPTX](Book1.pptx)сгенерированный кодом для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Предварительные темы**
- [Преобразование версии XLSB в XLSM](/cells/ru/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ru/net/convert-excel-to-html/)
- [Изображение](/cells/ru/net/convert-excel-to-image/)
- [Джейсон](/cells/ru/net/convert-workbook-to-json/)
- [Преобразование рабочей книги Excel в Ods, Sxc и Fods (OpenOffice/LibreOffice calc).](/cells/ru/net/convert-excel-to-ods/)
- [PDF](/cells/ru/net/convert-excel-workbook-to-pdf/)
- [Преобразование Excel в CSV, TSV и Txt](/cells/ru/net/convert-excel-to-csv-tsv-and-txt/)
- [Отслеживание процесса преобразования документа](/cells/ru/net/track-document-conversion-progress/)
- [Преобразование CSV, TSV и TXT в Excel](/cells/ru/net/convert-csv-tsv-and-txt-to-excel/)
