---
title: Visa Formler istället för Värden i ett Arbetssheet med JavaScript via C++
linktitle: Visa formler istället för värden i ett kalkylblad
type: docs
weight: 20
url: /sv/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Denna artikel ger exempel på kod för att använda JavaScript API via C++ för att programmässigt visa formler snarare än värden i ett Excel ark eller kalkylblad.
---

{{% alert color="primary" %}}

Det är möjligt att visa formler istället för beräknade värden i Microsoft Excel med hjälp av alternativet **Visa Formler** från fliken **Formler**. När formler visas visar Microsoft Excel formler i arket. Du kan uppnå samma sak med Aspose.Cells for JavaScript via C++.

{{% /alert %}}

Aspose.Cells tillhandahåller en egenskap [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--). Sätt den till **true** för att göra Microsoft Excel att visa formler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
