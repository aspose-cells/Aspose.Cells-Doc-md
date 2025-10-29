---
title: Sauts de ligne et retour à la ligne du texte
linktitle: Sauts de ligne et retour à la ligne du texte
description: Comment mettre en œuvre le saut de ligne de texte et le renvoi à la ligne dans l utilisation de la bibliothèque Aspose.Cells en JavaScript via C++. En utilisant la bibliothèque Aspose.Cells, vous pouvez facilement insérer du texte dans les cellules et définir la méthode de saut de ligne, comme le saut de ligne manuel, le saut de ligne automatique, etc. Ce document détaille comment implémenter ces fonctionnalités et fournit un code d exemple pour référence.
keywords: Aspose.Cells, sauts de ligne, retours à la ligne, mise en page du texte JavaScript via C++
type: docs
weight: 60
url: /fr/javascript-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}
Pour vous assurer que le texte dans une cellule peut être lu, des sauts de ligne explicites et un retour à la ligne du texte peuvent être appliqués. Le retour à la ligne du texte transforme une ligne en plusieurs dans une cellule, tandis que les sauts de ligne explicites insérés les mettent exactement où vous le souhaitez.
{{% /alert %}}

## **Pour retourner le texte dans une cellule**
 Pour sauter à la ligne dans une cellule, utilisez la méthode [**Aspose.Cells.Style.isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook
            }

            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cell = ws.cells;

            // Increase the width of First Column Width
            cell.columns.get(0).width = 35;

            // Increase the height of first row
            cell.rows.get(0).height = 36;

            // Add Text to the First Cell
            const firstCell = cell.checkCell(0, 0);
            firstCell.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Pour utiliser des sauts de ligne explicites**
 Vous pouvez utiliser '\n' en JavaScript pour insérer des sauts de ligne explicites dans une cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // No file selected - create a new workbook
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 65;

            // Add Text to the First Cell with Explicit Line Breaks
            const firstCell = cells.checkCell(0, 0);
            firstCell.putValue("I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
