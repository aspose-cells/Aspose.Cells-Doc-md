---
title: الحساب المباشر للدالة المخصصة دون كتابتها في ورقة العمل باستخدام Golang عبر C++
linktitle: حساب مباشر لوظيفة مخصصة
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لحساب الوظائف المخصصة مباشرة في Microsoft Excel دون كتابتها في ورقة عمل. من خلال تحميل ملف Excel القائم أو إنشاء واحد جديد، يمكننا استخدام الطرق المقدمة من Aspose.Cells لحساب الوظيفة المخصصة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، إكسل، وظائف مخصصة، حسابات مباشرة، لا حاجة للكتابة، ورق العمل
type: docs
weight: 90
url: /ar/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **حساب مباشر لوظيفة مخصصة بدون كتابتها في ورقة عمل**

يشرح هذا الموضوع كيف يمكنك حساب وظائفك المخصصة مباشرة دون كتابتها أولاً في ورقة عمل. يرجى استخدام طريقة [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) لهذا الغرض.

يرجى الاطلاع على الشفرة النموذجية التالية التي توضح استخدام هذه الطريقة. استخدمنا وظيفة مخصصة تسمى MyCompany::CustomFunction() ونحسب قيمتها بأنفسنا كـ "Aspose.Cells." ثم يتم دمج هذه القيمة تلقائيًا مع قيمة الخلية A1 وهي "مرحبًا بك في" بواسطة محرك الحساب، وتُرجع القيمة المحسوبة النهائية كـ "مرحبًا بك في Aspose.Cells.". كما يتضح في الشفرة، لم نكتب وظيفتنا المخصصة في أي مكان في ورقة عمل، وهي تحسب مباشرة بواسطة منطقنا المخصص.

### **نموذج برمجة**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **مخرجات الوحدة**

فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **مقال ذو صلة**

{{% alert color="primary" %}}

[تطبيق محرك حساب مخصص لتمديد محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
