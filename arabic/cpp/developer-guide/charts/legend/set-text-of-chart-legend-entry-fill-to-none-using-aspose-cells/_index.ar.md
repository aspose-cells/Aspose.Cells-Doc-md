---
title: تعيين نص إدخال أسطورة المخطط ليكون لا شيء باستخدام C++
linktitle: تعيين نص إدخال أسطورة المخطط ليكون لا شيء
description: تعلم كيفية استخدام Aspose.Cells for C++ لضبط تعبئة مدخل عنوان الشارة في الرسم البياني علىNone. سيُظهر دليلنا كيفية تعديل لون التعبئة للمدخلات في مخططات Microsoft Excel لتحسين التصور والتخصيص.
keywords: Aspose.Cells for C++، تعبئة مدخل شارة الرسم البياني، Microsoft Excel، التصور، التخصيص.
type: docs
weight: 320
url: /ar/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

إذا كنت ترغب في تعيين نص إدخال تسمية المخطط إلى لا شيء حتى لا يظهر داخل تسمية المخطط، فعليك تعيين [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) إلى **true**.

{{% /alert %}}

يقوم الكود العينة التالي بتعيين نص إدخال تسمية المخطط الثاني إلى لا شيء. يرجى تنزيل [ملف Excel عينة](5115219.xlsx) المستخدم في هذا الكود و[ملف Excel الخرج](5115217.xlsx) الذي تم إنشاؤه به للرجوع إليه.

تسلط الصورة الشاشية التالية الضوء على تأثير هذا الكود على [ملف Excel عينة](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
