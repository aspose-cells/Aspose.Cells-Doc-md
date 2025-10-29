---
title: Fonctionnalités de mise en page avec JavaScript via C++
linktitle: Fonctionnalités de mise en page
type: docs
weight: 60
url: /fr/javascript-cpp/page-setup-features/
description: Explorer les fonctionnalités de mise en page en utilisant Aspose.Cells for JavaScript via C++. Apprenez comment configurer les dimensions de la page, les orientations et les paramètres.
keywords: Fonctionnalités de mise en page JavaScript via C++, configurer les dimensions de la page JavaScript via C++, paramètres d orientation de la page JavaScript via C++
---

## **Introduction**
Avec Aspose.Cells for JavaScript via C++, vous pouvez manipuler diverses fonctionnalités de mise en page d'un classeur Excel. Ces fonctionnalités incluent la définition de la taille de la page, l'orientation, les marges, et plus encore. Une configuration appropriée de ces fonctionnalités permet une meilleure impression et visualisation.

## ** Définir la taille et l'orientation de la page**
Vous pouvez spécifier la taille de la page et l'orientation d'une feuille de calcul en utilisant la classe `PageSetup`. Elle offre diverses propriétés pour gérer les dimensions et la disposition de la page.

### **Code d'exemple**
Voici un exemple de code illustrant comment définir la taille et l'orientation de la page.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Réglage des marges**
Vous pouvez également définir les marges de la page en utilisant la même classe `PageSetup`. Les marges peuvent être ajustées pour les côtés gauche, droit, haut et bas.

### **Code d'exemple**
Voici comment vous pouvez définir les marges d'une feuille de calcul.
