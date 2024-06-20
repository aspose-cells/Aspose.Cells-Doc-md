---
title: تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
description: يصف هذا المقال كيفية توسيع محرك الحساب الافتراضي عن طريق تنفيذ محرك حساب مخصص باستخدام مكتبة Aspose.Cells. من خلال تحميل ملف Excel موجود أو إنشاء واحد جديد، يمكننا استخدام الطرق المقدمة من Aspose.Cells لتنفيذ محرك حساب مخصص والحصول على النتائج. في النهاية، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، محرك الحساب المخصص، يوسع محرك الحساب الافتراضي
type: docs
weight: 80
url: /ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **تنفيذ محرك الحساب المخصص**

Aspose.Cells يمتلك محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel تقريبًا. على الرغم من ذلك، يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي مما يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

ينفذ الكود التالي محرك الحساب المخصص. إنه ينفذ واجهة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) التي تحتوي على طريقة [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate). يتم استدعاء هذه الطريقة ضد جميع الصيغ. ضمن هذه الطريقة، نلتقط وظيفة **اليوم** ونضيف يوم واحد إلى تاريخ النظام. لذا، إذا كان التاريخ الحالي هو 27/07/2023، فسيقوم المحرك المخصص بحساب TODAY() كـ 28/07/2023.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **النتيجة**

يرجى التحقق من إخراج الوحدة لمثال الشفرة أعلاه ، يجب أن يكون قيمة (التاريخ والوقت) لـ A1 مع محرك مخصص بعد يوم واحد عن النتيجة بدون محرك مخصص.

### **مقال ذو صلة**

{{% alert color="primary" %}}

[حساب مباشر للدالة المخصصة دون كتابتها في ورقة العمل](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
