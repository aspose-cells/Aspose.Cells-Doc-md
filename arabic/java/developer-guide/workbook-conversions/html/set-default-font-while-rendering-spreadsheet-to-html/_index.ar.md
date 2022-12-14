---
title: قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على HTML
type: docs
weight: 830
url: /ar/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells يسمح لك بتعيين الخط الافتراضي أثناء تحويل جدول البيانات إلى HTML. الرجاء استخدام[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)لهذا الغرض. هذه الخاصية مفيدة عندما يكون هناك بعض الخلايا في جدول البيانات التي تحتوي على خطوط غير صالحة أو غير موجودة. ثم سيتم تقديم هذه الخلايا بخط محدد بـ[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) منشأه.

{{% /alert %}} 
## **قم بتعيين الخط الافتراضي أثناء عرض جدول البيانات على HTML**
يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف وإضافة بعض النص في الخلية B4 من ورقة العمل الأولى وتعيين الخط الخاص به إلى خط غير معروف / غير موجود. ثم يحفظ المصنف في HTML عن طريق تعيين أسماء خطوط افتراضية مختلفة مثل Courier New و Arial و Times New Roman وما إلى ذلك.

 تظهر لقطة الشاشة تأثير تعيين أسماء خطوط افتراضية مختلفة عبر[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)منشأه.

![ما يجب القيام به: image_بديل_نص](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 يقوم الرمز بإنشاء ملف[إخراج ملف HTML مع Courier New](5472568) ، ال[إخراج HTML مع Arial](5472567) و ال[إخراج ملف HTML باستخدام Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
