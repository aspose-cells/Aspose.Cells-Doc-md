---
title: تطابق الأعمدة والصفوف تلقائياً عند تحميل HTML في دفتر العمل باستخدام JavaScript عبر C++
linktitle: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 120
url: /ar/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: تعرف على كيفية ملاءمة الأعمدة والصفوف تلقائيًا أثناء تحميل ملفات HTML في دفتر العمل باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلقائيًا ضبط الأعمدة والصفوف أثناء تحميل ملف HTML الخاص بك داخل كائن Workbook. يرجى تعيين خاصية [**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

الرمز النموذجي التالي يقوم أولاً بتحميل HTML النموذجي في Workbook دون خيارات تحميل ويحفظه بصيغة XLSX. ثم يعيد تحميل نفس HTML داخل Workbook ولكن هذه المرة مع تعيين خاصية [**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--) إلى **true**، ويحفظه بصيغة XLSX. الرجاء تنزيل كلا الملفين الناتجين، ملف إكسل بدون auto-fit وملف إكسل مع auto-fit. يظهر الشاشة التالية تأثير خاصية [**HtmlLoadOptions.autoFitColsAndRows**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#autoFitColsAndRows--) على كلا الملفين.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Load HTML and Save XLSX</title>
    </head>
    <body>
        <h1>Load HTML String into Workbook and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result 1</a>
            <a id="downloadLink2" style="display: none;">Download Result 2</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, Utils } = AsposeCells;

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
            // Sample HTML.
            const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

            // Convert HTML string to Uint8Array (memory stream).
            const ms = new TextEncoder().encode(sampleHtml);

            // Load memory stream into workbook.
            const wb1 = new Workbook(ms);

            // Save the workbook in xlsx format.
            const outputData1 = wb1.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithout_AutoFitColsAndRows.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download outputWithout_AutoFitColsAndRows.xlsx';

            // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
            const opts = new HtmlLoadOptions();
            opts.autoFitColsAndRows = true;

            // Load memory stream into workbook with the above HTMLLoadOptions.
            const wb2 = new Workbook(ms, opts);

            // Save the workbook in xlsx format.
            const outputData2 = wb2.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputWith_AutoFitColsAndRows.xlsx';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download outputWith_AutoFitColsAndRows.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated files.</p>';
        });
    </script>
</html>
```
