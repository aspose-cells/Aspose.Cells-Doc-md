---
title: الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل
type: docs
weight: 650
url: /ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

يشرح هذا المقال كيف يمكنك حساب دوالك المخصصة مباشرة بدون كتابتها أولاً في ورقة عمل. يرجى استخدام [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) لهذا الغرض.

{{% /alert %}} 
## **الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل**
يرجى الاطلاع على الكود العينة التالي الذي يوضح استخدام هذه الطريقة. لقد استخدمنا دالة مخصصة تدعى *MyCompany.CustomFunction()* وقمنا بحساب قيمتها كـ "Aspose.Cells." بأنفسنا، ثم يتم دمج هذه القيمة تلقائيًا مع قيمة الخلية A1 وهي "مرحبًا بكم في " من قبل محرك الحساب وتُرجع القيمة المحسوبة النهائية كـ "مرحبًا بكم في Aspose.Cells." كما ترون في الكود فإننا لم نكتب دالتنا المخصصة في أي مكان في ورقة العمل وتتم حسابها مباشرة بواسطة منطقنا المخصص الخاص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **مخرجات الوحدة**
فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **مقال ذو صلة**
{{% alert color="primary" %}} 

- [تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
