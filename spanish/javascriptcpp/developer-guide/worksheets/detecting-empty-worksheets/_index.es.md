---
title: Detectar Hojas de Cálculo Vacías con JavaScript mediante C++
linktitle: Detectar hojas de cálculo vacías
type: docs
weight: 410
url: /es/javascript-cpp/detecting-empty-worksheets/
description: Este artículo muestra cómo detectar programáticamente hojas de cálculo vacías de libros de Excel usando la API JavaScript con la biblioteca C++.
keywords: detectar hoja de cálculo vacía JavaScript mediante C++, encontrar hoja de cálculo de Excel vacía JavaScript mediante C++
---

## **Buscar celdas pobladas**

Las hojas de cálculo pueden tener una o más celdas llenas con valores, donde un valor puede ser simple (texto, numérico, fecha/hora) o una fórmula o un valor basado en fórmula. En tal caso, es fácil detectar si una hoja de cálculo dada está vacía o no. Todo lo que tenemos que verificar son las propiedades [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) o [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--). Si las propiedades mencionadas devuelven cero o valores positivos, eso significa que una o más celdas han sido llenadas; sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas ha sido llenada en la hoja de cálculo dada.

{{% alert color="primary" %}}

Las colecciones de filas y columnas tienen índices basados en cero; por lo tanto, una celda en la fila 0 y columna 0 significa la primera celda en la hoja de cálculo, que es A1.

{{% /alert %}}

## **Comprobar celdas inicializadas vacías**

Todas las celdas que tienen valores se inicializan automáticamente; sin embargo, existe la posibilidad de que una hoja de cálculo tenga celdas solo con formato aplicado. En tal escenario, las propiedades [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) o [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) devolverán -1 indicando la ausencia de valores poblados, pero las celdas inicializadas debido al formato no se pueden detectar usando este método. Para verificar si una hoja de cálculo tiene celdas inicializadas vacías, se recomienda usar el método `Enumerator.MoveNext` en el enumerador adquirido de la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Si el método `Enumerator.MoveNext` devuelve **true**, eso significa que hay una o más celdas inicializadas en la hoja de cálculo dada.

## **Comprobar formas**

Es posible que una hoja de cálculo dada no tenga celdas llenas; sin embargo, podría contener formas y objetos como controles, gráficos, imágenes, etc. Si necesitamos verificar si una hoja de cálculo contiene alguna forma, podemos hacerlo inspeccionando la propiedad [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--). Cualquier valor positivo indica la presencia de forma(s) en la hoja de cálculo.

## **Ejemplo de Programación**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
