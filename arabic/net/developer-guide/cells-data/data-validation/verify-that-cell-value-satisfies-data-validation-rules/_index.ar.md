---
title: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 210
url: /ar/net/verify-that-cell-value-satisfies-data-validation-rules/
description: تعلم كيفية التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: الحصول على قيمة التحقق للخلية، الحصول على قيمة التحقق للخلية، التأكد مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية
---

{{% alert color="primary" %}} 

تسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى الخلايا. على سبيل المثال، يحدد التحقق العشري أنه يمكن إدخال أرقام فقط بين 10 و 20. إذا قام المستخدم بإدخال رقم مختلف، يعرض Microsoft Excel رسالة خطأ ويطالبه بإدخال رقم في النطاق الصحيح. إذا قام المستخدم بنسخ ولصق رقم، على سبيل المثال 3، في الخلية، لا يقوم Excel بتحقق التحقق أو عرض رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بشكل برمجي. في المثال أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 
## **مقدمة**
يوفر Aspose.Cells الأسلوب [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) للتحقق من قيم الخلية بشكل برمجي. إذا لم تلبي القيمة في الخلية قاعدة التحقق من البيانات المطبقة على تلك الخلية، يعيد **False**، وإلا **True**.

توضح العينة البرمجية التالية كيف يعمل أسلوب [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue). أولاً، يُدخل القيمة 3 في C1. نظرًا لأن هذا الأمر لا يلبي قاعدة التحقق من البيانات، يُعيد أسلوب [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **False**. ثم، يُدخل القيمة 15 في C1. نظرًا لأن هذه القيمة تلبي قاعدة التحقق من البيانات، يُعيد أسلوب [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) **True**. بالمثل، يُعيد **False** للقيمة 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **الناتج**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
