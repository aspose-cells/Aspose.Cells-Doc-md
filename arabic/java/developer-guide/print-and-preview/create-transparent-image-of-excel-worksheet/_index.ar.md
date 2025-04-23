---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /ar/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى إنشاء صورة لورقة العمل الخاصة بك كصورة شفافة. ترغب في تطبيق الشفافية على جميع الخلايا التي لا تحتوي على ألوان ملء. يوفر Aspose.Cells خاصية [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) لتطبيق الشفافية على صورة الورقة العمل. عندما تكون هذه الخاصية **false**، يتم رسم الخلايا التي لا تحتوي على ألوان ملء بلون أبيض وعندما تكون **true**، يتم رسم الخلايا التي لا تحتوي على ألوان ملء كمعتمدات.

{{% /alert %}}

في صورة ورقة العمل التالية، لم يتم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة تُرسم باللون الأبيض.

**صورة لورقة العمل بدون تطبيق الشفافية**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

بينما، في صورة ورقة العمل التالية، تم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة هي شفافة.

**صورة لورقة العمل بعد تطبيق الشفافية**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

يمكنك استخدام الكود المثال التالي لإنشاء صورة شفافة لورقة عمل Excel الخاصة بك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
