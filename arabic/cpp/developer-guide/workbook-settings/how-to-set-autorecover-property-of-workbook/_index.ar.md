---
title: كيفية تعيين خاصية AutoRecover لمصنف باستخدام C++
linktitle: كيفية تعيين خاصية AutoRecover للفصل
type: docs
weight: 220
url: /ar/cpp/how-to-set-autorecover-property-of-workbook/
description: تعلم كيفية تفعيل أو تعطيل خاصية AutoRecover للمصنف باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لضبط خاصية AutoRecover للمصنف. القيمة الافتراضية لهذه الخاصية هي **true**. عند تعيينها إلى **false**، يقوم Microsoft Excel بتعطيل AutoRecover (الحفظ التلقائي) على ملف Excel هذا.

 يوفر Aspose.Cells الخاصية [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) لتمكين أو تعطيل هذا الخيار.

{{% /alert %}}

يشرح الكود التالي كيفية استخدام خاصية [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) للمصنف. يبدأ بقراءة القيمة الافتراضية لهذه الخاصية، والتي هي **true**، ثم يغيرها إلى **false** ويحفظ المصنف. ثم يقرأ المصنف مرة أخرى ويلاحظ قيمة هذه الخاصية، والتي تكون **false** في ذلك الحين.

## كود C++ لضبط خاصية AutoRecover للمصنف

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **الناتج**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
