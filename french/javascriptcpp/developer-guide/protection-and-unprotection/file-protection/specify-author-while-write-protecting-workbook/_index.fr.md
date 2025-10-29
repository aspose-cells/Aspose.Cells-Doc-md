---
title: Spécifier l auteur lors de la protection en écriture du classeur avec JavaScript via C++
linktitle: Spécifier l auteur lors de la protection par mot de passe du classeur
type: docs
weight: 40
url: /fr/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Spécifier un nom d auteur lors de la protection en écriture d un classeur à l aide de Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier un nom d'auteur lors de la protection en écriture de votre classeur utilisant l'API Aspose.Cells. Veuillez utiliser la propriété [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) à cet effet.

## **Spécifier l'auteur lors de la protection en écriture du classeur**

Le code d'exemple suivant explique l'utilisation de la propriété [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--). Le code crée un classeur vide, le protège par mot de passe, spécifie le nom de l'auteur et l'enregistre en tant que [fichier Excel de sortie](67338582.xlsx). La capture d'écran suivante illustre l'effet du code d'exemple sur le fichier Excel de sortie pour votre référence.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
