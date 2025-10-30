---
title: Pivot Verbindung mit C++ hinzufügen
linktitle: Pivot Verbindung hinzufügen
type: docs
weight: 30
url: /de/cpp/add-pivot-connection/
description: Erfahren Sie, wie Sie eine Pivot Verbindung mit der Aspose.Cells Bibliothek in C++ hinzufügen.
keywords: Pivot Verbindung hinzufügen ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Slicer und Pivot-Tabelle in Excel verknüpfen möchten, müssen Sie mit einem Rechtsklick auf den Slicer die Option "Berichtsverbindungen..." auswählen. In der Optionsliste können Sie die Kontrollkästchen verwenden. Ebenso, wenn Sie Slicer und Pivot-Tabelle programmgesteuert mit der Aspose.Cells-API verknüpfen möchten, verwenden Sie bitte die [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/)-Methode. Damit können Sie Slicer und Pivot-Tabelle verknüpfen.

## **Slicer und PivotTable verknüpfen**

Der folgende Beispielcode lädt die [Beispieldatei](add-pivot-connection.xlsx), die bereits einen Slicer enthält. Er greift auf den Slicer zu und verknüpft dann den Slicer und die Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](add-pivot-connection-out.xlsx). 

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
