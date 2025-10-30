---
title: Pivot Tablo daki DataField in Veri Görüntüleme Formatlarıyla çalışma C++ ile
linktitle: Pivot Tablo daki DataField in Veri Görüntüleme Formatlarıyla çalışma
type: docs
weight: 140
url: /tr/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Aspose.Cells for C++ kullanarak Pivot Tablo da DataField in veri görüntüleme formatlarıyla nasıl çalışılacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, DataField'ın tüm veri görüntüleme formatlarını destekler.

{{% /alert %}}

## **"Smallest to Largest Sıralama" ve "Largest to Smallest Sıralama" Görüntüleme Format Seçeneği**

Aspose.Cells, pivot alanları için görüntüleme formatı ayarını yapma imkanı sağlar. Bunun için API, [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) özelliğini sunar. En büyükten en küçüğe sıralamak için [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) özelliği [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/) değerine ayarlanabilir. Aşağıdaki kod parçası, görüntüleme formatı ayarlarını gösterir.

Örnek kaynak ve çıktı dosyalarını buradan indirebilir ve örnek kodu test etmek için kullanabilirsiniz:

[Kaynak Excel Dosyası](101089332.xlsx)

[Çıktı Excel Dosyası](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
