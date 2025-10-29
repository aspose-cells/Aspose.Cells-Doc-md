---
title: التعامل مع وحدات المحور التلقائية مثل Microsoft Excel باستخدام C++
linktitle: التعامل مع وحدات المحور التلقائية
description: تعلم كيفية التعامل مع الوحدات التلقائية على محاور المخططات في Aspose.Cells for C++، مشابهة لما في Microsoft Excel. دليلنا سيعرض كيفية تكوين وتخصيص الوحدات التلقائية على محور المخطط، بما في ذلك عرض التدوين العلمي وتعديل المقياس.
keywords: Aspose.Cells for C++، محاور الرسم البياني، وحدات تلقائية، ميكروسوفت إكسل، تكوين، تخصيص، الترقيم العلمي، المقياس.
type: docs
weight: 120
url: /ar/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **سيناريوهات الاستخدام المحتملة**
لم تكن الإصدارات الأولى من Aspose.Cells قادرة على معالجة وحدات المحور الرسم البياني تلقائيًا بشكل صحيح عندما يتم تقديم الرسم البياني إلى صورة أو PDF. الآن، يدعم Aspose.Cells معالجة وحدات المحور الرسم البياني تلقائيًا. لا يوجد تغيير في الشفرة. فقط قم بتحويل رسم بياني إلى صورة أو PDF وسيقوم بتقديم محور الرسم البياني تمامًا مثلما يقوم Excel بتقديمه.

## **التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel**
الشفرة العينية التالية تحمل [ملف Excel عيني](61767755.xlsx) وتولد [رسم بياني PDF الناتج](61767752.pdf). يُظهر لقطة الشاشة وحدات المحور الرسم البياني التلقائية في مستطيلات حمراء ويُقارن أيضًا رسم البيان العيني مع رسم بياني PDF الناتج. كلاهما متطابق تمامًا.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **الكود المثالي**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
