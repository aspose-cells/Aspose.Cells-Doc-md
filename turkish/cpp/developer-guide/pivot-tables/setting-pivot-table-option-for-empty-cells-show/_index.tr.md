---
title: Pivot Tablo Seçeneğini Ayarlama  Boş Hücreleri Göster with C++
linktitle: Boş Hücreler İçin pivot tablo seçeneğini ayarlayın
type: docs
weight: 40
url: /tr/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Aspose.Cells kullanarak pivot tablolarında "Boş hücreleri göster" seçeneğini nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak farklı pivot tablo seçeneklerini ayarlayabilirsiniz. Bu seçeneklerden biri de "Boş hücreler için göster" seçeneğidir. Bu seçeneği ayarlayarak, pivot tablosundaki tüm boş hücreler belirtilen bir dize olarak gösterilir.

{{% /alert %}}

## **Boş Hücreler İçin Göster Pivot Tablo Seçeneği Ayarlama**

Bu seçeneği bulup Microsoft Excel'de ayarlamak için:

1. Bir pivot tablo seçin ve sağ tıklayın.
1. **PivotTablo Seçenekleri**'ni seçin.
1. **Düzen ve Biçim** sekmesini seçin.
1. **Boş hücreler için göster** seçeneğini seçin ve bir dize belirtin.

## **Aspose.Cells Kullanarak Pivot Tablo Seçeneği Ayarlama**

Aspose.Cells, "Boş hücreler için göster" pivot tablo seçeneğini ayarlamak için [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) ve [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) özelliklerini sağlar.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## İlgili Makaleler

- [Pivot Tablosu Biçimlendirme](/cells/tr/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
