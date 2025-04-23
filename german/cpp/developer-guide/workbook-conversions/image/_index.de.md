---
title: Excel in Bild mit C++ konvertieren
linktitle: Excel in Bild konvertieren
type: docs
weight: 300
url: /de/cpp/convert-excel-to-image/
description: Erfahren Sie, wie Sie Excel Arbeitsblätter mit Aspose.Cells for C++ in Bilder, einschließlich TIFF und SVG, umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. Dieser Artikel erklärt, wie man ein Arbeitsblatt in verschiedene Formate konvertiert.

{{% /alert %}}

## Arbeitsmappe in TIFF konvertieren

Eine Excel-Datei kann mehrere Blätter und Seiten enthalten. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) ermöglicht die Konvertierung von Excel in TIFF mit mehreren Seiten. Außerdem können Sie mehrere Optionen für TIFF steuern, wie [Kompression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Auflösung ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Der folgende Code zeigt, wie Excel in TIFF mit mehreren Seiten konvertiert wird. Die [Quell-Excel-Datei](workbook-to-tiff-with-mulitiple-pages.xlsx) und das generierte TIFF-Bild (workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz angehängt.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Arbeitsblatt in Bild konvertieren**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Möglicherweise müssen Sie beispielsweise ein Bild eines Arbeitsblatts in einer Anwendung oder auf einer Webseite verwenden. Sie möchten möglicherweise ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumententyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion zu nutzen, müssen Sie den [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)-Namensraum in Ihr Programm oder Projekt importieren. Es verfügt über mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) und andere.

Die [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)-Klasse repräsentiert ein Arbeitsblatt, das als Bild gerendert werden soll. Sie hat eine überladene Methode, [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), die ein Arbeitsblatt mit verschiedenen Attributen oder Optionen in Bilddateien umwandeln kann. Es gibt ein `System.Drawing.Bitmap`-Objekt zurück und Sie können eine Bilddatei auf Festplatte oder Stream speichern. Verschiedene Bildformate werden unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.

```cpp
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

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Zum jetzigen Zeitpunkt unterstützt die API zur Konvertierung von Arbeitsblättern in Bilder keine 3D-Bubble-Diagramme.

{{% /alert %}}

## **Arbeitsblatt in SVG konvertieren**

SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.

Aspose.Cells for C++ konnte seit Version 7.1.0 Arbeitsblätter in SVG-Bilder umwandeln. Das folgende Codebeispiel zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Konvertieren Sie ein Excel-Diagramm in ein Bild](/cells/de/cpp/convert-an-excel-chart-to-image/)
- [Konvertieren eines Diagramms in ein Bild im SVG-Format](/cells/de/cpp/converting-chart-to-image-in-svg-format/)
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Konvertierungsvorgang von Excel nach TIFF verfolgen](/cells/de/cpp/track-conversion-progress-of-excel-to-tiff/)
