---
title: Filtrado de Tablas Dinámicas por Etiqueta o Valor
description: Aspose.Cells for JavaScript via C++ admite capacidades completas de filtrado de Tabla Dinámica. Este artículo explica cómo filtrar los datos de una Tabla Dinámica mediante filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 principales y ocultando o mostrando elementos de la Tabla Dinámica.
linktitle: Filtrado por Etiqueta o Valor
keywords: Aspose.Cells, biblioteca de JavaScript via C++, hoja de cálculo, Tabla Dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro de los 10 principales, elemento de Tabla Dinámica, ocultar elemento de Tabla Dinámica
type: docs
weight: 10
url: /es/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una Tabla Dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, utilizar filtros de fecha cuando el campo contenga únicamente celdas de fecha y hora o valores en blanco, aplicar filtros de valor a números agregados, utilizar filtros de los 10 principales para clasificar según un campo de valores u ocultar y mostrar manualmente elementos individuales de la Tabla Dinámica mediante la propiedad `isHidden`. Cada estrategia se expone mediante API específicas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las Tablas Dinámicas son herramientas analíticas potentes, pero los resúmenes sin procesar suelen contener mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una Tabla Dinámica a las filas, columnas o valores que son importantes para un informe concreto. Aspose.Cells for JavaScript via C++ replica las capacidades de filtrado disponibles en Microsoft Excel y las expone de forma programática para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se explican en este artículo:
1. **Filtro de etiqueta** — filtra los elementos de los campos de fila o columna en función de sus etiquetas de texto.
2. **Filtro de fecha** — filtra los campos de fila o columna que contienen únicamente valores de fecha y hora (o valores en blanco).
3. **Filtro de valor** — filtra los elementos en función de los valores agregados de un campo de datos.
4. **Filtro de los 10 principales** — muestra únicamente los N elementos superiores o inferiores clasificados según un campo de valores.
5. **Ocultar / Mostrar elementos de Tablas Dinámicas** — controla manualmente la visibilidad de cada elemento individual de un campo.
Cada enfoque utiliza un método distinto de la clase `PivotField` o una propiedad de la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `pivotCache.refresh()` en la Tabla Dinámica para que los datos almacenados en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**
Un filtro de etiqueta permite filtrar los elementos de un campo de fila o de columna comparando sus rótulos de texto con un patrón. Esto resulta útil cuando desea mostrar únicamente productos cuyos nombres comienzan por una letra concreta, contienen una palabra determinada o cumplen algún otro criterio basado en rótulos.
Aspose.Cells expone el filtrado por etiqueta mediante el método `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. El argumento `filterType` selecciona el modo de comparación (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc.). Los argumentos `label1` y `label2` proporcionan el texto de comparación: pase `""` para `label2` cuando solo necesite una coincidencia de un solo valor (p. ej., que comience con o que contenga).
El ejemplo siguiente carga un libro de trabajo que contiene una Tabla Dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyos rótulos comienzan por un prefijo especificado, actualiza la Tabla Dinámica y guarda el resultado.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Filtro de fecha**
Los filtros de fecha permiten reducir una Tabla Dinámica mediante criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un intervalo de fechas concreto. Son filtros especializados que solo funcionan con campos que almacenan información de fecha y hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de filas o columnas contiene únicamente celdas de fecha y hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo tenga formato de fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fecha mediante el método `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha específicos, como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. En función del tipo de filtro seleccionado, se pasan uno o dos valores `DateTime` (para `Between`, se pasan las fechas de inicio y fin).
El ejemplo siguiente carga un libro de trabajo con una Tabla Dinámica cuya área de filas contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un intervalo de fechas concreto, actualiza la Tabla Dinámica y guarda el libro de trabajo.
{{% /alert %}}

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
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Filtro de valor**
Los filtros de valor operan sobre los valores agregados que una Tabla Dinámica calcula en su área de datos. En lugar de comparar etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso habituales incluyen mostrar únicamente los productos cuya suma de ventas supera un importe objetivo o únicamente las regiones cuyo número de transacciones se sitúa dentro de un intervalo.
Aspose.Cells expone el filtrado por valor mediante el método `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. El parámetro `valueFieldIndex` especifica qué campo de datos debe evaluarse (utilice `pivotTable.getDataFields().indexOf(dataField)` o recorra la colección para encontrar la posición). El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. Los dos argumentos `double` proporcionan el valor o los valores de umbral.
El ejemplo siguiente carga un libro de trabajo con una Tabla Dinámica, aplica un filtro de valor que conserva únicamente los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la Tabla Dinámica y guarda el libro de trabajo.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Filtro de los 10 principales**
El filtro de los 10 principales es una forma especializada de filtro de valor que conserva únicamente los N elementos superiores o inferiores en función de un campo de valores seleccionado. Se utiliza con frecuencia para generar informes de clasificación como "10 principales productos por ingresos" o "5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}
El filtro de los 10 principales solo es eficaz cuando la Tabla Dinámica tiene uno o más campos de valores en el área de datos. Sin al menos un campo de valores, no existe una medida agregada con la que clasificar los elementos y el filtro no se puede aplicar.
Aspose.Cells expone el filtrado de los 10 principales mediante el método `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. El parámetro `valueFieldIndex` es el índice del campo de datos cuyos valores agregados se utilizan para clasificar los elementos; `filterType` selecciona la unidad de `itemCount` (`Count` conserva un número fijo de elementos, mientras que `Percent` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje); `isTop` indica si se deben conservar los elementos superiores (true) o los inferiores (false); y `itemCount` define cuántos elementos o qué porcentaje se conservan.
El ejemplo siguiente carga un libro de trabajo con una Tabla Dinámica que contiene un campo de valores, aplica un filtro de los 10 principales para conservar únicamente los 10 elementos con la mayor suma de ventas, actualiza la Tabla Dinámica y guarda el libro de trabajo.
{{% /alert %}}

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
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Filtrado mediante la ocultación o visualización de elementos de Tablas Dinámicas**
Además de las API de filtrado estructurado, Aspose.Cells permite controlar directamente la visibilidad de cada elemento individual de una Tabla Dinámica. Al recorrer la colección `pivotField.getPivotItems()` de un `PivotField` y alternar el valor de la propiedad `isHidden`, puede suprimir selectivamente elementos concretos sin aplicar un filtro basado en fórmulas. Al establecer `pivotItem.isHidden = true`, el elemento se oculta de la Tabla Dinámica; al establecer `pivotItem.isHidden = false`, se muestra y vuelve a ser visible.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe concreto. El ejemplo siguiente carga una Tabla Dinámica, oculta un elemento concreto por nombre, demuestra cómo mostrarlo, actualiza la Tabla Dinámica y guarda el libro de trabajo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Resumen**
Aspose.Cells for JavaScript via C++ proporciona un conjunto completo de capacidades de filtrado de Tabla Dinámica que coinciden con las disponibles en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 principales permite gestionar los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `pivotItem.isHidden` ofrece una alternativa flexible a nivel de elemento. La combinación de estas estrategias —por ejemplo, aplicar un filtro de etiqueta y después ocultar elementos concretos— permite crear informes de Tabla Dinámica exactamente orientados por completo mediante código.

{{< app/cells/assistant language="javascript-cpp" >}}