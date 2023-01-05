---
title: قم بتعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى HTML
type: docs
weight: 370
url: /ar/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 يسمح لك Aspose.Cells بتعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى HTML. الرجاء استخدام[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) لهذا الغرض. هذه الخاصية مفيدة عندما يكون هناك بعض الخلايا في جدول البيانات التي تحتوي على خطوط غير صالحة أو غير موجودة. ثم سيتم عرض هذه الخلايا بخط محدد بامتداد[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) خاصية.

{{% /alert %}}

## قم بتعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى HTML

يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف وإضافة بعض النص في الخلية B4 من ورقة العمل الأولى وتعيين الخط الخاص به إلى خط غير معروف / غير موجود. ثم يحفظ المصنف في HTML عن طريق تعيين أسماء خطوط افتراضية مختلفة مثل Courier New و Arial و Times New Roman وما إلى ذلك.

 تظهر لقطة الشاشة تأثير تعيين أسماء خطوط افتراضية مختلفة عبر[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)خاصية.

![ما يجب القيام به: image_بديل_نص](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 يقوم الرمز بإنشاء ملف[إخراج ملف HTML مع Courier New](5115516) ، ال[الإخراج HTML مع Arial](5115518) ، و ال[إخراج ملف HTML باستخدام Times New Roman](5115517).

## عينة من الرموز

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
