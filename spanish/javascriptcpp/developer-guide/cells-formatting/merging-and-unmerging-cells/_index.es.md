---
title: Combinar y Descombinar Celdas con JavaScript a través de C++
linktitle: Fusionar y Desfusionar Celdas
description: Aspose.Cells es una biblioteca de JavaScript para trabajar con archivos de hojas de cálculo, que admite fusionar y deshacer la fusión de celdas. Este artículo presentará cómo fusionar y deshacer la fusión de celdas usando la biblioteca Aspose.Cells, con opciones para personalizar el estilo de la celda fusionada.
keywords: Aspose.Cells, biblioteca de JavaScript, hoja de cálculo, fusionar celdas, deshacer fusión, ajustes de estilo, estilos personalizados
type: docs
weight: 190
url: /es/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells admite esta función y también puede combinar celdas en una hoja de cálculo. También puedes descombinar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango original seleccionado.

{{% /alert %}} 
## **Introducción**
No siempre quieres el mismo número de celdas en cada fila o columna. Por ejemplo, es posible que desees colocar un título en una celda que abarque varias columnas. O, si estás creando una factura, es posible que desees menos columnas para el total. Para hacer una celda a partir de dos o más celdas, combínalas. Microsoft Excel permite a los usuarios seleccionar archivos y combinarlos para estructurar la hoja de cálculo según sus necesidades.

{{% alert color="primary" %}} 

Tenga en cuenta que cuando las celdas están fusionadas, solo se conserva los datos en la celda superior izquierda. Si hay datos en las otras celdas del rango, estos datos se eliminan. El formato, de igual manera, se basa en la celda de referencia, por lo que al fusionar celdas, la configuración de formato de la celda superior izquierda en el rango se aplica a la celda fusionada. Cuando se divide la celda, las nuevas celdas mantienen su configuración de formato original.

{{% /alert %}} 
## **Combina celdas en una hoja de cálculo**
### **Combinar celdas en Microsoft Excel**
Los siguientes pasos describen cómo combinar celdas en la hoja de cálculo utilizando MS Excel.

1. Copie los datos que desea en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea combinar.
1. Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en el icono **Combinar y centrar** en la barra de herramientas **Formato**.

### **Combinar celdas con Aspose.Cells**
La clase Aspose.Cells.Cells tiene algunos métodos útiles para la tarea. Por ejemplo, el método `merge()` fusiona las celdas en una sola dentro de un rango especificado.

El siguiente ejemplo muestra cómo combinar celdas (C6:E7) en una hoja de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Descombinar (Separar) celdas combinadas**
### **Usar Microsoft Excel**
Los siguientes pasos describen cómo separar celdas combinadas utilizando Microsoft Excel.

1. Seleccione la celda combinada.
   Cuando las celdas se han combinado, **Combinar y centrar** se selecciona en la barra de herramientas **Formato**.
1. Haga clic en **Combinar y centrar** en la barra de herramientas **Formato**.

### **Usar Aspose.Cells**
La clase Aspose.Cells.Cells tiene un método llamado `unmerge()` que divide las celdas en su estado original. El método desfusión las celdas usando la referencia de la celda en el rango de celdas fusionadas.

El siguiente ejemplo muestra cómo separar las celdas combinadas (C6). El ejemplo utiliza el archivo creado en el ejemplo anterior y separa las celdas combinadas.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Detectar celdas combinadas en una hoja de cálculo](/cells/es/javascript-cpp/detect-merged-cells-in-a-worksheet/)
