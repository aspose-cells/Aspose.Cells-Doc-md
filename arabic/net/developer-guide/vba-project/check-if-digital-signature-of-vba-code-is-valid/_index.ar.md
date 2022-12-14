---
title: تحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا
type: docs
weight: 120
url: /ar/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 يسمح لك Aspose.Cells بالتحقق مما إذا كان التوقيع الرقمي لكود VBA صالحًا باستخدام امتداد[**المصنف. VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) منشأه. سوف يعود**حقيقي** إذا كان التوقيع ساري المفعول وإلا سيعود**خاطئة**. يصبح التوقيع الرقمي لرمز VBA غير صالح عند تغيير رمز VBA.

{{% /alert %}}

## **تحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا في C#**

 يوضح الكود التالي استخدام هذه الخاصية باستخدام[نموذج ملف اكسل](5115030.xlsm)والتي يمكنك تنزيلها من الرابط المقدم. يحتوي ملف Excel نفسه على توقيع صالح ولكن عندما نقوم بتعديل كود VBA الخاص به وحفظ المصنف ثم إعادة التحقق ، نجد أن توقيعه أصبح غير صالح.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
