---
title: Cambiar el formato de una celda
linktitle: Cambiar el formato de una celda
description: Cómo usar la biblioteca Aspose.Cells en JavaScript vía C++ para cambiar el formato de las celdas, incluyendo fuente, color, borde, etc. Ajustando estas propiedades, tienes más control sobre la apariencia de las celdas.
keywords: Aspose.Cells, formateo de celdas, JavaScript vía C++, fuente, color, borde
type: docs
weight: 20
url: /es/javascript-cpp/how-to-change-format-of-cell/
---

## **Escenarios de uso posibles**
Cuando desee resaltar ciertos datos, puede cambiar el estilo de las celdas.

## **Cómo cambiar el formato de una celda en Excel**

Para cambiar el formato de una sola celda en Excel, siga estos pasos:

1. Abra Excel y abra el libro que contiene la celda que desea formatear.

2. Localice la celda que desea formatear.

3. Haga clic con el botón derecho en la celda y seleccione "Formato de celdas" en el menú contextual. Alternativamente, puede seleccionar la celda, ir a la pestaña Inicio en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Celdas" y seleccionar "Formato de celdas".

4. Aparecerá el cuadro de diálogo "Formato de celdas". Aquí, puede elegir varias opciones de formato para aplicar a la celda seleccionada. Por ejemplo, puede cambiar el estilo de fuente, el tamaño de fuente, el color de fuente, el formato de número, los bordes, el color de fondo, etc. Explore las diferentes pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haga clic en el botón "Aceptar" para aplicar el formato a la celda seleccionada.


## **Cómo cambiar el formato de una celda usando JavaScript**

Para cambiar el formato de una celda usando Aspose.Cells, puedes usar los siguientes métodos:
1. [Cell.style(Style)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [Cell.style(Style, explicitFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [Cell.style(Style, StyleFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **Código de muestra**
En este ejemplo, creamos un libro de Excel, añadimos algunos datos de muestra, accedemos a la primera hoja de cálculo y obtenemos dos celdas ("A2" y "B3"). Luego, obtenemos el estilo de la celda, configuramos varias opciones de formato (por ejemplo, color de fuente, negrita) y cambiamos el formato de la celda. Finalmente, guardamos el libro en un nuevo archivo.
![todo:image_alt_text](change-format.png)

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
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

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

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
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
