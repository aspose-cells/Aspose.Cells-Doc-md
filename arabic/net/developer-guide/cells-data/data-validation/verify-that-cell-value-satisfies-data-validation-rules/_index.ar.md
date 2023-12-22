---
title: تحقق من أن القيمة Cell تفي بقواعد التحقق من صحة البيانات
type: docs
weight: 210
url: /ar/net/verify-that-cell-value-satisfies-data-validation-rules/
description: تعرف على كيفية التحقق من أن قيمة Cell تفي بقواعد التحقق من صحة البيانات من خلال Aspose.Cells for .NET API..
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft يتيح Excel للمستخدمين إضافة قواعد التحقق من صحة البيانات إلى الخلايا. على سبيل المثال، يحدد التحقق من صحة العلامة العشرية أنه يمكن إدخال الأرقام بين 10 و20 فقط. إذا قام المستخدم بإدخال رقم مختلف. Microsoft يعرض برنامج Excel رسالة خطأ ويطالبهم بإدخال رقم في النطاق الصحيح. إذا قمت بنسخ رقم ولصقه، على سبيل المثال 3، في الخلية، فلن يقوم Excel بتشغيل عملية التحقق من الصحة أو إظهار رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تفي بقواعد التحقق من صحة البيانات المطبقة على الخلية برمجياً. في الحالة المذكورة أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 
##  **مقدمة**
 Aspose.Cells يوفر[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)طريقة للتحقق من صحة قيم الخلية برمجيا. إذا كانت القيمة الموجودة في خلية لا تستوفي قاعدة التحقق من صحة البيانات المطبقة على تلك الخلية، فستُرجع *False**، وإلا *True**.

 يوضح نموذج التعليمات البرمجية التالي كيفية[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) تعمل الطريقة. أولاً، يقوم بإدخال القيمة 3 في C1. لأن هذا لا يفي بقاعدة التحقق من صحة البيانات،[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) إرجاع الأسلوب**خطأ شنيع**. ثم يقوم بإدخال القيمة 15 في C1. نظرًا لأن هذه القيمة تفي بقاعدة التحقق من صحة البيانات، فإن الأسلوب [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) يُرجع **True**. وبالمثل، تقوم بإرجاع **خطأ** لقيمة 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **انتاج |**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
