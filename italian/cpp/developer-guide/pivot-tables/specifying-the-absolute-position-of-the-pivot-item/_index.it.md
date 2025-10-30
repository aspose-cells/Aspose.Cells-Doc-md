---
title: Specificare la posizione assoluta dell elemento Pivot con C++
linktitle: Specificare la posizione assoluta dell elemento pivot
type: docs
weight: 50
url: /it/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Impara come specificare la posizione assoluta degli elementi pivot in C++ usando Aspose.Cells.
---

{{% alert color="primary" %}}

A volte, gli utenti hanno bisogno di specificare la posizione assoluta degli elementi pivot. L'API Aspose.Cells ha introdotto alcune nuove proprietà e un metodo per raggiungere questo obiettivo.

- Aggiunta la proprietà [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) che può essere utilizzata per specificare l'indice di posizione in tutti i PivotItems indipendentemente dal nodo genitore. Aggiunta la proprietà [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) che può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo genitore.
- Aggiunto il metodo [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) per spostare l'elemento su o giù in base al valore del conteggio, dove il conteggio è il numero di posizioni da spostare l'elemento Pivot su o giù. Se il valore del conteggio è inferiore a zero, l'elemento verrà spostato verso l'alto, mentre se il valore è maggiore di zero, l'elemento Pivot si sposterà verso il basso. Il parametro di tipo Boolean `isSameParent` specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo genitore o meno.
- Come risposta, il metodo `PivotItem.Move(int count)` è stato deprecato; si consiglia di utilizzare invece il nuovo metodo [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}

Il seguente esempio di codice crea una tabella pivot e poi specifica le posizioni degli elementi Pivot nello stesso nodo genitore. Puoi scaricare il file Excel [sorgente](5112632.xlsx) e [output](5112619.xlsx) per tuo riferimento. Se apri il file Excel di output, vedrai che l'elemento Pivot "4H12" si trova alla posizione 0 nel genitore "K11" e "DIF400" è alla posizione 3. Similarmente, CA32 si trova alla posizione 1 e AAA3 alla posizione 2.

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

Nota: è necessario chiamare i metodi `PivotTable.RefreshData` e `PivotTable.CalculateData` prima di utilizzare le proprietà [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) e il metodo [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
