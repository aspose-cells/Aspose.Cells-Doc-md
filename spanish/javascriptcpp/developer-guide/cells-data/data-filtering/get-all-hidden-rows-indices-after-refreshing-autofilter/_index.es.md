---
title: Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro 
type: docs  
weight: 320  
url: /es/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Aprenda cómo obtener todos los índices de filas ocultas después de actualizar AutoFilter usando el script Aspose.Cells for Java a través de la API C++.  
keywords: Obtener todos los índices de filas ocultas después de actualizar AutoFilter JavaScript a través de C++, obtener todos los índices de filas ocultas después de actualizar AutoFilter JavaScript a través de C++, recuperar todos los índices de filas ocultas después de actualizar AutoFilter JavaScript a través de C++  
---

## **Escenarios de uso posibles**  

Cuando aplicas el autofiltrado en las celdas de la hoja, algunas filas se ocultan automáticamente. Pero puede ser que algunas filas ya estén ocultas manualmente por el usuario de Excel y no por un filtro automático. Por lo tanto, es difícil saber qué filas están ocultas por el filtro automático y cuáles están ocultas manualmente por el usuario de Excel. El script Aspose.Cells for Java a través de C++ maneja este problema usando el `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). Este método devuelve los índices de fila de todas las filas que están ocultas por el filtro automático y no manualmente por el usuario de Excel.  

## **Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro**  

Por favor, vea el siguiente código de ejemplo que carga el [archivo de Excel de muestra](64716909.xlsx) que contiene algunas filas ocultas manualmente por el usuario final de Excel. El código aplica y actualiza el filtro automático usando el método `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-), que devuelve los índices de todas las filas ocultas por el filtro automático. Luego, imprime los índices de las filas ocultas en la consola junto con los nombres y valores de las celdas.  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Salida de la consola**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
