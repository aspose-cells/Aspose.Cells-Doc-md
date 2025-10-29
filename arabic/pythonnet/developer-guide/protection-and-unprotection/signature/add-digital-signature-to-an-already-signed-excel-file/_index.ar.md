---
title: إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل
type: docs
weight: 20
url: /ar/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: تصف هذه المقالة كيفية إضافة توقيع رقمي إلى ملف إكسل موقع مسبقًا باستخدام رموز C# مع Aspose.Cells for Python via .NET.
keywords: إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا، كيفية إضافة توقيع رقمي إلى مستند Excel تم توقيعه مسبقًا.
---

## **سيناريوهات الاستخدام المحتملة**

يوفر Aspose.Cells for Python via .NET الطريقة [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) التي يمكنك استخدامها لإضافة توقيع رقمي إلى ملف إكسل موقع مسبقًا.

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إضافة توقيع رقمي إلى مستند إكسل موقع مسبقًا، إذا كان المستند الأصلي الناتج عن Aspose.Cells for Python via .NET، فإنه يعمل بشكل جيد. لكن إذا تم إنشاء المستند الأصلي بواسطة محركات أخرى (مثل Microsoft Excel وغيرها)، لا يمكن لـ Aspose.Cells for Python via .NET الحفاظ على استمرارية الملف بعد التحميل وإعادة الحفظ، مما يجعل التوقيع الأصلي غير صالح.

{{% /alert %}}

## **كيفية إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا**

يوضح مقتطفات الكود التالية كيفية استخدام أسلوب [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) لإضافة توقيع رقمي إلى ملف إكسل موقع مسبقًا. يرجى التحقق من [ملف إكسل نموذجي](50528280.xlsx) المستخدم في هذا الكود. هذا الملف موقع مسبقًا بالفعل. يرجى التحقق من [ملف إكسل الناتج](50528281.xlsx) الذي تم إنشاؤه بواسطة الكود. لقد استخدمنا شهادة العرض الديمو المُسماة [AsposeDemo.pfx](50528279.pfx) في هذا الكود ولديها كلمة مرور **aspose**. توضح اللقطة الشاشية تأثير الكود النموذجي على ملف إكسل النموذجي بعد التنفيذ.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
