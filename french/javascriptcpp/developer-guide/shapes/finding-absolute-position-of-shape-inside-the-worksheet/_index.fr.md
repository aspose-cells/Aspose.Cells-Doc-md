---
title: Trouver la position absolue d une forme à l intérieur de la feuille de calcul avec JavaScript via C++
linktitle: Trouver la position absolue de la forme dans la feuille de calcul
type: docs
weight: 8000
url: /fr/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Apprenez à trouver la position absolue d une forme à l intérieur d une feuille en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de connaître la position absolue d'une forme dans une feuille de calcul. Aspose.Cells for JavaScript via C++ fournit les propriétés [**Shape.leftToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#leftToCorner--) et [**Shape.topToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#topToCorner--) à cet effet. Ces propriétés renvoient la position absolue de la forme dans la feuille en pixels.

{{% /alert %}}

Le code d'exemple suivant affiche la position absolue de la première forme dans la feuille de calcul en pixels. Le code d'exemple affiche la sortie console suivante :

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shape Position</title>
    </head>
    <body>
        <h1>Get Shape Absolute Position</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file inside the workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Displays the absolute position of the shape
            const left = shape.leftToCorner;
            const top = shape.topToCorner;
            const message = `Absolute Position of this Shape is (${left} , ${top})`;
            console.log(message);
            resultDiv.innerHTML = `<p>${message}</p>`;
        });
    </script>
</html>
```
