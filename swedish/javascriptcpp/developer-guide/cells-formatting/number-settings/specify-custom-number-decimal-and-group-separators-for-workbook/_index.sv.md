---
title: Ange anpassade decimal och grupptalsavskiljare för arbetsboken
linktitle: Ange anpassade decimal och grupptalsavskiljare för arbetsboken
type: docs
weight: 110
url: /sv/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Ändra nummerdecimala och gruppseparatorer i Excel med Aspose.Cells for JavaScript via C++.
keywords: ange anpassad decimalseparator excel JavaScript via C++, ange anpassad gruppseparator excel JavaScript via C++, ändra decimal och gruppseparator i excel JavaScript via C++
---

{{% alert color="primary" %}}

I Microsoft Excel kan du ange anpassade decimal- och tusentalsavskiljare istället för att använda systemavskiljare från **Avancerade Excel-alternativ** enligt skärmbilden nedan.

Aspose.Cells tillhandahåller metoderna [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) och [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) för att ställa in anpassade separatorer för formatering/parsing av nummer.

{{% /alert %}}

## **Ange anpassade avskiljare i Microsoft Excel**

Följande skärmbild visar **Avancerade Excel-alternativ** och markerar avsnittet för att ange **Anpassade avskiljare**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specifika anpassade separatorer med Aspose.Cells for JavaScript via C++**

Följande exempelkod illustrerar hur man anger anpassade avskiljare med Aspose.Cells API. Det specificerar anpassade decimal- och grupptalsavskiljare som punkt och mellanslag respektive.

### JavaScript-kod för att ange anpassade nummerdecimala och gruppseparatorer

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

            // Save workbook as pdf
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
