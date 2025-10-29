---
title: تغيير تباعد الحروف لنص في مربع نص أو شكل في إكسل باستخدام C++
linktitle: تغيير تباعد الأحرف لصندوق النص أو الشكل في Excel
type: docs
weight: 280
url: /ar/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: تعلم كيفية تغيير تباعد الحروف لمربع نص أو شكل في إكسل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يمكنك تغيير تباعد الحروف في مربع نص أو شكل باستخدام الخاصية [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/).

{{% /alert %}}

يعتمد الرمز النموذجي التالي على تغيير تباعد الأحرف في مربع نص في ملف إكسل إلى نقطة 4 ثم يحفظه على القرص.

```c++
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

    // Load your excel file inside a workbook object
    Workbook wb(srcDir + u"sampleChangeTextBoxOrShapeCharacterSpacing.xlsx");

    // Access your text box which is also a shape object from shapes collection
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Access the first font setting object via GetCharacters() method
    FontSetting fs = shape.GetRichFormattings()[0];

    // Set the character spacing to point 4
    fs.GetTextOptions().SetSpacing(4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputChangeTextBoxOrShapeCharacterSpacing.xlsx", SaveFormat::Xlsx);

    std::cout << "Character spacing changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
