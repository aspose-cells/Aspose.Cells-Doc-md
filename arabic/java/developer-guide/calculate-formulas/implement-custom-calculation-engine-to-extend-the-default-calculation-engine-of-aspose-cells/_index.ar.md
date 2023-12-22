---
title: قم بتنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
type: docs
weight: 590
url: /ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

يحتوي Aspose.Cells على محرك حسابي قوي يمكنه حساب جميع صيغ Excel Microsoft تقريبًا. وعلى الرغم من ذلك، فإنه يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي الذي يوفر لك قدرًا أكبر من القوة والمرونة.

يتم استخدام الخاصية والفئات التالية في تنفيذ هذه الميزة.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **تنفيذ محرك الحساب المخصص**
تطبق التعليمة البرمجية التالية محرك الحساب المخصص. وهو ينفذ الواجهة[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) الذي له طريقة واحدة فقط[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). يتم استدعاء هذه الطريقة ضد كافة الصيغ الخاصة بك. داخل هذه الطريقة، نقوم بالتقاط**TODAY** وظيفة وإضافة يوم واحد إلى تاريخ النظام. لذا، إذا كان التاريخ الحالي هو 27/07/2023، فسيقوم المحرك المخصص بحساب TODAY() على أنه 28/07/2023.

###  **عينة البرمجة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **نتيجة**

يرجى التحقق من إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه، ويجب أن تكون قيمة (التاريخ والوقت) لـ A1 مع المحرك المخصص بعد يوم واحد من النتيجة بدون محرك مخصص.

###  **مقالات لها صلة**
{{% alert color="primary" %}} 

- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل](/cells/ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
