---
title: Implémentez le système de date 1904 avec JavaScript via C++
description: Aspose.Cells est une bibliothèque JavaScript pour travailler avec des fichiers de feuille de calcul. Elle supporte la mise en œuvre du système de date 1904, permettant aux utilisateurs de calculer et de formater en fonction du système de date du 1er janvier 1904. Cet article décrit comment implémenter le système de date 1904 en utilisant la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, système de date 1904, feuille de calcul, calcul, formatage, JavaScript via C++
type: docs
weight: 7000
url: /fr/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel supporte deux systèmes de date : le système de date 1900 (le système de date par défaut implémenté dans Excel pour Windows) et le système de date 1904. Le système de date 1904 est généralement utilisé pour assurer la compatibilité avec les fichiers Excel Macintosh et est le système par défaut si vous utilisez Excel pour Macintosh. Vous pouvez définir le système de date 1904 pour les fichiers Excel en utilisant Aspose.Cells for JavaScript via C++. 

{{% /alert %}} 

Pour implémenter le système de date 1904 dans Microsoft Excel (par exemple, Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Calcul**.
1. Sélectionnez l'option **Système de date 1904**.
1. Cliquez sur **OK**.

|**Sélection du système de date 1904 dans Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Consultez le code source suivant sur la manière d'accomplir ceci en utilisant les API Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
