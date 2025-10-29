---
title: Définir la couleur de l onglet de la feuille de calcul avec JavaScript via C++
linktitle: Définir la couleur de l onglet de la feuille de calcul
type: docs
weight: 120
url: /fr/javascript-cpp/set-worksheet-tab-color/
description: Cet article présente un code d exemple qui définit la couleur de l onglet de la feuille Excel de manière programmatique en utilisant JavaScript via C++.
keywords: définir la couleur de l onglet Excel JavaScript via C++, code pour définir la couleur de l onglet Excel JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de changer la couleur des onglets de feuille de calcul individuels pour les rendre plus visibles par rapport au reste. Par exemple, vous pouvez mettre Dépenses en rouge, Ventes en vert, Actifs en bleu, etc.

{{% /alert %}}
## **Définition de la couleur de l'onglet de feuille de calcul avec Microsoft Excel**
1. Cliquez avec le bouton droit sur un onglet dans la feuille d'onglets en bas de la feuille de calcul actuelle.
1. Sélectionnez **Couleur d'onglet**.
1. Sélectionnez une couleur dans la palette.
1. Cliquez sur **OK**.
## **Définir la couleur de l'onglet de la feuille de calcul avec Aspose.Cells**
Le code d'exemple ci-dessous montre comment définir la couleur de l'onglet avec Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
