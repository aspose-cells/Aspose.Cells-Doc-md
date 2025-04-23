---
title: تسمية بيانات مخصصة غنية النص لنقطة المخطط باستخدام ++C
description: تعلم كيفية إضافة تسميات بيانات مخصصة غنية النص لنقاط المخطط في Aspose.Cells for C++. سيظهر دليلنا كيفية تنسيق التسميات باستخدام خطوط وألوان وخيارات محاذاة مختلفة لتحسين المظهر ووضوح القراءة لرسومك البيانية.
keywords: Aspose.Cells for C++، التخطيط، النص الغني، التسميات المخصصة، الخطوط، الألوان، المحاذاة، المظهر، وضوح القراءة.
type: docs
weight: 10
url: /ar/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

 يمكنك استخدام Aspose.Cells لإنشاء تسمية بيانات مخصصة غنية النص لنقطة المخطط. يوفر Aspose.Cells طريقة [Characters](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) لاسترجاع كائن [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) الذي يمكن استخدامه لضبط خصائص الخط للنص مثل لونه، سمكه، وغيرها.

{{% /alert %}}

## تسمية بيانات مخصصة بتنسيق نص غني لنقطة الرسم البياني

يسمح الكود التالي بالوصول إلى نقطة المخطط الأولى من السلسلة الأولى، تعيين نصها ثم تعيين خط العشرة أحرف الأولى من خلال ضبط لونها إلى الأحمر وعرضها إلى **صحيح**.

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

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
