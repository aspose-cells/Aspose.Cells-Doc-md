---
title: قم بتعيين خاصية DefaultFont لـ PdfSaveOptions و ImageOrPrintOptions ليكون لها الأولوية
type: docs
weight: 30
url: /ar/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **سيناريوهات الاستخدام الممكنة**

 أثناء ضبط ملف**الخط الافتراضي** ممتلكات**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** و**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**، قد تتوقع أن يؤدي الحفظ إلى PDF أو الصورة إلى تعيين هذا الخط الافتراضي على كل النص الموجود في مصنف يحتوي على خط مفقود (غير مثبت).

 بشكل عام ، عند الحفظ إلى PDF أو صورة ، سيحاول Aspose.Cells أولاً تعيين الخط الافتراضي في المصنف (على سبيل المثال ، Workbook.DefaultStyle.Font). إذا كان الخط الافتراضي للمصنف لا يزال غير قادر على إظهار / عرض النص بشكل صحيح ، فسيحاول Aspose.Cells التقديم باستخدام الخط المذكور مقابل سمة DefaultFont في**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

لمواكبة توقعاتك ، لدينا خاصية منطقية تسمى "**CheckWorkbookDefaultFont** " في**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . يمكنك ضبطه على**خاطئة**لتعطيل تجربة الخط الافتراضي للمصنف أو السماح بامتداد**الخط الافتراضي** اضبط**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** أن يكون لها الأولوية.

## **قم بتعيين خاصية الخط الافتراضي لـ PdfSaveOptions / ImageOrPrintOptions**

 يفتح نموذج التعليمات البرمجية التالي ملف Excel. تحتوي الخلية A1 (في ورقة العمل الأولى) على نص معين إلى "Christmas Time Font text". اسم الخط هو "Christmas Time Personal Use" غير المثبت على الجهاز. وضعنا***الخط الافتراضي*** سمة من سمات**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** إلى "Times New Roman". وضعنا أيضا**CheckWorkbookDefaultFont** الخاصية المنطقية إلى**"خاطئة"** مما يضمن عرض نص الخلية A1 بخط "Times New Roman" ويجب ألا يستخدم الخط الافتراضي للمصنف ("Calibri" في هذه الحالة). يعرض الكود ورقة العمل الأولى لتنسيقات الصور PNG و TIFF. يتم عرضه أخيرًا بتنسيق ملف PDF.

{{% alert color="primary" %}}

 القيمة الافتراضية لـ***CheckWorkbookDefaultFont*** السمة هي**حقيقي**.

{{% /alert %}}

 هذه هي لقطة شاشة ملف[ملف نموذجي](49446913.xlsx) المستخدمة في رمز المثال.

![ما يجب القيام به: image_بديل_نص](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة الإخراج PNG بعد ضبط ملف**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**الملكية إلى "Times New Roman".

![ما يجب القيام به: image_بديل_نص](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 انظر الإخراج[TIFF](48496672.tiff) الصورة بعد ضبط ملف**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**الملكية إلى "Times New Roman".

انظر الإخراج[PDF](48496673.pdf)ملف بعد ضبط ملف**[PdfSaveOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**الملكية إلى "Times New Roman".

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
