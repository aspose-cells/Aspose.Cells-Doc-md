---
title: Cómo escalar una hoja de cálculo con JavaScript vía C++
linktitle: Cómo escalar una hoja de trabajo
type: docs
weight: 130
url: /es/javascript-cpp/how-to-scale-a-worksheet/
description: Este artículo le muestra un código que explica cómo escalar una hoja de cálculo usando Aspose.Cells for JavaScript vía C++.
keywords: Escalar una hoja de cálculo en JavaScript, Cómo escalar una hoja de cálculo usando JavaScript vía C++, Escalar una hoja de cálculo en JavaScript vía C++.
---

## **Escenarios de uso posibles**
Escalar una hoja de trabajo puede ser útil por varias razones, dependiendo del contexto en el que estés trabajando. Aquí algunas razones comunes para escalar una hoja de trabajo:
1. Ajustar al tamaño de página: Para asegurarte de que todo el contenido quepa en una sola página o en un número específico de páginas al imprimir, facilitando la lectura y gestión sin tener que pasar varias páginas.

1. Presentación: Para que la hoja de cálculo luzca más organizada y profesional, especialmente al compartirla con otros en reuniones o informes.

1. Legibilidad: Para ajustar el tamaño del texto y otros elementos para una mejor legibilidad, especialmente para personas que puedan tener dificultades para leer fuentes pequeñas.

1. Gestión del espacio: Para optimizar el uso del espacio en una hoja de cálculo, asegurando que no haya espacios en blanco innecesarios y que toda la información importante sea visible sin desplazamiento excesivo.

1. Visualización de datos: En el caso de gráficos y diagramas, el escalado puede ayudar a hacer que sean más comprensibles ajustando el tamaño para que se ajusten apropiadamente al espacio disponible.

1. Consistencia: Para mantener una apariencia y sensación coherentes en varias hojas de cálculo o documentos, lo cual es particularmente importante en entornos profesionales y educativos.

## **Cómo escalar una hoja de trabajo en Excel**
Escalar una hoja de cálculo en Excel puede ayudarte a ajustar tu contenido a una sola página o a un número específico de páginas al imprimir. Aquí están los pasos para escalar una hoja de cálculo:

1. Abre tu hoja de cálculo: Abre la hoja de Excel que deseas escalar.

1. Ve a la pestaña de Diseño de página: Haz clic en la pestaña de Diseño de página en la cinta.

1. Grupo de Escalar para ajustarse: En la pestaña de Diseño de página, encuentra el grupo Escalar para ajustarse. Aquí tienes opciones para ajustar la escala. Ancho: Esta opción te permite especificar cuántas páginas de ancho tendrá la hoja al imprimir. Alto: Esta opción te permite especificar cuántas páginas de alto tendrá la hoja al imprimir. Escala: También puedes establecer un porcentaje de escala personalizado aquí.
<br>
<img src="1.png" width=60% />

1. Ajusta ancho y alto: Establece el ancho y alto en el número de páginas deseado. Por ejemplo, configura ambos en 1 página si quieres que la hoja quepa en una sola página.

1. Ajusta el porcentaje de escala (si es necesario): Si prefieres establecer un porcentaje de escala específico, ajusta la casilla de Escala. Por ejemplo, establecerlo en 50% reducirá todo a la mitad de tamaño.


## **Cómo escalar una hoja de cálculo usando JavaScript a través de C++**
Script Aspose.Cells for Java a través de C++ es una biblioteca poderosa para trabajar con archivos de Excel automáticamente. Para escalar una hoja de cálculo con Aspose.Cells, debe seguir estos pasos: cargar el [archivo de ejemplo](sample.xlsx) y ajustar la configuración de impresión para que el contenido quepa en el número deseado de páginas o en un porcentaje específico del tamaño original.

### **Ejemplo: Ajustar a página completa**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Ejemplo: Escalar a porcentaje**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />
