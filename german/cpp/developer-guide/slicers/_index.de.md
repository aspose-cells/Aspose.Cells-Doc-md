---
title: Slicer mit C++ einfügen
linktitle: Slicer
type: docs
weight: 170
url: /de/cpp/create-slicer/
description: Slicer in Excel Dateien mit Aspose.Cells und C++ verwalten
---

## **Mögliche Verwendungsszenarien**

Ein Slicer dient zur schnellen Filterung von Daten. Er kann verwendet werden, um Daten in einer Tabelle oder Pivot-Tabelle zu filtern. Microsoft Excel ermöglicht das Erstellen eines Slicers, indem eine Tabelle oder Pivot-Tabelle ausgewählt und dann auf *Einfügen > Slicer* geklickt wird. Aspose.Cells erlaubt auch die Erstellung eines Slicers mit der [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/) Methode.

## **Erstellen Sie ein Schneidwerkzeug zu einem Pivot-Table**

Bitte beachten Sie den folgenden Beispielcode. Es lädt die [Beispieldatei Excel](67338470.xlsx), die das Pivot-Table enthält. Anschließend wird der Slicer basierend auf dem ersten Basis-Pivot-Feld erstellt. Schließlich speichert es die Arbeitsmappe im Format [output XLSX](67338471.xlsx) und [output XLSB](67338472.xlsb). Der folgende Screenshot zeigt den von Aspose.Cells in der Ausgabe-Excel-Datei erstellten Slicer.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erstellen Sie ein Schneidwerkzeug zu Excel-Tabelle**

Bitte beachten Sie den folgenden Beispielcode. Es lädt die [Beispieldatei Excel](sampleCreateSlicerToExcelTable.xlsx), die eine Tabelle enthält. Anschließend wird der Slicer basierend auf der ersten Spalte erstellt. Schließlich speichert es die Arbeitsmappe im Format [output XLSX](outputCreateSlicerToExcelTable.xlsx).

### **Beispielcode**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortgeschrittene Themen**
- [Slicer-Eigenschaften ändern](/cells/de/cpp/change-slicer-properties/)
- [Slicer zeichnen beim Rendern von Excel zu PDF](/cells/de/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatierung Schneidwerkzeug](/cells/de/cpp/formatting-slicer/)
- [Slicer entfernen](/cells/de/cpp/removing-slicer/)
- [Slicer rendern](/cells/de/cpp/rendering-slicer/)
- [Slicer aktualisieren](/cells/de/cpp/updating-slicer/)
