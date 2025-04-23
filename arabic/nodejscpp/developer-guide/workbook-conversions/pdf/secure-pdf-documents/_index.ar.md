---
title: تأمين مستندات PDF باستخدام Node.js عبر C++
linktitle: مستندات PDF الآمنة
type: docs
weight: 120
url: /ar/nodejs-cpp/secure-pdf-documents/
description: تعلم كيفية تأمين مستندات PDF باستخدام كلمات مرور مالك والمستخدم، وتعيين صلاحيات لملفات PDF باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع ملفات PDF المُشفرة. على سبيل المثال:

- تأمين المستندات بكلمات مرور للمالك والمستخدم حتى لا يمكن لأي شخص فتحه.
- تعيين قيود أو أذونات للمستند بعد فتحه، على سبيل المثال: تقييد ما إذا كان بإمكان محتوى المستند أن يُطبع أو يستخرج.

يشرح هذا المقال كيفية تمرير خيارات أمان PDF عند حفظ الجداول الإلكترونية إلى PDF.

{{% /alert %}}

توفر Aspose.Cells [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) للعمل مع الأمان. يمكنك تعيين كلمات مرور المالك والمستخدم أثناء الحفظ إلى PDF. ستكون كلمة مرور المالك أو كلمة مرور المستخدم مطلوبة لفتح مستند PDF المشفر للمشاهدة.

- يمكن أن تكون كلمة مرور المستخدم فارغة أو سلسلة فارغة؛ في هذه الحالة، لن يُطلب من المستخدم إدخال كلمة مرور عند فتح مستند PDF.
- يتيح فتح مستند PDF بكلمة مرور المالك الصحيحة الوصول الكامل (بدون أي قيود وصول محددة) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور للمستخدم) يسمح بوصول محدود حيث تم تحديد الأذونات.

يصف الكود النموذجي أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

إذا كانت جداول البيانات تحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل عرضها إلى PDF. يضمن هذا إعادة حساب القيم المعتمدة على الصيغ وعرض القيم الصحيحة في PDF.

{{% /alert %}}
