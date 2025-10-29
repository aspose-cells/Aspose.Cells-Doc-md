---
title: تعيين الهوامش مع JavaScript عبر C++
linktitle: ضبط الهوامش
type: docs
weight: 20
url: /ar/javascript-cpp/setting-margins/
description: في هذا المقال، ستتعلم كيفية تعيين هوامش ورقة عمل Excel باستخدام رمز عينة. تعلم أيضًا كيفية تعيين الهوامش برمجيًا لمركز الصفحة، الرأس، والتذييل باستخدام واجهة برمجة التطبيقات JavaScript عبر C++.
keywords: تعيين هامش ورقة عمل Excel إلى المركز JavaScript عبر C++, تعيين هامش الرأس والتذييل في ورقة العمل JavaScript عبر C++
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تماماً خيارات إعداد الصفحة في Microsoft Excel. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة للوظائف للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

{{% /alert %}}

## **ضبط الهوامش**

 يوفر Aspose.Cells for JavaScript عبر C++ فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

 تُستخدم الخاصية [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) لضبط إعدادات تخطيط الصفحة لورقة العمل. السمة [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) هي كائن من فئة [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) التي تمكّن المطورين من ضبط إعدادات تخطيط الصفحة المختلفة لورقة عمل مطبوعة. توفر فئة [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) خصائص وأساليب مختلفة تُستخدم لضبط إعدادات تخطيط الصفحة.

### **هوامش الصفحة**

ضبط هوامش الصفحة (اليسار، اليمين، الأعلى، الأسفل) باستخدام أعضاء فئة [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--). تُدرج بعض الأعضاء أدناه والتي تُستخدم لتحديد هوامش الصفحة:

- [**PageSetup.leftMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#leftMargin--)
- [**PageSetup.rightMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#rightMargin--)
- [**PageSetup.topMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#topMargin--)
- [**PageSetup.bottomMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#bottomMargin--)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Page Margins Example</title>
    </head>
    <body>
        <h1>Set Page Margins Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                // Proceed with a new empty workbook if no file selected
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            pageSetup.bottomMargin = 2;
            pageSetup.leftMargin = 1;
            pageSetup.rightMargin = 1;
            pageSetup.topMargin = 3;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetMargins_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page margins set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **توسيط على الصفحة**

 من الممكن تمركز شيء ما بشكل أفقي وعمودي على الصفحة. لهذا، هناك بعض الأعضاء المفيدة في فئة [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)، [**PageSetup.centerHorizontally**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerHorizontally--) و [**PageSetup.centerVertically**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerVertically--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Center On Page</title>
    </head>
    <body>
        <h1>Center On Page Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // Create a workbook object (blank workbook)
            const workbook = new Workbook();

            // Get the worksheets in the workbook
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pagesetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Center on page Horizontally and Vertically
            pageSetup.centerHorizontally = true;
            pageSetup.centerVertically = true;

            // Save the Workbook in Excel 97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **هوامش الرأس والتذييل**

تعيين هوامش الرأس والتذييل مع أعضاء فئة [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) مثل [**PageSetup.headerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerMargin--) و [**PageSetup.footerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerMargin--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Header/Footer Margins</title>
    </head>
    <body>
        <h1>Set Header/Footer Margins Example</h1>
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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Get the worksheets collection
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pageSetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Header / Footer margins (converted from setHeaderMargin/setFooterMargin)
            pageSetup.headerMargin = 2;
            pageSetup.footerMargin = 2;

            // Save the Workbook as Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
