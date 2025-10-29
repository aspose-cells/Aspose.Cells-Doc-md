---
title: الحصول على تحذيرات استبدال الخطوط أثناء تصيير ملف Excel باستخدام Golang عبر C++
linktitle: الحصول على تحذيرات استبدال الخط
type: docs
weight: 230
url: /ar/go-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: تعلم كيفية الحصول على التحذيرات بشأن استبدال الخطوط عند تصيير ملفات Excel إلى PDF باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، عند تقديم ملف Microsoft Excel إلى PDF، يقوم Aspose.Cells بتبديل الخطوط. توفر Aspose.Cells ميّزة تتيح للمطورين معرفة ما إذا كانت خطوط معينة قد تم تبديلها عن طريق إطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب تباين ملف PDF الناتج من Aspose.Cells عن ملف Microsoft Excel الأصلي بحيث يمكنك اتخاذ الإجراءات اللازمة. على سبيل المثال، تثبيت الخطوط المفقودة حتى تبدو نتائج التقديم متطابقة.

{{% /alert %}}

للحصول على تحذيرات استبدال الخط عند تحويل ملفات Excel إلى PDF، قم بتنفيذ واجهة `IWarningCallback` واضبط الخاصية `PdfSaveOptions.WarningCallback` بواجهتك المنفذة.

تظهر اللقطة الشاشية أدناه ملف Excel مصدري سنستخدمه في الكود التالي. يحتوي على بعض النص في الخلايا A6 وA7 بخطوط لا تتميز بالتقديم الجيد بواسطة Microsoft Excel.

|**لا تتم تقديم جميع الخطوط بشكل صحيح**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

ستقوم Aspose.Cells بتعويض الخطوط في الخلايا A6 و A7 بخطوط مناسبة كما يظهر أدناه.

|**خطوط مستبدلة**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **تحميل ملف المصدر وملف PDF الناتج**
يمكنك تنزيل ملف Excel المصدر وملف PDF الناتج من الروابط التالية:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **الكود**
الكود التالي ينفذ `IWarningCallback` ويضبط الخاصية `PdfSaveOptions.WarningCallback` بواجهة التنفيذ. الآن، كلما تم استبدال أي خط في أي خلية، ستقوم Aspose.Cells بإطلاق تحذير داخل طريقة `WarningCallback.Warning()`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsForFontSubstitutionWhileRenderingExcelFile.go" >}}
## **الناتج**
بعد تحويل ملف Excel الأصلي إلى PDF، يتم إخراج التحذيرات إلى وحدة التحكم في التصحيح كالتالي:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، من الأفضل استدعاء طريقة `Workbook.CalculateFormula` قبل عرض الجدول بصيغة PDF. القيام بذلك سيضمن إعادة حساب القيم المعتمدة على الصيغة، ويتم عرض القيم الصحيحة في PDF.

{{% /alert %}}
