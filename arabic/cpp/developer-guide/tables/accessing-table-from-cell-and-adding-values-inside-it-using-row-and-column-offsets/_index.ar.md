---  
title: الوصول إلى الجدول من الخلية وإضافة القيم بداخله باستخدام إزاحات الصف والعمود مع C++  
linktitle: الوصول إلى الجدول من الخلية وإضافة القيم داخله باستخدام إزاحة الصف والعمود  
type: docs  
weight: 230  
url: /ar/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: الوصول إلى جدول من خلية وإضافة قيم باستخدام Aspose.Cells مع C++.  
---  

{{% alert color="primary" %}}  

عادةً ما تضيف القيم داخل الجدول أو كائن القائمة باستخدام الطريقة [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/). ولكن في بعض الأحيان، قد تحتاج إلى إضافة القيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.  

للوصول إلى كائن جدول أو قائمة من خلية، استخدم الطريقة [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/). لإضافة قيم بداخله باستخدام إزاحات الصف والعمود، استخدم الطريقة [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

{{% /alert %}}  

يوضح لقطة الشاشة التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على جدول فارغ ويبرز الخلية D5 التي تقع داخل الجدول. سنصل إلى هذا الجدول من الخلية D5 باستخدام طريقة [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/) ثم نضيف القيم بداخله باستخدام طريقتي [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) و [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

## مثال  

### لقطات شاشة تقارن الملفات المصدرية والإخراجية  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

اللقطة الشاشية التالية تُظهر ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما يمكنك رؤية الخلية D5 التي تحتوي على قيمة والخلية F6 والتي تقع في الإزاحة 2،2 من الجدول وتحتوي على قيمة.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### كود C++ للوصول إلى الجدول من الخلية وإضافة القيم بداخله باستخدام إزاحات الصف والعمود  

يقوم الكود النموذجي التالي باستخدام ملف Excel المصدر كما هو موضح في اللقطة الشاشية أعلاه ويضيف القيم داخل الجدول ويولد ملف Excel الناتج كما هو موضح أعلاه.  

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
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell D5 which lies inside the table
    Cell cell = worksheet.GetCells().Get(u"D5");

    // Put value inside the cell D5
    cell.PutValue(u"D5 Data");

    // Access the Table from this cell
    ListObject table = cell.GetTable();

    // Add some value using Row and Column Offset
    table.PutCellValue(2, 2, u"Offset [2,2]");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
