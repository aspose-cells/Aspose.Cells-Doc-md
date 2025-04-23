---
title: Aktualisieren und Berechnen der Pivot Tabelle mit berechneten Elementen mit C++
linktitle: Pivot Tabelle aktualisieren und Berechnen von Pivot Tabellen mit berechneten Elementen
type: docs
weight: 40
url: /de/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aktualisieren und Berechnen der Pivot Tabelle mit berechneten Elementen mit Aspose.Cells und C++.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt jetzt das Aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen. Verwenden Sie bitte [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) und [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) wie gewohnt, um diese Funktion auszuführen.

{{% /alert %}}

## **Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen**

Das folgende Beispiel lädt die [Quell-Excel-Datei](5115238.xlsx), die eine Pivot-Tabelle mit drei berechneten Elementen wie "add", "div", "div2" enthält. Zuerst ändern wir den Wert der Zelle D2 auf 20 und aktualisieren sowie berechnen anschließend die Pivot-Tabelle mit den APIs von Aspose.Cells und speichern die Arbeitsmappe im PDF-Format. Die Ergebnisse im [Ausgabe-PDF](5115229.pdf) zeigen, dass Aspose.Cells die Pivot-Tabelle mit den berechneten Elementen erfolgreich aktualisiert und berechnet hat. Sie können dies überprüfen, indem Sie in Microsoft Excel manuell den Wert 20 in die Zelle D2 eingeben und dann die Pivot-Tabelle mit der Tastenkombination Alt+F5 aktualisieren oder die Schaltfläche "PivotTable aktualisieren" klicken.

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

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
