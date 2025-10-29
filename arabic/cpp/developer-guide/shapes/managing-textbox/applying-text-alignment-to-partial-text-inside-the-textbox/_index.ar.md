---
title: كيفية تطبيق/تعيين محاذاة النص لمربع النص باستخدام C++
linktitle: تطبيق / تعيين محاذاة النص لمربع النص
type: docs
weight: 20
url: /ar/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: كيفية تطبيق/تعيين محاذاة النص لمربع النص في Aspose.Cells باستخدام C++.
keywords: تطبيق / تعيين محاذاة مربع النص ورقة البيانات إكسل Aspose
---

يمكن لصناديق النص أن تعزز تعبيرية مستنداتنا ومخططاتنا، وتطبيق محاذاة مختلفة على أجزاء مختلفة من صندوق النص يمكن أن يساعد في تسليط الضوء على نقاط الاهتمام للقراء. لكن المحاذاة الافتراضية لصندوق النص لا تلبي جميع احتياجاتنا. لذلك، قد تحتاج إلى تعديل كل صندوق نص لتحقيق متطلباتك. إذا لم تمتلك الكثير من أدوات صناديق النص للتعديل، أنت محظوظ. وإذا كانت هناك العديد من صناديق النص للتعديل، أعتقد أنك ستواجه مشكلة. لا تقلق الآن، فإن [Aspose.Cells](https://products.aspose.com/cells/) يوفر واجهة برمجة تطبيقات لمساعدتك على القيام بذلك.

يطبق الكود النموذجي التالي تحديد محاذاة النص على مربع نص.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the shapes collection from the first worksheet
    ShapeCollection shapes = workbook.GetWorksheets().Get(0).GetShapes();

    // Add a TextBox to the worksheet
    Shape shape = shapes.AddTextBox(2, 0, 2, 0, 50, 120);

    // Set the text of the TextBox
    shape.SetText(u"This is a test.");

    // Set the horizontal and vertical alignment of the text
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook to the output directory
    workbook.Save(outDir + u"result.xlsx");

    std::cout << "TextBox added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يمكنك أيضًا تغيير محاذاة النص داخل بعض النصوص بداخل شكل صندوق النص باستخدام نص HTML المناسب. يطبق الرمز المساعد التالي محاذاة النص على جزء من النص داخل صندوق النص.

[ملف المصدر](SampleTextboxExcel2016.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleTextboxExcel2016.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output.xlsx";

    // Initialize an object of the Workbook class to load template file
    Workbook sourceWb(inputFilePath);

    // Access the target textbox whose text is to be aligned
    auto sourceTextBox = sourceWb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Create an object of the target workbook
    Workbook destWb;

    // Access first worksheet from the collection
    auto sheet = destWb.GetWorksheets().Get(0);

    // Create new textbox
    TextBox textBox = sheet.GetShapes().AddShape(MsoDrawingType::TextBox, 1, 0, 1, 0, 200, 200);

    // Alternatively text box can be added using following line as well
    // TextBox textBox = sheet.GetShapes().AddTextBox(1, 0, 1, 0, 200, 200);

    // Use Html string from a template file textbox
    textBox.SetHtmlText(sourceTextBox.GetHtmlText());

    // Save the workbook on disc
    destWb.Save(outputFilePath);

    std::cout << "Textbox copied and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
