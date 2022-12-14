---
title: احصل على تحذيرات لاستبدال الخط أثناء عرض ملف Excel
type: docs
weight: 230
url: /ar/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

في بعض الأحيان ، عند تحويل ملف Excel Microsoft إلى PDF ، يقوم Aspose.Cells باستبدال الخطوط. يوفر Aspose.Cells ميزة تتيح للمطورين معرفة الخط المعين الذي تم استبداله بإطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب اختلاف مظهر ملف PDF المعروض Aspose.Cells عن ملف Excel Microsoft الأصلي حتى تتمكن من اتخاذ الإجراءات المناسبة. على سبيل المثال ، تثبيت الخطوط المفقودة بحيث تبدو نتائج العرض كما هي.

{{% /alert %}} 

للحصول على تحذيرات لاستبدال الخط عند تحويل ملفات Excel إلى PDF ، قم بتنفيذ واجهة IWarningCallback وقم بتعيين خاصية PdfSaveOptions.WarningCallback مع الواجهة التي تم تنفيذها.

تُظهر لقطة الشاشة أدناه ملف Excel المصدر الذي سنستخدمه في الكود التالي. يحتوي على بعض النصوص في الخلايا A6 و A7 في الخطوط التي لم يتم تقديمها بشكل جيد بواسطة Microsoft Excel.

|**لم يتم تقديم جميع الخطوط بشكل صحيح**|
|:- |
|![ما يجب القيام به: image_بديل_نص](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
سيقوم Aspose.Cells باستبدال الخطوط الموجودة في الخلايا A6 و A7 بخطوط مناسبة كما هو موضح أدناه.

|**الخطوط المستبدلة**|
|:- |
|![ما يجب القيام به: image_بديل_نص](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **تنزيل ملف المصدر وإخراج PDF**
يمكنك تنزيل ملف Excel المصدر و PDF الناتج من الروابط التالية

- [المصدر. xlsx](5112611.xlsx)
- [الإخراج. pdf](5112616.pdf)
## **شفرة**
تقوم التعليمات البرمجية التالية بتنفيذ IWarningCallback وتعيين خاصية PdfSaveOptions.WarningCallback مع الواجهة التي تم تنفيذها. الآن ، عندما يتم استبدال أي خط في أي خلية ، سيقوم Aspose.Cells بإطلاق تحذير داخل طريقة WarningCallback.Warning ().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **انتاج |**
بعد تحويل ملف Excel المصدر إلى PDF ، يتم إخراج التحذيرات إلى وحدة التحكم في تصحيح الأخطاء كما يلي:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل استدعاء طريقة Workbook.CalculateFormula قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}
