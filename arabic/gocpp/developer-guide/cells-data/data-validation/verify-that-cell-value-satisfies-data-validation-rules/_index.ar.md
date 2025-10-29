---
title: التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات باستخدام Golang عبر C++
linktitle: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 210
url: /ar/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: تعلم كيفية التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات من خلال واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: الحصول على قيمة التحقق للخلية، الحصول على قيمة التحقق للخلية، التأكد مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى الخلايا. على سبيل المثال، تحدد التحقق العشري أن يتم إدخال أرقام بين 10 و20 فقط. إذا أدخل المستخدم رقمًا مختلفًا، يظهر Excel رسالة خطأ ويطالب بإدخال رقم في النطاق الصحيح. إذا نسخ ولصق رقم، مثل 3، في الخلية، فإن Excel لا يجري فحص تحقق أو يعرض رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بشكل برمجي. في المثال أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 

## **مقدمة**
 توفر Aspose.Cells طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) للتحقق من صحة قيم الخليّة برمجيًا. إذا كانت القيمة في خلية لا تلبي قاعدة التحقق من البيانات المطبقة على تلك الخلية، فإنه يُرجع **False**، وإذا كانت كذلك يُرجع **True**.

 يوضح رمز العينة التالي كيفية عمل طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/). أولاً، يدخل القيمة 3 في C1. نظرًا لعدم تلبيتها لقاعدة التحقق من البيانات، فإن طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) تُرجع **False**. ثم، يدخل القيمة 15 في C1. نظرًا لأنها تفي بقاعدة التحقق من البيانات، فإن طريقة [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) تُرجع **True**. بالمثل، تُرجع **False** للقيمة 30.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **الناتج**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
