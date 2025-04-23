---
title: تغيير خصائص المقاطع باستخدام C++
linktitle: تغيير خصائص المنقي
type: docs
weight: 70
url: /ar/cpp/change-slicer-properties/
description: تغيير خصائص مقطع في ملفات إكسل باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

قد تكون هناك مواقف تود فيها تغيير خصائص المنقي مثل النشر أو ارتفاع الصف. يوفر Aspose.Cells لك الخيار لتحديث هذه الخصائص.

## **تغيير خصائص المنقي**

يرجى الاطلاع على الكود العيني التالي. يحمل [ملف Excel العيني](sampleCreateSlicerToExcelTable.xlsx) الذي يحتوي على جدول. ينشئ بعد ذلك المنقي بناءً على العمود الأول ويقوم بتغيير خصائصه مثل ارتفاع الصف، العرض، القابلية للطباعة، العنوان، وما إلى ذلك. يحفظ المصنف كـ [ملف الإخراج لتغيير خصائص المنقي](outputChangeSlicerProperties.xlsx).

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
