---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ar/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى إنشاء صورة شفافة لورقة العمل الخاصة بك. تريد تطبيق الشفافية على جميع الخلايا التي لا تحتوي على ألوان تعبئة. يوفر Aspose.Cells للبايثون via .NET الخاصية [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) لتطبيق الشفافية على صورة ورقة العمل. عندما تكون هذه الخاصية **خاطئة**، يتم رسم الخلايا بدون ألوان تعبئة باللون الأبيض، وعندما تكون **صحيح**، تُرسم الخلايا بدون ألوان تعبئة بشكل شفاف.

{{% /alert %}} 

في صورة ورقة العمل التالية، لم يتم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة تُرسم باللون الأبيض.

|**الإخراج بدون شفافية: خلفية الخلية بيضاء**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

بينما، في صورة ورقة العمل التالية، تم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة هي شفافة.

|**الإخراج مع تمكين الشفافية**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

الكود العيني التالي يولِّد صورة شفافة من ورقة عمل Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

