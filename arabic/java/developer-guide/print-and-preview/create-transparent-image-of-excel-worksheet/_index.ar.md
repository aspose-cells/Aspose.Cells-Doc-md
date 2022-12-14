---
title: قم بإنشاء صورة شفافة لورقة عمل Excel
type: docs
weight: 80
url: /ar/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تحتاج إلى إنشاء صورة ورقة العمل الخاصة بك كصورة شفافة. تريد تطبيق الشفافية على جميع الخلايا التي لا تحتوي على ألوان تعبئة. يوفر Aspose.Cells ملف[**ImageOrPrintOptions.setTransparent ()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) لتطبيق الشفافية على صورة ورقة العمل. عندما تكون هذه الخاصية**خاطئة** ، ثم يتم رسم الخلايا التي لا تحتوي على ألوان تعبئة باللون الأبيض وعندما يتم ذلك**حقيقي**، يتم رسم الخلايا التي لا تحتوي على ألوان تعبئة شفافة.

{{% /alert %}}

في صورة ورقة العمل التالية ، لم يتم تطبيق الشفافية. يتم رسم الخلايا التي لا تحتوي على ألوان تعبئة باللون الأبيض.

**صورة ورقة العمل دون تطبيق الشفافية**

![ما يجب القيام به: image_بديل_نص](create-transparent-image-of-excel-worksheet_1.png)

بينما ، في صورة ورقة العمل التالية ، تم تطبيق الشفافية. الخلايا التي لا تحتوي على ألوان تعبئة شفافة.

**صورة ورقة العمل بعد تطبيق الشفافية**

![ما يجب القيام به: image_بديل_نص](create-transparent-image-of-excel-worksheet_2.png)

يمكنك استخدام نموذج التعليمات البرمجية التالي لإنشاء صورة شفافة لورقة عمل Excel الخاصة بك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
