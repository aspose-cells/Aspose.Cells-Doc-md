---
title: Usando la función FormulaText en Aspose.Cells for JavaScript a través de C++
linktitle: Usando la función FormulaText en Aspose.Cells
description: Este artículo presenta cómo usar la función FormulaText en la biblioteca Aspose.Cells para procesar fórmulas en Microsoft Excel. Aprende a obtener y establecer el texto de la fórmula de las celdas y guardar archivos de Excel modificados usando JavaScript a través de C++.
keywords: Aspose.Cells, Excel, funciones FormulaText JavaScript a través de C++
type: docs
weight: 60
url: /es/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText es una función de Excel 2013 y versiones posteriores. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como su nombre indica, imprime el texto de la fórmula que está presente en una celda dada. Este artículo te mostrará cómo usar esta función con Aspose.Cells for JavaScript a través de C++.

{{% /alert %}} 

El siguiente código de ejemplo muestra el uso de FormulaText con Aspose.Cells for JavaScript a través de C++. El código primero escribe una fórmula en la celda A1 y luego imprime el texto de la fórmula usando FormulaText en la celda A2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **Salida de la consola**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
