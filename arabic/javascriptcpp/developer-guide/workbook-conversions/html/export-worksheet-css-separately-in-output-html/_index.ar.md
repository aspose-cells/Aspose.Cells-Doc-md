---
title: تصدير CSS ورقة العمل بشكل منفصل في HTML الناتج باستخدام JavaScript عبر C++
linktitle: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج
type: docs
weight: 80
url: /ar/javascript-cpp/export-worksheet-css-separately-in-output/
description: تعرّف على كيفية تصدير CSS ورقة العمل بشكل منفصل عند تحويل ملف إكسل إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يوفر Aspose.Cells for JavaScript عبر C++ الميزة لتصدير CSS ورقة العمل بشكل منفصل عند تحويل ملف إكسل إلى HTML. يرجى استخدام خاصية [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--) لهذا الغرض وتعيينها على **true** أثناء حفظ ملف إكسل بصيغة HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

يُنشئ الكود النموذجي التالي ملف إكسل، يضيف بعض النصوص في الخلية **B5** باللون **الأحمر**، ثم يحفظه بصيغة HTML باستخدام خاصية [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--). يرجى الاطلاع على [ملف HTML الناتج](60489766.zip) المولَّد بواسطة الكود للمرجعة. ستجد داخله ملف **stylesheet.css** كنتيجة للكود النموذجي.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet CSS Separately Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color, Utils } = AsposeCells;

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
            // Create a new workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - export worksheet css separately
            const opts = new HtmlSaveOptions();
            opts.exportWorksheetCSSSeparately = true;

            // Save the workbook in html 
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportWorksheetCSSSeparately.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **تصدير جدول عمل واحد إلى HTML**

عند تحويل مجلد عمل يتضمن عدة أوراق إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++، يتم إنشاء ملف HTML بالإضافة إلى مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح هذا الملف في المتصفح، تكون الألسنة مرئية. نفس السلوك مطلوب لمجلد عمل يحتوي على ورقة عمل واحدة عند تحويله إلى HTML. سابقًا، لم يتم إنشاء مجلد منفصل للمجلدات ذات الورقة الواحدة، وتم إنشاء ملف HTML فقط. مثل هذا الملف لا يُظهر الألسنة عند فتحه في المتصفح. يقوم MS Excel أيضًا بإنشاء مجلد وHTML مناسب عند تحويل ورقة واحدة، ولذلك تم تنفيذ نفس السلوك باستخدام واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells. يمكن تحميل الملف التجريبي من الرابط التالي للاستخدام في الكود أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, EncodingType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML save options
            const options = new HtmlSaveOptions();

            // Set optional settings (converted from setters to properties)
            options.encoding = EncodingType.UTF8;
            options.exportImagesAsBase64 = true;
            options.exportGridLines = true;
            options.exportSimilarBorderStyle = true;
            options.exportBogusRowData = true;
            options.excludeUnusedStyles = true;
            options.exportHiddenWorksheet = true;

            // Save the workbook in HTML format with specified HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSampleSingleSheet.htm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
