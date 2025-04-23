---
title: Excel in Pdf, Image und andere Formate mit C++ konvertieren
linktitle: Arbeitsmappen Konvertierungen
type: docs
weight: 65
url: /de/cpp/convert-workbook-to-different-formats/
description: Konvertieren Sie Excel Dateien in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML und mehr mit Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in ein anderes zu speichern.

{{% /alert %}}

## **Excel-Arbeitsmappe in PDF konvertieren**

PDF-Dateien werden häufig verwendet, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es ist ein standardisiertes Dokumentformat und Softwareentwickler werden oft gefragt, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente umzuwandeln.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

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

## **Excel-Arbeitsmappe in JPG konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in JPG.
Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als JPG speichert.

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

## **Excel-Arbeitsmappe in Bild konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Bilder.
Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als Bilder speichert.

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

## **Excel-Arbeitsmappe in XPS konvertieren**

Das XPS-Dokumentenformat besteht aus strukturierter XML-Auszeichnung, die das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite sowie Rendering-Regeln zur Verteilung, Archivierung, Darstellung, Verarbeitung und zum Drucken von Dokumenten definiert.

Das Markup-Sprachenformat für XPS ist ein Teilmenge von XAML, was es ermöglicht, Vektorgrafikelemente in Dokumenten zu integrieren, indem XAML verwendet wird, um die Windows Presentation Foundation (WPF) Primitive zu kennzeichnen. Die verwendeten Elemente werden in Bezug auf Pfade und andere geometrische Primitive beschrieben.

Eine XPS-Datei ist tatsächlich ein Unicode-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, aus denen das Dokument besteht. Diese umfassen eine XML-Markup-Datei für jede Seite, Text, eingebettete Schriftarten, Rasterbilder, 2D-Vektorgrafiken sowie Digital Rights Management-Informationen. Der Inhalt einer XPS-Datei kann einfach durch Öffnen in einer Anwendung geprüft werden, die ZIP-Dateien unterstützt.

Ab Aspose.Cells 6.0.0 wird die Konvertierung von Microsoft Excel in XPS unterstützt.

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

## **Excel in Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Ods, Sxc und Fods Dateien. Das unten stehende Codebeispiel zeigt, wie die [Vorlage](book1.xlsx) in Ods, Sxc und Fods Dateien konvertiert wird.

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

## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**

MHTML kombiniert normales HTML mit externen Ressourcen (das heißt, Inhalt, der normalerweise verknüpft ist, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als MHTML-Datei speichert.

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

## **Excel-Arbeitsmappe in HTML konvertieren**

Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.

Das folgende Beispiel zeigt, wie man eine Arbeitsmappe als HTML-Datei speichert.

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

## **Bildvoreinstellungen für HTML einstellen**

Ab Version 8.0.2 hat Aspose.Cells die [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) für die [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) Klasse öffentlich gemacht, um Entwicklern die Angabe von Bildeinstellungen beim Speichern von Tabellen in HTML-Format zu ermöglichen.

Im Folgenden sind einige Bild-Einstellungen aufgeführt, die angewendet werden können:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): Gibt den Bildtyp an. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): Gibt die Qualität des Bildes zwischen 0 und 100 an, wenn [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) als Jpeg angegeben ist.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): Holt oder setzt den Komprimierungstyp für die Bilder, wenn [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) als Tiff angegeben ist.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png angegeben ist.

Der unten stehende Code demonstriert, wie man [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) verwendet, um verschiedene Präferenzen festzulegen.

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

## **Excel-Arbeitsmappe in Markdown konvertieren**

Das Aspose.Cells API unterstützt den Export von Tabellen in das Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, übergeben Sie [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Sie können auch die [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach Markdown festzulegen.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt mit [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Enumeration-Mitglied in Markdown exportiert werden kann. Bitte beachten Sie die [Ausgabedatei im Markdown-Format](md_sample.txt), die durch den Code erzeugt wurde.

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

## **Excel-Arbeitsmappe in JSON konvertieren**

Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine JSON (JavaScript Object Notation)-Datei.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt in JSON mit [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Enumeration-Mitglied exportiert werden kann. Bitte sehen Sie den Code, um die [Quelle-Datei](Book1.xlsx) in die [Ausgabe-JSON-Datei](Book1.Json) zu konvertieren.

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

## **Excel in XML umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in das Excel 2003 Spreadsheet XML- und das Plain-XML-Format.

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

## **Excel-Arbeitsmappe in TIFF umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine TIFF-Datei.

Der unten stehende Codeausschnitt zeigt, wie Excel in TIFF umgewandelt wird:

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

## **Excel-Arbeitsmappe in DOCX umwandeln**

Das Aspose.Cells API bietet Unterstützung für die Konvertierung von Tabellen in das DOCX-Format. Um die Arbeitsmappe in DOCX zu exportieren, übergeben Sie [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Sie können auch die [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach DOCX festzulegen.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt mit [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Enumeration-Mitglied in DOCX exportiert werden kann. Bitte beachten Sie die [Ausgabedatei im DOCX-Format](Book1.docx), die vom Code erzeugt wird.

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

## **Excel-Arbeitsmappe in PPTX umwandeln**

Das Aspose.Cells API unterstützt die Konvertierung von Tabellen in das PPTX-Format. Um die Arbeitsmappe in PPTX zu exportieren, übergeben Sie [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Sie können auch die [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach PPTX festzulegen.

Das folgende Codebeispiel zeigt, wie die aktive Tabelle mit [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Enumeration Mitglied in PPTX exportiert wird. Bitte sehen Sie sich die [Ausgabedatei PPTX](Book1.pptx) an, die vom Code generiert wurde, zur Referenz.

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

## **Excel-Arbeitsmappe in EPUB konvertieren**

Die Aspose.Cells API unterstützt die Konvertierung von Tabellen in das EPUB-Format. Um die Arbeitsmappe in EPUB zu exportieren, übergeben Sie [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweites Parameter an die [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export der Tabelle in EPUB festzulegen.

Das folgende Codebeispiel zeigt, wie die aktive Tabelle mit [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Enumeration Mitglied in EPUB exportiert wird.

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

## **Excel-Arbeitsmappe nach AZW3 konvertieren**

Die Aspose.Cells API unterstützt die Konvertierung von Tabellen in das AZW3-Format. Um die Arbeitsmappe in AZW3 zu exportieren, übergeben Sie [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweites Parameter an die [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export der Tabelle in AZW3 festzulegen.

Das folgende Codebeispiel zeigt, wie die aktive Tabelle mit [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) Enumeration Mitglied in AZW3 exportiert wird.

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

## **Erweiterte Themen**
- [Konvertieren der Überarbeitung von XLSB zu XLSM](/cells/de/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/de/cpp/convert-excel-to-html/)
- [Bild](/cells/de/cpp/convert-excel-to-image/)
- [Json](/cells/de/cpp/convert-workbook-to-json/)
- [Excel-Arbeitsmappe in Ods, Sxc und Fods (OpenOffice / LibreOffice calc) konvertieren.](/cells/de/cpp/convert-excel-to-ods/)
- [Pdf](/cells/de/cpp/convert-excel-workbook-to-pdf/)
- [Excel in CSV, TSV und Txt konvertieren](/cells/de/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Fortschritt der Dokumentkonvertierung nachverfolgen](/cells/de/cpp/track-document-conversion-progress/)
- [CSV, TSV und TXT in Excel konvertieren](/cells/de/cpp/convert-csv-tsv-and-txt-to-excel/)
