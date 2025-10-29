---
title: إعداد رؤوس وتذييلات مختلفة لصفحات مختلفة باستخدام JavaScript عبر C++
linktitle: ضبط رؤوس وأسافل مختلفة لصفحات مختلفة
type: docs
weight: 35
url: /ar/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: يقدم هذا المقال رمزًا نمونه يُظهر كيفية ضبط رؤوس وتذييلات صفحة إعداد ورقة إكسل برمجياً باستخدام Aspose.Cells for JavaScript عبر C++. تعيين رؤوس وتذييلات للصفحات الأولى، الفردية، الزوجية.
keywords: تعيين رؤوس وتذييلات إكسل للصفحة الأولى JavaScript عبر C++، تعيين رؤوس وتذييلات الصفحات الفردية JavaScript عبر C++، تعيين رؤوس وتذييلات الصفحات الزوجية JavaScript عبر C++
---

{{% alert color="primary" %}}

يدعم MS Excel تعيين رؤوس وتذييلات مختلفة للصفحة الأولى والصفحات الفردية والزوجية منذ Excel 2007.
يدعم Aspose.Cells for JavaScript عبر C++ نفس الميزة.

{{% /alert %}}

## **ضبط رؤوس وأسافل مختلفة في MS Excel**

**![ضبط رؤوس وأسافل مختلفة](difpage.png)**

1. انقر على **تخطيط الصفحة > عناوين الطباعة > رأس/تسفل**.
 1. تحقق من **صفحات فردية ومختلفة** أو **صفحة أولى مختلفة**.
1. أدخل رؤوس وأسافل مختلفة.

## **تعيين رؤوس وتذييلات مختلفة باستخدام Aspose.Cells for JavaScript عبر C++**

تتصرف Aspose.Cells بنفس الطريقة كما تفعل Excel.
1. يعين الأعلام [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) و [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. أدخل رؤوس وأسافل مختلفة.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
