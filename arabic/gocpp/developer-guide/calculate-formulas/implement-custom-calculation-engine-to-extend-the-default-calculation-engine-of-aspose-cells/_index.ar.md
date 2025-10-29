---
title: تنفيذ محرك حساب مخصص لتوسيع محرك الحساب الافتراضي لمكتبة Aspose.Cells مع Golang عبر C++
linktitle: تطبيق محرك حساب مخصص
description: تصف هذه المقالة كيفية توسيع محرك الحساب الافتراضي عن طريق تنفيذ محرك حساب مخصص باستخدام مكتبة Aspose.Cells مع Golang عبر C++. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق المقدمة بواسطة Aspose.Cells لتنفيذ محرك حساب مخصص والحصول على النتائج. وأخيرًا، نحفظ ملف Excel المعدل إلى القرص.
keywords: Aspose.Cells، إكسل، محرك حساب مخصص، يمدد محرك الحساب الافتراضي، C++
type: docs
weight: 80
url: /ar/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **تنفيذ محرك الحساب المخصص**

Aspose.Cells يمتلك محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel تقريبًا. على الرغم من ذلك، يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي مما يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

ينفذ الكود التالي محرك الحساب المخصص. إنه ينفذ واجهة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) التي تحتوي على طريقة [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/). يتم استدعاء هذه الطريقة ضد جميع الصيغ. ضمن هذه الطريقة، نلتقط وظيفة **اليوم** ونضيف يوم واحد إلى تاريخ النظام. لذا، إذا كان التاريخ الحالي هو 27/07/2023، فسيقوم المحرك المخصص بحساب TODAY() كـ 28/07/2023.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **النتيجة**

يرجى التحقق من إخراج الوحدة لمثال الشفرة أعلاه ، يجب أن يكون قيمة (التاريخ والوقت) لـ A1 مع محرك مخصص بعد يوم واحد عن النتيجة بدون محرك مخصص.

### **مقال ذو صلة**

{{% alert color="primary" %}}

[حساب مباشر لوظيفة مخصصة بدون كتابتها في ورقة عمل](/cells/ar/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
