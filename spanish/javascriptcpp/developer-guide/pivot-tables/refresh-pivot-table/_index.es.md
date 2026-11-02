---
title: Actualizar tablas dinámicas y cachés en Aspose.Cells for JavaScript via C++
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for JavaScript via C++ mediante la API de actualización de tablas dinámicas v26.7+. Este artículo cubre workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData y pivotCache.getPivotTables con ejemplos de código prácticos.
linktitle: Actualizar tablas dinámicas
keywords: Aspose.Cells, JavaScript via C++, tabla dinámica, actualización, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /es/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece una API de actualización por capas que le permite recargar los datos de las tablas dinámicas en cuatro ámbitos distintos, desde el libro de trabajo completo hasta una sola tabla dinámica. A partir de **Aspose.Cells for JavaScript via C++ v26.7**, el método heredado `pivotTable.refreshData()` queda marcado como obsoleto y debe sustituirse por las API más eficientes, que tienen en cuenta la caché, descritas en este artículo.
{{% /alert %}}

## Introducción
Actualizar una tabla dinámica rara vez es una sola operación. Internamente, Aspose.Cells mantiene una cadena de datos por capas que conecta los datos de origen originales con los valores mostrados en la hoja de cálculo. Comprender esta cadena es clave para elegir la API de actualización adecuada en cada situación.
La cadena de datos de cuatro capas es:
1. **Fuente de datos**: los rangos originales de la hoja de cálculo, la consulta a una base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **`PivotCache`**: la instantánea en memoria de los datos de origen. Todas las tablas dinámicas se construyen sobre un `PivotCache`; aquí se recopilan y agregan todos los datos.
3. **`PivotTable`**: el objeto de vista que define los campos de fila, columna, valor y filtro. Un `PivotTable` lee *únicamente* de su `PivotCache`, nunca directamente de la fuente de datos.
4. **`Cells`**: las celdas de la hoja de cálculo devueltas por `getCells()`, donde el objeto `PivotTable` renderiza sus valores calculados y sus estilos.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (el tipo de enumeración `PivotTableSourceType`) indica de dónde proceden los datos de la caché. A partir de la versión v26.7, `pivotCache.refresh()` solo admite los tipos de origen **`SHEET`** y **`CONSOLIDATION`**, es decir, datos que residen en rangos de la hoja de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) todavía no se pueden actualizar mediante la API de caché.
Debido a esta cadena, Aspose.Cells ofrece dos rutas fundamentales de actualización:
- **`pivotTable.calculateData()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver a consultar la fuente de datos.
Todos los escenarios de este artículo utilizan datos de origen almacenados en celdas de hojas de cálculo, por lo que el tipo de origen es `SHEET` y las operaciones de actualización se comportan como se describe.
{{% /alert %}}

## Inicio rápido
Si solo necesita el código más breve posible que actualice todas las tablas dinámicas del libro de trabajo, basta una sola llamada:

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
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Todo lo demás en este artículo explica cuándo elegir una API más acotada en su lugar.

## Importaciones necesarias
Todos los ejemplos de JavaScript de este artículo comienzan con la siguiente importación de módulo porque los tipos de tabla dinámica se exponen mediante el namespace `Aspose.Cells.Pivot`:
- `const Aspose = require('aspose.cells');`

## Actualizar todas las tablas dinámicas del libro de trabajo
Cuando necesite garantizar que todas las cachés de tablas dinámicas y todas las tablas dinámicas del libro de trabajo reflejen los datos de origen más recientes, la API más simple y completa es `workbook.refreshAll()`. Una sola llamada recorre todo el libro de trabajo: actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de todo el documento cuando el rendimiento no es un factor importante.
El siguiente ejemplo crea un libro de trabajo con un rango de origen `Fruit`/`Year`/`Amount`, crea una tabla dinámica, modifica algunos valores de origen y, a continuación, utiliza `refreshAll()` para actualizar todos los componentes con una sola llamada.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Crear un nuevo libro
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Escribir la fila de encabezado en las celdas A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Escribir filas de datos en las celdas A2:C9 (8 filas de datos de frutas de 2020 y 2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Agregar una tabla dinámica: rango de origen "A1:C9", celda de destino "E3"
            const pivotTableIndex = worksheet.pivotTables.add(
                "=A1:C9",
                "E3",
                "PivotTable1"
            );
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Asignar campos de tabla dinámica: Fruit a Filas, Year a Columnas, Amount a Datos
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Modificar varios valores de Amount en los datos de origen para simular cambios
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Actualizar todas las tablas dinámicas y cachés de tablas dinámicas del libro
            workbook.refreshAll();
            // Guardar el libro
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Actualizar todas las tablas dinámicas de una sola hoja de cálculo
En ocasiones, solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo concreta, por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas de cálculo no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells ofrece `worksheet.refreshPivotTables()`, que está limitada a una sola instancia de `Worksheet`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTableIndex = worksheet.pivotTables.add("=A1:C9", "E3", "PivotTable1");
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## Actualizar una sola tabla dinámica
Cuando necesite un control detallado de una sola tabla dinámica, la API basada en caché ofrece dos opciones. La elección depende de qué haya cambiado realmente: los datos de origen subyacentes o solo los ajustes de vista o diseño de la tabla dinámica en sí.

### Los datos de origen cambiaron: use `pivotCache.refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.getPivotCache().refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada objeto `PivotTable` que depende de esa caché.

### Solo cambiaron la vista o el diseño: use `pivotTable.calculateData()`
Si los datos de origen *no* han cambiado, pero solo se han modificado los ajustes de vista o diseño de la tabla dinámica (por ejemplo, si se ha movido un campo a otra área o se ha activado o desactivado un ajuste de actualización al abrir), no es necesario volver a consultar la fuente de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` mostrada. En este caso, `pivotTable.calculateData()` es la opción correcta.
El siguiente ejemplo modifica una propiedad que no pertenece a la fuente de la tabla dinámica y, a continuación, llama a `calculateData()` para volver a renderizarla a partir de la caché existente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Escribir la fila de encabezado Fruit / Year / Amount
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // Escribir 8 filas de datos (filas 2-9, que caben en el rango de origen A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Agregar una tabla dinámica colocada en la celda de destino E3, usando A1:C9 como origen
                const pivotTableIndex = worksheet.pivotTables.add(
                    "=A1:C9",
                    "E3",
                    "PivotTable1"
                );
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                // Asignar campos: Fruit a Row, Year a Column, Amount a Data
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Modificar una propiedad de vista/diseño: este es un cambio solo de presentación,
                // por lo que NO requiere volver a leer los datos de origen mediante PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() vuelve a renderizar la visualización (datos + estilo) de ESTA tabla dinámica a partir de los
                // datos ya almacenados en PivotCache. Como los datos de origen no cambiaron,
                // no se realiza ningún viaje de ida y vuelta a la fuente; solo se recalculan los valores almacenados en caché
                // en las celdas de la hoja de cálculo.
                pivotTable.calculateData();
                // Guardar el libro en disco
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Con frecuencia, un libro de trabajo contiene muchas tablas dinámicas que se apoyan todas en una única caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de una caché compartida, utilice `pivotCache.getPivotTables()`. Este método devuelve la colección de todos los objetos `PivotTable` que dependen de la caché especificada.

## Migración desde el método obsoleto `pivotTable.refreshData()`
Antes de Aspose.Cells for JavaScript via C++ v26.7, la forma habitual de actualizar una tabla dinámica era llamar a `pivotTable.refreshData()` por separado en cada tabla dinámica. A partir de la versión v26.7, ese método queda marcado como **obsoleto** y debe sustituirse por las API que tienen en cuenta la caché, descritas anteriormente.
Hay dos razones por las que el enfoque `refreshData()` por tabla resulta problemático en libros de trabajo reales:
- Vuelve a obtener los datos de la fuente *cada vez* que se invoca, incluso cuando la fuente no ha cambiado.
Las sustituciones recomendadas son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros de trabajo con varias tablas dinámicas que comparten una única caché.

## ¿Qué API de actualización debo utilizar?
La siguiente tabla resume las API de actualización disponibles y cuándo elegir cada una.
| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro de trabajo | `workbook.refreshAll()` | Una llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `worksheet.refreshPivotTables()` | Limitada a una hoja de cálculo. |
| Los datos de origen cambiaron para una caché | `pivotTable.getPivotCache().refresh()` | Actualiza TODAS las tablas dinámicas de esa caché compartida. |
| Solo cambiaron los ajustes de vista o diseño | `pivotTable.calculateData()` | Evita la consulta innecesaria a la fuente. |
| Enumerar todas las tablas dinámicas de una caché compartida | `pivotCache.getPivotTables()` | Utilícela para enumerarlas antes de una actualización masiva. |
En la práctica, prefiera las API basadas en caché en lugar del método obsoleto `refreshData()` por tabla. Son conscientes de las cachés compartidas, evitan obtener datos de la fuente de forma redundante y le permiten elegir el ámbito más pequeño que satisfaga su requisito de actualización.

## Problemas comunes
- **Olvidarse de actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores mostrados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica celdas de origen, llame a `pivotCache.refresh()` (o `workbook.refreshAll()`) antes de `workbook.save()`; de lo contrario, el archivo guardado todavía contendrá los valores agregados anteriores.
- **Llamar al método obsoleto `refreshData()` por tabla.** En la versión v26.7, `pivotTable.refreshData()` está marcado como obsoleto y vuelve a obtener los datos de la fuente en cada llamada. Con varias tablas dinámicas que comparten una caché, esto significa N recuperaciones redundantes de la fuente. Sustitúyalo por una única llamada a `pivotCache.refresh()` seguida de `pivotTable.calculateData()` para cada tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `getConsolidationFunction()`, etc.) sin modificar los datos de origen, `pivotCache.refresh()` es innecesario y lento. Llame a `pivotTable.calculateData()` para volver a renderizar a partir de la caché existente.
- **Origen externo no compatible con `pivotCache.refresh()`.** Si el origen de la tabla dinámica procede de una conexión externa (base de datos, cubo OLAP, etc.), `pivotCache.refresh()` no puede actualizarlo en la versión v26.7; actualmente solo admite los tipos de origen `SHEET` y `CONSOLIDATION`. Para fuentes externas, vuelva a abrir el libro de trabajo o reconstruya la caché a partir del origen.

{{< app/cells/assistant language="javascript-cpp" >}}