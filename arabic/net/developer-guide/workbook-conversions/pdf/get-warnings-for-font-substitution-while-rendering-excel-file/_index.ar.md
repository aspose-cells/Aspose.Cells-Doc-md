---
title: الحصول على تحذيرات لاستبدال الخطوط أثناء تقديم ملف Excel
type: docs
weight: 230
url: /ar/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

في بعض الأحيان، عند تقديم ملف Microsoft Excel إلى PDF، يقوم Aspose.Cells بتبديل الخطوط. توفر Aspose.Cells ميّزة تتيح للمطورين معرفة ما إذا كانت خطوط معينة قد تم تبديلها عن طريق إطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب تباين ملف PDF الناتج من Aspose.Cells عن ملف Microsoft Excel الأصلي بحيث يمكنك اتخاذ الإجراءات اللازمة. على سبيل المثال، تثبيت الخطوط المفقودة حتى تبدو نتائج التقديم متطابقة.

{{% /alert %}} 

للحصول على تحذيرات لاستبدال الخطوط عند تقديم ملفات Excel إلى PDF، قم بتنفيذ واجهة IWarningCallback وضبط خاصية PdfSaveOptions.WarningCallback بواجهة الواجهة المنفذة الخاصة بك.

تظهر اللقطة الشاشية أدناه ملف Excel مصدري سنستخدمه في الكود التالي. يحتوي على بعض النص في الخلايا A6 وA7 بخطوط لا تتميز بالتقديم الجيد بواسطة Microsoft Excel.

|**لا تتم تقديم جميع الخطوط بشكل صحيح**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
ستقوم Aspose.Cells بتعويض الخطوط في الخلايا A6 و A7 بخطوط مناسبة كما يظهر أدناه.

|**خطوط مستبدلة**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **تحميل ملف المصدر وملف PDF الناتج**
يمكنك تحميل ملف Excel المصدر وملف PDF الناتج من الروابط التالية

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **الكود**
يقوم الكود التالي بتنفيذ واجهة IWarningCallback وتعيين خاصية PdfSaveOptions.WarningCallback بالواجهة المنفذة. الآن، عندما يتم تعويض أي خط في أي خلية، سيقوم Aspose.Cells بإطلاق تحذير داخل طريقة WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **الناتج**
بعد تحويل ملف Excel الأصلي إلى PDF، يتم إخراج التحذيرات إلى وحدة التحكم في التصحيح كالتالي:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء طريقة Workbook.CalculateFormula قبل عرض الجدول إلى صيغة PDF. فعل ذلك سيضمن إعادة حساب قيم الصيغ وعرض القيم الصحيحة في PDF.

{{% /alert %}}
