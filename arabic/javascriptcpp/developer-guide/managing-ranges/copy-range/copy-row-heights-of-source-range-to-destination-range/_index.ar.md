---
title: نسخ ارتفاعات الصفوف من النطاق المصدر إلى النطاق الوجهة باستخدام JavaScript عبر C++
linktitle: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة
type: docs
weight: 590
url: /ar/javascript-cpp/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

أحيانًا يحتاج المستخدمون إلى نسخ ارتفاعات الصفوف من نطاق المصدر إلى نطاق الوجهة. يوفر Aspose.Cells for JavaScript عبر C++ تعداد [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) لهذا الغرض. عند تعيين الخاصية [**PasteOptions.pasteType**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/#pasteType--) بقيمة [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/)، سيتم نسخ ارتفاعات جميع الصفوف داخل النطاق المصدر إلى النطاق الوجهة.

{{% /alert %}}

يوضح الكود النموذجي التالي كيفية استخدام تعداد [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) لنسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة. بمجرد فتح ملف Excel الناتج الذي تم إنشاؤه بواسطة هذا الكود في Microsoft Excel، ستلاحظ أن ارتفاعات الصفوف في النطاق الوجهة مطابقة تمامًا لارتفاعات النطاق المصدر.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Copy Row Heights Between Ranges</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteOptions, PasteType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Creating a new workbook
            const workbook = new Workbook();

            // Source worksheet (first worksheet)
            const srcSheet = workbook.worksheets.get(0);

            // Add destination worksheet
            const dstSheet = workbook.worksheets.add("Destination Sheet");

            // Set the row height of the 4th row (index 3). This row height will be copied to destination range
            srcSheet.cells.rows.get(3).height = 50;

            // Create source range to be copied
            const srcRange = srcSheet.cells.createRange("A1:D10");

            // Create destination range in destination worksheet
            const dstRange = dstSheet.cells.createRange("A1:D10");

            // PasteOptions, we want to copy row heights of source range to destination range
            const opts = new PasteOptions();
            opts.pasteType = PasteType.RowHeights;

            // Copy source range to destination range with paste options
            dstRange.copy(srcRange, opts);

            // Write informative message in cell D4 of destination worksheet
            const infoCell = dstSheet.cells.get("D4");
            infoCell.value = "Row heights of source range copied to destination range";

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
