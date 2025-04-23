---
title: تغيير اتجاه تسميات العلامات باستخدام C++
linktitle: تغيير اتجاه التسمية التلقائية
description: تعلم كيفية تغيير اتجاه تسميات العلامات في Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية تعديل توجيه تسميات العلامات على المحاور، بما في ذلك التوجيه الأفقي، الرأسي، والمائل.
keywords: Aspose.Cells for C++، تسميات العلامات، الاتجاه، التوجيه، المحاور، أفقي، رأسي، مائل.
type: docs
weight: 170
url: /ar/cpp/change-tick-label-direction/
---

## **تغيير اتجاه التسمية التلقائية**

توفر Aspose.Cells إمكانية تغيير اتجاه تسميات العلامات على الرسم البياني باستخدام خاصية [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/). تقبل الخاصية [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) قيمة تعداد [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). يوفر تعداد [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) الأعضاء التالية:

- أفقي
- رأسي
- دوران 90
- دوران 270
- مكدس

الصورة التالية تقارن بين الملفات المصدر وملفات الإخراج:

### **صورة الملف الأصلي**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **صورة الملف الإخراج**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

مقتطف الكود التالي يغير اتجاه تسمية العلامة المحورية من دوران 90 إلى أفقي.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يمكن تحميل ملفات المصدر والإخراج من الروابط التالية.

[ملف المصدر](105480221.xlsx)

[ملف الإخراج](105480223.xlsx)
