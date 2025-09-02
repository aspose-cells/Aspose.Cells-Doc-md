---
title: Specifying DBNum Custom Pattern Formatting
linktitle: Specifying DBNum Custom Pattern Formatting
description: Aspose.Cells is a library for JavaScript via C++ that supports formatting dates and numbers using custom formatting patterns. This article shows how to specify the 'dbnum' custom format pattern for better control over number display.
keywords: Aspose.Cells, JavaScript via C++, electronic spreadsheet, custom format pattern, formatting, 'dbnum', control display
type: docs
weight: 110
url: /javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Possible Usage Scenarios**

Aspose.Cells for JavaScript via C++ supports the *DBNum* custom pattern formatting. For example, if your cell value is 123 and you specify its custom formatting as [DBNum2][$-804]General then it will be displayed like 壹佰贰拾叁. You can specify your custom formatting of the cell using [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) method and [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) method.

## **Sample Code**

The following sample code illustrates how to specify *DBNum* custom pattern formatting. Please check its [output PDF](43352081.pdf) for more help.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```