---
title: Z محور باستخدام C++
linktitle: المحور Z
description: تعلم كيفية العمل مع محور Z في Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية تكوين وتخصيص محور Z، بما في ذلك مقياسه وعلاماته، لتعزيز مخططاتك.
keywords: Aspose.Cells for C++، محور Z، التخطيط، التكوين، التخصيص، المقياس، العلامات.
type: docs
weight: 210
url: /ar/cpp/z-axis/
---

## **سيناريوهات الاستخدام المحتملة**
بالنسبة لبعض الرسوم البيانية ثلاثية الأبعاد مثل العمود ثلاثي الأبعاد، والمخروط ثلاثي الأبعاد، أو الهرم ثلاثي الأبعاد الذي يحتوي على محور العمق (السلسلة)، المعروف أيضًا بمحور Z، يمكنك تغييره. يمكنك تحديد الفاصل بين علامات التدرج، وتسميات المحور وعمليات أخرى.

## **قم بالتعامل مع المحور الأساسي والثانوي على غرار Microsoft Excel**
 يرجى مراجعة رمز العينة التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في ورقة العمل الأولى. ثم نضيف رسمًا بيانيًا ونحدد نوعه إلى عمود3D، ثم يمكنك رؤية محور Z المسمى أيضًا محور العمق. 

![todo:image_alt_text](excel.png)

## **الكود المثالي**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
