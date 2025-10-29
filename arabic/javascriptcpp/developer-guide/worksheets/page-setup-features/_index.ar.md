---
title: خصائص إعداد الصفحة مع جافا سكريبت عبر C++
linktitle: ميزات إعداد الصفحة
type: docs
weight: 60
url: /ar/javascript-cpp/page-setup-features/
description: استكشف ميزات إعداد الصفحة باستخدام Aspose.Cells for JavaScript عبر C++. تعلم كيفية تكوين أبعاد الصفحة، الاتجاهات، والإعدادات.
keywords: ميزات إعداد الصفحة جافا سكريبت عبر C++، تكوين أبعاد الصفحة جافا سكريبت عبر C++، إعدادات اتجاه الصفحة جافا سكريبت عبر C++
---

## **مقدمة**
باستخدام Aspose.Cells for JavaScript عبر C++، يمكنك تعديل ميزات إعداد الصفحة المختلفة لمصنف إكسل. تشمل هذه الميزات تعيين حجم الصفحة، الاتجاه، الهوامش، والمزيد. يتيح التكوين الصحيح لهذه الميزات تحسين تجربة الطباعة والمشاهدة.

## **ضبط حجم الصفحة والاتجاه**
يمكنك تحديد حجم الصفحة واتجاهها في ورقة العمل باستخدام فئة `PageSetup`. توفر خصائص متعددة لإدارة أبعاد الصفحة وتخطيطها.

### **مثال على الكود**
إليك مثال على رمز يوضح كيفية ضبط حجم الصفحة والاتجاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ضبط الهوامش**
يمكنك أيضًا ضبط الهوامش للصفحة باستخدام نفس فئة `PageSetup`. يمكن تعديل الهوامش للجوانب اليسار، اليمين، الأعلى، والأسفل.

### **مثال على الكود**
إليك كيفية ضبط هوامش ورقة العمل.
