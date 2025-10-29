---
title: تعيين خاصية DefaultFont من خيارات الحفظ PdfSaveOptions و ImageOrPrintOptions لتكون لها أولوية مع C++
linktitle: تعيين خاصية DefaultFont في خيارات PdfSave و ImageOrPrint لديها الأولوية
type: docs
weight: 30
url: /ar/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: تعلم كيفية إعطاء أولوية لإعدادات الخط عند حفظ المستندات باستخدام Aspose.Cells في C++.
---

## **سيناريوهات الاستخدام المحتملة**

أثناء ضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)، قد تتوقع أن يقوم الحفظ إلى ملف PDF أو صورة بضبط ذلك DefaultFont لجميع النص في مصفوفة العمل الذي يحتوي على خط مفقود (غير مثبت).

 بشكل عام، عند الحفظ بصيغة PDF أو صورة، ستحاول Aspose.Cells أولاً تعيين الخط الافتراضي لمصنَّف العمل (أي، Workbook.DefaultStyle.Font). إذا لم يكن بالإمكان عرض النص بشكل صحيح، فستحاول Aspose.Cells استخدام الخط المذكور مقابل خاصية DefaultFont في [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

لتلبية توقعاتك، لدينا خاصية بوليانية تسمى "**CheckWorkbookDefaultFont**" في [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). يمكنك تعيينها إلى **false** لتعطيل تجربة الخط الافتراضي للمصنَّف أو السماح لإعداد **DefaultFont** في [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) للحصول على الأولوية.

## **تعيين خاصية DefaultFont في خيارات PdfSave/ImageOrPrintOptions**

يفتح رمز النموذج التالي ملف Excel. الخلية A1 في ورقة العمل الأولى تحتوي على نص مضبط ليكون "نص خط وقت عيد الميلاد". اسم الخط هو "Christmas Time Personal Use" غير مثبت على الجهاز. نقوم بضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) إلى "Times New Roman". ونضبط الخاصية **CheckWorkbookDefaultFont** إلى **"false"** لضمان عرض نص الخلية A1 باستخدام خط "Times New Roman" وعدم استخدام الخط الافتراضي للملف ("Calibri" في هذه الحالة). يقوم الكود بعرض ورقة العمل الأولى بصيغة PNG و TIFF، وأخيرًا بصيغة ملف PDF.

{{% alert color="primary" %}}

القيمة الافتراضية لخاصية **CheckWorkbookDefaultFont** هي **true**.

{{% /alert %}}

هذه هي صورة الشاشة من [ملف القالب](49446913.xlsx) المستخدم في كود المثال.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة PNG الناتجة بعد ضبط الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) على "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

انظر الصورة [TIFF](48496672.tiff) الناتجة بعد ضبط الخاصية [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) على "Times New Roman".

راجع ملف [PDF](48496673.pdf) الناتج بعد تعيين خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) إلى "Times New Roman".

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
