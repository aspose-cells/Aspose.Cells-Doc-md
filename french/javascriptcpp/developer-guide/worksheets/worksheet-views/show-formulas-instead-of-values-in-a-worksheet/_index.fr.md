---
title: Afficher les formules au lieu des valeurs dans une feuille de calcul avec JavaScript via C++
linktitle: Afficher les formules au lieu des valeurs dans une feuille de calcul
type: docs
weight: 20
url: /fr/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Cet article fournit un code d exemple pour utiliser l API JavaScript via C++ afin d afficher de manière programmatique les formules plutôt que les valeurs dans une feuille ou une feuille de calcul Excel.
---

{{% alert color="primary" %}}

Il est possible d'afficher les formules au lieu des valeurs calculées dans Microsoft Excel en utilisant l'option **Afficher les formules** dans le ruban **Formules**. Lorsqu'elles sont affichées, Excel affiche les formules dans la feuille de calcul. Vous pouvez obtenir le même résultat en utilisant Aspose.Cells for JavaScript via C++.

{{% /alert %}}

Aspose.Cells fournit une propriété [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--). Définissez-la sur **true** pour que Microsoft Excel affiche les formules.

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
