---
title: Arbeitsblatt in Bild umwandeln unter Verwendung von ImageOrPrint Optionen mit C++
linktitle: Arbeitsblatt in Bild umwandeln
type: docs
weight: 90
url: /de/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Lernen Sie, wie Sie ein Arbeitsblatt in eine Bilddatei umwandeln und verschiedene Bild sowie Druckoptionen mit Aspose.Cells und C++ anwenden.
---

{{% alert color="primary" %}}

Dieses Dokument ist dafür ausgelegt, ein detailliertes Verständnis dafür zu vermitteln, wie man ein Arbeitsblatt in eine Bilddatei umwandelt und verschiedene Bild- und Druckoptionen für das Bild anwendet, wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

## **Arbeitsblätter als Bilder speichern - Unterschiedliche Ansätze**

Manchmal müssen Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Möglicherweise möchten Sie die Arbeitsblattbilder in Ihren Anwendungen oder Webseiten anzeigen, sie in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Einfach ausgedrückt, möchten Sie ein Arbeitsblatt als Bild gerendert haben, um es woanders verwenden zu können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Zusätzlich unterstützt Aspose.Cells die Einstellung verschiedener Optionen wie Bildformat, Auflösung (vertikal und horizontal), Bildqualität und weitere Bild- und Druckoptionen.

Sie könnten Office-Automatisierung in Betracht ziehen, aber diese hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, wie Sicherheit, Stabilität, Skalierbarkeit, Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, wobei der wichtigste ist, dass Microsoft selbst dringend von Office-Automatisierung bei Softwarelösungen abrät.

Dieser Artikel zeigt, wie man in Visual Studio eine Konsolenanwendung erstellt, die Konvertierung eines Arbeitsblatts in ein Bild durchführt. Dies erfolgt mit nur wenigen und einfachsten Zeilen Code unter Verwendung der Aspose.Cells API, unter Verwendung verschiedener Bild- und Druckoptionen.

Sie müssen den Namespace [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) in Ihrem Programm/Ihrem Projekt einbeziehen. Er verfügt über mehrere wertvolle Klassen, zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) usw.

Die Klasse [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) repräsentiert ein Arbeitsblatt, für das Bilder gerendert werden sollen. Sie hat eine Überladung der Methode [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), die ein Arbeitsblatt direkt in eine Bilddatei oder -dateien mit Ihren gewünschten Attributen oder Optionen umwandeln kann. Sie kann ein Bitmap-Objekt zurückgeben, und Sie können eine Bilddatei auf die Festplatte oder in einen Stream speichern. Mehrere Bildformate werden unterstützt, wie BMP, PNG, GIF, JPEG, TIFF, EMF und weitere.

## **Verwendung von Aspose.Cells zur Umwandlung eines Arbeitsblatts in ein Bild mit ImageOrPrint-Optionen**

### **Erstellung einer Vorlage-Arbeitsmappe in Microsoft Excel**

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt. Nun werde ich das Arbeitsblatt „Sheet1“ der Vorlage in eine Bilddatei „SheetImage.tiff“ umwandeln und dabei verschiedene Bildoptionen wie horizontale und vertikale Auflösung, Tiff-Komprimierung usw. anwenden.

### **Aspose.Cells herunterladen und installieren**

Zunächst müssen Sie [herunterladen](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. Installieren Sie es auf Ihrem Entwicklungscomputer. Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat keine Zeitbegrenzung und füllt nur Wasserzeichen in die erstellten Dokumente ein.

### **Ein Projekt erstellen**

Starten Sie Visual Studio und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C++-Konsolenanwendung.

### **Referenzen hinzufügen**

Dieses Projekt wird Aspose.Cells verwenden. Daher müssen Sie eine Referenz auf die Aspose.Cells-Komponente in Ihr Projekt hinzufügen. Zum Beispiel fügen Sie eine Referenz auf `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib` hinzu.

### **Konvertieren Sie ein Arbeitsblatt in eine Bilddatei**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konversionsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code wandelt die ersten beiden Arbeitsblätter in einem Arbeitsbuch in JPG-Bilder um.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Bildkonvertierung mit WorkbookRender**

Ein TIFF-Bild kann mehr als einen Frame enthalten. Sie können das gesamte Arbeitsbuch in ein einziges TIFF-Bild mit mehreren Frames oder Seiten speichern:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
