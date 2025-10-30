---
title: Extraer texto de la forma SmartArt tipo engranaje con JavaScript a través de C++
linktitle: Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje
type: docs
weight: 500
url: /es/javascript-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aprende cómo extraer texto de la forma SmartArt tipo engranaje usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**

Aspose.Cells puede extraer texto de la forma SmartArt tipo engranaje. Para hacerlo, primero debes convertir la forma SmartArt en una forma agrupada usando la propiedad [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--). Luego, debes obtener el array de todas las formas individuales que componen la forma agrupada usando la propiedad [**GroupShape.groupedShapes**](https://reference.aspose.com/cells/javascript-cpp/groupshape/#groupedShapes--). Finalmente, puedes iterar todas las formas individuales una por una en un bucle y extraer su texto usando la propiedad [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--).

## **Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje**

El siguiente código de muestra carga el [archivo Excel de muestra](67338483.xlsx) que contiene una Forma de Arte SmartArt de Tipo de Engranaje. Luego extrae el texto de sus formas individuales como se discutió anteriormente. Consulte la salida de la consola del código a continuación para una referencia.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Gear SmartArt Text Example</h1>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Get the result of gear type smart art shape in the form of group shape.
            const groupShape = shape.resultOfSmartArt;

            // Get the list of individual shapes consisting of group shape.
            const shapes = groupShape.groupedShapes;

            // Extract the text of gear type shapes and display them.
            const results = [];
            for (let i = 0; i < shapes.count; i++) {
                const s = shapes.get(i);

                if (s.type === AsposeCells.AutoShapeType.Gear9 || s.type === AsposeCells.AutoShapeType.Gear6) {
                    const text = s.text;
                    results.push(text);
                    console.log("Gear Type Shape Text: " + text);
                }
            }

            if (results.length) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Found gear shape texts:</p><ul>' + results.map(t => '<li>' + t + '</li>').join('') + '</ul>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No gear type SmartArt shapes found in the first shape.</p>';
            }
        });
    </script>
</html>
```

## **Salida de la consola**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
