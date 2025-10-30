---
title: Text in Spalten mit Aspose.Cells für C++ konvertieren
linktitle: Text in Spalten konvertieren
type: docs
weight: 30
url: /de/cpp/convert-text-to-columns-using-aspose-cells/
description: Lernen Sie, wie Sie Text in Excel Dateien mit Aspose.Cells for C++ in Spalten umwandeln.
---

## **Mögliche Verwendungsszenarien**

Sie können Ihren Text in Spalten mit Microsoft Excel umwandeln. Diese Funktion ist unter dem Register *Daten* in den *Datentools* verfügbar. Um den Inhalt einer Spalte in mehrere Spalten aufzuteilen, sollte die Daten einen spezifischen Trennzeichen wie ein Komma (oder ein anderes Zeichen) enthalten, anhand dessen Microsoft Excel den Inhalt einer Zelle in mehrere Zellen aufteilt. Aspose.Cells bietet diese Funktion auch über die [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)-Methode.

## **Text in Spalten konvertieren mit Aspose.Cells**

Der folgende Beispielcode erklärt die Verwendung der [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)-Methode. Der Code fügt zuerst einige Personennamen in Spalte A des ersten Arbeitsblatts ein. Vorname und Nachname sind durch ein Leerzeichen getrennt. Dann wendet er die [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)-Methode auf Spalte A an und speichert die Datei als Ergebnis-Excel-Datei. Wenn Sie die [Ausgabedatei](25395213.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A und die Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Beispielcode**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
