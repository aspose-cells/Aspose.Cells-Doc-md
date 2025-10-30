---
title: Determinar si una Forma es una Forma de Arte Smart con JavaScript a través de C++
linktitle: Determinar si la Forma es una Forma de Arte Inteligente
type: docs
weight: 400
url: /es/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Aprende cómo determinar si una forma en Excel es una forma de Arte Smart usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  

Las formas de arte inteligente son formas especiales en Microsoft Excel que permiten crear diagramas complejos automáticamente. Puedes verificar si la forma es una forma de arte inteligente o una forma normal usando la propiedad [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--).  

## **Determinar si la Forma es una Forma de Arte Inteligente**  

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](55541792.xlsx) que contiene una forma de arte inteligente como se muestra en esta captura de pantalla. Luego imprime el valor de la propiedad [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) de la primera forma. Por favor, consulta la salida de la consola del código de ejemplo a continuación.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Código de muestra**  

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

## **Salida de la consola**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
