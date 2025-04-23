---
title: Absolute Position des Pivot Elements mit C++ angeben
linktitle: Angabe der absoluten Position des Pivot Elements
type: docs
weight: 50
url: /de/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Erfahren Sie, wie Sie die absolute Position von Pivot Elementen in C++ mit Aspose.Cells festlegen.
---

{{% alert color="primary" %}}

Manchmal müssen Benutzer die absolute Position der Pivot-Elemente angeben. Die Aspose.Cells API hat einige neue Eigenschaften und eine Methode bereitgestellt, um diese Anforderung zu erfüllen.

- Hinzugefügte [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) Eigenschaft, die verwendet werden kann, um den Position-Index in allen Pivot-Elementen unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügte [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) Eigenschaft, die verwendet werden kann, um den Position-Index in den Pivot-Elementen unter dem gleichen übergeordneten Knoten anzugeben.
- Die Methode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) wurde hinzugefügt, um das Element basierend auf dem Zählwert nach oben oder unten zu verschieben, wobei der Zählwert die Anzahl der Positionen ist, um die das Pivot-Element nach oben oder unten verschoben werden soll. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, während bei einem Zählwert größer als null das Pivot-Element nach unten verschoben wird. Der Boolesche Parameter `isSameParent` gibt an, ob die Verschiebung im selben Elternknoten erfolgen soll.
- Der veraltete `PivotItem.Move(int count)`-Methode; es wird empfohlen, stattdessen die neu hinzugefügte Methode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) zu verwenden.

{{% /alert %}}

Der folgende Beispielcode erstellt eine Pivot-Tabelle und gibt dann die Positionen der Pivot-Elemente im selben Elternknoten an. Sie können die [Quelldatei Excel](5112632.xlsx) und die [Ausgabedatei Excel](5112619.xlsx) herunterladen. Wenn Sie die Ausgabedatei öffnen, sehen Sie, dass das Pivot-Element "4H12" an Position 0 im Elternknoten "K11" ist und "DIF400" an Position 3. Ebenso befindet sich CA32 an Position 1 und AAA3 an Position 2.

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

    // Create workbook
    Workbook wb(srcDir + u"source.xlsx");

    // Add new worksheet for pivot table
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet wsPivot = worksheets.Add(u"pvtNew Hardware");
    Worksheet wsData = worksheets.Get(u"New Hardware - Yearly");

    // Get the pivot tables collection for the pivot sheet
    PivotTableCollection pivotTables = wsPivot.GetPivotTables();

    // Add PivotTable to the worksheet
    int index = pivotTables.Add(u"='New Hardware - Yearly'!A1:D621", u"A3", u"HWCounts_PivotTable");

    // Get the PivotTable object
    PivotTable pvtTable = pivotTables.Get(index);

    // Add vendor row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Vendor");

    // Add item row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Item");

    // Add data field
    pvtTable.AddFieldToArea(PivotFieldType::Data, u"2014");

    // Turn off the subtotals for the vendor row field
    PivotField pivotField = pvtTable.GetRowFields().Get(u"Vendor");
    pivotField.SetSubtotals(PivotFieldSubtotalType::None, true);

    // Turn off grand total
    pvtTable.SetShowColumnGrandTotals(false);

    // Refresh and calculate data before modifying pivot items
    pvtTable.RefreshData();
    pvtTable.CalculateData();

    // Set positions for specific pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"4H12").SetPositionInSameParentNode(0);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"DIF400").SetPositionInSameParentNode(3);

    // Recalculate data after modifying pivot items
    pvtTable.CalculateData();

    // Set positions for additional pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"CA32").SetPositionInSameParentNode(1);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"AAA3").SetPositionInSameParentNode(2);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Bitte beachten Sie, dass es erforderlich ist, die Methoden `PivotTable.RefreshData` und `PivotTable.CalculateData` aufzurufen, bevor Sie die Eigenschaften [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) und die Methode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) verwenden.

{{% /alert %}}
