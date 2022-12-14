---
title: قم بتطبيق محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
type: docs
weight: 590
url: /ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

يحتوي Aspose.Cells على محرك حساب قوي يمكنه حساب جميع صيغ Excel Microsoft تقريبًا. على الرغم من ذلك ، فإنه يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي الذي يوفر لك قدرًا أكبر من القوة والمرونة.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [الخلاصةحساب المحرك](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [بيانات الحساب](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **تنفيذ محرك الحساب المخصص**
تقوم التعليمات البرمجية التالية بتنفيذ محرك الحساب المخصص. يقوم بتنفيذ الواجهة[الخلاصةحساب المحرك](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) التي لديها طريقة واحدة فقط[حساب (بيانات الحساب)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). يتم استدعاء هذه الطريقة مقابل جميع الصيغ الخاصة بك. داخل هذه الطريقة ، نلتقط ملف**مجموع** الصيغة وتزيد قيمتها بمقدار 30. لذلك إذا كانت القيمة المحسوبة Aspose.Cells هي 20 ، فإن محركنا المخصص سيجعلها 50 بإضافة 30.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **إخراج وحدة التحكم**
هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **مقالات لها صلة**
{{% alert color="primary" %}} 

- [حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل](/cells/ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
