---
title: Anger den absoluta positionen för pivotobjekt med C++
linktitle: Specificera den absoluta positionen för pivotposten
type: docs
weight: 50
url: /sv/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Lär dig hur du anger den absoluta positionen för pivotobjekt i C++ med Aspose.Cells.
---

{{% alert color="primary" %}}

Ibland måste användare ange den absoluta positionen för pivotobjekt. Aspose.Cells API har exponerat några nya egenskaper och en metod för att uppnå detta krav.

- Lagt till egenskapen [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) som kan användas för att ange positionens index för alla PivotItems oavsett föräldernod. Lagt till egenskapen [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) som kan användas för att ange positionens index för PivotItems under samma föräldernod.
- Lagt till [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) metod för att flytta objektet upp eller ned baserat på räknevärdet, där räknevärdet är antalet positioner att flytta PivotItem upp eller ned. Om räknevärdet är mindre än noll flyttas objektet upp, medan om räknevärdet är större än noll flyttas PivotItem ned. den booleska typen `isSameParent`-parametern specificerar om flyttningen ska göras inom samma föräldraenhet eller inte.
- Äldre `PivotItem.Move(int count)`-metoden; därför rekommenderas det att använda den nyare metoden [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) istället.

{{% /alert %}}

Följande exempel på kod skapar en pivottabell och specificerar sedan pivotobjektets positioner inom samma föräldranod. Du kan ladda ner [käll-Excel](5112632.xlsx) och [utdata-Excel](5112619.xlsx) filer för referens. Om du öppnar utdatafilen ser du att pivotobjektet "4H12" är på position 0 inom föräldern "K11" och "DIF400" är på position 3. På samma sätt är CA32 på position 1 och AAA3 på position 2.

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

Observera att det är nödvändigt att kalla `PivotTable.RefreshData` och `PivotTable.CalculateData`-metoderna innan du använder [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) egenskaper och [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) metod.

{{% /alert %}}
