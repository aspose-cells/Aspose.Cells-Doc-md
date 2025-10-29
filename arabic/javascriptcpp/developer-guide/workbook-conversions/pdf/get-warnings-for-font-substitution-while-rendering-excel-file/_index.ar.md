---
title: الحصول على تحذيرات حول استبدال الخطوط أثناء تصيير ملف إكسل باستخدام JavaScript عبر C++
linktitle: الحصول على تحذيرات لاستبدال الخطوط أثناء تقديم ملف Excel
type: docs
weight: 230
url: /ar/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: تعلم كيفية الحصول على تحذيرات حول استبدال الخطوط عند تصيير ملفات إكسل إلى PDF باستخدام Aspose.Cells for JavaScript عبر C++.
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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
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
