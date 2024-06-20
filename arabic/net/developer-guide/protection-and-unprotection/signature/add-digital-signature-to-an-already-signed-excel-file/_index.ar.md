---
title: إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل
type: docs
weight: 20
url: /ar/net/add-digital-signature-to-an-already-signed-excel-file/
description: يصف هذا المقال كيفية إضافة توقيع رقمي إلى ملف Excel موقع مسبقًا باستخدام رموز C# مع Aspose.Cells for .Net.
keywords: إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا، كيفية إضافة توقيع رقمي إلى مستند Excel تم توقيعه مسبقًا.
---

## **سيناريوهات الاستخدام المحتملة**

Aspose.Cells توفر أسلوب [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) الذي يمكنك استخدامه لإضافة توقيع رقمي إلى ملف إكسل موقع مسبقًا.

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إضافة توقيع رقمي إلى مستند إكسل تم توقيعه بالفعل، إذا كان المستند الأصلي هو وثيقة تم إنشاؤها بواسطة Aspose.Cells، سيعمل بشكل جيد. ولكن إذا كان المستند الأصلي قد تم إنشاؤه بواسطة محركات أخرى (مثل Microsoft Excel وما إلى ذلك)، فإن Aspose.Cells لن تتمكن من الحفاظ على الوثيقة بعد التحميل وإعادة حفظها، وهذا سيجعل التوقيع الأصلي غير صالح.

{{% /alert %}}

## **كيفية إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا**

يوضح مقتطفات الكود التالية كيفية استخدام أسلوب [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) لإضافة توقيع رقمي إلى ملف إكسل موقع مسبقًا. يرجى التحقق من [ملف إكسل نموذجي](50528280.xlsx) المستخدم في هذا الكود. هذا الملف موقع مسبقًا بالفعل. يرجى التحقق من [ملف إكسل الناتج](50528281.xlsx) الذي تم إنشاؤه بواسطة الكود. لقد استخدمنا شهادة العرض الديمو المُسماة [AsposeDemo.pfx](50528279.pfx) في هذا الكود ولديها كلمة مرور **aspose**. توضح اللقطة الشاشية تأثير الكود النموذجي على ملف إكسل النموذجي بعد التنفيذ.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
