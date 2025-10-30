---
title: Gestionar Celdas con Cadena Html
type: docs
weight: 600
url: /es/javascript-cpp/manage-cells-html-string/
description: Aprende cómo gestionar cadenas HTML en celdas a través del Script Aspose.Cells for Java mediante API C++.
keywords: Agregar cadena HTML dentro de la celda con JavaScript mediante C++, Establecer cadena HTML dentro de la celda con JavaScript mediante C++, Agregar cadena HTML con JavaScript mediante C++, Obtener cadena HTML de la celda con JavaScript mediante C++, Gestionar la cadena HTML de las celdas con JavaScript mediante C++
---

## **Escenarios de uso posibles**
Cuando necesitas establecer datos con estilo para una celda específica, puedes asignar una cadena HTML a la celda. Por supuesto, también puedes obtener la cadena HTML de la celda. Este carácter Script Aspose.Cells for Java mediante C++ ofrece esta función. Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos.
- [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)

## **Obtener y establecer cadenas HTML usando Script Aspose.Cells for Java mediante C++**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Obtener la celda específica en la primera hoja de cálculo.
1. Establecer cadena HTML en la celda.
1. Obtener cadena HTML de la celda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the newly added worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            let c3 = cells.get("C3");
            // set html string for C3 cell.
            c3.htmlString = "<b>test bold</b>";

            let c4 = cells.get("C4");
            // set html string for C4 cell.
            c4.htmlString = "<i>test italic</i>";

            // get the html string of specific cell.
            console.log(c3.htmlString);
            console.log(c4.htmlString);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Resultado generado por el código de ejemplo

La siguiente captura de pantalla muestra la salida del código de muestra anterior.

![todo:image_alt_text](htmlstring.png)
