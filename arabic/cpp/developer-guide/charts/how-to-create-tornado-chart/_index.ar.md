---
title: كيفية إنشاء مخطط إعصار باستخدام C++
linktitle: إنشاء مخطط إعصار
type: docs
weight: 73
url: /ar/cpp/create-tornado-chart/
description: تعلم كيفية إنشاء مخطط إعصار باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: إنشاء مخطط إعصار باستخدام C++، إضافة مخطط إعصار، إدراج مخطط إعصار
---

## **مقدمة**
الرسم البياني للإعصار، المعروف أيضًا باسم الرسم البياني للإعصار أو الرسم البياني للتورنادو، هو نوع من تصور البيانات يُستخدم في التحليل الحساسية في برنامج إكسل. يساعدك على فهم تأثير تغيير المتغيرات على نتيجة معينة.

## **كيفية إنشاء رسم بياني للإعصار في إكسل**
يمكنك إنشاء رسم بياني للإعصار في إكسل من خلال اتباع هذه الخطوات:
1. حدد البيانات وانتقل إلى إدراج --> الرسوم البيانية --> إدراج رسم بياني عمودي أو شريطي --> رسم بياني عمودي مكدس. انقر عليه.
<br>
<img src="1.png" width=70% />
2. تغيير محور الصف: انقر بزر الماوس الأيمن فوق محور الصف. انقر على تنسيق المحور. في العلامات، انقر على القائمة المنسدلة لموضع العلامة وحدد العنصر المنخفض.
<br>
<img src="2.png" width=70% />
3. حدد أي شريط وانتقل إلى التنسيق. ضبط عرض الفجوة المناسب.
<br>
<img src="3.png" width=70% />
4. لنقم بإزالة علامة الناقص (-) من رسم بياني الإعصار. حدد محور السين. انتقل إلى التنسيق. في خيارات المحور، انقر على الرقم. في الفئة، حدد مخصص. في رمز التنسيق اكتب ###0،###0. انقر على إضافة.
<br>
<img src="4.png" width=70% />
5. انقر على محور Y واذهب إلى خيارات المحور. في خيارات المحور، حدد الفئات بترتيب عكسي.
<br>
<img src="5.png" width=70% />

## **كيفية إضافة رسم بياني للإعصار في Aspose.Cells**
يرجى الاطلاع على الكود النموذجي التالي. يقوم بتحميل [ملف إكسل نموذجي](sample.xlsx) الذي يحتوي على بعض البيانات النموذجية. ثم يقوم بإنشاء رسم بياني عمودي مكدس بناءً على البيانات الأولية وتعيين الخصائص ذات الصلة. في النهاية، يقوم بحفظ الدفتر إلى [تنسيق XLSX الناتج](out.xlsx). تُظهر اللقطة الشاشية التالية الرسم البياني للإعصار الذي تم إنشاؤه بواسطة Aspose.Cells في ملف الإكسل الناتج.
<br>
<img src="6.png" width=70% />

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
