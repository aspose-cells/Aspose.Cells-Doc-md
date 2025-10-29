---
title: تحويل المخطط إلى صورة في صيغة SVG باستخدام C++
linktitle: تحويل الرسم البياني إلى صورة بتنسيق SVG
type: docs
weight: 240
url: /ar/cpp/converting-chart-to-image-in-svg-format/
description: تعلم كيفية تحويل المخططات إلى صور SVG باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

تعتبر الرسومات البيانية القابلة للتحجيم (SVG) تنسيق صورة ناقل معتمد على XML للرسوميات ثنائية الأبعاد والتي تدعم أيضًا التفاعل والرسوم المتحركة. مواصفات SVG هي معيار مفتوح تم تطويره من قبل W3C (المؤتمر العالمي للشبكة العنكبوتية) منذ عام 1999.

تم تعريف صور SVG وسلوكها في ملفات نص XML. وهذا يعني أنه يمكن البحث عنها وفهرستها وتدوينها وضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نص، ولكن غالبًا ما يتم إنشاؤها باستخدام برمجيات الرسم.

يمكن لـ Aspose.Cells حفظ المخططات كصور بصيغ متعددة مثل BMP، JPEG، PNG، GIF، SVG، وما إلى ذلك. يوضح هذا المقال كيفية حفظ مخطط بصيغة SVG.

{{% /alert %}}

يشرح الرمز العينة التالي كيفية استخدام Aspose.Cells لتحويل الرسم البياني إلى صورة في تنسيق SVG. يحمل الرمز ملف Microsoft Excel المصدر ثم يحفظ الرسم البياني الأول الذي تم العثور عليه في الورقة العمل الأولى إلى SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
