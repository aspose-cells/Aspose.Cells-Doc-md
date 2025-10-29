---
title: Détecter le type d hyperlien
type: docs
weight: 160
url: /fr/javascript-cpp/detect-hyperlink-type/
description: Apprenez à détecter le type de lien hypertexte via le Script Aspose.Cells for JavaAPI C++.
keywords: Détecter le type de lien hypertexte JavaScript via C++, Détecter le type de lien hypertexte JavaScript via C++, Obtenir le type de lien hypertexte JavaScript via C++
---

## **Détecter le type de lien hypertexte**

Un fichier Excel peut avoir différents types de liens hypertextes comme externe, référence de cellule, chemin de fichier, etc. Le Script Aspose.Cells for JavaAPI C++ supporte la détection du type de lien hypertexte. Les types de liens hypertextes sont représentés par l'énumération [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). L'énumération [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) comporte les membres suivants.

- Externe : lien externe
- CheminFichier : Chemin local et complet vers des fichiers/dossiers.
- Email : Email
- RéférenceDeCellule : Lien vers une cellule ou plage nommée.

Pour vérifier le type de lien hypertexte, la classe [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) fournit une propriété [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) avec un type de retour [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). Le code ci-dessous illustre l'utilisation de la propriété [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) en utilisant ce [fichier Excel source](94896195.xlsx).

### Code source

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


Ce qui suit est le résultat généré par le code donné ci-dessus.

### Sortie de la Console
