---
title: الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لحساب الوظائف المخصصة مباشرة في Microsoft Excel دون كتابة الوظيفة في ورقة عمل. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells لحساب الوظيفة المخصصة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة عمل**

 يشرح هذا الموضوع كيف يمكنك حساب وظائفك المخصصة مباشرةً دون كتابتها أولاً في ورقة عمل. الرجاء استخدام[**Worksheet.CalculateFormula (صيغة السلسلة، خيارات CalculationOptions)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)طريقة لهذا الغرض.

الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يوضح استخدام هذا الأسلوب. لقد استخدمنا دالة مخصصة باسم MyCompany.CustomFunction() وقمنا بحساب قيمتها كـ "Aspose.Cells". بأنفسنا ثم يتم ربط هذه القيمة تلقائيًا بقيمة الخلية A1 وهي "مرحبًا بك في" بواسطة محرك الحساب وترجع القيمة المحسوبة النهائية كـ "مرحبًا بك في Aspose.Cells."". كما ترون في الكود الذي لدينا لم يتم كتابة وظيفتنا المخصصة في أي مكان في ورقة العمل ويتم حسابها مباشرة من خلال المنطق المخصص الخاص بنا.

###  **عينة البرمجة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **إخراج وحدة التحكم**

يوجد أدناه إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **مقالات لها صلة**

{{% alert color="primary" %}}

[قم بتنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
