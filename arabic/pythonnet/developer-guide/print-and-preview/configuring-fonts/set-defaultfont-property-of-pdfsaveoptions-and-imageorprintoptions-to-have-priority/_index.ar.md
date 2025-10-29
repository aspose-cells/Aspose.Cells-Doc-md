---
title: تعيين خاصية DefaultFont في خيارات PdfSave و ImageOrPrint لديها الأولوية
type: docs
weight: 30
url: /ar/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **سيناريوهات الاستخدام المحتملة**

أثناء ضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)، قد تتوقع أن يقوم الحفظ إلى ملف PDF أو صورة بضبط ذلك DefaultFont لجميع النص في مصفوفة العمل الذي يحتوي على خط مفقود (غير مثبت).

بشكل عام، عند الحفظ كملف PDF أو صورة، ستقوم Aspose.Cells لبایتون via .NET بمحاولة تعيين الخط الافتراضي للمصنف (أي، Workbook.DefaultStyle.Font). إذا لم تتمكن من عرض النص بشكل صحيح باستخدام خط العمل الافتراضي، فستحاول Aspose.Cells لبایتون via .NET أن تقوم بالعرض باستخدام الخط المشار إليه في سمات DefaultFont في [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

لتلبية توقعاتك، لدينا خاصية منطقية تسمى "**check_workbook_default_font**" في [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). يمكنك تعيينها إلى **false** لتعطيل محاولة استخدام الخط الافتراضي للمصنف أو إعطاء أولوية لضبطية "**default_font**" في [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

## **تعيين خاصية DefaultFont في خيارات PdfSave/ImageOrPrintOptions**

يفتح الكود النموذجي التالي ملف إكسل. الخلية A1 (في أول ورقة عمل) تحتوي على نص معين وهو "وقت عيد الميلاد نص الخط". اسم الخط هو "عيد الميلاد للاستخدام الشخصي" غير مثبت على الجهاز. قمنا بتعيين سمة ***default_font*** الخاصة في [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) إلى "Times New Roman". كما قمنا بتعيين الخاصية المنطقية **check_workbook_default_font** إلى **"false"** لضمان أن يتم عرض نص الخلية A1 باستخدام خط "Times New Roman" ولا يستخدم الخط الافتراضي للمصنف (الذي هو "Calibri" في هذه الحالة). يقوم الكود برسم الورقة الأولى إلى صيغتي صورة PNG و TIFF. وأخيرًا، يرسم إلى ملف PDF.

{{% alert color="primary" %}}

القيمة الافتراضية لخاصية ***CheckWorkbookDefaultFont*** هي **true**.

{{% /alert %}}

هذه هي صورة الشاشة من [ملف القالب](49446913.xlsx) المستخدم في كود المثال.

![todo:image_alt_text](1.png)

هذه هي صورة الناتج بصيغة PNG بعد ضبط الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) على "Times New Roman".

![todo:image_alt_text](2.png)

انظر الإخراج [TIFF](48496672.tiff) بعد ضبط الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) إلى "تايمز نيو رومان".

انظر الإخراج [PDF](48496673.pdf) بعد ضبط الخاصية [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) إلى "تايمز نيو رومان".

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
