---
title: قم بتنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells
description: توضح هذه المقالة كيفية توسيع محرك الحساب الافتراضي من خلال تطبيق محرك حساب مخصص باستخدام مكتبة Aspose.Cells. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells لتنفيذ محرك حساب مخصص والحصول على النتائج. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **تنفيذ محرك الحساب المخصص**

يحتوي Aspose.Cells على محرك حسابي قوي يمكنه حساب جميع صيغ Excel Microsoft تقريبًا. وعلى الرغم من ذلك، فإنه يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي الذي يوفر لك قدرًا أكبر من القوة والمرونة.

يتم استخدام الخاصية والفئات التالية في تنفيذ هذه الميزة.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[بيانات الحساب](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

تطبق التعليمة البرمجية التالية محرك الحساب المخصص. وهو ينفذ الواجهة**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** الذي لديه**[احسب (بيانات بيانات الحساب)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** طريقة. يتم استدعاء هذه الطريقة ضد كافة الصيغ الخاصة بك. داخل هذه الطريقة، نقوم بالتقاط**TODAY** وظيفة وإضافة يوم واحد إلى تاريخ النظام. لذا، إذا كان التاريخ الحالي هو 27/07/2023، فسيقوم المحرك المخصص بحساب TODAY() على أنه 28/07/2023.

###  **عينة البرمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **نتيجة**

يرجى التحقق من إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه، ويجب أن تكون قيمة (التاريخ والوقت) لـ A1 مع المحرك المخصص بعد يوم واحد من النتيجة بدون محرك مخصص.

###  **مقالات لها صلة**

{{% alert color="primary" %}}

[الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
