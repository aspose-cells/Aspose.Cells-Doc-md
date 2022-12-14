---
title: قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على الصور
type: docs
weight: 840
url: /ar/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

 الرجاء استخدام[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) لتعيين الخط الافتراضي أثناء عرض جدول البيانات على الصور. لن تكون هذه الخاصية فعالة إلا عندما يتعذر على الخط الافتراضي للمصنف عرض الأحرف الخاصة بك. الخط الافتراضي المحدد بـ[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) يتم استخدام الخاصية لجميع تلك الخلايا التي تحتوي على خطوط غير صالحة أو غير موجودة.

{{% /alert %}} 
## **قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على الصور**
يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف ، ويضيف بعض النص في الخلية A4 من ورقة العمل الأولى ويعين الخط الخاص به على خط غير صالح أو غير موجود. ثم يأخذ صورتين من ورقة العمل. يتم التقاط الصورة الأولى عن طريق ضبط[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الملكية ل*ساعي جديد* ويتم التقاط الصورة الثانية عن طريق ضبط[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الملكية ل*تايمز نيو رومان*.

 هذه هي صورة الإخراج بعد ضبط ملف[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الملكية ل*ساعي جديد*.

![ما يجب القيام به: image_بديل_نص](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 هذه هي صورة الإخراج بعد ضبط ملف[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الملكية ل*تايمز نيو رومان*.

![ما يجب القيام به: image_بديل_نص](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
