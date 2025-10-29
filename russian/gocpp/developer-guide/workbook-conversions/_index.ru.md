---
title: Конвертация Excel в Pdf, Image и другие форматы с помощью Golang через C++
linktitle: Преобразования рабочих книг
type: docs
weight: 65
url: /ru/go-cpp/convert-workbook-to-different-formats/
description: Конвертация файлов Excel в Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML и другие с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование между многими форматами. Технически преобразование означает загрузку книги в одном файле формата и сохранение её в другом.

{{% /alert %}}

## **Конвертировать книгу Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными структурами и отдельными лицами. Это стандартный формат документа, и разработчикам часто требуется найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **Преобразовать рабочую книгу Excel в JPG**
Aspose.Cells поддерживает преобразование файлов Excel в JPG.
Приведенный ниже пример кода показывает, как сохранить рабочую книгу в формате JPG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Преобразование рабочей книги Excel в изображение**
Aspose.Cells поддерживает преобразование файлов Excel в изображения.
Приведенный ниже пример кода показывает, как сохранить рабочую книгу в виде изображений.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **Преобразование рабочей книги Excel в XPS**

Формат документа XPS состоит из структурированной разметки XML, которая определяет макет документа и визуальное оформление каждой страницы, а также правила отображения для распределения, архивирования, отображения, обработки и печати документов.

Язык разметки для XPS — это подмножество XAML, что позволяет внедрять в документы векторную графику, используя XAML для разметки элементов Windows Presentation Foundation (WPF). Используемые элементы описываются в терминах путей и других геометрических примитивов.

Файл XPS — это, по сути, ZIP-архив в формате Unicode, использующий Open Packaging Conventions, содержащий файлы, составляющие документ. Включая XML-разметку каждой страницы, текст, встроенные шрифты, растровые изображения, двумерную векторную графику и информацию о цифровых правах. Содержимое файла XPS можно легко просмотреть, открыв его в приложении, поддерживающем ZIP-архивы.

Начиная с Aspose.Cells 6.0.0, поддерживается преобразование Microsoft Excel в XPS.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **Конвертация Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells поддерживает преобразование Excel в файлы Ods, Sxc и Fods. Ниже приведён пример кода, показывающий, как преобразовать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **Преобразование книги Excel в файлы MHTML**

MHTML объединяет обычный HTML с внешними ресурсами (то есть контентом, который обычно ссылается, таким как изображения, анимации, звук и т. д.) в один файл. Они используются для электронных писем с расширением файла .mht.

Aspose.Cells поддерживает чтение и запись файлов MHTML.

В приведенном ниже примере кода показано, как сохранить книгу в формате MHTML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **Преобразование книги Excel в HTML**

API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/), чтобы дать возможность управлять несколькими аспектами итогового HTML.

Приведенный ниже пример кода демонстрирует, как сохранить рабочую книгу в файл HTML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **Установка параметров изображения для HTML**

Начиная с версии 8.0.2, Aspose.Cells предоставил [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) для класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), что позволяет разработчикам задавать предпочтения по изображениям при сохранении таблиц в HTML.

Ниже перечислены некоторые свойства изображений, которые можно применять:

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/): указывает тип изображения. Обратите внимание, что все формы, включая диаграммы, отображаются как изображения в выходном HTML.
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/): указывает качество изображения в диапазоне от 0 до 100, когда [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) указан как Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/): получает или задает вертикальное разрешение изображения в точках на дюйм.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/): получает или задает горизонтальное разрешение изображения в точках на дюйм.
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/): получайте или задавайте тип сжатия изображений, когда [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) указан как Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/): указывает, должен ли фон изображения быть прозрачным, когда указан формат изображения как Png.

Приведенный ниже код демонстрирует, как использовать [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) для указания различных предпочтений.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **Преобразование электронной таблицы Excel в Markdown**

API Aspose.Cells поддерживает экспорт таблиц в формат Markdown. Для экспорта активного листа в Markdown передайте [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) для задания дополнительных настроек при экспорте листа в Markdown.

Следующий пример демонстрирует экспорт активного листа в Markdown с использованием члена перечисления [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/). Посмотрите [генерируемый файл Markdown](md_sample.txt) для примера.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **Конвертировать книгу Excel в JSON**

Aspose.Cells поддерживает преобразование рабочей книги в файл JSON (JavaScript Object Notation).

Следующий пример показывает экспорт активного листа в JSON с использованием члена перечисления [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). Посмотрите код, который преобразует [исходный файл](Book1.xlsx) в [выходной JSON-файл](Book1.Json).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **Преобразовать Excel в XML**
Aspose.Cells поддерживает преобразование книги Excel в XML документ электронной таблицы Excel 2003 и обычные данные XML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **Преобразовать книгу Excel в TIFF**
Aspose.Cells поддерживает конвертацию книги в файл TIFF.

Ниже приведен фрагмент кода, показывающий, как преобразовать Excel в TIFF:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **Преобразовать книгу Excel в DOCX**

API Aspose.Cells поддерживает преобразование таблиц в формат DOCX. Чтобы экспортировать книгу в DOCX, передайте [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) для задания дополнительных настроек при экспорте листа в DOCX.

Следующий пример демонстрирует экспорт активного листа в DOCX с использованием члена перечисления [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/). Посмотрите [сгенерированный файл DOCX](Book1.docx) как пример.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **Преобразовать книгу Excel в PPTX**

API Aspose.Cells поддерживает преобразование таблиц в формат PPTX. Чтобы экспортировать книгу в PPTX, передайте [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) для задания дополнительных настроек при экспорте листа в PPTX.

Следующий пример кода демонстрирует экспорт активного листа в PPTX с помощью [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) члена перечисления. Пожалуйста, посмотрите [выходной PPTX-файл](Book1.pptx), созданный кодом, для справки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **Преобразовать рабочую книгу Excel в EPUB**

API Aspose.Cells поддерживает преобразование таблиц Excel в формат EPUB. Чтобы экспортировать рабочую книгу в EPUB, передайте [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) для указания дополнительных настроек при экспорте листа в EPUB.

Следующий пример кода демонстрирует экспорт активного листа в EPUB с помощью [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) члена перечисления.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **Преобразовать рабочую книгу Excel в AZW3**

API Aspose.Cells поддерживает преобразование таблиц Excel в формат AZW3. Чтобы экспортировать рабочую книгу в AZW3, передайте [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) для указания дополнительных настроек при экспорте листа в AZW3.

Следующий пример кода демонстрирует экспорт активного листа в AZW3 с помощью [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) члена перечисления.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **Продвинутые темы**
- [Преобразование версии XLSB в XLSM](/cells/ru/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ru/cpp/convert-excel-to-html/)
- [Изображение](/cells/ru/cpp/convert-excel-to-image/)
- [Json](/cells/ru/cpp/convert-workbook-to-json/)
- [Преобразовать Excel-таблицу в Ods, Sxc и Fods (OpenOffice / LibreOffice calc).](/cells/ru/cpp/convert-excel-to-ods/)
- [Pdf](/cells/ru/cpp/convert-excel-workbook-to-pdf/)
- [Преобразовать Excel в CSV, TSV и Txt](/cells/ru/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Отслеживание прогресса конвертации документов](/cells/ru/cpp/track-document-conversion-progress/)
- [Преобразовать CSV, TSV и TXT в Excel](/cells/ru/cpp/convert-csv-tsv-and-txt-to-excel/)
