---  
title: الحصول على تحذيرات بشأن استبدال الخطوط أثناء التحويل من Excel إلى PDF باستخدام Node.js عبر C++  
linktitle: الحصول على تحذيرات لاستبدال الخطوط أثناء تقديم ملف Excel  
type: docs  
weight: 230  
url: /ar/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: تعلم كيفية الحصول على تحذيرات بشأن استبدال الخطوط عند تحويل ملفات Excel إلى PDF باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

في بعض الأحيان، عند تقديم ملف Microsoft Excel إلى PDF، يقوم Aspose.Cells بتبديل الخطوط. توفر Aspose.Cells ميّزة تتيح للمطورين معرفة ما إذا كانت خطوط معينة قد تم تبديلها عن طريق إطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب تباين ملف PDF الناتج من Aspose.Cells عن ملف Microsoft Excel الأصلي بحيث يمكنك اتخاذ الإجراءات اللازمة. على سبيل المثال، تثبيت الخطوط المفقودة حتى تبدو نتائج التقديم متطابقة.

{{% /alert %}}  

للحصول على تحذيرات بشأن استبدال الخط أثناء عرض ملفات إكسيل على PDF، قم بتنفيذ واجهة IWarningCallback وضبط خاصية PdfSaveOptions.warningCallback بواجهتك المنفذة.

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
الكود التالي يُنفذ واجهة IWarningCallback ويضبط خاصية PdfSaveOptions.warningCallback بواجهة المنفذة. الآن، كلما تم استبدال أي خط في أي خلية، ستطلق Aspose.Cells تحذيرًا داخل أسلوب WarningCallback.Warning().

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
```  
## **الناتج**  
بعد تحويل ملف Excel الأصلي إلى PDF، يتم إخراج التحذيرات إلى وحدة التحكم في التصحيح كالتالي:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل أن تقوم بإتصال طريقة Workbook.calculateFormula قبل تقديم الجدول إلى تنسيق PDF. من خلال ذلك ستضمن أن القيم التي تعتمد على الصيغ تم احتسابها من جديد وتم تقديم القيم الصحيحة في الـPDF.

{{% /alert %}}  

