---
title: نطاق تصدير Cells في ورقة عمل إلى صورة
type: docs
weight: 130
url: /ar/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

يمكنك عمل صورة لورقة عمل باستخدام Aspose.Cells. ومع ذلك ، في بعض الأحيان تحتاج فقط إلى تصدير نطاق من الخلايا في ورقة عمل إلى صورة. تشرح هذه المقالة كيفية تحقيق ذلك.

{{% /alert %}}

 لالتقاط صورة لنطاق ، اضبط منطقة الطباعة على النطاق المطلوب ثم اضبط جميع الهوامش على 0. قم أيضًا بتعيين[**ImageOrPrintOptions.setOnePagePerSheet ()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) إلى**حقيقي**.

يأخذ الكود التالي صورة للنطاق E8: H10. يوجد أدناه لقطة شاشة للمصنف المصدر المستخدم في التعليمات البرمجية. يمكنك تجربة الكود مع أي مصنف.

**ملف الإدخال**

![ما يجب القيام به: image_بديل_نص](export-range-of-cells-in-a-worksheet-to-image_1.png)

يؤدي تنفيذ الكود إلى إنشاء صورة للنطاق من E8: H10 فقط.

**صورة الإخراج**

![ما يجب القيام به: image_بديل_نص](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 قد تجد أيضا المقال[تحويل ورقة العمل إلى تنسيقات صور مختلفة](/cells/ar/java/converting-worksheet-to-different-image-formats/) معاون، مساعد، مفيد، فاعل خير.
