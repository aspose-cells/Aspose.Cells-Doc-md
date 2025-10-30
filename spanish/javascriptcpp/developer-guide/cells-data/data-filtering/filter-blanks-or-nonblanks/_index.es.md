---
title: Cómo filtrar celdas en blanco o no en blanco
type: docs
weight: 85
url: /es/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: Aprende cómo filtrar vacíos y no vacíos usando el script Aspose.Cells for Java a través de la API C++.
keywords: Filtrar celdas en blanco, filtrar celdas no en blanco, filtrar celdas en blanco en la hoja de cálculo, filtrar celdas no en blanco en la hoja de cálculo, filtrar celdas en blanco en Excel, filtrar celdas no en blanco en Excel, filtrar celdas en blanco y no en blanco en Excel
---

## **Escenarios de uso posibles**
Filtrar datos en Excel es una herramienta valiosa que mejora el análisis, la exploración y la presentación de datos al permitir a los usuarios centrarse en subconjuntos específicos de datos según sus criterios, lo que hace que el proceso general de manipulación e interpretación de datos sea más eficiente y efectivo.

## **Cómo filtrar celdas en blanco o no en blanco en Excel**
En Excel, puedes filtrar fácilmente celdas en blanco o no en blanco utilizando las opciones de filtrado. Así es como puedes hacerlo:

### **Cómo filtrar celdas en blanco en Excel**
1. Selecciona el Rango: Haz clic en la letra del encabezado de columna para seleccionar toda la columna o selecciona el rango donde deseas filtrar celdas en blanco.
1. Abre el Menú de Filtro: Ve a la pestaña "Datos" en la cinta de opciones.
<br>
<image src="1.png" width="70%" />
1. Opciones de Filtro: Haz clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar Celdas en Blanco: Haz clic en la flecha de filtro en la columna que deseas filtrar en blanco. Desmarca todas las opciones excepto "En blanco" y haz clic en Aceptar. Esto mostrará solo las celdas en blanco en esa columna.
<br>
<image src="2.png" width="70%" />
1. El resultado es el siguiente:
<br>
<image src="3.png" width="70%" />

### **Cómo filtrar celdas no en blanco en Excel**
1. Selecciona el Rango: Haz clic en la letra del encabezado de columna para seleccionar toda la columna o selecciona el rango donde deseas filtrar celdas no en blanco.
1. Abre el Menú de Filtro: Ve a la pestaña "Datos" en la cinta de opciones.
<br>
<image src="1.png" width="70%" />
1. Opciones de Filtro: Haz clic en el botón "Filtro". Esto agregará flechas de filtro al rango seleccionado.
1. Filtrar Celdas no en Blanco: Haz clic en la flecha de filtro en la columna que deseas filtrar no en blanco. Desmarca todas las opciones excepto "No en blanco" o "Personalizado" y establece las condiciones correspondientes. Haz clic en Aceptar. Esto mostrará solo las celdas que no están en blanco en esa columna.
<br>
<image src="4.png" width="70%" />
1. El resultado es el siguiente:
<br>
<image src="5.png" width="70%" />

## **Cómo filtrar vacíos usando el script Aspose.Cells for Java a través de C++**
Si una columna contiene texto y algunas celdas están vacías, y se requiere filtrar solo aquellas filas que contienen celdas vacías, se pueden usar las funciones [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) y [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) como se demuestra a continuación. 

Consulta el siguiente código de muestra que carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos ficticios. El código de muestra utiliza tres métodos para filtrar en blanco. Luego guarda el libro como [archivo de Excel de salida](FilteredBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **Cómo filtrar no vacíos usando el script Aspose.Cells for Java a través de C++**

Vea el siguiente código de ejemplo que carga el archivo de Excel de ejemplo [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos de prueba. Después de cargar el archivo, llame a la función [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-) para filtrar datos no vacíos y, finalmente, guarde el libro como [archivo de Excel de salida](FilteredNonBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
