---
title: تحويل ملف XLSX إلى صيغة PDF باستخدام C++
linktitle: تحويل ملف XLSX إلى تنسيق PDF
type: docs
weight: 30
url: /ar/cpp/convert-xlsx-file-to-pdf-format/
description: تعلم كيفية تحويل ملفات Excel إلى صيغة PDF باستخدام Aspose.Cells for C++ بدقة وموثوقية عالية.
---

{{% alert color="primary" %}}

يمثّل PDF (الصيغة المحمولة للوثائق) المستندات بشكل مستقل عن البرنامج والأجهزة أو نظام التشغيل المستخدم لإنشاء تلك المستندات. يمكن أن يحتوي ملف PDF على أي مزيج من النص، والرسومات، والصور بطريقة غير مرتبِطة بجهاز معين ودون اعتماد على الدقة. غالبًا ما تكون ملفات PDF مضغوطة، مما يقلل من حجمها مقارنة بالملف الأصلي.

في بعض الأحيان، تحتاج إلى تحويل ملف Microsoft Excel إلى PDF. لهذا، تحتاج إلى حل سريع وآمن ودقيق وموثوق يسمح لك بتوزيع مستندات PDF حول العالم. هناك العديد من أدوات التحويل التي يمكن أن تؤدي هذه المهمة. ولكن يجب التأكد من أن تنسيق المستند الأصلي في Excel يُحتفظ به في ملف PDF الناتج. يجب أن يتم عرض الصور، والمخططات، والأشكال، وتنسيقات البيانات، والخطوط، والسمات، والألوان، وإعدادات الصفحة، واتجاه النص، والحدود، والمخططات وغيرها بدقة وبدقة عالية. [Aspose.Cells](https://products.aspose.com/cells/cpp/) يضمن تحويل عالي الجودة.

تم تصميم هذا المستند لتوفير فهم شامل لكيفية تحويل مستند Microsoft Excel (الذي يحتوي على صور، ومخططات، وتنسيقات، وما إلى ذلك) إلى PDF. لتحقيق ذلك، يُوضح كيفية إنشاء تطبيق وحدة تحكم بسيط في C++ لتحويل ملف Excel إلى PDF باستخدام API الخاص بـ Aspose.Cells. يتم تنفيذ التحويل بدقة عالية وبدقة متناهية.

{{% /alert %}}

## **تحويل Excel إلى PDF**

يستخدم هذا المثال ملف Excel (SampleInput.xlsx) كنموذج. يحتوي دفتر العمل على أوراق عمل مع مخططات وصور. كل ورقة تحتوي على أنواع مختلفة من التنسيقات باستخدام الخطوط والصفات والألوان وتأثيرات التظليل والحدود. توجد مخطط عمود على الورقة الأولى وصورة في الأخيرة.

### **ملف Excel القالب**

يحتوي ملف النموذج على ثلاث أوراق عمل، بما في ذلك المخططات والصور كميديا. تحتوي الورقة الأولى على مخططات، والأخيرة تحتوي على صورة، كما هو موضح في لقطات الشاشة أدناه.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|الورقة العمل الأولى **(توقعات المبيعات)**|الورقة العمل الثانية **(تقرير المبيعات)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|الصفحة العملية الثالثة **(ادخال البيانات)**|الصفحة العملية الأخيرة **(الصورة)**|

### **عملية التحويل**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

إذا احتوى جدول البيانات على صيغ، فمن الأفضل استدعاء طريقة [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل تصيير جدول البيانات إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ بشكل صحيح، وعرض القيم الصحيحة في PDF.

{{% /alert %}}

### **النتيجة**

عند تشغيل الرمز أعلاه، يتم إنشاء ملف PDF في مجلد Files في دليل التطبيق الخاص بك.
توضح اللقطات الشاشة التالية صفحات ملف PDF. يرجى ملاحظة أن الهوامش العلوية والسفلية محتفظ بها أيضًا في ملف PDF الناتج.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|الورقة العمل الأولى **(توقعات المبيعات)**|الورقة العمل الثانية **(تقرير المبيعات)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|الصفحة العملية الثالثة **(ادخال البيانات)**|الصفحة العملية الأخيرة **(الصورة)**|
{{< app/cells/assistant language="cpp" >}}
