---
title: حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل
type: docs
weight: 90
url: /ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل**

 يشرح هذا الموضوع كيف يمكنك حساب وظائفك المخصصة مباشرةً دون كتابتها أولاً في ورقة عمل. الرجاء استخدام[**Worksheet.CalculateFormula (صيغة السلسلة ، خيار CalculationOptions)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)طريقة لهذا الغرض.

الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يوضح استخدام هذه الطريقة. لقد استخدمنا وظيفة مخصصة تسمى MyCompany.CustomFunction () ونحسب قيمتها كـ "Aspose.Cells." من جانبنا ومن ثم يتم ربط هذه القيمة تلقائيًا بقيمة الخلية A1 التي هي "مرحبًا بك في" بواسطة محرك الحساب وترجع القيمة المحسوبة النهائية كـ "مرحبًا بك في Aspose.Cells." ". كما ترى في الكود الذي لدينا لم تكتب وظيفتنا المخصصة في أي مكان في ورقة العمل ويتم حسابها مباشرة من خلال منطقنا المخصص.

### **عينة البرمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **إخراج وحدة التحكم**

يوجد أدناه إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **مقالات لها صلة**

{{% alert color="primary" %}}

[قم بتطبيق محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
