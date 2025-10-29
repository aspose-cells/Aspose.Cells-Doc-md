---
title: Fusionner ou dissocier une plage de cellules avec JavaScript via C++
linktitle: Fusionner ou séparer une plage de cellules
type: docs
weight: 190
url: /fr/javascript-cpp/merge-or-unmerge-range-of-cells/
description: Fusionner et défaire la fusion de cellules dans une plage dans Excel avec JavaScript via C++.
keywords: Fusionner et défaire la fusion de cellules en JavaScript dans une plage, fusionner et défaire la fusion de cellules avec JavaScript, fusionner et défaire la fusion de cellules dans une plage avec JavaScript, fusionner et défaire la fusion de cellules dans Excel en utilisant JavaScript, fusionner et défaire la fusion de cellules dans Excel avec JavaScript, JavaScript pour fusionner et défaire la fusion de cellules dans Excel, fusionner des cellules dans Excel en JavaScript, défaire la fusion de cellules dans Excel en JavaScript, fusionner des cellules dans une plage avec JavaScript
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour fusionner ou diviser une plage de cellules. Aspose.Cells fournit les méthodes [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) et [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) à cette fin. Cet article explique comment fusionner une plage de cellules dans une cellule unique.

{{% /alert %}}

## **Exemple**

Le code d'échantillon suivant crée d'abord une plage - A1:D4 - puis fusionne les cellules de la plage en une seule cellule en utilisant la méthode [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--). De même, vous pouvez diviser des cellules en créant une plage et en appelant la méthode [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create and Merge Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeInitialized = false;
        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeInitialized = true;
            runButton.disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait.</p>';
                return;
            }

            // Creating a workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range
            const range = worksheet.cells.createRange("A1:D4");

            // Merge range into a single cell
            range.merge();

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range merged successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
