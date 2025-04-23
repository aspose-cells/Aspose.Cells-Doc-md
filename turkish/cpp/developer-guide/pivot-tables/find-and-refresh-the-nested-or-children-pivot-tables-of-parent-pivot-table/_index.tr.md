---
title: Parent Pivot Tablo nun iç içe veya çocuğu olan pivot tablolarını bulma ve yenileme (C++)
linktitle: İç içe veya çocuk pivot tablolarını bul ve yenile
type: docs
weight: 60
url: /tr/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Bir ebeveyn pivot tablosunun iç içe veya çocuk pivot tablolarını nasıl bulup yenileyeceğinizi Aspose.Cells for C++ kullanarak öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, bir pivot tablosu diğer bir pivot tablosunu veri kaynağı olarak kullandığı için buna çocuk pivot tablosu veya yerleşik pivot tablosu denir. [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) yöntemi kullanarak bir ana pivot tablosunun çocuk pivot tablolarını bulabilirsiniz.

## **Ana Pivot Tablosunun İçindeki Yerleşik veya Çocuk Pivot Tablolarını Bul ve Yenile**

Aşağıdaki örnek kod, üç pivot tablosunu içeren [örnek Excel dosyasını](61767747.xlsx) yükler. Alt iki pivot tablosu yukarıdaki pivot tablosunun alt pivot tablolarıdır ve bu ekran görüntüsünde gösterildiği gibi. Kod, [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) yöntemini kullanarak alt pivot tablosunu bulur ve ardından birer birer yeniler.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access third pivot table
    PivotTable ptParent = ws.GetPivotTables().Get(2);

    // Access the children of the parent pivot table
    Vector<PivotTable> ptChildren = ptParent.GetChildren();

    // Refresh all the children pivot table
    int count = ptChildren.GetLength();
    for (int idx = 0; idx < count; idx++)
    {
        // Access the child pivot table
        PivotTable ptChild = ptChildren[idx];

        // Refresh the child pivot table
        ptChild.RefreshData();
        ptChild.CalculateData();
    }

    std::cout << "Children pivot tables refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
