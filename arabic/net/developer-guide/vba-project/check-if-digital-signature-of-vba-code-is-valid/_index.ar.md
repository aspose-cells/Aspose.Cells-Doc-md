---
title: تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا
type: docs
weight: 120
url: /ar/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بالتحقق مما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا باستخدام الخاصية [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned). سيعيد **true** إذا كان التوقيع صالحًا وإلا سيعيد **false**. يصبح التوقيع الرقمي لشيفر آلي VBA غير صالح عند تغيير شيفر آلي VBA.

{{% /alert %}}

## **تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا في C#**

الكود التالي يوضح استخدام هذه الخاصية باستخدام [ملف الإكسل العيني](5115030.xlsm) الذي يمكنك تنزيله من الرابط المُقدم. يحتوي نفس ملف Excel على توقيع صالح ولكن عند تعديل شيفر آلي VBA وحفظ سجل العمل ثم إعادة التحقق ، نجد أن توقيعه أصبح غير صالح.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
{{< app/cells/assistant language="csharp" >}}
