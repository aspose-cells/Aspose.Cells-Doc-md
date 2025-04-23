---
title: Конвертация Excel в PDF, изображение и другие форматы с помощью C++
linktitle: Преобразования рабочих книг
type: docs
weight: 65
url: /ru/cpp/convert-workbook-to-different-formats/
description: Конвертация файлов Excel в Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML и другие с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование между многими форматами. Технически преобразование означает загрузку книги в одном файле формата и сохранение её в другом.

{{% /alert %}}

## **Конвертировать книгу Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными структурами и отдельными лицами. Это стандартный формат документа, и разработчикам часто требуется найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать рабочую книгу Excel в JPG**
Aspose.Cells поддерживает преобразование файлов Excel в JPG.
Приведенный ниже пример кода показывает, как сохранить рабочую книгу в формате JPG.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразование рабочей книги Excel в изображение**
Aspose.Cells поддерживает преобразование файлов Excel в изображения.
Приведенный ниже пример кода показывает, как сохранить рабочую книгу в виде изображений.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразование рабочей книги Excel в XPS**

Формат документа XPS состоит из структурированной разметки XML, которая определяет макет документа и визуальное оформление каждой страницы, а также правила отображения для распределения, архивирования, отображения, обработки и печати документов.

Язык разметки для XPS — это подмножество XAML, что позволяет внедрять в документы векторную графику, используя XAML для разметки элементов Windows Presentation Foundation (WPF). Используемые элементы описываются в терминах путей и других геометрических примитивов.

Файл XPS — это, по сути, ZIP-архив в формате Unicode, использующий Open Packaging Conventions, содержащий файлы, составляющие документ. Включая XML-разметку каждой страницы, текст, встроенные шрифты, растровые изображения, двумерную векторную графику и информацию о цифровых правах. Содержимое файла XPS можно легко просмотреть, открыв его в приложении, поддерживающем ZIP-архивы.

Начиная с Aspose.Cells 6.0.0, поддерживается преобразование Microsoft Excel в XPS.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Конвертация Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells поддерживает преобразование Excel в файлы Ods, Sxc и Fods. Ниже приведён пример кода, показывающий, как преобразовать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Преобразование книги Excel в файлы MHTML**

MHTML объединяет обычный HTML с внешними ресурсами (то есть контентом, который обычно ссылается, таким как изображения, анимации, звук и т. д.) в один файл. Они используются для электронных писем с расширением файла .mht.

Aspose.Cells поддерживает чтение и запись файлов MHTML.

В приведенном ниже примере кода показано, как сохранить книгу в формате MHTML.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразование книги Excel в HTML**

API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), чтобы дать возможность управлять несколькими аспектами итогового HTML.

Приведенный ниже пример кода демонстрирует, как сохранить рабочую книгу в файл HTML.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Установка параметров изображения для HTML**

Начиная с версии 8.0.2, Aspose.Cells предоставил [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) для класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), что позволяет разработчикам задавать предпочтения по изображениям при сохранении таблиц в HTML.

Ниже перечислены некоторые свойства изображений, которые можно применять:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): указывает тип изображения. Обратите внимание, что все формы, включая диаграммы, отображаются как изображения в выходном HTML.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): указывает качество изображения в диапазоне от 0 до 100, когда [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) указан как Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): получает или задает вертикальное разрешение изображения в точках на дюйм.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): получает или задает горизонтальное разрешение изображения в точках на дюйм.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): получайте или задавайте тип сжатия изображений, когда [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) указан как Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): указывает, должен ли фон изображения быть прозрачным, когда указан формат изображения как Png.

Приведенный ниже код демонстрирует, как использовать [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) для указания различных предпочтений.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразование электронной таблицы Excel в Markdown**

API Aspose.Cells поддерживает экспорт таблиц в формат Markdown. Для экспорта активного листа в Markdown передайте [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) для задания дополнительных настроек при экспорте листа в Markdown.

Следующий пример демонстрирует экспорт активного листа в Markdown с использованием члена перечисления [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Посмотрите [генерируемый файл Markdown](md_sample.txt) для примера.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Конвертировать книгу Excel в JSON**

Aspose.Cells поддерживает преобразование рабочей книги в файл JSON (JavaScript Object Notation).

Следующий пример показывает экспорт активного листа в JSON с использованием члена перечисления [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Посмотрите код, который преобразует [исходный файл](Book1.xlsx) в [выходной JSON-файл](Book1.Json).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать Excel в XML**
Aspose.Cells поддерживает преобразование книги Excel в XML документ электронной таблицы Excel 2003 и обычные данные XML.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать книгу Excel в TIFF**
Aspose.Cells поддерживает конвертацию книги в файл TIFF.

Ниже приведен фрагмент кода, показывающий, как преобразовать Excel в TIFF:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать книгу Excel в DOCX**

API Aspose.Cells поддерживает преобразование таблиц в формат DOCX. Чтобы экспортировать книгу в DOCX, передайте [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) для задания дополнительных настроек при экспорте листа в DOCX.

Следующий пример демонстрирует экспорт активного листа в DOCX с использованием члена перечисления [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Посмотрите [сгенерированный файл DOCX](Book1.docx) как пример.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать книгу Excel в PPTX**

API Aspose.Cells поддерживает преобразование таблиц в формат PPTX. Чтобы экспортировать книгу в PPTX, передайте [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) для задания дополнительных настроек при экспорте листа в PPTX.

Следующий пример кода демонстрирует экспорт активного листа в PPTX с помощью [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) члена перечисления. Пожалуйста, посмотрите [выходной PPTX-файл](Book1.pptx), созданный кодом, для справки.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать рабочую книгу Excel в EPUB**

API Aspose.Cells поддерживает преобразование таблиц Excel в формат EPUB. Чтобы экспортировать рабочую книгу в EPUB, передайте [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) для указания дополнительных настроек при экспорте листа в EPUB.

Следующий пример кода демонстрирует экспорт активного листа в EPUB с помощью [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) члена перечисления.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразовать рабочую книгу Excel в AZW3**

API Aspose.Cells поддерживает преобразование таблиц Excel в формат AZW3. Чтобы экспортировать рабочую книгу в AZW3, передайте [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) в качестве второго параметра метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) для указания дополнительных настроек при экспорте листа в AZW3.

Следующий пример кода демонстрирует экспорт активного листа в AZW3 с помощью [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) члена перечисления.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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
