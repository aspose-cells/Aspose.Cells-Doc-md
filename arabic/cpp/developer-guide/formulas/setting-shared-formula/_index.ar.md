---
title: تعيين الصيغة المشتركة باستخدام C++
linktitle: ضبط الصيغ المشتركة
type: docs
weight: 10
url: /ar/cpp/setting-shared-formula/
description: تعلم كيفية تعيين الصيغ المشتركة في أوراق عمل Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

إذا كنت تريد إضافة وظيفة في ورقة عمل تقوم بإجراء حسابات، يشرح هذا المقال كيفية تحقيق ذلك باستخدام Aspose.Cells.

{{% /alert %}}

## ضبط الصيغة المشتركة باستخدام Aspose.Cells

من المفترض أن يكون لديك ورقة عمل مليئة بالبيانات بتنسيق يبدو مثل الورقة العمل النموذجية التالية.

|**ملف الإدخال مع عمود واحد من البيانات**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

ترغب في إضافة وظيفة في B2 التي ستقوم بحساب ضريبة المبيعات للصف الأول من البيانات. الضريبة **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells.

يتيح لك Aspose.Cells تحديد صيغة باستخدام الخاصية [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/). هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3 و B4 و B5، وهلم جرا.) في العمود.

إما أن تفعل ما فعلته للخلية الأولى، بحيث تقوم بشكل فعال بتعيين الصيغة لكل خلية، مع تحديث مرجع الخلية وفقًا لذلك (A3*0.09، A4*0.09، A5*0.09 وهكذا). يتطلب هذا تحديث مراجع الخلايا لكل صف. كما يتطلب أن يقوم Aspose.Cells بتحليل كل صيغة بشكل فردي، مما قد يكون مكلفًا من حيث الوقت لأوراق عمل كبيرة وصيغ معقدة. كما يضيف الكود خطوطًا إضافية على الرغم من أن الحلقات يمكن أن تقصرها بعض الشيء.

وهجاهدًا عبارة عن استخدام **صيغة مشتركة**. مع الصيغة المشتركة، تُحدث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث تُحسب الضريبة بشكل صحيح. الأسلوب [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) أكثر كفاءة من الأسلوب الأول.

تُظهر المثال التالي كيفية استخدامه.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
