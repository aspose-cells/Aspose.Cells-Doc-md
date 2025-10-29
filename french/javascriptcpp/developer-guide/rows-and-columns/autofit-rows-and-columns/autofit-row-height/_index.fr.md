---
title: Ajuster automatiquement la hauteur des lignes lors du chargement d un fichier avec JavaScript via C++
linktitle: Ajuster automatiquement la hauteur de la ligne lorsque le fichier est chargé
type: docs
weight: 120
url: /fr/javascript-cpp/autofit-row-height/
description: Apprenez à ajuster la hauteur des lignes dont la hauteur n est pas personnalisée lors du chargement d’un fichier avec Aspose.Cells for JavaScript via C++.
keywords: Ajuster automatiquement la hauteur des lignes lors du chargement d’un fichier JavaScript via C++, ajuster automatiquement la hauteur des lignes lors de l ouverture d un fichier Excel JavaScript via C++ 
---

## **Scénarios d'utilisation possibles**
La hauteur de la ligne s'ajuste automatiquement au style de police du contenu, mais lorsque la hauteur de la ligne mise en cache ne correspond pas à la hauteur du contenu dans le fichier, MS Excel ajuste automatiquement la hauteur de la ligne lors du chargement du fichier, tandis que Aspose.Cells for JavaScript via C++ ne l'ajustera pas automatiquement pour améliorer les performances. Si vous souhaitez utiliser le programme Aspose.Cells pour faire correspondre automatiquement les hauteurs de ligne lors du chargement de fichiers, vous pouvez y parvenir via le paramètre [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) dans votre code.

Veuillez vous référer à l'image suivante. Nous pouvons observer que la hauteur de la ligne en ligne 11 est de 15, mais Excel a automatiquement ajusté la hauteur de la ligne lors du chargement du fichier.
<br>
<img src="1.png" width=70% />

## **Ajuster la hauteur des lignes en utilisant Aspose.Cells for JavaScript via C++**
Si vous chargez directement le fichier et l'enregistrez au format PDF, les données ne seront pas entièrement affichées dans le PDF parce que sa hauteur de ligne mise en cache n'est que de 15.
<br>
<img src="2.png" width=70% />
<br>
Si vous définissez le paramètre [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) sur true lors du chargement du fichier, alors Aspose.Cells ajustera automatiquement la hauteur des lignes. La hauteur ajustée peut efficacement répondre aux exigences d'affichage du texte.
<br>
<img src="3.png" width=70% />

## **Code Exemple JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
