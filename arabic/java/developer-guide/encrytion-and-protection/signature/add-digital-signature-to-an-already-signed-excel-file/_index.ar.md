---
title: إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل
type: docs
weight: 20
url: /ar/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells الطريقة [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) التي يمكنك استخدامها لإضافة توقيع رقمي إلى ملف Excel موقعًا مسبقًا.

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إضافة توقيع رقمي إلى مستند إكسل تم توقيعه بالفعل، إذا كان المستند الأصلي هو وثيقة تم إنشاؤها بواسطة Aspose.Cells، سيعمل بشكل جيد. ولكن إذا كان المستند الأصلي قد تم إنشاؤه بواسطة محركات أخرى (مثل Microsoft Excel وما إلى ذلك)، فإن Aspose.Cells لن تتمكن من الحفاظ على الوثيقة بعد التحميل وإعادة حفظها، وهذا سيجعل التوقيع الأصلي غير صالح.

{{% /alert %}}

## **إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل**

يوضح الرمز النموذجي التالي كيفية الاستفادة من الطريقة [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) لإضافة توقيع رقمي إلى ملف Excel موقعًا مسبقًا. يرجى التحقق من [ملف Excel النموذجي](50528287.xlsx) المستخدم في هذا الرمز. تم توقيع هذا الملف رقميًا بالفعل. يرجى التحقق من [ملف Excel الناتج](50528288.xlsx) الذي تم إنشاؤه من خلال الرمز. لقد استخدمنا شهادة العرض التوضيحي المسماة [AsposeTest.pfx](50528289.pfx) في هذا الرمز والتي تحتوي على كلمة مرور *aspose*. تظهر اللقطة الشاشية تأثير الرمز النموذجي على ملف Excel النموذجي بعد التنفيذ.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
