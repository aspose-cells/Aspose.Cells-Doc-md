---
title: تغيير الخط على حروف اليونيكود المحددة فقط أثناء الحفظ إلى PDF باستخدام C++
linktitle: تغيير خط حروف اليونيكود
type: docs
weight: 260
url: /ar/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: تعلم كيفية تغيير خط الحرف اليونيكود المحدد أثناء الحفظ إلى PDF باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

بعض الأحرف اليونيكود غير قابلة للعرض بواسطة الخط المحدد من قبل المستخدم. أحد الأحرف اليونيكود هو **الشرطة الغير قابلة للانفصال** (U+2011) ورقمه اليونيكود هو 8209. هذا الحرف لا يمكن عرضه باستخدام الخط **تايمز نيو رومان**, ولكن يمكن عرضه بالخطوط الأخرى مثل **أريال يونيكود ام اس**.

 عندما يظهر مثل هذا الحرف داخل كلمة أو جملة معينة والتي تكون مكتوبة بخط معين مثل Times New Roman، فإن Aspose.Cells يغير خط الكلمة أو الجملة بأكملها إلى خط يمكنه عرض هذا الحرف مثل Arial Unicode MS.

 ومع ذلك، هذا سلوك غير مرغوب لبعض المستخدمين، ويريدون فقط تغيير خط الحرف المحدد بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

 للتعامل مع هذه المشكلة، يوفر Aspose.Cells خاصية `PdfSaveOptions.IsFontSubstitutionCharGranularity`، والتي يجب ضبطها على `true` بحيث يتغير خط الحرف المحدد الذي لا يمكن عرضه إلى خط قابل للعرض، ويظل باقي الكلمة أو الجملة في الخط الأصلي.

{{% /alert %}}

## **مثال**

الصورة المرفقة تقارن بين ملفي PDF الناتجين من الشفرة النموذجية التالية.

تم توليد واحد بدون ضبط خاصية `PdfSaveOptions.IsFontSubstitutionCharGranularity`، والآخر بعد ضبطها على `true`.

 كما هو موضح في ملف PDF الأول، تغير خط الجملة بأكملها من Times New Roman إلى Arial Unicode MS بسبب الشرطة غير الفاصلة. بينما في الملف الثاني، تغير فقط خط الشرطة غير الفاصلة.

|**ملف PDF الأول**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**ملف PDF الثاني**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **الكود المثالي**

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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style style = cell1.GetStyle();
    style.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(style);
    cell2.SetStyle(style);

    // Put the values inside the cell
    cell1.PutValue(u"Hello without Non-Breaking Hyphen");
    cell2.PutValue(u"Hello\u2011 with Non-Breaking Hyphen");

    // Autofit the columns
    worksheet.AutoFitColumns();

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.pdf");

    // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
    PdfSaveOptions opts;
    opts.SetIsFontSubstitutionCharGranularity(true);
    workbook.Save(outDir + u"SampleOutput2_out.pdf", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
