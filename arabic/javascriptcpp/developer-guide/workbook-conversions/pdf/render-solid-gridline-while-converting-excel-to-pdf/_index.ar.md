---
title: عرض شبكة صلبة أثناء تحويل Excel إلى PDF باستخدام JavaScript عبر C++
linktitle: عرض خطوط الشبكة الصلبة أثناء تحويل إكسل إلى PDF
type: docs
weight: 390
url: /ar/javascript-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: تعلم كيفية عرض شبكات صلبة أثناء تحويل Excel إلى PDF باستخدام Aspose.Cells for JavaScript عبر C++. 
keywords: عرض شبكة صلبة إلى PDF JavaScript عبر C++, تحويل Excel إلى PDF مع شبكة صلبة باستخدام JavaScript عبر C++, PdfSaveOptions للشبكة الصلبة JavaScript عبر C++ 
---

للتوافق مع الإصدارات القديمة، تقوم Aspose.Cells بشكل افتراضي برسم خطوط الشبكة كنقطة أثناء تحويل إكسيل إلى PDF. ومع ذلك، يعرّف إكسيل الحديثة خطوط الشبكة كخطوط صلبة اليوم.

باستخدام الخيار [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)، يمكن لـ Aspose.Cells for JavaScript عبر C++ أيضًا عرض خطوط الشبكة كخطوط صلبة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Generate PDF with Gridlines</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links (as in original JavaScript example)
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an empty Workbook
            const wb = new Workbook();

            // Prepare data
            const worksheet = wb.worksheets.get(0);
            const cell = worksheet.cells.get("D9");
            cell.value = "gridline";

            // Enable to print gridline
            worksheet.pageSetup.printGridlines = true;

            // Set to render gridline as solid line
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.gridlineType = AsposeCells.GridlineType.Hair;

            // Save the pdf file with PdfSaveOptions
            const outputData = wb.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_Cs.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

![solid-gridline.png](solid-gridline.png)
