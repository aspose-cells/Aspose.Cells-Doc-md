---
title: C++ ile Pivot Tablo Düzenini Değiştirme
linktitle: Pivot Tablosu Yerleşimini Değiştirme
type: docs
weight: 10
url: /tr/cpp/changing-the-layout-of-pivot-table/
description: Aspose.Cells for C++ kullanarak Pivot Tablo nun düzenini Kapsüllü, Taslak ve Tablo biçimlerinde değiştirmeyi öğrenin.
---

{{% alert color="primary" %}}

Microsoft Excel, *PivotTable Araçları > Tasarım > Rapor Düzeni* menü komutlarını kullanarak Pivot Tablo düzenini değiştirmeye izin verir. Bu üç biçimde düzeni değiştirebilirsiniz:

- Kompakt Formda Göster
- Açıklamalı Formda Göster
- Tablo Formunda Göster

Aspose.Cells ayrıca [**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/), [**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/) ve [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) metodlarını sağlar, bu metodlar Pivot Tablo'nun düzenini bu üç biçimde değiştirmek için kullanılır.

{{% /alert %}}

Aşağıdaki örnek kod önce Pivot Tablo'yu **Kapsüllü Form**da gösterir, sonra **Taslak Form**da ve son olarak **Tablo Form**da gösterir.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_sample.xlsx";

    // Create workbook object from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 1 - Show the pivot table in compact form
    pivotTable.ShowInCompactForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"CompactForm_out.xlsx");

    // 2 - Show the pivot table in outline form
    pivotTable.ShowInOutlineForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"OutlineForm_out.xlsx");

    // 3 - Show the pivot table in tabular form
    pivotTable.ShowInTabularForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"TabularForm_out.xlsx");

    std::cout << "Pivot table forms saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
