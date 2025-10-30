---
title: Çalışmaktan Bir Sayfadan Pivot Tablo Silme (C++)
linktitle: Pivot Tabloyu Sil
type: docs
weight: 60
url: /tr/cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells kullanarak Excel Sayfalarından PivotTabloyu kaldırmak için C++ kodu.
keywords: c++ ile çalışma sayfasından pivot tabloyu kaldırma, c++ ile Excel den pivot tabloyu kaldırma, c++ kullanarak pivot tabloyu nasıl silerim, c++ ile pivot tabloyu sil, c++ ile excel den pivot tabloyu sil, c++ pivot tablo sil, pivot tabloyu kaldır, pivot tabloyu sil, pivot tabloyu nasıl silerim
---

{{% alert color="primary" %}}

Aspose.Cells, bir Çalışma Sayfasından Pivot Tablosunu silme veya kaldırma özelliği sağlar. Pivot tablosu nesnesini veya pivot tablosu pozisyonunu kullanarak pivot tablosunu silebilirsiniz. Pivot tablosunu nesnesini kullanarak pivot tablosunu silmek için lütfen [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) yöntemini ve pivot tablosu koleksiyonundaki pozisyonunu kullanarak pivot tablosunu silme yöntemi [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, çalışma sayfasındaki iki pivot tabloyu siler. İlk olarak [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) yöntemi kullanılarak pivot tablo kaldırılır, ardından [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) yöntemi kullanılır.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
