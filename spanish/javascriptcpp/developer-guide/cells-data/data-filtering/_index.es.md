---
title: Filtrado de Datos
type: docs
weight: 85
url: /es/javascript-cpp/data-filtering/
description: Aprende cómo agregar un filtro de datos usando el Aspose.Cells for JavaScript a través de la API en C++.
keywords: Agregar Filtro por Color JavaScript vía C++, Agregar Filtros de Fecha JavaScript vía C++, Agregar Filtros de Número JavaScript vía C++, Agregar Filtro Dinámico JavaScript vía C++, Agregar Filtros de Texto JavaScript vía C++, Agregar filtro personalizado con Contains JavaScript vía C++, Agregar filtro personalizado con NotContains JavaScript vía C++, Agregar filtro personalizado con BeginsWith JavaScript vía C++, Agregar filtro personalizado con EndsWith JavaScript vía C++
---

{{% alert color="primary" %}}
Microsoft Excel ofrece funciones útiles para autofiltar datos en hojas de cálculo. Aspose.Cells soporta completamente las funciones de autofiltro de Microsoft Excel. Este artículo explica cómo usar estas funciones en Microsoft Excel, y cómo programarlas usando Aspose.Cells for JavaScript a través de C++.
{{% /alert %}}

## **Datos de Autofiltro**

El autofiltrado es la forma más rápida de seleccionar solo aquellos elementos de la hoja de cálculo que desea mostrar en una lista. La función de autofiltro permite a los usuarios filtrar elementos en una lista según un criterio establecido. Filtrar según texto, números o fechas.

### **Autofiltro en Microsoft Excel**

Para activar la función de autofiltro en Microsoft Excel:

1. Haz clic en la fila de encabezado en una hoja de cálculo.
1. Desde el menú **Datos**, selecciona **Filtrar** y luego **Autofiltro**.

Cuando aplicas un autofiltro a una hoja de cálculo, aparecen interruptores de filtro (flechas negras) a la derecha de los encabezados de las columnas.

1. Haz clic en una flecha de filtro para ver una lista de opciones de filtro.

Algunas de las opciones de autofiltro son:

|**Opciones**|**Descripción**|
| :- | :- |
|All|Mostrar todos los elementos en la lista una vez.|
|Custom|Personalizar criterios de filtro como contiene/no contiene|
|Filter by Color|Filtros basados en el color rellenado|
|Date Filters|Filtrar filas basadas en diferentes criterios en la fecha|
|Number Filters|Diferentes tipos de filtro en números como comparación, promedios y Top 10, etc.|
|Text Filters|Diferentes filtros como comienza con, termina con, contiene, etc,|
|Blanks/Non Blanks|Estos filtros pueden implementarse a través de Filtro de Texto en Blanco|

Los usuarios filtran manualmente sus datos de hoja de cálculo en Microsoft Excel utilizando estas opciones.

### **Autofiltro con Aspose.Cells for JavaScript a través de C++**

Aspose.Cells proporciona una clase, Workbook que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite el acceso a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para crear un autofiltro, utilice la propiedad AutoFilter de la clase Worksheet. La propiedad AutoFilter es un objeto de la clase AutoFilter, que proporciona la propiedad Range para especificar el rango de celdas que forman una fila de encabezado. Un autofiltro se aplica al rango de celdas que es la fila de encabezado.

En cada hoja de cálculo, solo se puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para el filtrado personalizado de datos, utilice el método AutoFilter.Custom.

En el ejemplo dado a continuación, hemos creado el mismo autofiltro usando Aspose.Cells for JavaScript a través de C++ que creamos en Microsoft Excel en la sección anterior.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range of the heading row
            worksheet.autoFilter.range = "A1:B1";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">AutoFilter created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Diferentes tipos de filtro**

Aspose.Cells ofrece múltiples opciones para aplicar diferentes tipos de filtros como Filtro de Color, Filtro de Fecha, Filtro de Número, Filtro de Texto, Filtros en Blanco y Filtros no en Blanco.

##### **Color de relleno**

Aspose.Cells provee una función AddFillColorFilter para filtrar datos basados en la propiedad de color de relleno de las celdas. En el ejemplo dado a continuación, se utiliza un archivo de plantilla con diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado por color. Los archivos de muestra se pueden descargar desde los siguientes enlaces.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Coloured Cells Example</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiating a CellsColor object for foreground color
            const clrForeground = workbook.createCellsColor();
            clrForeground.color = AsposeCells.Color.fromArgb(255, 0, 0); // Red color

            // Instantiating a CellsColor object for background color
            const clrBackground = workbook.createCellsColor();
            clrBackground.color = AsposeCells.Color.fromArgb(255, 255, 255); // White color

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddFillColorFilter function to apply the filter
            worksheet.autoFilter.addFillColorFilter(0, AsposeCells.BackgroundType.Solid, clrForeground, clrBackground);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredColouredCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fecha, como filtrar todas las filas con fechas en enero de 2018. El siguiente ejemplo muestra cómo implementar este filtro usando la función AddDateFilter. Se proporcionan archivos de ejemplo.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Date Filter</title>
    </head>
    <body>
        <h1>Date Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddDateFilter function to apply the filter
            worksheet.autoFilter.addDateFilter(0, AsposeCells.DateTimeGroupingType.Month, 2018, 1, 0, 0, 0, 0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Fecha dinámica**

A veces se requieren filtros dinámicos basados en la fecha, como todas las celdas que tienen fechas en enero, independientemente del año. En este caso, se utiliza la función DynamicFilter según se muestra en el siguiente ejemplo de código. Se proporcionan los archivos de ejemplo a continuación.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Dynamic Date Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call DynamicFilter function to apply the filter
            worksheet.autoFilter.dynamic_Filter(0, AsposeCells.DynamicFilterType.January);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDynamicDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Número**

Se pueden aplicar filtros personalizados utilizando Aspose.Cells como seleccionar celdas que tengan números dentro de un rango dado. El siguiente ejemplo demuestra el uso de la función Custom() para filtrar números. Los archivos de muestra se dan a continuación.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Filter Numbers</title>
    </head>
    <body>
        <h1>Filter Numbers Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call Custom function to apply the filter
            worksheet.autoFilter.custom(0, AsposeCells.FilterOperatorType.GreaterOrEqual, 5, true, AsposeCells.FilterOperatorType.LessOrEqual, 10);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Texto**

Si una columna contiene texto y se desea seleccionar celdas que contienen un texto en particular, se puede usar la función Filter(). En el siguiente ejemplo, el archivo de plantilla contiene una lista de países y se desea seleccionar la fila que contiene un nombre de país en particular. El siguiente código demuestra cómo filtrar texto. Se proporcionan archivos de ejemplo.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter AutoFilter Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call Filter function to apply the filter
            const autoFilter = worksheet.autoFilter;
            autoFilter.filter(0, "Angola");

            // Call refresh function to update the worksheet
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredText.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Vacíos**

Si una columna contiene texto y algunas celdas están en blanco, y se requiere un filtro para seleccionar solo aquellas filas donde las celdas en blanco están presentes, se puede utilizar la función CoincidirBlancos() como se demuestra a continuación. Los archivos de ejemplo se muestran a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [EnBlancoFiltrado.xlsx](72417325.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Blank Rows Example</title>
    </head>
    <body>
        <h1>Filter Blank Rows Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchBlanks function to apply the filter
            worksheet.autoFilter.matchBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filtering completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **No vacíos**

Cuando se deben filtrar celdas que contienen texto, utilizar la función de filtro CoincidirNoVacios como se demuestra a continuación. Los archivos de ejemplo se muestran a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [NoVaciosFiltrado.xlsx](72417326.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Filter Non-Blank Example</h1>
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

            // Read the selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filtrar filas que contienen alguna cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra. Se proporcionan archivos de ejemplo a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows containing string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.Contains, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Filtro personalizado con NoContiene**

Excel proporciona filtros personalizados como filtrar filas que no contienen una cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows not containing string "Be"
            worksheet.autoFilter.custom(0, FilterOperatorType.NotContains, "Be");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Filtro personalizado que comienza con**

Excel proporciona filtros personalizados como filtrar filas que comienzan con una cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Countries Starting With "Ba"</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows starting with string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.BeginsWith, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Filtro personalizado que termina con**

Excel proporciona filtros personalizados como filtrar filas que terminan con una cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply AutoFilter Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            const autoFilter = worksheet.autoFilter;
            autoFilter.range = "A1:A18";

            // Initialize filter for rows end with string "ia"
            autoFilter.custom(0, AsposeCells.FilterOperatorType.BeginsWith, "ia");

            // Refresh the filter to show/hide filtered rows
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Temas avanzados**
- [Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos](/cells/es/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro](/cells/es/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
