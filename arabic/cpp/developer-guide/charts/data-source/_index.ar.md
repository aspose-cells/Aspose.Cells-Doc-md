---
title: تعيين مصدر البيانات للمخطط باستخدام ++C
linktitle: مصدر البيانات
type: docs
weight: 10
url: /ar/cpp/data-formatting-in-charts/
description: تعرف على مصادر البيانات المدعومة بواسطة Aspose.Cells for C++. سيرشدك دليلنا خلال الأنواع المختلفة من مصادر البيانات المتاحة ويعرض لك كيفية الاتصال بها واسترجاع البيانات منها لملء أوراق العمل الخاصة بك.
keywords: Aspose.Cells for C++، رسم المخططات، تنسيق البيانات، التسميات، الألوان، الخطوط، المظهر، قابلية الاستخدام.
---

في موضوعاتنا السابقة، قدمنا العديد من الأمثلة لشرح كيف يمكنك ضبط مصدر البيانات لمخططك. في هذا الموضوع، سنوفر مزيدًا من التفاصيل حول أنواع البيانات التي يمكن تعيينها لمخطط.

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات التي يتعين التعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells وهي كما يلي:

- بيانات الرسم البياني.
- بيانات الفئة.

### **بيانات الرسم البياني**

بيانات الرسم البياني هي البيانات التي نستخدمها كمصدر لبناء الرسوم البيانية الخاصة بنا. يمكننا إضافة مجموعة من الخلايا (تحتوي على بيانات الرسم البياني) عن طريق استدعاء [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) إلى [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **بيانات الفئة**

تُستخدم بيانات الفئة لوسم بيانات الرسم البياني ويمكن إضافتها إلى [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) باستخدام خاصية [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/). يتم تقديم مثال كامل أدناه لتوضيح استخدام بيانات الرسم البياني والفئة. بعد تنفيذ رمز المثال أعلاه، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل كما هو موضح أدناه.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **الموضوعات المتقدمة**
- [تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/cpp/create-dynamic-charts/)
- [طريقة سهلة لضبط الرسوم البيانية باستخدام طريقة Chart.SetChartDataRange](/cells/ar/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني](/cells/ar/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
