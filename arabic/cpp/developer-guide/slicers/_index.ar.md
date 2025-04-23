---
title: إدراج slicer باستخدام C++
linktitle: قاطعات
type: docs
weight: 170
url: /ar/cpp/create-slicer/
description: إدارة slicers لملفات إكسل باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

السلايسر هو أداة تستخدم لتصفية البيانات بسرعة. يمكن استخدامها لتصفية البيانات سواء في جدول أو جدول محوري. تتيح لك Microsoft Excel إنشاء slicer عن طريق تحديد جدول أو جدول محوري ثم النقر على *إدراج > Slicer*. كما تتيح Aspose.Cells إنشاء slicer باستخدام طريقة [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/).

## **إنشاء مُقطَّع إلى جدول محوري**

يرجى الاطلاع على الكود النموذجي التالي. يحمل [ملف Excel النموذجي](67338470.xlsx) الذي يحتوي على الجدول المحوري. ثم يقوم بإنشاء المقطع على أساس حقل الجدول المحوري الأساسي الأول. وأخيرًا ، يحفظ المصنف في [XLSX الناتج](67338471.xlsx) و[XLSB الناتج](67338472.xlsb) تنسيق. تُظهر لقطة الشاشة التالية المقطع الذي تم إنشاؤه بواسطة Aspose.Cells في ملف Excel الناتج.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إنشاء مُقطَّع إلى جدول Excel**

يرجى الاطلاع على رمز العينة التالي. يقوم بتحميل ملف Excel العيني ([sampleCreateSlicerToExcelTable.xlsx](sampleCreateSlicerToExcelTable.xlsx)) الذي يحتوي على جدول. ثم يقوم بإنشاء المُقطَّع بناءً على العمود الأول. أخيرًا، يحفظ برنامج العمل بتنسيق [XLSX](outputCreateSlicerToExcelTable.xlsx).

### **الكود المثالي**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **الموضوعات المتقدمة**
- [تغيير خصائص المنقي](/cells/ar/cpp/change-slicer-properties/)
- [رسم المنقي أثناء تحويل Excel إلى PDF](/cells/ar/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [تنسيق المنقي](/cells/ar/cpp/formatting-slicer/)
- [إزالة قالب التصفية](/cells/ar/cpp/removing-slicer/)
- [تقديم المقطع](/cells/ar/cpp/rendering-slicer/)
- [تحديث المقسم](/cells/ar/cpp/updating-slicer/)
