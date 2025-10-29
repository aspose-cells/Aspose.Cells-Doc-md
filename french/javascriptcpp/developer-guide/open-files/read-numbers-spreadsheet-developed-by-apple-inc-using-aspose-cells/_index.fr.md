---
title: Lire des feuilles de calcul Numbers développées par Apple Inc. en utilisant Aspose.Cells for JavaScript via C++
linktitle: Lire Numbers Spreadsheet Developpé par Apple Inc. en utilisant Aspose.Cells
type: docs
weight: 140
url: /fr/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Apprenez comment lire des feuilles Numbers développées par Apple Inc. en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Scénarios d'utilisation possibles**

Numbers est une application de feuille de calcul développée par Apple Inc. Aspose.Cells peut lire les fichiers Numbers, mais ne supporte pas l’écriture dans ceux-ci. Il peut lire les données, le style, et les formules des fichiers Numbers.

## ** Lire des feuilles Numbers développées par Apple Inc. en utilisant Aspose.Cells for JavaScript via C++**

Le code d’exemple suivant charge le [Exemple de feuille Numbers](sampleNumbersByAppleInc.numbers) et le convertit en [Format PDF de sortie](outputNumbersByAppleInc.pdf). Vous devrez utiliser la classe [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) et spécifier [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) comme paramètre dans son constructeur pour le charger avec succès. Téléchargez-les tous deux depuis les liens donnés. Vous pouvez essayer le code avec n’importe quelle feuille Numbers. Veuillez également lire les commentaires du code pour plus d’aide.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
