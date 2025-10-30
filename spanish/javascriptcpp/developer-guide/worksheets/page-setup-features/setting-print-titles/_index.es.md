---
title: Cómo establecer los títulos de impresión con JavaScript vía C++
linktitle: Cómo establecer títulos de impresión
type: docs
weight: 200
url: /es/javascript-cpp/how-to-set-print-titles/
description: Este artículo te muestra cómo configurar los títulos de impresión usando la biblioteca Aspose.Cells para JavaScript vía C++.
keywords: Imprimir filas y columnas repetidamente, Cómo establecer títulos de impresión en JavaScript, Establecer y limpiar títulos de impresión usando JavaScript, Cómo limpiar títulos de impresión en JavaScript, Cómo añadir títulos de impresión usando JavaScript, Cómo eliminar títulos de impresión usando JavaScript, Cómo establecer títulos de impresión en Excel, Cómo limpiar títulos de impresión en Excel.  
---

## **Escenarios de uso posibles**  

Configurar títulos de impresión en Excel asegura que filas o columnas específicas se repitan en cada página impresa, lo cual es especialmente útil para hojas de cálculo grandes que abarcan varias páginas. Aquí tienes algunas razones para establecer títulos de impresión:  

1. Mejor legibilidad: Los títulos de impresión ayudan a los lectores a entender los datos manteniendo los encabezados visibles en todas las páginas, facilitando la interpretación de la información sin tener que volver a la primera página.  

1. Presentación profesional: Mostrar consistentemente encabezados o etiquetas en cada página crea una apariencia más pulida y profesional en los documentos impresos.  

1. Mejor navegación: Para documentos con datos extensos, repetir los encabezados en cada página permite una navegación y referencia más rápida, reduciendo la necesidad de volver a pasar entre páginas.  

1. Reducción de errores: Cuando los encabezados están presentes en cada página, se minimizan las oportunidades de malentendidos o errores de entrada de datos, ya que los usuarios pueden ver fácilmente el contexto de los datos.  

1. Consistencia: Asegurar que información importante, como encabezados de columnas o etiquetas de filas, siempre sea visible mantiene la consistencia y claridad en todo el documento.  

## **Cómo establecer títulos de impresión en Excel**  

Para establecer títulos de impresión en Excel, sigue estos pasos:  

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.  
1. Acceder a Títulos de impresión: En el grupo "Configurar página", haz clic en "Títulos de impresión".  
1. Configurar filas para repetir: En el cuadro de diálogo "Configurar página", ve a la pestaña "Hoja". En la sección "Títulos de impresión", especifica las filas a repetir en la parte superior haciendo clic en el cuadro junto a "Filas para repetir en la parte superior" y seleccionando la(s) fila(s) que deseas repetir.  
1. Configurar columnas para repetir (si es necesario): De manera similar, puedes especificar las columnas para repetir en la izquierda haciendo clic en el cuadro junto a "Columnas para repetir en la izquierda" y seleccionando la(s) columna(s) que deseas repetir.  
<br>  
<img src="3.png" width=60% />  

1. Confirmar y imprimir: Haz clic en "Aceptar" para aplicar la configuración. Cuando imprimas la hoja, las filas o columnas especificadas aparecerán en cada página impresa.  

## **Cómo borrar títulos de impresión en Excel**  

Para borrar títulos de impresión en Excel, necesitas eliminar las filas o columnas que están configuradas para repetirse en cada página impresa. Aquí te decimos cómo hacerlo:  

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.  
1. Acceder a Títulos de impresión: En el grupo "Configurar página", haz clic en "Títulos de impresión".  
1. Borrar títulos de impresión: En el cuadro de diálogo "Configurar página", ve a la pestaña "Hoja". Borra el contenido de los cuadros "Filas para repetir en la parte superior" y "Columnas para repetir en la izquierda" eliminando cualquier contenido dentro de ellos.  
<br>  
<img src="4.png" width=60% />  

1. Confirmar y cerrar: Haz clic en "Aceptar" para aplicar los cambios.  

## ** Cómo establecer títulos de impresión con Aspose.Cells for JavaScript vía C++**  

Para establecer títulos de impresión en una hoja de cálculo específica: Primero, carga el [archivo de muestra](input.xlsx), y luego debes modificar las propiedades [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) y [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) del objeto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) para la hoja deseada. Configurar estas propiedades con una cadena de rango establecerá los títulos de impresión.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
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

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

El resultado de la salida:  
<br>  
<img src="1.png" width=60% />  

## ** Cómo limpiar títulos de impresión en Aspose.Cells for JavaScript vía C++**  

Para borrar los títulos de impresión en una hoja de cálculo específica: Primero, carga el [archivo de muestra](input.xlsx), y luego debes modificar las propiedades [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) y [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) del objeto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) para la hoja deseada. Configurar estas propiedades con una cadena vacía borrará los títulos de impresión.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

El resultado de la salida:  
<br>  
<img src="2.png" width=60% />
