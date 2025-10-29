---
title: تحديد كيفية قطع النص في HTML الناتج باستخدام HtmlCrossType مع JavaScript عبر C++
linktitle: تحديد كيفية عبور النص في ملف الـHTML الناتج باستخدام HtmlCrossType
type: docs
weight: 140
url: /ar/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: تعلم كيفية التحكم في تجاوز النص في HTML عن طريق تحديد HtmlCrossType في Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما يحتوي الخلية على نص أو سلسلة لكن أكبر من عرض الخلية، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو لا تحتوي على شيء. عند حفظ ملف Excel كـ HTML، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع العبور باستخدام تعداد [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). يحتوي على القيم التالية:

- **HtmlCrossType.Default**: عرض مثل MS Excel؛ يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، فإن النص سيعبر أو سيتم اقتطاعه.

- **HtmlCrossType.MSExport**: عرض النص كما في تصدير HTML من برنامج MS Excel.

- **HtmlCrossType.Cross**: عرض النص عبر HTML؛ الأداء لإنشاء ملفات HTML كبيرة سيكون أكثر من عشرة أضعاف أسرع من تعيين القيمة إلى Default أو FitToCell.

- **HtmlCrossType.FitToCell**: عرض النص فقط ضمن عرض الخلية.

## **تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType**

الشفرة النموذجية التالية تقوم بتحميل [ملف Excel النموذجي](51740732.xlsx) وتخزينه بتنسيق HTML عن طريق تحديد قيم [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) المختلفة. يرجى تنزيل [ملفات HTML الناتجة](51740734.zip) التي تم إنشاؤها باستخدام هذه الشفرة. يحتوي ملف Excel النموذجي على صورة محاطة باللون الأحمر كما هو موضح في لقطة الشاشة التي توضح تأثير قيم [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) على HTML الناتج.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
