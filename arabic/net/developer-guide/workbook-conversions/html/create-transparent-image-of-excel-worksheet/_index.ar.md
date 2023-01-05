---
title: قم بإنشاء صورة شفافة لورقة عمل Excel
type: docs
weight: 170
url: /ar/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تحتاج إلى إنشاء صورة ورقة العمل الخاصة بك كصورة شفافة. تريد تطبيق الشفافية على جميع الخلايا التي لا تحتوي على ألوان تعبئة. يوفر Aspose.Cells ملف[**خيارات ImageOrPrint. شفاف**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)لتطبيق الشفافية على صورة ورقة العمل. عندما تكون هذه الخاصية**خاطئة** ، ثم يتم رسم الخلايا التي لا تحتوي على ألوان تعبئة باللون الأبيض وعندما يتم ذلك**حقيقي**، يتم رسم الخلايا التي لا تحتوي على ألوان تعبئة شفافة.

{{% /alert %}} 

في صورة ورقة العمل التالية ، لم يتم تطبيق الشفافية. يتم رسم الخلايا التي لا تحتوي على ألوان تعبئة باللون الأبيض.

|**الإخراج بدون شفافية: خلفية الخلية بيضاء**|
|:- |
|![ما يجب القيام به: image_بديل_نص](create-transparent-image-of-excel-worksheet_1.png)|

بينما ، في صورة ورقة العمل التالية ، تم تطبيق الشفافية. الخلايا التي لا تحتوي على ألوان تعبئة شفافة.

|**الإخراج مع تمكين الشفافية**|
|:- |
|![ما يجب القيام به: image_بديل_نص](create-transparent-image-of-excel-worksheet_2.png)|

يُنشئ نموذج التعليمات البرمجية التالي صورة شفافة من ورقة عمل Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
