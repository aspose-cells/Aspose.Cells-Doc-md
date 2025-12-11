---
title: Render Office Add-Ins while converting Excel to PDF with JavaScript via C++
linktitle: Render Office Add-Ins while converting Excel to PDF
type: docs
weight: 100
url: /javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Possible Usage Scenarios**

Earlier, Aspose.Cells could not render Office Add‑Ins when an Excel file is saved to PDF format. Now Aspose.Cells renders them correctly. You do not need to use any special method or property to render Office Add‑Ins in the output PDF. Just save your Excel file to PDF format, and it will render Office Add‑Ins.

## **Render Office Add-Ins while converting Excel to PDF**

The following sample code saves the [sample Excel file](60489769.xlsx) which contains the Office Add‑Ins. Please see the [output PDF generated with the previous version, i.e., 17.11](60489770.pdf) and the [output PDF generated with the newer version, i.e., 17.12 and onward](60489771.pdf). The previous version’s output PDF is blank, but the newer version’s output PDF shows the Office Add‑Ins.

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```