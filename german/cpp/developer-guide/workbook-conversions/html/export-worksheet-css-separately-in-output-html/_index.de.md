---
title: Exportiere Tabellen CSS separat im Ausgab HTML mit C++
linktitle: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren
type: docs
weight: 80
url: /de/cpp/export-worksheet-css-separately-in-output/
description: Erfahren Sie, wie Sie Tabellen CSS beim Konvertieren von Excel Dateien nach HTML separat exportieren, indem Sie Aspose.Cells for C++ verwenden.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die Funktion, Tabellen-CSS beim Konvertieren Ihrer Excel-Datei nach HTML separat zu exportieren. Verwenden Sie dazu die [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/)-Eigenschaft und setzen Sie sie beim Speichern der Excel-Datei im HTML-Format auf **true**.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt einen Text in Zelle **B5** in **Rot** hinzu und speichert sie dann im HTML-Format unter Verwendung der [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/)-Eigenschaft. Bitte sehen Sie sich das [Ausgabe-HTML](60489766.zip) an, das vom Code generiert wurde. Sie werden **stylesheet.css** innerhalb davon als Ergebnis des Beispielcodes finden.

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Einzelnes Blatt-Workbook nach HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern mit Aspose.Cells nach HTML konvertiert wird, erstellt sie eine HTML-Datei sowie einen Ordner mit CSS und mehreren HTML-Dateien. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Tabs sichtbar. Das gleiche Verhalten ist für eine Arbeitsmappe mit nur einem Arbeitsblatt erforderlich. Früher wurde für einzelne Blätter kein separater Ordner erstellt; es wurde nur eine HTML-Datei erzeugt. Diese HTML-Datei zeigt beim Öffnen im Browser keinen Tab. Microsoft Excel erstellt ebenfalls einen passenden Ordner und HTML für ein einzelnes Blatt, daher ist das gleiche Verhalten über Aspose.Cells APIs implementiert. Die Beispieldatei kann für die Verwendung im untenstehenden Beispielcode heruntergeladen werden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

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
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
