---
title: Convertir JSON en CSV avec JavaScript via C++
linktitle: Convertir JSON en CSV
type: docs
weight: 210
url: /fr/javascript-cpp/convert-json-to-csv/
description: Apprenez comment convertir des données JSON en CSV en utilisant Aspose.Cells for JavaScript via C++.
---

## **Convertir JSON en CSV**

Aspose.Cells for JavaScript via C++ supporte la conversion de JSON simple ou imbriqué en CSV. Pour cela, l'API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) offre des options pour la disposition JSON comme [**JsonLayoutOptions.arrayAsTable**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions/#arrayAsTable--) (traite le tableau comme un tableau). La classe [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) traite le JSON en utilisant les options de disposition définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions).

L'exemple de code suivant montre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) pour charger le fichier JSON source et générer le fichier CSV de sortie.

### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON to CSV Example</title>
    </head>
    <body>
        <h1>Import JSON to CSV Example</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const jsonText = await file.text();

            // Create empty workbook
            const workbook = new Workbook();

            // Get Cells from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Set JsonLayoutOptions
            const importOptions = new JsonLayoutOptions();
            importOptions.convertNumericOrDate = true;
            importOptions.arrayAsTable = true;
            importOptions.ignoreTitle = true;

            // Import JSON data into worksheet cells starting at A1 (0,0)
            JsonUtility.importData(jsonText, cells, 0, 0, importOptions);

            // Save Workbook as CSV
            const outputData = workbook.save(SaveFormat.Csv);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleJson_out.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            resultDiv.innerHTML = '<p style="color: green;">JSON imported and CSV prepared. Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
