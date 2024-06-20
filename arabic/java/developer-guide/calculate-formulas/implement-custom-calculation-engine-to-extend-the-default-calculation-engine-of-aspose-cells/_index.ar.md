---
title: تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
type: docs
weight: 590
url: /ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells يمتلك محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel تقريبًا. على الرغم من ذلك، يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي مما يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **تنفيذ محرك الحساب المخصص**
يقوم الكود التالي بتنفيذ محرك الحساب المخصص. ينفذ واجهة [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) التي تحتوي على طريقة واحدة فقط [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). يتم استدعاء هذه الطريقة لجميع الصيغ الخاصة بك. داخل هذه الطريقة، نقوم بالتقاط وظيفة **TODAY** وإضافة يوم واحد إلى تاريخ النظام. لذا إذا كان التاريخ الحالي هو 27/07/2023، فسوف يقوم المحرك المخصص بحساب TODAY() كـ 28/07/2023.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **النتيجة**

يرجى التحقق من إخراج الوحدة لمثال الشفرة أعلاه ، يجب أن يكون قيمة (التاريخ والوقت) لـ A1 مع محرك مخصص بعد يوم واحد عن النتيجة بدون محرك مخصص.

### **مقال ذو صلة**
{{% alert color="primary" %}} 

- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل](/cells/ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
