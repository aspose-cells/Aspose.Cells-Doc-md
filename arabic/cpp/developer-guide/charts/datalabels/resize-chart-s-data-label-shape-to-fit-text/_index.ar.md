---  
title: تغيير حجم شكل تسمية البيانات في المخطط ليناسب النص باستخدام ++C  
description: تعرف على كيفية تغيير حجم شكل تسمية البيانات في المخطط ليناسب النص في Aspose.Cells for C++. ستوضح لك دليلتنا كيفية تعديل حجم وشكل حاوية التسمية لضمان عرض النص بشكل صحيح بدون تقطيع أو تداخل.  
keywords: Aspose.Cells for C++، التخطيط، تسميات البيانات، تغيير حجم الشكل، ملائمة النص، التقطيع، التداخل.  
type: docs  
weight: 220  
url: /ar/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

توفر تطبيق Excel الخيار **تغيير شكل لملاءمة النص** لتسميات بيانات الرسم البياني من أجل زيادة حجم الشكل بحيث يتناسب النص بداخله.  

{{% /alert %}}  

## **كيفية تغيير شكل تسمية بيانات الرسم البياني لملاءمة النص في Microsoft Excel**  

يمكن الوصول إلى هذا الخيار على واجهة إكسل عن طريق تحديد أي من تسميات البيانات على المخطط. انقر بزر الماوس الأيمن واختر قائمة **تكوين تسميات البيانات**. في علامة التبويب **الحجم والخصائص**، قم بتوسيع **المحاذاة** للكشف عن الخصائص ذات الصلة بما في ذلك خيار **تغيير حجم الشكل لملاءمة النص**.  

## **كيفية تغيير حجم شكل تسمية البيانات في المخطط ليناسب النص باستخدام Aspose.Cells for C++**  

لمحاكاة ميزة إكسل في تغيير حجم أشكال تسمية البيانات لتناسب النص، قدمت واجهات برمجة التطبيقات Aspose.Cells الخاصية [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) من نوع Boolean. يُظهر الكود التالي سيناريو الاستخدام البسيط الخاص بـ [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) الخاصية.  

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Create an instance of Workbook containing the Chart
    Workbook book(inputFilePath);

    // Access the Worksheet that contains the Chart
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Iterate through each Chart in the Worksheet
    for (int32_t i = 0; i < sheet.GetCharts().GetCount(); i++)
    {
        Chart chart = sheet.GetCharts().Get(i);

        // Iterate through each NSeries in the Chart
        for (int32_t index = 0; index < chart.GetNSeries().GetCount(); index++)
        {
            // Access the DataLabels of indexed NSeries
            DataLabels labels = chart.GetNSeries().Get(index).GetDataLabels();

            // Set ResizeShapeToFitText property to true
            labels.SetIsResizeShapeToFitText(true);
        }

        // Calculate Chart
        chart.Calculate();
    }

    // Save the result
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    book.Save(outputFilePath);

    std::cout << "Chart calculations and modifications completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

