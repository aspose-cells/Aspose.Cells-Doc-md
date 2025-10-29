---
title: Créer une entrée de signet PDF pour la feuille de graphique avec JavaScript via C++
linktitle: Créer une entrée PdfBookmark pour la feuille de graphique
type: docs
weight: 50
url: /fr/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Apprendre à créer une entrée PdfBookmarkEntry pour les feuilles de graphique en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Auparavant, Aspose.Cells créerait [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) pour une feuille normale. Mais désormais, Aspose.Cells peut également créer [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) pour les feuilles de graphique. Étant donné qu'une feuille de graphique ne possède pas d'autres cellules sauf la cellule A1, elle créera un [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) uniquement pour la cellule A1.  

## **Créer une entrée PdfBookmark pour une feuille de graphique**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767756.xlsx) qui contient quatre feuilles. Deux d'entre elles sont des feuilles normales et les deux autres sont des feuilles de graphique. Il crée quatre entrées de signet comme suit  

- Signet-I  
- Signet-II-Graph1  
- Signet-III  
- Signet-IV-Graph2  

La capture d'écran suivante montre le [PDF de sortie](61767757.pdf) généré par le code d'exemple pour référence.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF Bookmark Entry for Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfBookmarkEntry, PdfSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access all four worksheets
            const sheet1 = workbook.worksheets.get(0);
            const sheet2 = workbook.worksheets.get(1);
            const sheet3 = workbook.worksheets.get(2);
            const sheet4 = workbook.worksheets.get(3);

            // Create Pdf Bookmark Entry for Sheet1
            const ent1 = new PdfBookmarkEntry();
            ent1.destination = sheet1.cells.get("A1");
            ent1.text = "Bookmark-I";

            // Create Pdf Bookmark Entry for Sheet2 - Chart
            const ent2 = new PdfBookmarkEntry();
            ent2.destination = sheet2.cells.get("A1");
            ent2.text = "Bookmark-II-Chart1";

            // Create Pdf Bookmark Entry for Sheet3
            const ent3 = new PdfBookmarkEntry();
            ent3.destination = sheet3.cells.get("A1");
            ent3.text = "Bookmark-III";

            // Create Pdf Bookmark Entry for Sheet4 - Chart
            const ent4 = new PdfBookmarkEntry();
            ent4.destination = sheet4.cells.get("A1");
            ent4.text = "Bookmark-IV-Chart2";

            // Arrange all Bookmark Entries
            const lst = [];
            lst.push(ent2);
            lst.push(ent3);
            lst.push(ent4);

            // Create Pdf Save Options with Bookmark Entries
            const opts = new PdfSaveOptions();
            opts.bookmark = ent1;

            // Save the output Pdf
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreatePdfBookmarkEntryForChartSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
