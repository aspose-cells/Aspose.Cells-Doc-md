---
title: Obtenir la largeur et la hauteur du papier de la mise en page de la feuille avec JavaScript via C++
linktitle: Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul
type: docs
weight: 50
url: /fr/javascript-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Découvrez comment obtenir la largeur et la hauteur du papier de la mise en page de la feuille Excel en utilisant JavaScript via C++ de manière programmatique.
keywords: Largeur du papier de la mise en page Excel JavaScript via C++, Hauteur du papier de la mise en page Excel JavaScript via C++
---

## **Scénarios d'utilisation possibles**

Parfois, vous devez connaître la largeur et la hauteur du papier tel qu’il a été défini dans la mise en page de la feuille de calcul. Veuillez utiliser les propriétés [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) et [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--) à cette fin.

## **Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul**

Le code d’échantillon suivant explique l’utilisation des propriétés [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) et [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--). Il change d’abord la taille du papier en *A2*, puis trouve la largeur et la hauteur du papier, puis le change en *A3*, *A4*, *Letter* et trouve respectivement la largeur et la hauteur du papier.

### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Paper Size Example</h1>
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

            // If a file is selected, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set paper size to A2 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA2;
            console.log("PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A3 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA3;
            console.log("PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A4 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
            console.log("PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to Letter and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperLetter;
            console.log("PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            const outputLines = [
                "PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight
            ];

            document.getElementById('result').innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```

### **Sortie console**



{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
