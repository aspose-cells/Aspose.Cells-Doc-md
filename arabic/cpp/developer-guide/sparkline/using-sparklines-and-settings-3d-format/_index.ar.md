---
title: استخدام Sparklines والإعدادات 3D Format مع C++
linktitle: استخدام الشرائط وإعدادات تنسيق ثلاثي الأبعاد
type: docs
weight: 40
url: /ar/cpp/using-sparklines-and-settings-3d-format/
description: تعلم كيفية استخدام sparklines وتطبيق تنسيق 3D في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **استخدام الشرائط**
يمكن لبرنامج Microsoft Excel 2010 تحليل المعلومات بطرق أكثر من أي وقت مضى. يسمح للمستخدمين بتتبع وتسليط الضوء على اتجاهات البيانات المهمة باستخدام أدوات تحليل البيانات والرؤية الجديدة. الشرائط هي رسومات مصغرة يمكنك وضعها داخل الخلايا بحيث يمكنك عرض البيانات والرسم البياني على الجدول نفسه. عند استخدام الشرائط بشكل صحيح، يكون تحليل البيانات أسرع وأكثر دقة. كما أنها توفر رؤية بسيطة للمعلومات، مما يجنب ورقات العمل المزدحمة بالرسوم البيانية الكثيرة.

توفر Aspose.Cells واجهة برمجة التطبيقات للتلاعب في الشرائط في جداول البيانات.
### **الشرائط في Microsoft Excel**
لإدراج الشرائط في Microsoft Excel 2010:

1. حدد الخلايا التي ترغب في ظهور الشرائط فيها. لجعلها سهلة الرؤية، حدد الخلايا على جانب البيانات.
1. انقر على **Insert** في الشريط واختر **column** في **Sparklines**.
1. حدد أو أدخل نطاق الخلايا في ورقة العمل التي تحتوي على البيانات. ستظهر الرسوم البيانية.

تساعد الشرائط في رؤية الاتجاهات، على سبيل المثال، سجل الفوز أو الخسارة لدوري الكرة اللينة. يمكن للشرائط حتى الإشارة إلى مجموع الموسم بأكمله لكل فريق في الدوري.
### **شرائط البيانات باستخدام Aspose.Cells**
يمكن للمطورين إنشاء، حذف أو قراءة sparklines (في ملف النموذج) باستخدام الواجهة البرمجية التي توفرها Aspose.Cells. الفئات التي تدير sparklines موجودة في مساحة الأسماء [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) لذلك تحتاج إلى استيراد هذه المساحة قبل استخدام هذه الميزات.

من خلال إضافة رسومات مخصصة لنطاق البيانات المعطى، يحصل المطورون على حرية إضافة أنواع مختلفة من الرسوم الصغيرة إلى مناطق الخلايا المحددة.

يوضح المثال أدناه ميزة شرائط البيانات. يوضح المثال كيفية:

1. فتح ملف قالب بسيط.
1. قراءة معلومات شرائط البيانات لورقة عمل.
1. إضافة شرائط بيانات جديدة لنطاق بيانات معطى إلى منطقة خلية.
1. حفظ ملف Excel على القرص.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ضبط تنسيق ثلاثي الأبعاد**
قد تحتاج أحيانًا إلى أنماط الرسوم البيانية ثلاثية الأبعاد حتى تتمكن من الحصول على النتائج المناسبة لسيناريو العمل الخاص بك. يوفر Aspose.Cells واجهة برمجة التطبيقات ذات الصلة لتطبيق تنسيقات Microsoft Excel 2007 ثلاثية الأبعاد.

يتم تقديم مثال كامل أدناه لتوضيح كيفية إنشاء رسم بياني وتطبيق تنسيق Microsoft Excel 2007 ثلاثي الأبعاد. بعد تنفيذ كود المثال، سيتم إضافة رسم بياني للأعمدة (مع تأثيرات ثلاثية الأبعاد) إلى ورقة العمل.

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

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
