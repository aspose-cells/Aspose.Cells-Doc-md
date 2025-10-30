---
title: Cómo establecer el área de impresión con JavaScript vía C++
linktitle: Cómo definir el área de impresión
type: docs
weight: 200
url: /es/javascript-cpp/how-to-set-print-area/
description: Este artículo muestra código que explica cómo establecer el área de impresión usando la biblioteca Aspose.Cells para JavaScript vía C++.
keywords: Limitar rango de impresión, establecer rango de impresión, limpiar rango de impresión, usar JavaScript vía C++, cómo establecer área de impresión, establecer y limpiar área de impresión usando JavaScript vía C++, cómo limpiar área de impresión en JavaScript, cómo agregar área de impresión, cómo eliminar área de impresión, cómo establecer área de impresión en Excel, cómo limpiar área de impresión en Excel.
---

## **Escenarios de uso posibles**

Configurar un área de impresión en un documento, como una hoja de cálculo de Excel, ayuda a controlar qué contenido se incluye al imprimir. Aquí algunas razones para establecer un área de impresión:

1. Centrarse en datos específicos: Puedes imprimir solo las secciones más relevantes, evitando contenido innecesario.
1. Mejorar el diseño: Ayuda a organizar y ajustar el contenido de forma ordenada en las páginas imprimidas, evitando divisiones o saltos de página no deseados.
1. Ahorrar recursos: Limitando el área de impresión, puedes reducir el uso de papel y tinta.
1. Presentación profesional: Asegura que solo se imprima la versión pulida y finalizada de los datos, especialmente importante para informes o presentaciones.
1. Consistencia: Al imprimir el mismo documento varias veces, tener un área de impresión estable garantiza la consistencia en el resultado.

<br>
Establecer un área de impresión es especialmente útil en documentos grandes donde solo una parte necesita ser compartida o revisada en forma impresa.

## **Cómo establecer el área de impresión en Excel**

Para establecer un área de impresión en Excel, siga estos pasos:

1. Seleccionar las celdas: Haga clic y arrastre para seleccionar el rango de celdas que desea establecer como área de impresión.
1. Abrir la pestaña Diseño de página: Vaya a la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Establecer área de impresión: En el grupo "Configuración de página", haga clic en "Área de impresión". En el menú desplegable, seleccione "Establecer área de impresión".
<br>
<img src="3.png" width=60% />

1. Agregar a la área de impresión: Si desea agregar más celdas al área de impresión existente, seleccione las celdas adicionales, vaya a "Área de impresión" en la pestaña "Diseño de página" y elija "Agregar a área de impresión".

<br>
Esta acción definirá las celdas seleccionadas como el área de impresión. Cuando imprima la hoja de cálculo, solo esta área definida se imprimirá.

## **Cómo borrar el área de impresión en Excel**

Para borrar el área de impresión en Excel, siga estos pasos:

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Borrar área de impresión: En el grupo "Configuración de página", haga clic en "Área de impresión". En el menú desplegable, seleccione "Borrar área de impresión".
<br>
<img src="4.png" width=60% />

<br>
Esta acción eliminará cualquier área de impresión configurada anteriormente, permitiendo que toda la hoja de cálculo se imprima.

## **Qué sucede después de limpiar el área de impresión**

Borrar el área de impresión en una aplicación de hojas de cálculo como Excel utilizando Aspose.Cells resultará en que toda la hoja de cálculo se incluya al imprimir el documento. Si se establece un área de impresión, solo el rango especificado de celdas se imprimirá. Al borrar el área de impresión, se asegura que no se defina un rango específico y que la impresión por defecto, que incluye toda la hoja, tenga efecto.

1. Comportamiento de impresión predeterminado: Se considerará toda la hoja de cálculo para la impresión. Esto significa que todas las celdas con datos o formato serán impresas.
1. Sin límites de área de impresión: Se eliminarán los límites de área de impresión previamente definidos. Si había filas y columnas específicas designadas para imprimir, ya no estarán restringidas a esos límites.
1. Impresión de contenido completo: Todo el contenido, incluidos encabezados, pies de página y cualquier otro dato dentro de la hoja de cálculo, se incluirá en el trabajo de impresión.

## **Cómo establecer área de impresión usando Aspose.Cells for JavaScript vía C++**

Para establecer el área de impresión en una hoja de cálculo específica: Primero, carga el [archivo de ejemplo](input.xlsx), y luego debes modificar la propiedad [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) del objeto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) para la hoja de cálculo deseada. Establecer esta propiedad a una cadena de rango establecerá el área de impresión.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

El resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo limpiar el área de impresión usando Aspose.Cells for JavaScript vía C++**

Para borrar el área de impresión en una hoja de cálculo específica: Primero, cargue el [archivo de ejemplo](input.xlsx), y luego necesita modificar la propiedad [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) del objeto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) para la hoja deseada. Configurar esta propiedad con una cadena vacía borrará el área de impresión.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

El resultado de la salida:
<br>
<img src="2.png" width=60% />
