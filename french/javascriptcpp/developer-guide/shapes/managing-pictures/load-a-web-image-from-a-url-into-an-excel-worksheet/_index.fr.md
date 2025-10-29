---
title: Charger une image Web à partir d une URL dans une feuille de calcul Excel avec JavaScript via C++
linktitle: Charger une image web à partir d une URL dans une feuille de calcul Excel
type: docs
weight: 30
url: /fr/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Comment convertir une image à partir d une URL en une image Excel réelle en utilisant Aspose.Cells for JavaScript via C++.
keywords: excel afficher l image depuis l URL, excel url vers image, afficher l image dans excel à partir de l url, excel insérer une image depuis url, convertir url en image dans excel, image excel depuis url, charger image depuis url dans excel, JavaScript, Excel
---

## Charger une image à partir d'une URL dans une feuille de calcul Excel

Aspose.Cells for JavaScript via C++ fournit un moyen simple et facile de charger des images depuis des URLs dans les feuilles de calcul Excel. Cet article explique comment télécharger les données d'image dans un flux, puis l'insérer dans la feuille en utilisant l'API Aspose.Cells. Avec cette méthode, les images font partie intégrante du fichier Excel et ne sont pas téléchargées à chaque ouverture de la feuille.

## Code d'exemple

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Il peut arriver que vous souhaitiez toujours obtenir l'image mise à jour à partir d'une URL. Pour cela, vous pouvez suivre les instructions données dans l'article [Insérer une image liée à partir d'une adresse Web](/cells/fr/javascript-cpp/insert-a-linked-picture-from-web-address/). En suivant cette méthode, l'image est chargée depuis l'URL à chaque ouverture de la feuille.
{{% /alert %}}
