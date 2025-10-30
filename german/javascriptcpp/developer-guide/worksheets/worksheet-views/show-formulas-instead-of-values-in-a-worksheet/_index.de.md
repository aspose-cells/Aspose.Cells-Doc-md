---
title: Formeln anstelle von Werten in einem Arbeitsblatt mit JavaScript via C++ anzeigen
linktitle: Statt Werte in einem Arbeitsblatt Formeln anzeigen
type: docs
weight: 20
url: /de/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Dieser Artikel bietet Beispielcode für die Verwendung der JavaScript API über C++, um Formeln programmgesteuert statt Werte in einem Excel Arbeitsblatt oder einer Tabelle anzuzeigen.
---

{{% alert color="primary" %}}

Es ist möglich, in Microsoft Excel anstelle der berechneten Werte die **Formeln**-Option aus der **Formeln**-Registerkarte anzuzeigen. Wenn Formeln angezeigt werden, zeigt Microsoft Excel die Formeln im Arbeitsblatt an. Sie können das Gleiche mit Aspose.Cells for JavaScript via C++ erreichen.

{{% /alert %}}

Aspose.Cells bietet eine Eigenschaft [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--). Stellen Sie sie auf **true** ein, um Microsoft Excel anzuweisen, Formeln anzuzeigen.

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
