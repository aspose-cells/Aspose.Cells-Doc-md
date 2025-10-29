---
title: Obtenir la validation de la cellule dans les fichiers ODS
type: docs
weight: 180
url: /fr/javascript-cpp/get-cell-validation-in-ods-files/
description: Apprenez comment obtenir la validation des cellules dans les fichiers ODS via le script Aspose.Cells for Java en C++ API.
keywords: Obtenez la validation de cellule JavaScript via C++, Obtenir la validation de cellule JavaScript via C++
---

## **Obtenir la validation de la cellule dans les fichiers ODS**  

Avec Aspose.Cells for JavaScript via C++, vous pouvez obtenir la validation appliquée à une cellule dans les fichiers ODS. Pour cela, l'API fournit la propriété [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) de la classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).  

L'exemple de code suivant illustre l'utilisation de la propriété [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) en chargeant le fichier [source ODS](101089354.ods) et en lisant la validation de la cellule A9.  

### **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
