---
title: Birleştirilmiş hücreler için Satır Yüksekliğini Otomatik Ayarla, C++ ile
linktitle: Bir çalışma kitabı nesnesi oluşturur ve birden fazla çalışma sayfası ekler. Her çalışma sayfasında farklı yöntemler kullanarak otomatik uyarlama işlemlerini gerçekleştirir. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra elde edilen sonuçları gösterir.
type: docs
weight: 120
url: /tr/cpp/autofit-rows-for-merged-cells/
description: Excel de birleştirilmiş hücreler için satırların otomatik sığmasını nasıl sağlayacağınızı öğrenin Aspose.Cells for C++ kullanarak.
---

{{% alert color="primary" %}}

Microsoft Excel, bir hücrenin içeriğine göre otomatik olarak hücre yüksekliğini ayarlamak için bir özellik sağlar. Bu özellik otomatik satırı uyarlama adını taşır. Microsoft Excel, birleştirilmiş hücrelerde otomatik sığdırma işlemini varsayılan olarak ayarlamaz. Bazen özellik, birleştirilmiş hücreler üzerinde otomatik satır uyarlama işlemi gerçekten uygulamak isteyen bir kullanıcı için önemli hale gelir.

{{% /alert %}}

## **Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama Yöntemi**
Aspose.Cells, [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/) API'si aracılığıyla bu özelliği destekler. Bu API'yi kullanarak, birleştirilmiş hücreler de dahil olmak üzere bir çalışma sayfasındaki satırları otomatik olarak uyarlama mümkün olmaktadır. İşte birleştirilmiş hücreleri otomatik olarak uyarlamanın tüm olası türlerinin bir listesi:

- Hiçbiri
- İlk Satır
- Son Satır
- HerSatir

## **Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama**

Aşağıdaki kodu inceleyin, bir çalışma kitabı nesnesi oluşturur ve birden çok çalışma sayfası ekler. Her çalışma sayfasında otomatik uyma işlemi için farklı metodlar kullanın. Ekran görüntüsü, örnek kodun yürütülmesinden sonra elde edilen sonuçları gösterir.

<br>
<img src="result.png" width=80% />

## **C++ Örnek Kodu**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet1 = workbook.GetWorksheets().Get(0);

    // Create a range A1:B2
    Range range = sheet1.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    sheet1.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style = sheet1.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet1.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Only expands the height of the first row.
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::FirstLine);

    // Autofit rows in the sheet (including the merged cells)
    sheet1.AutoFitRows(options);

    // Add a new worksheet
    int index = workbook.GetWorksheets().Add();
    Worksheet sheet2 = workbook.GetWorksheets().Get(index);
    sheet2.SetName(U16String(u"Sheet2"));

    // Create a range A1:B2
    Range range2 = sheet2.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range2.Merge();

    // Insert value to the merged cell A1
    sheet2.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style2 = sheet2.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style2.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet2.GetCells().Get(0, 0).SetStyle(style2);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options2;

    // Only expands the height of the last row.
    options2.SetAutoFitMergedCellsType(AutoFitMergedCellsType::LastLine);

    // Autofit rows in the sheet (including the merged cells)
    sheet2.AutoFitRows(options2);

    // Add another new worksheet
    index = workbook.GetWorksheets().Add();
    Worksheet sheet3 = workbook.GetWorksheets().Get(index);
    sheet3.SetName(U16String(u"Sheet3"));

    // Create a range A1:B2
    Range range3 = sheet3.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range3.Merge();

    // Insert value to the merged cell A1
    sheet3.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style3 = sheet3.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style3.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet3.GetCells().Get(0, 0).SetStyle(style3);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options3;

    // Only expands the height of each row.
    options3.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    sheet3.AutoFitRows(options3);

    // Add another new worksheet
    index = workbook.GetWorksheets().Add();
    Worksheet sheet4 = workbook.GetWorksheets().Get(index);
    sheet4.SetName(U16String(u"Sheet4"));

    // Create a range A1:B2
    Range range4 = sheet4.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range4.Merge();

    // Insert value to the merged cell A1
    sheet4.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style4 = sheet4.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style4.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet4.GetCells().Get(0, 0).SetStyle(style4);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options4;

    // Ignore merged cells.
    options4.SetAutoFitMergedCellsType(AutoFitMergedCellsType::None);

    // Autofit rows in the sheet (not including the merged cells)
    sheet4.AutoFitRows(options4);

    // Save the Excel file
    workbook.Save(U16String(u"out.xlsx"));

    Aspose::Cells::Cleanup();
}
```
