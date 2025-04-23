---
title: تعيين خاصية DefaultFont في خيارات PdfSave و ImageOrPrint لديها الأولوية
type: docs
weight: 30
url: /ar/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **سيناريوهات الاستخدام المحتملة**

أثناء ضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)، قد تتوقع أن يقوم الحفظ إلى ملف PDF أو صورة بضبط ذلك DefaultFont لجميع النص في مصفوفة العمل الذي يحتوي على خط مفقود (غير مثبت).

بشكل عام، عند الحفظ إلى PDF أو صورة، سيحاول Aspose.Cells أولاً ضبط الخط الافتراضي للمصفوفة العمل (أي، Workbook.DefaultStyle.Font). إذا لم يتمكن الخط الافتراضي للمصفوفة العمل من إظهار/تقديم النص بشكل صحيح، فسيحاول Aspose.Cells تقديمه بالخط الذي ذُكر ضده في السمة DefaultFont في [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

للتعامل مع توقعاتك، لدينا خاصية بولية تسمى "**CheckWorkbookDefaultFont**" في [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). يمكنك ضبطها على **false** لتعطيل محاولة الخط الافتراضي للمصفوفة العمل أو ترك الإعداد **DefaultFont** في [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) ليكون له الأولوية.

## **تعيين خاصية DefaultFont في خيارات PdfSave/ImageOrPrintOptions**

يفتح الكود العيني العيني التالي ملف Excel. الخلية A1 (في الورقة العمل الأولى) يحتوي على نص مضبوط إلى "نص خط زمن الكريسماس". اسم الخط هو "خط زمن الكريسماس الشخصي" الذي لا يتم تثبيته على الجهاز. نضبط سمة ***DefaultFont*** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) إلى "تايمز نيو رومان". نضبط أيضًا خاصية البولية **CheckWorkbookDefaultFont** على **"false"** مما يضمن أن نص الخلية A1 يتم تقديمه بخط "تايمز نيو رومان" ويجب أن لا يستخدم الخط الافتراضي للمصفوفة العمل ("كاليبري" في هذه الحالة). يقوم الكود بتقديم الورقة العمل الأولى إلى تنسيقات الصورة PNG وTIFF. يقوم أخيرًا بالتقديم إلى تنسيق ملف PDF.

{{% alert color="primary" %}}

القيمة الافتراضية لخاصية ***CheckWorkbookDefaultFont*** هي **true**.

{{% /alert %}}

هذه هي صورة الشاشة من [ملف القالب](49446913.xlsx) المستخدم في كود المثال.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة الناتج بصيغة PNG بعد ضبط الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) على "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

انظر الإخراج [TIFF](48496672.tiff) بعد ضبط الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) إلى "تايمز نيو رومان".

انظر الإخراج [PDF](48496673.pdf) بعد ضبط الخاصية [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) إلى "تايمز نيو رومان".

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
{{< app/cells/assistant language="csharp" >}}
