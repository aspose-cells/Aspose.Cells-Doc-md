---
title: حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل
type: docs
weight: 650
url: /ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 تشرح هذه المقالة كيف يمكنك حساب وظائفك المخصصة مباشرة دون كتابتها أولاً في ورقة عمل. الرجاء استخدام[Worksheet.calculateFormula (صيغة السلسلة ، خيار CalculationOptions)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) طريقة لهذا الغرض.

{{% /alert %}} 
## **حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل**
الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يوضح استخدام هذه الطريقة. لقد استخدمنا وظيفة مخصصة مسماة*MyCompany.CustomFunction ()*ونحسب قيمتها كـ "Aspose.Cells." بأنفسنا ومن ثم يتم ربط هذه القيمة تلقائيًا بقيمة الخلية A1 التي هي "مرحبًا بك في" بواسطة محرك الحساب وترجع القيمة المحسوبة النهائية كـ "مرحبًا بك في Aspose.Cells.". كما ترى في الكود ، لم نكتب وظيفتنا المخصصة في أي مكان في ورقة العمل ويتم حسابها مباشرة من خلال منطقنا المخصص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **إخراج وحدة التحكم**
يوجد أدناه إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **مقالات لها صلة**
{{% alert color="primary" %}} 

- [قم بتطبيق محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
