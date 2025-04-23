---
title: قفل علامة مائية بكلمة فن باستخدام C++
linktitle: قفل علامة الماؤ
type: docs
weight: 170
url: /ar/cpp/locking-wordart-watermark/
description: تعلم كيفية قفل علامات مائية بكلمة فن في ورق عمل إكسل باستخدام Aspose.Cells for C++. منع التحرير، أو الحركة، أو التحديد برمجياً.
---

{{% alert color="primary" %}}

 تتيح واجهات برمجة التطبيقات Aspose.Cells إضافة علامات مائية بكلمة فن على الورقة بطريقة تجعل كلمة الفن ككيان يمكنك تحريكه وتحديد موضعه على الورقة. من الممكن أيضًا قفل كائن كلمة الفن لأي تفاعل مثل التحرير، أو الحركة، أو التحديد. يوضح هذا المقال استخدام طريقة [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) لقفل بعض جوانب العلامة المائية.

{{% /alert %}}

 تتيح واجهات برمجة التطبيقات Aspose.Cells قفل جوانب معينة من العلامة المائية بحيث يمكن تقييد تفاعل المستخدم أو حجبه تمامًا. يوضح مقتطف التعليمات البرمجية التالي استخدام API Aspose.Cells for C++ لقفل التحديد، أو الحركة، أو التحرير، أو إعادة التحجيم للعلامة المائية عن طريق إنشاء ملف بيانات جديد.

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

    // Lock Shape Aspects
    wordart.SetIsLocked(true);
    wordart.SetLockedProperty(ShapeLockType::Selection, true);
    wordart.SetLockedProperty(ShapeLockType::ShapeType, true);
    wordart.SetLockedProperty(ShapeLockType::Move, true);
    wordart.SetLockedProperty(ShapeLockType::Resize, true);
    wordart.SetLockedProperty(ShapeLockType::Text, true);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the color
    wordArtFormat.SetOneColorGradient(Color::Red(), 0.2, GradientStyleType::Horizontal, 2);

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    wordart.SetHasLine(false);

    // Save the file
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
