---
title: قياس عرض وارتفاع قيمة الخلية بوحدة البكسل باستخدام ++C
linktitle: قياس الحجم
type: docs
weight: 260
url: /ar/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: تعلم كيفية قياس عرض وارتفاع قيمة الخلية بوحدة البكسل من خلال API Aspose.Cells for C++.
keywords: قياس عرض قيمة الخلية بوحدة البكسل، قياس ارتفاع قيمة الخلية بوحدة البكسل، الحصول على عرض قيمة الخلية بوحدة البكسل، الحصول على ارتفاع قيمة الخلية بوحدة البكسل
---

{{% alert color="primary" %}}

في بعض الأحيان تحتاج إلى حساب عرض وارتفاع قيمة الخلية لتناسب قيمة الخلية داخل الخلية. توفر Aspose.Cells الطرق [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) و [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) لهذا الغرض. من خلال استخدام هذه الأساليب يمكنك حساب عرض وارتفاع قيمة الخلية ثم تعيين عرض العمود وارتفاع الصف لتلك الخلية على التوالي وبعد ذلك سيتم ضبط أو تناسب قيمة الخلية داخل الخلية.

بدلاً من ذلك، يمكنك أيضًا [تلقائية طول الأعمدة والصفوف لخلية أو نطاق خلايا](/cells/ar/cpp/autofit-rows-and-columns/) باستخدام واجهات برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

الكود التالي يشرح استخدام الطرق [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) و [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell B2 and add some value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in unit of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [الحصول على عرض النص لقيمة الخلية](/cells/ar/cpp/get-text-width-of-cell-value/)
{{< app/cells/assistant language="cpp" >}}
