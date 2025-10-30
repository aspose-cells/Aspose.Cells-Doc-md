---
title: Determina se una forma è una forma Art Smart con JavaScript tramite C++
linktitle: Determinare se la forma è una forma di arte intelligente
type: docs
weight: 400
url: /it/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Impara come determinare se una forma in Excel è una forma Art Smart usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**  

Le forme Smart Art sono forme speciali in Microsoft Excel che consentono di creare diagrammi complessi automaticamente. Puoi verificare se la forma è una forma smart art o una forma normale usando la proprietà [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--).  

## **Determinare se la forma è una forma SmartArt**  

Il seguente esempio di codice carica il [file Excel di esempio](55541792.xlsx) contenente una forma smart art come mostrato in questo screenshot. Successivamente stampa il valore della proprietà [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) della prima forma. Si prega di consultare l'output della console del codice di esempio fornito di seguito.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Output della console**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
