---
title: قم بتعيين خاصية DefaultFont لـ PdfSaveOptions و ImageOrPrintOptions ليكون لها الأولوية
type: docs
weight: 30
url: /ar/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **سيناريوهات الاستخدام الممكنة**

 أثناء ضبط ملف**الخط الافتراضي** ممتلكات[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) و[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) ، قد تتوقع أن يؤدي الحفظ إلى PDF أو الصورة إلى تعيين ذلك**الخط الافتراضي** لكل النص الموجود في المصنف الذي يحتوي على خط مفقود (غير مثبت).

 بشكل عام ، عند الحفظ في PDF أو الصورة ، سيحاول Aspose.Cells أولاً تعيين الخط الافتراضي في المصنف (على سبيل المثال ،[**المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). إذا كان الخط الافتراضي للمصنف لا يزال غير قادر على إظهار / عرض النص بشكل صحيح ، فسيحاول Aspose.Cells التقديم بالخط المذكور مقابل**الخط الافتراضي** السمة في[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

لمواكبة توقعاتك ، لدينا خاصية منطقية تسمى "**CheckWorkbookDefaultFont** " في[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . يمكنك تعيينه على "خطأ" لتعطيل تجربة الخط الافتراضي للمصنف أو السماح بامتداد**الخط الافتراضي** اضبط[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) أن يكون لها الأولوية.

## **قم بتعيين خاصية الخط الافتراضي لـ PdfSaveOptions / ImageOrPrintOptions**

يفتح نموذج التعليمات البرمجية التالي ملف Excel. تحتوي الخلية A1 (في ورقة العمل الأولى) على نص معين إلى "Christmas Time Font text". اسم الخط هو "Christmas Time Personal Use" غير المثبت على الجهاز. وضعنا**الخط الافتراضي**سمة من سمات[**خيارات PdfSave**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)إلى "Times New Roman". وضعنا أيضا**CheckWorkbookDefaultFont**خاصية منطقية لـ "**خاطئة**"الذي يضمن عرض نص الخلية A1 بخط" Times New Roman "ويجب ألا يستخدم الخط الافتراضي للمصنف (" Calibri "في هذه الحالة). يعرض الرمز ورقة العمل الأولى لتنسيقات الصور PNG و TIFF. يتم عرضه أخيرًا بتنسيق ملف PDF.

{{% alert color="primary" %}}

 القيمة الافتراضية لـ***CheckWorkbookDefaultFont*** السمة هي**حقيقي**.

{{% /alert %}}

هذه هي لقطة شاشة ملف[ملف نموذجي](49446914.xlsx)المستخدمة في رمز المثال.

![ما يجب القيام به: image_بديل_نص](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة الإخراج PNG بعد ضبط ملف[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)الملكية إلى "Times New Roman".

![ما يجب القيام به: image_بديل_نص](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

انظر الإخراج[TIFF](out1_imageTIFF.tiff)الصورة بعد ضبط ملف[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)الملكية إلى "Times New Roman".

انظر الإخراج[PDF](out1_pdf.pdf)ملف بعد ضبط ملف[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)الملكية إلى "Times New Roman".

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
