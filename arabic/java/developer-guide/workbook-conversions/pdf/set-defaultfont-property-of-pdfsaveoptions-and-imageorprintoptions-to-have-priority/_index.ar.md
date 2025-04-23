---
title: تعيين خاصية DefaultFont في خيارات PdfSave و ImageOrPrint لديها الأولوية
type: docs
weight: 30
url: /ar/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **سيناريوهات الاستخدام المحتملة**

أثناء تعيين خاصية DefaultFont لـ**[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)** و**[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**، قد تتوقع أن يقوم الحفظ إلى PDF أو الصورة بتعيين تلك **DefaultFont** إلى جميع النصوص في السجل الحسابي التي تحتوي على خطوط غير مثبتة.

عموماً، عند الحفظ إلى PDF أو صورة، سيحاول Aspose.Cells أولاً تعيين الخط الافتراضي للمصنف (أي، [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font-)). إذا لم يتمكن الخط الافتراضي للمصنف من عرض النص بشكل صحيح، فسيحاول Aspose.Cells عرض النص باستخدام الخط المذكور في خاصية **DefaultFont** في [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

لتعامل مع توقعاتك، لدينا خاصية Boolean تسمى "**CheckWorkbookDefaultFont**" في **[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)** / **[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**. يمكنك تعيينها على القيمة البولية لتعطيل محاولة الخط الافتراضي للسجل الحسابي أو السماح لإعداد **DefaultFont** في **[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)** / **[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** بالأولوية.

## **تعيين خاصية DefaultFont في خيارات PdfSave/ImageOrPrintOptions**

يفتح الكود العيني التالي ملف Excel. الخلية A1 (في الورقة الحسابية الأولى) بها نص محدد ليكون "كلمة أوقات عيد الميلاد". اسم الخط هو "كريسماس تايم شخصي" الذي لم يتم تثبيته على الجهاز. نقوم بتعيين سمة **DefaultFont** لـ**[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)** / **[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** إلى "Times New Roman". نقوم أيضًا بتعيين خاصية Boolean **CheckWorkbookDefaultFont** إلى "**false**" والتي تضمن أن يتم عرض نص الخلية A1 بخط "Times New Roman" ويجب ألا يستخدم الخط الافتراضي للورقة الحسابية ("Calibri" في هذه الحالة). يقوم الكود بعرض الورقة الحسابية الأولى إلى تنسيقات الصور PNG و TIFF. وأخيرًا، يقوم بالحفظ إلى تنسيق ملف PDF.

{{% alert color="primary" %}}

القيمة الافتراضية لخاصية ***CheckWorkbookDefaultFont*** هي **true**.

{{% /alert %}}

هذه هي لقطة شاشة لملف القالب المستخدم في كود المثال.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة الناتج بصيغة PNG بعد ضبط الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) على "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

راجع صورة [TIFF] الناتجة (out1_imageTIFF.tiff) بعد ضبط الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) على "Times New Roman".

راجع ملف [PDF] الناتج (out1_pdf.pdf) بعد ضبط الخاصية [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) على "Times New Roman".

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
