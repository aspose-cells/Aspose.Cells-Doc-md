---
title: تحديد مجموعة خطوط فردية أو خاصة لعرض الملف باستخدام C++
linktitle: تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر
type: docs
weight: 40
url: /ar/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: تعلم كيفية تحديد مجموعة خطوط فردية أو خاصة لعرض الملف باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عموماً، تقوم بتحديد مجلد الخطوط أو قائمة الخطوط لجميع ملفات العمل، ولكن أحيانًا، يتعين عليك تحديد مجموعة خطوط فردية أو خاصة لملفات العمل الخاصة بك. يوفر Aspose.Cells فئة [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) التي يمكن استخدامها لتحديد مجموعة الخطوط الفردية أو الخاصة لملف العمل الخاص بك.

## **تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر**

يحمّل رمز المثال التالي ملف إكسل [نموذجي](67338268.xlsx) مع مجموعته الخاصة من الخطوط، والتي تم تحديدها باستخدام فئة [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/). يرجى الاطلاع على [نموذج الخط](67338271.zip) المستخدم داخل الكود بالإضافة إلى [ملف PDF الناتج](67338269.pdf) الذي تم إنشاؤه منه. تُظهر الصورة أدناه كيف يبدو ملف PDF الناتج إذا تم العثور على الخط بنجاح.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
