---
title: تحقق من أن Cell القيمة تلبي قواعد التحقق من صحة البيانات
type: docs
weight: 210
url: /ar/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft يسمح Excel للمستخدمين بإضافة قواعد التحقق من صحة البيانات إلى الخلايا. على سبيل المثال ، يحدد التحقق العشري أنه يمكن إدخال الأرقام بين 10 و 20 فقط. إذا قام المستخدم بإدخال رقم مختلف. يظهر Microsoft Excel رسالة خطأ ويطلب منهم إدخال رقم في النطاق الصحيح. إذا قمت بنسخ رقم ولصقه ، على سبيل المثال 3 ، في الخلية ، فلن يقوم Excel بتشغيل التحقق من الصحة أو إظهار رسالة خطأ.

في بعض الأحيان ، يكون من الضروري التحقق مما إذا كانت القيمة تفي بقواعد التحقق من صحة البيانات المطبقة على الخلية برمجيًا. في الحالة المذكورة أعلاه ، على سبيل المثال ، يجب أن يفشل الإدخال.

{{% /alert %}} 
## **مقدمة**
 يوفر Aspose.Cells ملف[Cell.GetValidationValue ()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) طريقة للتحقق من صحة قيم الخلية برمجيًا. إذا كانت القيمة الموجودة في خلية لا تفي بقاعدة التحقق من صحة البيانات المطبقة على تلك الخلية ، فإنها ترجع**خطأ شنيع** ، آخر**حقيقي**.

 يوضح نموذج التعليمات البرمجية التالي كيفية عمل ملف[Cell.GetValidationValue ()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) طريقة العمل. أولاً ، يُدخل القيمة 3 في C1. لأن هذا لا يفي بقاعدة التحقق من صحة البيانات ، فإن[Cell.GetValidationValue ()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) طريقة إرجاع**خطأ شنيع** . ثم تقوم بإدخال القيمة 15 في C1. لأن هذه القيمة تفي بقاعدة التحقق من صحة البيانات ، فإن[Cell.GetValidationValue ()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) طريقة إرجاع**حقيقي** . وبالمثل ، فإنه يعود**خطأ شنيع** للقيمة 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **انتاج |**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
