---
title: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 90
url: /ar/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

يسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى خلايا ورق العمل. على سبيل المثال، يمكن تطبيق تحقق عشري لتقييد الأرقام بين 10 و 20. إذا تم إدخال أي رقم آخر خارج هذا النطاق المحدد، يظهر Microsoft Excel رسالة خطأ ويطلب من المستخدم إعادة إدخال رقم من النطاق الصحيح. إذا قام المستخدم بنسخ ولصق رقم، على سبيل المثال 3، في الخلية، فإن Excel لا تقوم بتشغيل فحص التحقق أو عرض رسالة خطأ.

{{% /alert %}}

## التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات

في بعض الأحيان، يكون من الضروري التحقق ديناميكيًا مما إذا كانت القيمة المعطاة تفي بقواعد التحقق من البيانات المطبقة على الخلية. لهذا الغرض، توفر واجهة برمجة التطبيقات Aspose.Cells الطريقة [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). إذا لم تفي قيمة في الخلية بقاعدة التحقق من البيانات المطبقة على تلك الخلية، فإنه يعيد **خطأ**، وإلا **صحيح**.

يتم استخدام الملف النموذجي التالي لمايكروسوفت إكسل مع الشيفرة البرمجية النموذجية أدناه لاختبار الطريقة [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). كما يمكنك رؤية في اللقطة الفوتوغرافية أن الخلية **C1** لديها **تحقق بيانات عشرية** مطبقة وسوف تقبل فقط القيم بين 10 و 20. كلما كانت قيمة الخلية بين 10 و 20، ستعيد الطريقة [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) **صحيح**، وإلا، ستعيد **خطأ**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

يوضح الكود المثال التالي كيفية عمل طريقة [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). أولاً، يُدخل القيمة 3 إلى C1. لأن هذا لا يُرضي قاعدة التحقق من البيانات، فإن طريقة [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) تعيد **False**. ثم، يُدخل القيمة 15 إلى C1. لأن هذه القيمة تُرضي قاعدة التحقق من البيانات، فإن طريقة [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) تعيد **True**. بالمثل، تُعيد **False** للقيمة 30.

## كود جافا للتحقق مما إذا كانت قيمة الخلية تُرضي قواعد التحقق من البيانات

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## الناتج على واجهة الأوامر الناتجة عن الكود المثال

هنا الناتج على واجهة الأوامر عند تنفيذ الكود المثال مع ملف Excel المعروض أعلاه.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
