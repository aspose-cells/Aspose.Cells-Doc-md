---
title: تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا
type: docs
weight: 120
url: /ar/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

يتيح Aspose.Cells لبايثون via .NET التحقق من صحة التوقيع الرقمي لشيفرة VBA باستخدام الخاصية [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed). سترجع **true** إذا كان التوقيع صالحًا، وإلا سترجع **false**. يصبح التوقيع الرقمي لشيفرة VBA غير صالح عند تعديل الكود.

{{% /alert %}}

## **تحقق مما إذا كان التوقيع الرقمي لشيفرة VBA صالحًا في بايثون**

الكود التالي يوضح استخدام هذه الخاصية باستخدام [ملف الإكسل العيني](5115030.xlsm) الذي يمكنك تنزيله من الرابط المُقدم. يحتوي نفس ملف Excel على توقيع صالح ولكن عند تعديل شيفر آلي VBA وحفظ سجل العمل ثم إعادة التحقق ، نجد أن توقيعه أصبح غير صالح.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

