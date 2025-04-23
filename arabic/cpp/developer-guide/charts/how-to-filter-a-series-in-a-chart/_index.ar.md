---
title: ثلاث طرق لترشيح بيانات المخطط باستخدام C++
linktitle: ثلاثة أساليب لتصفية بيانات الرسم البياني
description: تعلم كيفية تصفية المخططات في إكسل باستخدام Aspose.Cells for C++. سيُظهر دليلنا الشامل كيف تطبق المرشحات على المخططات، وتخصيص عناصر المخطط، واستخدام أدوات تحليل البيانات لتحقيق رؤى أفضل واتخاذ قرارات مستنيرة.
keywords: Aspose.Cells for C++، تصفية المخططات في إكسل، تحليل البيانات، اتخاذ القرار، التصوير البياني.
type: docs
weight: 2210
url: /ar/cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. تصفية السلاسل لعرض رسم بياني**

### **خطوات تصفية السلاسل من رسم بياني في إكسل**
يمكننا في إكسل تصفية سلسلة معينة من المخطط، مما يؤدي إلى عدم عرض تلك السلاسل المصفاة في المخطط. يُعرض المخطط الأصلي في **الشكل 1**. ومع ذلك، عند تصفية **Testseries2** و**Testseries4**، سيظهر المخطط كما هو موضح في **الشكل 2**.

في Aspose.Cells، يمكننا تنفيذ عملية مماثلة. لملف [عينة](seriesFiltered.xlsx) كهذا، إذا أردنا تصفية **Testseries2** و**Testseries4**، يمكننا تنفيذ الكود التالي. بالإضافة إلى ذلك، سنحتفظ بقائمتين: واحدة ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)) لتخزين جميع السلاسل المختارة وأخرى ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)) لتخزين السلاسل المصفاة.

يرجى **ملاحظة** أنه في الكود، عندما نقوم بتعيين **chart->GetNSeries()->Get(0)->SetIsFiltered(true);**، سيتم إزالة السلسلة الأولى في [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) ووضعها في الموقع المناسب داخل [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/). بعد ذلك، ستصبح **NSeries[1]** السابقة العنصر الأول في القائمة، وستتحرك جميع السلاسل التالية للأمام بموقع واحد. مما يعني أنه إذا ثم تشغيل **chart->GetNSeries()->Get(1)->SetIsFiltered(true);**، فإننا نزيل السلسلة الثالثة الأصلية فعليًا. قد يؤدي ذلك أحيانًا إلى ارتباك، لذلك نوصي باتباع الخطوة في الكود التي تحذف السلاسل من النهاية إلى البداية.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **الكود المثالي**
تحميل ملف إكسل العيني ([ملف إكسل مرشّحة.xlsx](seriesFiltered.xlsx)).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. مرشّح البيانات واسمح للرسم البياني بالتغيير**

تصفية بياناتك هي طريقة رائعة للتعامل مع مرشحات المخططات التي تحتوي على الكثير من البيانات. عندما تقوم بتصفية البيانات، سيتغير المخطط. إحدى القضايا التي سنواجهها هي التأكد من بقاء المخطط على الشاشة. عند التصفية، تحصل على صفوف مخفية، وأحيانًا، سيكون المخطط في تلك الصفوف المخفية.

![todo:image_alt_text](Figure3.png)

### **خطوات استخدام مرشحات البيانات لتغيير الرسم البياني في إكسل**

1. انقر داخل نطاق البيانات الخاص بك.
2. انقر على علامة التبويب **البيانات**، وقم بتشغيل المرشحات بالنقر فوق المرشحات. ستحتوي الصف المسمى على السهم المنسدل.
3. إنشاء رسم بياني من خلال الانتقال إلى علامة التبويب **إدراج** وتحديد رسم بياني للأعمدة.
4. الآن قم بتصفية بياناتك باستخدام السهوم المنسدلة في البيانات. لا تستخدم مرشحات الرسم البياني.

### **الكود المثالي**
يعرض رمز النموذج التالي نفس الميزة باستخدام Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. فلتر البيانات باستخدام جدول واسمح للرسم البياني بالتغيير**

استخدام جدول مشابه للطريقة 2، استخدام نطاق، ولكن لكم مزايا مع الجداول على النطاقات. عند تغيير النطاق إلى جدول وإضافة البيانات، سيقوم الرسم البياني بالتحديث تلقائيًا. مع نطاق، سيتعين عليك تغيير مصدر البيانات.

### **تنسيق باعتباره جدولاً في إكسل**

انقر داخل بياناتك واستخدم **CTRL + T** أو استخدم علامة التبويب الرئيسية، **تنسيق باعتبارها جدولاً**

![todo:image_alt_text](Figure4.png)

### **الكود المثالي**
يرفع الرمز النموذجي التالي [ملف إكسل النموذجي](TableFilters.xlsx) ويظهر نفس الميزة باستخدام Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
