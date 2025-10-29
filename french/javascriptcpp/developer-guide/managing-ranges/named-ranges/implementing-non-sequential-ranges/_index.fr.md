---
title: Implémentation de plages non séquentielles avec JavaScript via C++
linktitle: Mise en œuvre de plages non séquentielles
type: docs
weight: 700
url: /fr/javascript-cpp/implementing-non-sequential-ranges/
description: Apprenez comment créer des plages non séquentielles nommées avec Aspose.Cells for JavaScript via C++. Utilisez efficacement des plages de cellules non adjacentes.
---

{{% alert color="primary" %}} 

Normalement, les plages nommées sont rectangulaires avec des cellules continues et adjacentes. Mais parfois, vous pouvez avoir besoin d'utiliser une plage de cellules non séquentielle où les cellules ne sont pas adjacentes. Aspose.Cells for JavaScript via C++ prend en charge la création d'une plage nommée avec des cellules non adjacentes.

{{% /alert %}} 

L'exemple de code ci-dessous montre comment créer une plage non séquentielle nommée avec Aspose.Cells for JavaScript via C++.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add NonSequenced Range Name</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a Name for non sequenced range
            const index = workbook.worksheets.names.add("NonSequencedRange");

            const name = workbook.worksheets.names.get(index);

            // Creating a non sequence range of cells
            name.refersTo = "=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6";

            // Saving the workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and name added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
