---
title: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 210
url: /ar/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: تعلم كيفية التحقق مما إذا كانت قيمة الخلية تفي بقواعد التحقق من البيانات عبر واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: الحصول على قيمة التحقق من صحة الخلية عبر Node.js باستخدام C++، التحقق مما إذا كانت قيمة تفي بقواعد التحقق من البيانات المطبقة على الخلية باستخدام Node.js عبر C++
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى الخلايا. على سبيل المثال، تحدد التحقق العشري أن يتم إدخال أرقام بين 10 و20 فقط. إذا أدخل المستخدم رقمًا مختلفًا، يظهر Excel رسالة خطأ ويطالب بإدخال رقم في النطاق الصحيح. إذا نسخ ولصق رقم، مثل 3، في الخلية، فإن Excel لا يجري فحص تحقق أو يعرض رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بشكل برمجي. في المثال أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 
## **مقدمة**
توفر Aspose.Cells for Node.js via C++ طريقة [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) للتحقق من صحة قيم الخلايا برمجياً. إذا كانت قيمة في خلية لا تفي بقواعد التحقق من البيانات المطبقة على تلك الخلية، فإنه يُرجع **false**، وإلا يُرجع **true**.

يوضح كود العينة التالي كيف تعمل طريقة [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--). أولاً، يدخل القيمة 3 في C1. نظرًا لأنها لا تفي بقواعد التحقق من البيانات، فإن طريقة [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) تُرجع **false**. ثم، يُدخل القيمة 15 في C1. نظرًا لأنها تفي بقواعد التحقق من البيانات، فإن الطريقة تُرجع **true**. بالمثل، تُرجع **false** للقيمة 30.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **الناتج**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
