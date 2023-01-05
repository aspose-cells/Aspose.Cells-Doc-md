---
title: تحقق من أن Cell القيمة تلبي قواعد التحقق من صحة البيانات
type: docs
weight: 90
url: /ar/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft يسمح Excel للمستخدمين بإضافة قواعد التحقق من صحة البيانات إلى خلايا ورقة العمل. على سبيل المثال ، يمكن تطبيق التحقق العشري لتقييد الأرقام بين 10 و 20. إذا تم إدخال أي رقم آخر خارج هذا النطاق المحدد ، يعرض Microsoft Excel رسالة خطأ ويطلب من المستخدم إعادة إدخال رقم من النطاق الصحيح. إذا قام المستخدم بنسخ رقم ، على سبيل المثال 3 ، في الخلية ، فلن يقوم Excel بتشغيل التحقق من الصحة أو إظهار رسالة خطأ.

{{% /alert %}}

## تحقق من أن Cell القيمة تلبي قواعد التحقق من صحة البيانات

في بعض الأحيان ، من الضروري التحقق ديناميكيًا مما إذا كانت قيمة معينة تفي بقواعد التحقق من صحة البيانات المطبقة على الخلية. لهذا الغرض ، توفر واجهات برمجة التطبيقات Aspose.Cells امتداد[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) طريقة. إذا كانت القيمة الموجودة في خلية لا تفي بقاعدة التحقق من صحة البيانات المطبقة على تلك الخلية ، فإنها ترجع**خطأ شنيع** ، آخر**حقيقي**.

يتم استخدام نموذج ملف Excel Microsoft التالي مع نموذج التعليمات البرمجية أدناه لاختبار[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) طريقة. كما ترى في اللقطة أن الخلايا**C1** لديها**التحقق من صحة البيانات العشرية** تم تطبيقه ولن يقبل إلا القيم**بين 10 و 20** . عندما تكون قيمة الخلية بين 10 و 20 ،[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) طريقة العودة**حقيقي** وإلا فإنه سيعود**خطأ شنيع**.

![ما يجب القيام به: image_بديل_نص](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 يوضح نموذج التعليمات البرمجية التالي كيفية عمل ملف[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) طريقة العمل. أولاً ، يُدخل القيمة 3 في C1. لأن هذا لا يفي بقاعدة التحقق من صحة البيانات ، فإن[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) طريقة إرجاع**خطأ شنيع** . ثم تقوم بإدخال القيمة 15 في C1. لأن هذه القيمة تفي بقاعدة التحقق من صحة البيانات ، فإن[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) طريقة إرجاع**حقيقي** . وبالمثل ، فإنه يعود**خطأ شنيع** للقيمة 30.

## كود Java للتحقق مما إذا كانت قيمة Cell تفي بقواعد التحقق من صحة البيانات

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## ناتج وحدة التحكم التي تم إنشاؤها بواسطة نموذج التعليمات البرمجية

فيما يلي إخراج وحدة التحكم الذي تم إنشاؤه عند تنفيذ نموذج التعليمات البرمجية مع نموذج ملف Excel الموضح أعلاه.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
