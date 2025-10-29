---
title: حفظ الملف إلى كائن الاستجابة باستخدام جافا سكريبت عبر ++C
linktitle: حفظ الملف في كائن الاستجابة
type: docs
weight: 50
url: /ar/javascript-cpp/saving-file-to-response-object/
description: تعلم كيفية إنشاء ملفات بشكل ديناميكي وإرسالها مباشرة إلى متصفح العميل باستخدام سكريبت Aspose.Cells for Java عبر ++C.
---

{{% alert color="primary" %}}  

تجعل Aspose.Cells من الممكن التلاعب بالملفات. يشرح هذا المقال الطرق المختلفة التي يمكن بواسطتها حفظ الملفات في كائن الاستجابة.  

{{% /alert %}}  

## **حفظ الملف في كائن الاستجابة**  

من الممكن أيضًا إنشاء ملف بشكل ديناميكي وإرسالها مباشرة إلى متصفح العميل. للقيام بذلك، استخدم نسخة محملة إضافية من طريقة [**Save**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) التي تقبل المعلمات التالية:  

- كائن استجابة جافا سكريبت.  
- اسم الملف.  
- [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/)، نوع إعلان المحتوى النوعي لملف الإخراج.  
- [**SaveOptions**](https://reference.aspose.com/cells/javascript-cpp/saveoptions/)، نوع تنسيق الملف  

يحدد تعداد [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/) ما إذا كان ملف الإرسال إلى المتصفح يوفر خيار الفتح مباشرة في المتصفح أو في تطبيق مرتبط بـ .xls/.xlsx أو امتداد آخر.  

يحتوي التعداد على أنواع الحفظ المحددة مسبقًا التالية:  

|**النوع**|**الوصف**|  
| :- | :- |  
|المرفقات|يُرسل جدول البيانات إلى المستعرض ويُفتح في تطبيق كمرفق مرتبط بامتداد .xls/.xlsx أو امتدادات أخرى|  
|مضمن|يُرسل المستند إلى المتصفح ويعرض خيارًا لحفظ جدول البيانات على القرص أو فتحه داخل المتصفح|  

### **ملفات XLS**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Save XLS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsSaveOptions, Utils } = AsposeCells;

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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Simulate the JavaScript "response" which is null in this example
            let response = null;

            if (response != null) {
                // Server-side streaming scenario (not used in browser example)
                // Save in Excel2003 XLS format to response stream with options
                const options = new XlsSaveOptions();
                workbook.save(response, "output.xls", AsposeCells.ContentDisposition.Inline, options);
                response.end();
                document.getElementById('result').innerHTML = '<p style="color: green;">File written to response stream.</p>';
            } else {
                // Browser: save workbook and provide download link
                const options = new XlsSaveOptions();
                const outputData = workbook.save(SaveFormat.Excel97To2003, options);
                const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';
                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved. Click the download link to get the file.</p>';
            }
        });
    </script>
</html>
```  

### **ملفات XLSX**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an Excel file to load or leave empty to create a new workbook. Click "Save as XLSX" to generate and download output.xlsx.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlSaveOptions, Utils } = AsposeCells;

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

            // Load workbook from selected file or create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Save the workbook in XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook generated successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```  

### **ملفات PDF**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as PDF</button>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Prepare PDF save options
            const pdfOptions = new PdfSaveOptions();

            // Save workbook as PDF and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, pdfOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **ملاحظة**  

نظرًا لغياب كائن استجابة قياسي في جافا سكريبت، لا توجد هذه الوظيفة في سكريبت Aspose.Cells for Java عبر ++C. يمكنك الرجوع إلى الكود التالي لحفظ الملف على التدفق، ثم إجراء عمليات على التدفق.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to a memory buffer in XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">File is ready. Click the download link to save the workbook.</p>';
        });
    </script>
</html>
```
