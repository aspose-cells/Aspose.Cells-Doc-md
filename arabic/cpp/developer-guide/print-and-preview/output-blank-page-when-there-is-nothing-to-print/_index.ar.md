---  
title: إخراج صفحة فارغة عندما لا يوجد شيء للطباعة باستخدام C++  
linktitle: إخراج صفحة فارغة عند عدم وجود شيء للطباعة  
type: docs  
weight: 90  
url: /ar/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: التعامل مع أوراق العمل الفارغة وطباعة صفحات فارغة باستخدام Aspose.Cells مع C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

إذا كانت الورقة فارغة، فإن Aspose.Cells لن تطبع شيئًا عند تصدير ورقة العمل إلى صورة. يمكنك تغيير هذا السلوك باستخدام خاصية [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/). عند تعيينها **true**، سيتم طباعة الصفحة الفارغة.  

## **إخراج صفحة فارغة عند عدم وجود شيء للطباعة**  

يخلق رمز المثال التالي ملف عمل فارغ يحتوي على ورقة عمل فارغة ويعرض ورقة العمل الفارغة كصورة بعد تعيين الخاصية [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) على أنها **true**. ونتيجة لذلك، فإنه يتم إنشاء صفحة فارغة حيث لا يوجد شيء للطباعة والذي يمكنك رؤيته في الصورة أدناه.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **الكود المثالي**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
