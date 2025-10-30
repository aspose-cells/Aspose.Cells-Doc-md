---
title: Konvertera Excel till Pdf, Bild och andra format med C++
linktitle: Arbetsbokskonverteringar
type: docs
weight: 65
url: /sv/cpp/convert-workbook-to-different-formats/
description: Konvertera Excel filer till Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML och mer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering mellan många format. Teknisk sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel Arbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, myndigheter och individer. Det är ett standarddokumentformat, och programvaruutvecklare ombeds ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

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

## **Konvertera Excel-arbetsbok till JPG**
Aspose.Cells stöder konvertering av Excel-filer till JPG.
Exemplet nedan visar hur man sparar en arbetsbok som JPG.

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

## **Konvertera Excel-arbetsbok till bild**
Aspose.Cells stöder konvertering av Excel-filer till bilder.
Exemplet nedan visar hur man sparar en arbetsbok som bilder.

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

## **Konvertera Excel-arbetsbok till XPS**

XPS-dokumentformatet består av strukturerad XML-markering som definierar layouten för ett dokument och det visuella utseendet för varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

 markup-språket för XPS är en delmängd av XAML, vilket gör att det kan innehålla vektorgrafik-element i dokumenten, med XAML för att markera Windows Presentation Foundation (WPF) primitives. De använda elementen beskrivs i termer av vägar och andra geometriska primitiva.

En XPS-fil är faktiskt ett Unicode ZIP-arkiv som använder Open Packaging Conventions, och innehåller filer som utgör dokumentet. Dessa inkluderar en XML-markupfil för varje sida, text, inbäddade typsnitt, rasterbilder, 2D vektorgrafik samt digitala rättighetsstyrningsinformation. Innehållet i en XPS-fil kan enkelt granskas genom att öppna den i ett program som stöder ZIP-filer.

Från Aspose.Cells 6.0.0, stöds konvertering från Microsoft Excel till XPS.

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

## **Konvertera Excel till Ods, Sxc och Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells stöder konvertering av Excel-filer till Ods, Sxc och Fods filer. Exemplet nedan visar hur du konverterar [mall](book1.xlsx) till Ods, Sxc och Fods filer.

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

## **Konvertera Excel arbetsbok till MHTML-filer**

MHTML kombinerar vanlig HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljuddokument med mera) till en enda fil. De används för e-postmeddelanden med filändelsen .mht.

Aspose.Cells stödjer att läsa och skriva MHTML-filer.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

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

## **Konvertera Excelfil till HTML**

Aspose.Cells API stöder export av kalkylblad till HTML-format. För detta använder Aspose.Cells klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) för att ge flexibilitet att kontrollera flera aspekter av utdata-HTML:en.

Kodexemplet nedan visar hur du sparar en arbetsbok som en HTML-fil.

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

## **Inställning av bildpreferenser för HTML**

Från version 8.0.2 har Aspose.Cells exponerat [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) för klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) vilket möjliggör för utvecklare att specificera bildpreferenser vid sparande av kalkylblad till HTML-format.

Nedanför finns detaljer om några av bildinställningarna som kan tillämpas:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): Specificerar bildtypen. Observera att alla former, inklusive diagram, renderas som bilder i utdata-HTML.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): Anger bildkvaliteten mellan 0 till 100 när [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) anges som Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): Hämtar eller anger den vertikala upplösningen för bilden i punkter per tum.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): Hämtar eller anger den horisontella upplösningen för bilden i punkter per tum.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): Hämta eller sätta kompressionstyp för bilder när [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) är specificerat som Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): Anger om bakgrunden för en bild ska vara transparent när ImageFormat anges som Png.

Koden nedan visar hur man använder [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) för att ange olika preferenser.

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

## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells API stöder export av kalkblad till Markdown-format. För att exportera det aktiva kalkbladet till Markdown, skicka [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Du kan också använda [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) klass för att specificera ytterligare inställningar för export av kalkblad till Markdown.

Följande kodexempel visar hur man exporterar det aktiva kalkbladet till Markdown med hjälp av [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration-medlem. Se den genererade [Markdown-utdatafilen](md_sample.txt) som referens.

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

## **Konvertera Excel-arbetsbok till JSON**

Aspose.Cells stödjer konvertering av en arbetsbok till JSON (JavaScript Object Notation).

Följande kodexempel visar hur man exporterar det aktiva kalkbladet till JSON med hjälp av [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration-medlem. Se koden för att konvertera [källfilen](Book1.xlsx) till den [utgångs-JSON filen](Book1.Json) som genererats av koden som referens.

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

## **Konvertera Excel till XML**
Aspose.Cells stöder konvertering av en arbetsbok till Excel 2003 Spreadsheet XML och vanliga XML-data.

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

## **Konvertera Excel-arbetsbok till TIFF**
Aspose.Cells stöder konvertering av en arbetsbok till TIFF-fil.

Kodsnutten nedan visar hur man konverterar Excel till TIFF:

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

## **Konvertera Excel-arbetsbok till DOCX**

Aspose.Cells API stöder konvertering av kalkblad till DOCX-format. För att exportera arbetsboken till DOCX, skicka [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Du kan också använda [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) klass för att specificera ytterligare inställningar för export av kalkblad till DOCX.

Följande kodexempel visar hur man exporterar det aktiva kalkbladet till DOCX med hjälp av [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration-medlem. Se den genererade [DOCX-utdatafilen](Book1.docx) som referens.

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

## **Konvertera Excel-arbetsbok till PPTX**

Aspose.Cells API stöder konvertering av kalkblad till PPTX-format. För att exportera arbetsboken till PPTX, skicka [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Du kan också använda [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) klass för att specificera ytterligare inställningar för export av kalkblad till PPTX.

Följande kodexempel demonstrerar export av aktivt kalkylblad till PPTX med hjälp av [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerationsmedlem. Se den [utgångs-PPTX-fil](Book1.pptx) som genererats av koden för referens.

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

## **Konvertera Excel-arbetsbok till EPUB**

Aspose.Cells API stöder konvertering av kalkylblad till EPUB-format. För att exportera arbetsboken till EPUB, skicka [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metoden. Du kan också använda [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-klassen för att specificera ytterligare inställningar för export av kalkylbladet till EPUB.

Följande kodexempel demonstrerar export av aktivt kalkylblad till EPUB med hjälp av [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerationsmedlem.

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

## **Konvertera Excel-arbetsbok till AZW3**

Aspose.Cells API stöder konvertering av kalkylblad till AZW3-format. För att exportera arbetsboken till AZW3, skicka [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metoden. Du kan också använda [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-klassen för att specificera ytterligare inställningar för export av kalkylblad till AZW3.

Följande kodexempel demonstrerar export av aktivt kalkylblad till AZW3 med hjälp av [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerationsmedlem.

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

## **Fortsatta ämnen**
- [Konvertera revidering av XLSB till XLSM](/cells/sv/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/sv/cpp/convert-excel-to-html/)
- [Bild](/cells/sv/cpp/convert-excel-to-image/)
- [Json](/cells/sv/cpp/convert-workbook-to-json/)
- [Konvertera Excelarbetsbok till Ods, Sxc och Fods (OpenOffice / LibreOffice calc).](/cells/sv/cpp/convert-excel-to-ods/)
- [Pdf](/cells/sv/cpp/convert-excel-workbook-to-pdf/)
- [Konvertera Excel till CSV, TSV och Txt](/cells/sv/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Spåra Dokumentkonverteringsframsteg](/cells/sv/cpp/track-document-conversion-progress/)
- [Konvertera CSV, TSV och TXT till Excel](/cells/sv/cpp/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="cpp" >}}
