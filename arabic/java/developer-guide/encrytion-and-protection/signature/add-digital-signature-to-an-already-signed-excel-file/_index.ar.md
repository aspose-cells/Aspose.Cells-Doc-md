---
title: أضف التوقيع الرقمي إلى ملف Excel موقع بالفعل
type: docs
weight: 20
url: /ar/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **سيناريوهات الاستخدام الممكنة**

يوفر Aspose.Cells ملف[**Workbook.addDigitalSignature (DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) الطريقة التي يمكنك استخدامها لإضافة توقيع رقمي إلى ملف Excel موقّع بالفعل.

{{% alert color="primary" %}}

يرجى ملاحظة أثناء إضافة توقيع رقمي إلى مستند Excel موقع بالفعل ، إذا كان المستند الأصلي هو مستند تم إنشاؤه بواسطة Aspose.Cells ، فإنه يعمل بشكل جيد. ولكن إذا تم إنشاء المستند الأصلي بواسطة محركات أخرى (مثل Microsoft Excel وما إلى ذلك) ، فلن يتمكن Aspose.Cells من الاحتفاظ بالملف كما هو بعد تحميله وإعادة حفظه ، سيؤدي ذلك إلى جعل التوقيع الأصلي غير صالح.

{{% /alert %}}

## **أضف التوقيع الرقمي إلى ملف Excel موقع بالفعل**

يشرح نموذج التعليمات البرمجية التالي كيفية الاستفادة من[**Workbook.addDigitalSignature (DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) لإضافة توقيع رقمي إلى ملف Excel موقع بالفعل. رجاء تاكد من[نموذج لملف Excel](50528287.xlsx)المستخدمة في هذا الرمز. هذا الملف موقّع رقميًا بالفعل. رجاء تاكد من[إخراج ملف Excel](50528288.xlsx)التي تم إنشاؤها بواسطة الكود. لقد استخدمنا الشهادة التجريبية المسماة[AsposeTest.pfx](50528289.pfx)في هذا الرمز الذي يحتوي على كلمة مرور*أوقف*تُظهر لقطة الشاشة تأثير نموذج التعليمات البرمجية على نموذج ملف Excel بعد التنفيذ.

![ما يجب القيام به: image_بديل_نص](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
