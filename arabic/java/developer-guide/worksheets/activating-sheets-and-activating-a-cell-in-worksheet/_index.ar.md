---
title: تنشيط الأوراق وتفعيل Cell في ورقة العمل
type: docs
weight: 5
url: /ar/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى ورقة عمل محددة لتكون نشطة ويتم عرضها عندما يفتح المستخدم ملف Excel Microsoft في Excel. وبالمثل ، قد ترغب في تنشيط خلية معينة وتعيين أشرطة التمرير لإظهار الخلية النشطة. Aspose.Cells قادر على القيام بكل هذه المهام كما هو موضح أدناه.

-  ان**الورقة النشطة** هي ورقة تعمل عليها: اسم الورقة النشطة في علامة التبويب غامق افتراضيًا.
-  ان**خلية نشطة** هي خلية محددة ، الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. فقط خلية واحدة نشطة في كل مرة. يتم تمييز الخلية النشطة بحد ثقيل.

{{% /alert %}}

## **تنشيط الأوراق وتفعيل Cell**

يوفر Aspose.Cells استدعاءات API محددة لتنشيط جدول وخانة. على سبيل المثال ، ملف[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)الخاصية مفيدة لتعيين الورقة النشطة في مصنف. وبالمثل ، فإن[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)يمكن استخدام الخاصية لتعيين خلية نشطة والحصول عليها في ورقة العمل.

للتأكد من أن أشرطة التمرير الأفقية أو الرأسية موجودة في موضع فهرس الصفوف والأعمدة الذي تريده لإظهار بيانات محددة ، استخدم[**ورقة العمل. FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)و[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)الخصائص.

يوضح المثال التالي كيفية تنشيط ورقة عمل وإنشاء خلية نشطة فيها. يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية. يتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين.

**تعيين خلية B2 كخلية نشطة**

![ما يجب القيام به: image_بديل_نص](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java كود لتعيين ورقة عمل نشطة في Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 في**تقييم** الوضع ، وهذا هو ؛ بدون تعيين ترخيص صالح ، ستكون ورقة العمل النشطة دائمًا هي الورقة التي تحتوي على العلامة المائية للتقييم. لا يمكن تجاوز هذا السلوك إلا من خلال تعيين الترخيص في بداية التطبيق.

{{% /alert %}}
