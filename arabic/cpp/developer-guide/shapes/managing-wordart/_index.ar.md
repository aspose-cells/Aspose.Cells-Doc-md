---
title: إضافة علامة مائية WordArt إلى ورقة العمل باستخدام C++
linktitle: إدارة كلمة اللهن
type: docs
weight: 180
url: /ar/cpp/add-wordart-watermark-to-worksheet/
description: تعلم كيفية إضافة علامات مائية WordArt إلى أوراق عمل إكسل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

استخدام كلمة الفن لإضافة تأثيرات نص خاصة إلى جداول البيانات، على سبيل المثال، تمدد عنوان عبر الجزء العلوي من الملف، زينة النص، وجعل النص يتناسب مع شكل محدد مسبقًا، أو تطبيق النص إلى ورقة Excel كعلامة مائية خلفية. تصبح كلمة الفن كائنًا يمكنك نقله أو تحديد موقعه في جداول البيانات لإضافة زخرفة.

{{% /alert %}} 

المثال التالي يوضح كيفية إضافة شكل WordArt لتعيين علامة مائية في الخلفية لورقة العمل.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إضافة نص Word Art بأنماط مدمجة](/cells/ar/cpp/add-word-art-text-with-built-in-styles/)
- [تأمين علامة مائية WordArt](/cells/ar/cpp/locking-wordart-watermark/)
- [تعيين نمط WordArt المحدد مسبقًا لنص الشكل](/cells/ar/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="cpp" >}}
