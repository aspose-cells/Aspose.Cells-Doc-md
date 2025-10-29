---
title: Json avec JavaScript via C++
linktitle: Json
type: docs
weight: 300
url: /fr/javascript-cpp/convert-workbook-to-json/
description: Apprenez comment convertir un classeur Excel en JSON en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Aspose.Cells supporte la conversion d'un classeur en fichier Json (JavaScript Object Notation).
{{% /alert %}}

## **Convertir un classeur Excel en JSON**

L’API Aspose.Cells prend en charge la conversion des feuilles de calcul au format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) pour spécifier des paramètres additionnels lors de l’exportation de la feuille de calcul au format JSON.

L’exemple de code suivant montre comment exporter la feuille de calcul active en JSON en utilisant le membre d’énumération [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json). Voir le code pour convertir le [fichier source](book1.xlsx) en [fichier JSON de sortie](book1.Json) généré par le code à titre de référence.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Convertir CSV en JSON](/cells/fr/javascript-cpp/convert-csv-to-json/)
- [Convertir Excel en JSON](/cells/fr/javascript-cpp/convert-excel-to-json/)
- [Convertir JSON en CSV](/cells/fr/javascript-cpp/convert-json-to-csv/)
- [Convertir JSON en Excel](/cells/fr/javascript-cpp/convert-json-to-excel/)
