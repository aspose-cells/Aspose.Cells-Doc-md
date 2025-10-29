---
title: التحقق من صحة التوقيع الرقمي لكود VBA باستخدام Golang عبر C++
linktitle: تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا
type: docs
weight: 120
url: /ar/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: تعلم كيفية التحقق من صحة التوقيع الرقمي في كود VBA باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

يسمح Aspose.Cells بالتحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا باستخدام الخاصية [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/). ستُرجع **true** إذا كان التوقيع صالحًا؛ وإذا لم يكن كذلك، فسيُرجع **false**. يصبح التوقيع الرقمي أو رمز VBA غير صالح عند تغيير رمز VBA.

{{% /alert %}}

## **تحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا في C++**

يوضح الكود التالي استخدام هذه الخاصية باستخدام [ملف إكسل النموذجي](5115030.xlsm) الذي يمكنك تنزيله من الرابط المقدم. يحتوي نفس ملف إكسل على توقيع صالح، ولكن عند تعديل رمز VBA الخاص به وحفظ دفتر العمل وإعادة التحقق، نلاحظ أن توقيعه أصبح غير صالح.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
