---
title: Filtrado de tablas dinámicas por etiqueta o valor
description: Aspose.Cells for JavaScript via C++ ofrece capacidades integrales de filtrado de tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas mediante filtros por etiqueta, filtros por fecha, filtros por valor, filtros de los 10 principales y la ocultación o visualización de elementos pivote.
linktitle: Filtrado por etiqueta o valor
keywords: Aspose.Cells, biblioteca de JavaScript vía C++, hoja de cálculo, tabla dinámica, filtro, filtro por etiqueta, filtro por valor, filtro por fecha, filtro de los 10 principales, elemento pivote, ocultar elemento pivote
type: docs
weight: 10
url: /es/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros por etiqueta a campos de fila o columna basados en texto, utilizar filtros por fecha cuando el campo contenga únicamente celdas de fecha y hora o celdas vacías, aplicar filtros por valor a números agregados, utilizar filtros de los 10 principales para clasificar según un campo de valor u ocultar y mostrar manualmente elementos pivote individuales mediante la propiedad `isHidden`. Cada estrategia está disponible mediante API específicas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las tablas dinámicas son herramientas analíticas potentes, pero los resúmenes sin procesar suelen contener mucha más información de la que se desea presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe concreto. Aspose.Cells for JavaScript via C++ reproduce las capacidades de filtrado disponibles en Microsoft Excel y las expone mediante programación para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se explican en este artículo:
1. **Filtro por etiqueta** — filtra los elementos de los campos de fila o columna según sus etiquetas de texto.
2. **Filtro por fecha** — filtra los campos de fila o columna que contienen únicamente valores de fecha y hora o celdas vacías.
3. **Filtro por valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 principales** — muestra únicamente los N elementos superiores o inferiores clasificados según un campo de valor.
5. **Ocultar o mostrar elementos pivote** — controla manualmente la visibilidad de cada elemento individual de un campo.
Cada enfoque utiliza un método diferente de la clase `PivotField` o una propiedad de la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `pivotCache.refresh()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro por etiqueta**
Un filtro por etiqueta permite filtrar los elementos de un campo de fila o columna comparando sus rótulos de texto con un patrón. Esto resulta útil cuando desea mostrar únicamente productos cuyos nombres comiencen por una letra concreta, contengan una palabra determinada o coincidan con otro criterio basado en rótulos.
Aspose.Cells expone el filtrado por etiqueta mediante el método `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. El argumento `filterType` selecciona el modo de comparación (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc.). Los argumentos `label1` y `label2` proporcionan el texto de comparación; pase `""` para `label2` cuando solo necesite una coincidencia de un solo valor, por ejemplo, que comience por una secuencia o que la contenga.
El siguiente ejemplo carga un libro de trabajo que contiene una tabla dinámica existente, aplica un filtro por etiqueta para que solo permanezcan visibles los elementos cuyos rótulos comiencen por un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

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
                    // Cargar el libro de trabajo existente que contiene una tabla dinámica
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Acceder a la hoja de cálculo por índice (primera hoja de cálculo)
                    const worksheet = workbook.worksheets.get(0);
                    // Acceder a la tabla dinámica por índice
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Obtener el primer PivotField de fila
                    const rowField = pivotTable.rowFields.get(0);
                    // Aplicar el filtro de etiquetas: mostrar solo los elementos de fila cuyas etiquetas comienzan con el prefijo proporcionado
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Actualizar y recalcular los datos de la tabla dinámica para que el filtro surta efecto
                    pivotTable.refreshData();
                    // Guardar el libro de trabajo de nuevo en el disco
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

## **Filtro por fecha**
Los filtros por fecha permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un intervalo de fechas concreto. Son filtros especializados que solo funcionan con campos que almacenan información de fecha y hora.

{{% alert color="primary" %}}
El filtro por fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha y hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro por fecha no producirá el resultado esperado. Asegúrese de que el campo tenga formato de fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fecha mediante el método `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha específicos, como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Dependiendo del tipo de filtro seleccionado, se pasan uno o dos valores `DateTime`; para `Between`, se pasan las fechas de inicio y fin.
El siguiente ejemplo carga un libro de trabajo con una tabla dinámica cuyo área de fila contiene un campo de fecha, aplica un filtro por fecha que restringe los elementos visibles a un intervalo de fechas concreto, actualiza la tabla dinámica y guarda el libro de trabajo.
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
                // Cargar el libro de trabajo existente que contiene la tabla dinámica
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Acceder a la hoja de cálculo que contiene la tabla dinámica (por índice)
                const worksheet = workbook.worksheets.get(0);
                // Acceder a la tabla dinámica por índice
                const pivotTable = worksheet.pivotTables.get(0);
                // Obtener el campo dinámico de fecha del área de filas
                // (El filtro de fechas solo funciona cuando el área de filas/columnas contiene únicamente celdas de fecha y hora o celdas vacías)
                const dateField = pivotTable.rowFields.get(0);
                // Definir el criterio de fecha para el filtro Entre
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Aplicar el filtro de fecha en el campo dinámico
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Actualizar y recalcular la tabla dinámica para que el filtro surta efecto
                pivotTable.refreshData();
                // Persistir el libro de trabajo
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

## **Filtro por valor**
Los filtros por valor operan sobre los valores agregados que calcula una tabla dinámica en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar únicamente productos cuya suma de ventas supere un importe objetivo o solo regiones cuyo número de transacciones se encuentre dentro de un intervalo.
Aspose.Cells expone el filtrado por valor mediante el método `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. El parámetro `valueFieldIndex` especifica qué campo de datos se debe evaluar; utilice `pivotTable.getDataFields().indexOf(dataField)` o recorra la colección para encontrar la posición. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. Los dos argumentos `double` proporcionan el valor o los valores de umbral.
El siguiente ejemplo carga un libro de trabajo con una tabla dinámica, aplica un filtro por valor que conserva únicamente los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la tabla dinámica y guarda el libro de trabajo.

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
                // Encuentra manualmente el índice del campo de datos ya que PivotFieldCollection no tiene IndexOf
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
                pivotTable.refreshData();
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
El filtro de los 10 principales es una forma especializada de filtro por valor que conserva únicamente los N elementos más altos o más bajos según un campo de valor elegido. Se utiliza habitualmente para informes de clasificación como "los 10 productos principales por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}
El filtro de los 10 principales solo es eficaz cuando la tabla dinámica tiene uno o más campos pivote de valor en el área de datos. Sin al menos un campo de valor, no existe una medida agregada con la que clasificar los elementos y el filtro no puede aplicarse.
Aspose.Cells expone el filtrado de los 10 principales mediante el método `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. El parámetro `valueFieldIndex` es el índice del campo de datos cuyos valores agregados se utilizan para clasificar los elementos; `filterType` selecciona la unidad de `itemCount` (`Count` conserva un número fijo de elementos y `Percent` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje); `isTop` indica si se deben conservar los elementos superiores (true) o inferiores (false); y `itemCount` define cuántos elementos o qué porcentaje se conservan.
El siguiente ejemplo carga un libro de trabajo con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 principales para conservar únicamente los 10 elementos con mayor suma de ventas, actualiza la tabla dinámica y guarda el libro de trabajo.
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
                // Cargar el libro de trabajo existente que contiene la tabla dinámica
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Acceder a la hoja de cálculo que contiene la tabla dinámica (índice 0)
                const worksheet = workbook.worksheets.get(0);
                // Acceder a la tabla dinámica por índice
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirmar que hay al menos un campo dinámico de valor en el área de datos
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Obtener el campo dinámico de fila objetivo (el campo al que se aplicará Top 10)
                const rowField = pivotTable.rowFields.get(0);
                // El primer (y único) campo de datos está en el índice 0; Top 10 se clasifica por él.
                const valueFieldIndex = 0;
                // Aplicar el filtro Top 10 al campo de fila:
                //   - valueFieldIndex = 0 — el campo de datos utilizado para clasificar los elementos
                //   - filterType  = PivotFilterType.Count (mantener un número fijo de elementos;
                //     PivotFilterType.Percent interpretaría 10 como "top 10 percent")
                //   - isTop       = true (top N; false significaría bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Actualizar los datos de la tabla dinámica y recalcularla para que el filtro surta efecto
                pivotTable.refreshData();
                // Guardar el libro de trabajo
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

## **Filtrar ocultando o mostrando elementos pivote**
Además de las API de filtrado estructurado, Aspose.Cells permite controlar directamente la visibilidad de cada elemento pivote individual. Al iterar por la colección `pivotField.getPivotItems()` de un `PivotField` y alternar la propiedad `isHidden`, puede suprimir selectivamente elementos concretos sin aplicar un filtro basado en fórmulas. Al establecer `pivotItem.isHidden = true`, el elemento se oculta de la tabla dinámica; al establecer `pivotItem.isHidden = false`, se muestra y vuelve a ser visible.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de cada elemento, por ejemplo, para ocultar unas pocas categorías con nombre que no deben aparecer en un informe concreto. El ejemplo siguiente carga una tabla dinámica, oculta un elemento concreto por nombre, demuestra cómo mostrarlo, actualiza la tabla dinámica y guarda el libro de trabajo.

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
                // Cargar un libro existente que contiene una tabla dinámica
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Acceder a la primera hoja de cálculo que contiene la tabla dinámica
                const sheet = workbook.worksheets.get(0);
                // Acceder a la tabla dinámica por índice (la primera tabla dinámica de la hoja)
                const pivotTable = sheet.pivotTables.get(0);
                // Obtener el campo dinámico de destino (el primer campo de etiqueta de fila en el que ocultaremos o mostraremos elementos)
                const pivotField = pivotTable.rowFields.get(0);
                // Recorrer la colección PivotItems del campo dinámico seleccionado
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Ocultar los elementos de la tabla dinámica que coincidan con un nombre o criterio específico
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demostrar cómo volver a mostrar un elemento de tabla dinámica previamente oculto
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Actualizar y recalcular la tabla dinámica para que los cambios surtan efecto
                pivotTable.refreshData();
                // Guardar el libro: los elementos ocultos permanecen en los datos subyacentes
                // pero se excluyen del resultado de la tabla dinámica mostrado
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
Aspose.Cells for JavaScript via C++ proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que coincide con las disponibles en Microsoft Excel. Los filtros por etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 principales gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `pivotItem.isHidden` ofrece una alternativa flexible a nivel de elemento. La combinación de estas estrategias —por ejemplo, aplicar un filtro por etiqueta y después ocultar elementos concretos— permite crear informes de tablas dinámicas dirigidos con precisión y totalmente mediante código.

{{< app/cells/assistant language="javascript-cpp" >}}