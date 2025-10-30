---
title: Obtener dirección, cuenta de celdas, desplazamiento, columna completa y fila completa del rango con JavaScript vía C++
linktitle: Obtener dirección, contar celdas, desplazamiento, columna completa y fila completa del rango
type: docs
weight: 330
url: /es/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Escenarios de uso posibles**
Aspose.Cells for JavaScript vía C++ proporciona el objeto Range que tiene varios métodos útiles que facilitan al usuario trabajar con Rangos de Excel. Este artículo ilustra el uso de los siguientes métodos o propiedades del objeto Range.

- **Dirección**

Obtiene la dirección del rango.

- **Recuento de celdas**

Obtiene el recuento de todas las celdas en el rango.

- **Desplazamiento**

Obtiene el rango mediante desplazamiento.

- **Columna completa**

Obtiene un objeto Range que representa toda la columna (o columnas) que contiene el rango especificado.

- **Fila completa**

Obtiene un objeto Range que representa toda la fila (o filas) que contiene el rango especificado.

## **Obtener Dirección, Recuento de celdas, Desplazamiento, Columna completa y Fila completa del Rango**
El siguiente código de ejemplo explica el uso de los métodos y propiedades como se discutió anteriormente. Consulte la salida de la consola del código que se muestra a continuación como referencia.

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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **Salida de la consola**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
