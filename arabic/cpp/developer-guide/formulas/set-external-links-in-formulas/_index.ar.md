---
title: إعداد الروابط الخارجية في الصيغ باستخدام ++C
linktitle: تحديد الروابط الخارجية في الصيغ
type: docs
weight: 20
url: /ar/cpp/set-external-links-in-formulas/
description: تعلم كيفية تضمين روابط لملفات خارجية في الصيغ باستخدام Aspose.Cells مع ++C.
---

{{% alert color="primary" %}} 

في بعض الأحيان، من الضروري تضمين روابط إلى ملفات خارجية في الصيغ، على سبيل المثال، لتقييم قيمة خلية أو نطاق مقابلها. يوفر Aspose.Cells هذه الميزة ويوضح هذا المستند كيفية استخدامها.

{{% /alert %}} 

يظهر الكود النموذجي أدناه كيفية تضمين الملفات الخارجية في الصيغ.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
