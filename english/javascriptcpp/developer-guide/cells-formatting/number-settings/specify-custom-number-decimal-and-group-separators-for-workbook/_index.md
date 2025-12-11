---
title: Specify Custom Number Decimal and Group Separators for Workbook
linktitle: Specify Custom Number Decimal and Group Separators for Workbook
type: docs
weight: 110
url: /javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Change number decimal and group separators in Excel using Aspose.Cells for JavaScript via C++.
keywords: specify custom decimal separator excel JavaScript via C++, specify custom group separator excel JavaScript via C++, change decimal and group separator excel JavaScript via C++
---

{{% alert color="primary" %}}

In Microsoft Excel, you can specify the Custom Decimal and Thousands Separators instead of using System Separators from the **Advanced Excel Options** as shown in the screenshot below.

Aspose.Cells provides the [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) and [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) methods to set the custom separators for formatting/parsing numbers.

{{% /alert %}}

## **Specifying Custom Separators using Microsoft Excel**

The following screenshot shows the **Advanced Excel Options** and highlights the section to specify the **Custom Separators**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specifying Custom Separators using Aspose.Cells for JavaScript via C++**

The following sample code illustrates how to specify the custom separators using the Aspose.Cells API. It specifies the Custom Number Decimal and Group Separators as a dot and a space, respectively.

### JavaScript code to specify custom number decimal and group separators

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```