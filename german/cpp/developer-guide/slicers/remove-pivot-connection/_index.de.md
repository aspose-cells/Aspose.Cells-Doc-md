---
title: Pivot Verbindung mit C++ entfernen
linktitle: Pivot Verbindung entfernen
type: docs
weight: 30
url: /de/cpp/remove-pivot-connection/
description: Erfahren Sie, wie Sie die Pivot Verbindung mit der Aspose.Cells Bibliothek in C++ entfernen.
keywords: Entfernen Sie die Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den Slicer und die Pivot-Tabelle in Excel trennen möchten, müssen Sie mit der rechten Maustaste auf den Slicer klicken und das Element "Berichtsverbindungen..." auswählen. In der Optionsliste können Sie das Kontrollkästchen bedienen. Ebenso, wenn Sie den Slicer und die Pivot-Tabelle mithilfe der Aspose.Cells-API programmgesteuert trennen möchten, verwenden Sie bitte die Methode [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/). Es wird den Slicer und die Pivot-Tabelle trennen.

## **Slicer und Pivot-Tabelle dissoziieren**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](remove-pivot-connection.xlsx), die einen vorhandenen Slicer enthält. Es greift auf die Slicer zu und entkoppelt dann den Slicer und die Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](remove-pivot-connection-out.xlsx). 

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
