---
title: قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على الصور
type: docs
weight: 360
url: /ar/net/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}}

 الرجاء استخدام[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) لتعيين الخط الافتراضي أثناء عرض جداول البيانات على الصور. ستكون هذه الخاصية فعالة فقط عندما يتعذر على الخط الافتراضي للمصنف عرض الأحرف الخاصة بك. الخط الافتراضي المحدد بـ[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) يتم استخدام الخاصية لجميع تلك الخلايا التي تحتوي على خطوط غير صالحة أو غير موجودة.

{{% /alert %}}

## قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على الصور

ينشئ نموذج التعليمات البرمجية التالي مصنفًا ، ويضيف بعض النص في الخلية A4 من ورقة العمل الأولى ، ويعين الخط الخاص به على خط غير صالح أو غير موجود. ثم يأخذ صورتين من ورقة العمل. يتم التقاط الصورة الأولى عن طريق ضبط[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) ملكية ل*ساعي جديد* ويتم التقاط الصورة الثانية عن طريق ضبط[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) ملكية ل*تايمز نيو رومان*.

 هذه هي صورة الإخراج بعد ضبط ملف[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) ملكية ل*ساعي جديد*.

![ما يجب القيام به: image_بديل_نص](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 هذه هي صورة الإخراج بعد ضبط ملف[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) ملكية ل*تايمز نيو رومان*.

![ما يجب القيام به: image_بديل_نص](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## عينة من الرموز

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
