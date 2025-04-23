---
title: ضبط مظهر الرسم البياني باستخدام C++
linktitle: تنسيق الرسم البياني
description: تعلم كيفية تكوين مظهر الرسوم البيانية في Aspose.Cells for C++. سيرشدك دليلنا إلى كيفية تعديل تخطيطات الأشكال اللونية، الألوان، الخطوط، والآثار لتحقيق النمط المرئي المطلوب وتعزيز أوراق العمل الخاصة بك.
keywords: Aspose.Cells for C++، الرسوم البيانية، مظهر الرسم البياني، التخطيطات، الألوان، الخطوط، الآثار، أوراق العمل.
type: docs
weight: 20
url: /ar/cpp/setting-chart-appearance/
---

## **ضبط مظهر الرسم البياني**
في كيفية إنشاء رسم بياني أعطينا مقدمة موجزة عن أنواع الرسوم البيانية وكائنات الرسم البياني التي تقدمها Aspose.Cells، ووصفنا كيفية إنشاء واحد. يتناول هذا المقال كيفية تخصيص مظهر الرسوم البيانية عن طريق تعيين خصائصها:

- تعيين منطقة الرسم البياني.
- تعيين خطوط الرسم البياني.
- تطبيق السمات.
- تعيين عناوين للرسوم البيانية والمحاور.
- العمل مع خطوط الشبكة.

### **تعيين منطقة الرسم البياني**
هناك أنواع مختلفة من المناطق في رسم بياني وتوفر Aspose.Cells قدرة للمطورين على تعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة عن طريق تغيير لون الأمامية والخلفية وتنسيق الملء وما إلى ذلك.

في المثال الوارد أدناه، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من المناطق في رسم بياني. هذه المناطق تشمل:

- منطقة الرسم
- منطقة الرسم البياني
- منطقة مجموعات السلاسل
- منطقة نقطة واحدة في مجموعة سلاسل

الكود البرمجي التالي يوضح كيفية ضبط منطقة الرسم البياني.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

### **تعيين خطوط الرسم البياني**
يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على خطوط السلسلة أو علامات البيانات في [SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/). يُظهر مقتطف الكود التالي كيفية تعيين خطوط الرسم البياني باستخدام API الخاص بـ Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Applying a dotted line style on the lines of a SeriesCollection
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Dot);

    // Applying a triangular marker style on the data markers of a SeriesCollection
    chart.GetNSeries().Get(0).GetMarker().SetMarkerStyle(ChartMarkerType::Triangle);

    // Setting the weight of all lines in a SeriesCollection to medium
    chart.GetNSeries().Get(1).GetBorder().SetWeight(WeightType::MediumLine);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تطبيق سمات مايكروسوفت اكسيل 2007/2010 على الرسوم البيانية**
يمكن للمطورين تطبيق سمات ألوان/ثيمات مختلفة الخاصة بـ Microsoft Excel على [SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) أو كائنات رسم بياني أخرى كما هو موضح في المثال أدناه.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Instantiate the workbook to open the file that contains a chart
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Get the first chart in the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Specify the FillFormat's type to Solid Fill of the first series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::Solid);

    // Get the CellsColor of SolidFill
    CellsColor cc = chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().GetCellsColor();

    // Create a theme in Accent style
    cc.SetThemeColor(ThemeColor(ThemeColorType::Accent6, 0.6));

    // Apply the theme to the series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().SetCellsColor(cc);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart theme applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ضبط عناوين الرسوم البيانية أو المحاور**
يمكنك استخدام Microsoft Excel لتعيين عناوين الرسم البياني ومحاورها في بيئة WYSIWYG. كما يسمح Aspose.Cells للمطورين بتعيين عناوين الرسم البياني والمحاور أثناء التشغيل. تحتوي جميع الرسوم البيانية ومحاورها على خاصية [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) والتي يمكن استخدامها لتعيين عناوينها كما هو موضح في المثال أدناه.

يوضح مقتطف الكود التالي كيفية ضبط عناوين الرسوم البيانية والمحاور.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **العمل مع خطوط الشبكة الرئيسية**
من الممكن تخصيص شكل خطوط الشبكة الرئيسية. يمكن إخفاء أو إظهار خطوط الشبكة أو تحديد لونها وإعدادات أخرى. فيما يلي، نُوضّح كيفية إخفاء خطوط الشبكة وكيفية تغيير لونها.

#### **إخفاء خطوط الشبكة الرئيسية**
يمكن للمطورين السيطرة على ظهور خطوط الشبكة الرئيسية عن طريق تعيين خاصية [IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/isvisible/) على كائن [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) لتكون **true** أو **false**.

الكود البرمجي التالي يوضح كيفية إخفاء خطوط الشبكة الرئيسية. بعد إخفاء خطوط الشبكة الرئيسية، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل بدون خطوط شبكة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Hiding the major gridlines of Category Axis
    chart.GetCategoryAxis().GetMajorGridLines().SetIsVisible(false);

    // Hiding the major gridlines of Value Axis
    chart.GetValueAxis().GetMajorGridLines().SetIsVisible(false);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **تغيير إعدادات خطوط الشبكة الرئيسية**
لا يستطيع المطورون فقط التحكم في رؤية خطوط الشبكة الرئيسية ولكن أيضًا خصائص أخرى بما في ذلك لونها وما إلى ذلك.

الكود البرمجي التالي يوضح كيفية تغيير لون خطوط الشبكة الرئيسية. بعد تعيين لون خطوط الشبكة الرئيسية، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل بخطوط شبكة معدلة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the color of Category Axis' major gridlines to silver
    chart.GetCategoryAxis().GetMajorGridLines().SetColor(Color::Silver());

    // Setting the color of Value Axis' major gridlines to red
    chart.GetValueAxis().GetMajorGridLines().SetColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [تعيين رمز تنسيق القيم لسلاسل الرسم البياني](/cells/ar/cpp/set-the-values-format-code-of-chart-series/)
- [تعيين صورة كحشو خلفية في الرسم البياني](/cells/ar/cpp/set-picture-as-background-fill-in-the-chart/)
