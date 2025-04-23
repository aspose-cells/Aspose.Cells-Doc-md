---
title: Hesaplanan Öğeleri olan Pivot Tabloyu C++ ile Yenile ve Hesapla
linktitle: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 40
url: /tr/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aspose.Cells kullanarak hesaplanan öğeleri ile pivot tabloyu yenile ve hesapla.
---

{{% alert color="primary" %}}

Aspose.Cells artık hesaplanmış öğeleri içeren pivot tablosunu yenileme ve hesaplama işlemini destekler. Bunun için bu işlemi gerçekleştirmek için değişkenleri [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) ve [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) kullanmalısınız.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

 Aşağıdaki örnek kod, üç hesaplanan öğe içeren pivot tabloyu ("add", "div", "div2") içeren [kaynak excel dosyasını](5115238.xlsx) yükler. İlk olarak D2 hücresinin değerini 20 yapar, ardından Aspose.Cells API'leri kullanarak pivot tabloyu yeniler ve hesaplar ve çalışma kitabını PDF formatında kaydeder. [Çıktı PDF'sinde](5115229.pdf) Aspose.Cells'in pivot tabloyu başarıyla yenilediği ve hesapladığı görülür. Bunu, Microsoft Excel’de D2 hücresine manuel olarak 20 değerini koyup Alt+F5 kısayolu veya Pivot Tabloyu Yenile düğmesine tıklayarak doğrulayabilirsiniz.

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
