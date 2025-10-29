---
title: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 210
url: /ar/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: تعرف على كيفية التحقق من أن قيمة الخلية تلبي قواعد التحقق من البيانات من خلال واجهة برمجة التطبيقات Aspose.Cells للبايثون via .NET..
keywords: مكتبة Excel بلغة البايثون، الحصول على قيمة التحقق من الخلية بلغة البايثون، الحصول على قيمة التحقق من الخلية بلغة البايثون، التحقق ما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بلغة البايثون.
---

{{% alert color="primary" %}} 

تسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى الخلايا. على سبيل المثال، يحدد التحقق العشري أنه يمكن إدخال أرقام فقط بين 10 و 20. إذا قام المستخدم بإدخال رقم مختلف، يعرض Microsoft Excel رسالة خطأ ويطالبه بإدخال رقم في النطاق الصحيح. إذا قام المستخدم بنسخ ولصق رقم، على سبيل المثال 3، في الخلية، لا يقوم Excel بتحقق التحقق أو عرض رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بشكل برمجي. في المثال أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 
## **مقدمة**
يوفر Aspose.Cells للبايثون via .NET الطريقة [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) للتحقق من قيم الخلية بشكل برمجي. إذا لم تلبي القيمة في الخلية قاعدة التحقق من البيانات المطبقة على تلك الخلية، فإنه يعيد **False**، وإلا **True**.

توضح الشيفة البرمجية العينة التالية كيف تعمل طريقة [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#). أولًا، يُدخل القيمة 3 في C1. لأن هذا لا يلبي قاعدة التحقق من البيانات، فإن طريقة [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) تعيد **False**. ثم، يُدخل القيمة 15 في C1. لأن هذه القيمة تلبي قاعدة التحقق من البيانات، فإن طريقة [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) تعيد **True**. وبالمثل، تعيد **False** للقيمة 30.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **الناتج**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
