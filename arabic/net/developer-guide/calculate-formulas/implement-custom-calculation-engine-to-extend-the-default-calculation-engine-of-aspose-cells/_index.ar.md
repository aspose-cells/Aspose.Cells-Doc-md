---
title: قم بتطبيق محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
type: docs
weight: 80
url: /ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **تنفيذ محرك الحساب المخصص**

يحتوي Aspose.Cells على محرك حساب قوي يمكنه حساب جميع صيغ Excel Microsoft تقريبًا. على الرغم من ذلك ، فإنه يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي الذي يوفر لك قدرًا أكبر من القوة والمرونة.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- **[CalculationOptions.CustomEngine] (https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[بيانات الحساب] (https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

تقوم التعليمات البرمجية التالية بتنفيذ محرك الحساب المخصص. يقوم بتنفيذ الواجهة**[AbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** الذي يحتوي على**[حساب (بيانات الحساب)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** طريقة. يتم استدعاء هذه الطريقة مقابل جميع الصيغ الخاصة بك. داخل هذه الطريقة ، نلتقط ملف**مجموع** الصيغة وتزيد قيمتها بمقدار 30. لذلك إذا كانت القيمة المحسوبة Aspose.Cells هي 20 ، فإن محركنا المخصص سيجعلها 50 بإضافة 30.

### **عينة البرمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **إخراج وحدة التحكم**

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **مقالات لها صلة**

{{% alert color="primary" %}}

[حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
