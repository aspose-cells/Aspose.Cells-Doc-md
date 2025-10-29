---
title: توفير مسار ملف HTML لورقة العمل المصدرة عبر واجهة IFilePathProvider باستخدام JavaScript عبر C++
linktitle: توفير مسار ملف HTML لورقة العمل المصدرة عبر واجهة IFilePathProvider
type: docs
weight: 70
url: /ar/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **سيناريوهات الاستخدام المحتملة**
افترض أن لديك ملف إكسل يتضمن عدة أوراق عمل وتريد تصدير كل ورقة إلى ملف HTML منفصل. إذا كانت أي من أوراق العمل تحتوي على روابط لورقات أخرى، فستلزم إصلاح تلك الروابط المكسورة في HTML المصدّر. يوفر Aspose.Cells for JavaScript عبر C++ واجهة [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider)، والتي يمكنك تنفيذها لإصلاح الروابط المعطوبة.

## **توفير مسار ملف HTML لواجهة IFilePathProvider**
يرجى تنزيل [ملف إكسل النموذجي](5115213.zip) المستخدم في الكود التالي وملفات HTML المصدرة. كل هذه الملفات داخل مجلد Temp. ينبغي فك ضغطه على محرك C:. بعدها، سيصبح المجلد C:\Temp. بعدها، يمكنك فتح ملف Sheet1.html في المتصفح والنقر على الرابطين بداخله. هذه الروابط تشير إلى هذين المصنفين HTML المصدَّرين اللذين داخل مجلد C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

اللقطة الشاشية التالية تظهر كيفية الرؤية C:\Temp\Sheet1.html وروابطها

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

تظهر الصورة التالية مصدر HTML. كما ترى، الآن تشير الروابط إلى دليل C:\Temp\OtherSheets. تم تحقيق ذلك باستخدام واجهة [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **الكود المثالي**
يرجى ملاحظة أن مجلد C:\Temp هو فقط لأغراض التوضيح. يمكنك استخدام أي مجلد تفضله ووضع [ملف إكسل النموذجي](5115211.xlsx) بداخله وتشغيل الكود المقدم. وسوف ينشئ مجلد فرعي باسم OtherSheets داخل مجلدك، ويصدر ملفات HTML لأوراق العمل الثانية والثالثة بداخله. يرجى تغيير المتغير dirPath داخل الكود المقدم وإحالته إلى المجلد الذي تختاره قبل التنفيذ.

{{% alert color="primary" %}} 

سيعمل الكود النموذجي فقط عند ضبط ترخيص Aspose.Cells. إذا حاولت تشغيل الكود بدون ضبط الترخيص، فسيدخل في حلقة لانهائية. لذلك، أضفنا عملية فحص لطباعة رسالة وإيقاف التنفيذ عندما لا يكون الترخيص مضبوطًا. يمكنك إما شراء ترخيص أو طلب ترخيص مؤقت لمدة 30 يومًا من فريق Aspose.Purchase.

{{% /alert %}} 

يرجى ملاحظة أن تعليق هذه الأسطر داخل الكود سوف يكسر الروابط في Sheet1.html، ولن تُفتح Sheet2.html أو Sheet3.html عند النقر على روابطها داخل Sheet1.html.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet to HTML with FilePathProvider Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

        // Implementation of IFilePathProvider for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Converted method name from getFullName -> fullName per universal getter/setter conversion rule
            fullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and assign FilePathProvider (converted setter to property assignment)
            const options = new HtmlSaveOptions();
            options.filePathProvider = new FilePathProvider();

            // Save workbook to HTML using options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - IFilePathProvider</title>
    </head>
    <body>
        <h1>Aspose.Cells IFilePathProvider Example (Browser)</h1>
        <p>Select the Sample_filepath.xlsx file to export worksheets to separate HTML files.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="links"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

        // Implementation of IFilePathProvider interface for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Gets the full path of the file by worksheet name when exporting worksheet to html separately.
            // So the references among the worksheets could be exported correctly.
            getFullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('links');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select the Sample_filepath.xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check license
            if (!workbook.isLicensed()) {
                resultDiv.innerHTML = '<p style="color: red;">You must set the license to execute this code successfully.</p>';
                return;
            }

            // Export each worksheet to separate HTML using HtmlSaveOptions and FilePathProvider
            const sheetCount = workbook.worksheets.count;

            for (let i = 0; i < sheetCount; i++) {
                // Set the active worksheet to current index
                workbook.worksheets.activeSheetIndex = i;

                // Create html save option
                const options = new HtmlSaveOptions();
                options.exportActiveWorksheetOnly = true;
                // Provide file path provider so hyperlinks among sheets are preserved correctly
                options.filePathProvider = new FilePathProvider();

                // Save the active worksheet to HTML (returns Uint8Array)
                const outputData = workbook.save(SaveFormat.Html, options);

                // Create downloadable blob for the HTML
                const blob = new Blob([outputData], { type: 'text/html' });

                // Determine filename similar to original logic
                const sheetIndex = i + 1;
                let filename = '';
                if (i === 0) {
                    filename = 'Sheet1.html';
                } else {
                    filename = `OtherSheets_Sheet${sheetIndex}_out.html`;
                }

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.textContent = 'Download ' + filename;
                link.style.display = 'block';
                linksDiv.appendChild(link);
            }

            resultDiv.innerHTML = '<p style="color: green;">Worksheets exported successfully! Use the links below to download each HTML file.</p>';
        });
    </script>
</html>
```
