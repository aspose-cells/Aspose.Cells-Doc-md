---
title: Trovare la posizione assoluta della forma all’interno del foglio di lavoro con JavaScript tramite C++
linktitle: Trova la posizione assoluta della forma all interno del foglio di lavoro
type: docs
weight: 8000
url: /it/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Impara come trovare la posizione assoluta di una forma all’interno di un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}}

A volte, è necessario conoscere la posizione assoluta di una forma in un foglio di lavoro. Aspose.Cells for JavaScript tramite C++ fornisce le proprietà [**Shape.leftToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#leftToCorner--) e [**Shape.topToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#topToCorner--) per questo scopo. Queste proprietà restituiscono la posizione assoluta della forma all’interno del foglio di lavoro in pixel.

{{% /alert %}}

Il codice di esempio seguente visualizza la posizione assoluta della prima forma nel foglio di lavoro in pixel. Il codice di esempio visualizza l'output della console seguente:

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
