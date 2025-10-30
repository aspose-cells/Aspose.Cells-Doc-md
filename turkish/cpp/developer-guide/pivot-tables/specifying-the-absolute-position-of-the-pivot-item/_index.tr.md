---
title: C++ ile Pivot Öğesi nin Mutlak Konumunu Belirtme
linktitle: Pivot Öğesinin Mutlak Konumunu Belirtme
type: docs
weight: 50
url: /tr/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Aspose.Cells kullanarak C++ ta pivot öğelerinin mutlak konumunu nasıl belirteceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazen kullanıcıların pivot öğelerinin mutlak konumunu belirtmesi gerekir. Aspose.Cells API, bu ihtiyacı karşılamak için birkaç yeni özellik ve yöntem ortaya çıkardı.

- Tüm ebeveyn düğümün bağımsızında PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) özelliği eklendi. - Aynı ebeveyn düğümdeki PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) özelliği eklendi.
- PivotItem'i yukarı veya aşağı hareket ettirmek için sayım değerine göre `[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)` yöntemi eklendi. Burada sayım, PivotItem'i yukarı veya aşağı hareket ettirmek için kaç pozisyon hareket edileceğini belirtir. Eğer sayım değeri sıfırdan küçükse, öğe yukarı taşınır; eğer sıfırdan büyükse, aşağı taşınır. Boolean tip `isSameParent` parametresi, hareket işleminin aynı ebeveyn düğümde olup olmayacağını belirtir.
- `PivotItem.Move(int count)` yöntemi kullanımdan kaldırılmıştır; bu nedenle, önerilen yeni yöntem [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) kullanılmasıdır.

{{% /alert %}}

Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından Pivot Öğeleri'nin konumlarını aynı ebeveyn düğümde belirtir. Referansınız için [kaynak Excel](5112632.xlsx) ve [çıktı Excel](5112619.xlsx) dosyalarını indirebilirsiniz. Çıktı Excel dosyasını açarsanız, Pivot Öğesi "4H12"'nin ebeveyn "K11" içinde 0. pozisyonda olduğunu ve "DIF400"'ün ise 3. pozisyonda olduğunu göreceksiniz. Benzer şekilde, CA32 1. pozisyonda ve AAA3 2. pozisyondadır.

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

Lütfen, `[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/)`, `[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)` özelliklerini ve `[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)` yöntemini kullanmadan önce `PivotTable.RefreshData` ve `PivotTable.CalculateData` yöntemlerini çağırmanız gerektiğini unutmayın.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
