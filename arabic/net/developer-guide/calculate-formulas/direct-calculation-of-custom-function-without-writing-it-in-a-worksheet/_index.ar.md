---
title: الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لحساب الوظائف المخصصة مباشرة في Microsoft Excel دون كتابتها في ورقة عمل. من خلال تحميل ملف Excel القائم أو إنشاء واحد جديد، يمكننا استخدام الطرق المقدمة من Aspose.Cells لحساب الوظيفة المخصصة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، إكسل، وظائف مخصصة، حسابات مباشرة، لا حاجة للكتابة، ورق العمل
type: docs
weight: 90
url: /ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل**

تشرح هذه القائمة كيف يمكنك حساب وظائفك المخصصة مباشرة دون كتابتها أولاً في ورق العمل. يُرجى استخدام الطريقة [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) لهذا الغرض.

يرجى الاطلاع على الرمز العيني التالي الذي يوضح استخدام هذه الطريقة. لقد استخدمنا وظيفة مخصصة باسم MyCompany.CustomFunction() وقمنا بحساب قيمتها كـ 'Aspose.Cells.' بأنفسنا ثم يتم دمج هذه القيمة تلقائيًا مع قيمة الخلية A1 التي هي 'مرحبًا بك في ' بواسطة محرك الحساب وتعيد القيمة المحسوبة النهائية كـ 'مرحبا بك في Aspose.Cells.' كما ترون في الرمز البرمجي لم نكتب وظيفتنا المخصصة في أي مكان في ورقة العمل ويتم حسابها مباشرة بواسطة منطقنا المخصص.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **مخرجات الوحدة**

فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **مقال ذو صلة**

{{% alert color="primary" %}}

[تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
