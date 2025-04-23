---  
title: تغيير مصدر بيانات المخطط إلى ورقة الهدف أثناء نسخ الصفوف أو النطاق باستخدام C++  
description: تعلم كيفية تغيير مصدر بيانات المخطط إلى ورقة الهدف أثناء نسخ الصفوف أو النطاق في Aspose.Cells for C++. دليلنا سيرٌي كيف تقوم بتحديث مدى بيانات المخطط وربطه بورقة الهدف، لضمان أن تظهر الصفوف أو النطاق المنسوخ بدقة في المخطط.  
keywords: Aspose.Cells for C++، رسم بياني، مصدر البيانات، ورقة الهدف، الصفوف، النطاق، النسخ، التحديث، مدى البيانات، الربط.  
type: docs  
weight: 440  
url: /ar/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **سيناريوهات الاستخدام المحتملة**

عند نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة، فإن مصدر البيانات للمخطط لا يتغير. على سبيل المثال، إذا كان مصدر البيانات للمخطط =Sheet1!$A$1:$B$4، فبعد نسخ الصفوف أو النطاق إلى ورقة جديدة، سيظل المصدر كما هو، وهو =Sheet1!$A$1:$B$4. لا يزال يشير إلى ورقة العمل القديمة، وهي Sheet1. هذا هو السلوك أيضًا في Microsoft Excel. ولكن إذا أردت أن يشير إلى ورقة العمل الجديدة، يرجى استخدام الخاصية [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) وتعيينها إلى **true** أثناء استدعاء الطريقة [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). الآن، إذا كانت ورقة العمل الهدف هي DestSheet، فإن مصدر البيانات لمخططك سيتغير من =Sheet1!$A$1:$B$4 إلى =DestSheet!$A$1:$B$4.

## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**

يوضح الكود النموذجي التالي استخدام الخاصية [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) أثناء نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة. يستخدم الكود ملف Excel النموذجي (5113699.xlsx) ويولد ملف Excel الناتج (5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
