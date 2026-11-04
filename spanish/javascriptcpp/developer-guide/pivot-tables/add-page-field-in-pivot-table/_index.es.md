---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells for JavaScript via C++
description: Aprenda a agregar y configurar campos de filtro en tablas dinámicas mediante Aspose.Cells for JavaScript via C++, incluidos la adición de campos de filtro, el filtrado de selección única y el filtrado de selección múltiple.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Agregar campos de filtro
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en las tablas dinámicas. Puede agregar un campo de filtro mediante una API de alto nivel que simplifica las operaciones o mediante la colección de nivel inferior `getPageFields()`, y puede controlar el filtro en modo de selección única, limpiarlo para mostrar todos los elementos de filtro o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos de filtro a la vez mediante la interfaz de casillas de verificación de Excel.
{{% /alert %}}

## **Introducción**
Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como una lista desplegable en la parte superior de una tabla dinámica visualizada en Excel, y la selección de uno de los elementos de filtro disponibles reconstruye el cuerpo de la tabla dinámica de modo que solo se resuman los registros pertenecientes a ese elemento de filtro. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.Page` en lugar de `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Agregar un campo de filtro**

### Agregar un campo de filtro con `addFieldToArea`
El siguiente ejemplo crea un conjunto de datos pequeño de Fruit / Year / Amount, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtros, actualiza la tabla dinámica y guarda el libro de trabajo.

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
            worksheet.name = "Data";
            // Configurar la fila de encabezado
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Poblar 9 filas de datos de ejemplo: fruta, año y cantidad
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // Agregar una tabla dinámica anclada en la celda E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Agregar campos a sus áreas: Fruit como fila, Amount como datos y Year como campo de página
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Actualizar y calcular los datos de la tabla dinámica
            pivotTable.calculateData();
            // Guardar el libro
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### Agregar un campo de filtro con `getPageFields().add`
Cuando ya trabaje con una instancia de `PivotField`, puede pasarla directamente a `pivotTable.getPageFields().add(pivotField)`. La tabla dinámica y el campo de filtro se construyen exactamente igual que en el escenario anterior; solo el registro final en el área de filtros se sustituye por la llamada a la API de nivel inferior.

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
            // — La tabla dinámica y el campo de página se construyen exactamente como en
            //   el Escenario 1a (datos Fruit/Year/Amount, tabla dinámica en E3, Fruit→Fila,
            //   Amount→Datos). A continuación, obtenemos el PivotField Year de la
            //   colección BaseFields y lo pasamos a PageFields.Add: la
            //   alternativa de bajo nivel a AddFieldToArea. El resultado es
            //   funcionalmente idéntico al del Escenario 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Encabezados
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Datos de ejemplo (9 filas)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Agregar la tabla dinámica en E3 que cubre A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Fruit → Fila, Amount → Datos (Year se añadirá a Página a continuación)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Enfoque de bajo nivel: obtener el PivotField Year existente de BaseFields
            // y registrarlo en el área Página mediante PageFields.Add(PivotField).
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Actualizar para que el nuevo campo de página se refleje en el libro guardado
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Filtrado de selección única (mostrar un elemento de filtro)**
En el comportamiento predeterminado de selección única, el campo de filtro se representa como una única lista desplegable y el entero `pivotField.currentPageItem` selecciona qué elemento de filtro controla el cuerpo de la tabla dinámica. Al asignar un índice concreto, se elige ese único elemento; al asignar el valor centinela especial `0x7FFD` (32765 en decimal), se limpia el filtro de modo que todos los elementos de filtro se resuman a la vez. La selección única es el comportamiento predeterminado; no es necesario habilitarla de forma explícita.

### Mostrar todos los elementos
Establecer `currentPageItem` en el valor mágico `0x7FFD` equivale a limpiar el filtro: el cuerpo de la tabla dinámica resume todos los elementos de filtro como si no se hubiera aplicado ningún filtro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Crear un nuevo libro de trabajo
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Llenar los datos de fruta/año/cantidad
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // Crear una tabla dinámica en E3
            const pivotTables = sheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:C7", 2, 4);
            // Configurar los campos de la tabla dinámica: Fruit→Fila, Amount→Datos, Year→Página
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Limpiar el filtro de página para que todos los elementos del campo de página estén visibles.
            // 0x7FFD (decimal 32765) es el valor centinela especial que significa "todos los elementos":
            // equivale a seleccionar "(Todos)" en el menú desplegable del campo de página de Excel.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
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

### Mostrar un elemento específico
Establecer `currentPageItem` en un índice real selecciona únicamente ese elemento de filtro. El índice es la posición del elemento en la lista ordenada de elementos del campo de filtro, por lo que, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

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
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Crear libro
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Agregar datos de ejemplo (Fruta/Año/Cantidad)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Agregar tabla dinámica en E3
                const pivotTables = sheet.pivotTables;
                const pivotTable = pivotTables.add("=A1:C5", 2, 4);
                // Agregar campos: Fruit→Fila, Amount→Datos, Year→Página
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Operaciones específicas del campo de página
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = segundo elemento en orden clasificado (por ejemplo, "2021")
                // Actualizar y calcular la tabla dinámica
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Filtrado de selección múltiple**
El filtrado de selección múltiple convierte la lista desplegable de filtro en una lista de casillas de verificación y permite que el usuario final elija varios elementos de filtro de forma simultánea. Aspose.Cells expone dos propiedades que trabajan juntas. `pivotField.isMultipleItemSelectionAllowed` debe establecerse en `true` antes de que la interfaz de selección múltiple surta algún efecto. Una vez habilitada, `pivotItem.isHidden` controla qué elementos aparecen en la lista de casillas de verificación, por lo que puede mostrar todos los elementos o incluir en una lista blanca solo elementos concretos.

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — La tabla dinámica y el campo de página se construyen exactamente como en
                //   el Escenario 1a (datos Fruit/Year/Amount,动态 en E3, Fruit→Fila,
                //   Amount→Datos, Year→Página mediante AddFieldToArea).
                //   A continuación, aplicamos el filtrado de selección múltiple al campo de página.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Datos de ejemplo: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTable = pivots.add("=A1:C10", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Habilitar la selección múltiple en el campo de página
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Parte A — seleccionar TODOS los elementos (hacer visible cada elemento)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Parte B — seleccionar solo elementos específicos por valor de origen
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Nota:** Al utilizar el filtrado de selección múltiple mediante `pivotItem.isHidden`, **al menos un `PivotItem` debe seguir visible** (`isHidden === false`). Si se ocultan todos los elementos, Excel puede bloquearse al abrir el archivo o mostrar una tabla dinámica vacía. Verifique siempre que la lista blanca de selección múltiple incluya al menos un elemento de los datos de origen.

## **¿Qué API y qué modo debo usar?**
La tabla siguiente resume cuándo utilizar cada API y cada modo, de modo que pueda elegir la combinación adecuada sin tener que leer todos los escenarios en detalle.
| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por el nombre de la columna de origen (caso más común) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | De alto nivel, en una sola línea. Utilícela salvo que necesite una referencia a `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `pivotTable.getPageFields().add(pivotField)` | n/a | Utilícela cuando el objeto de campo se haya obtenido en otro lugar o deba reutilizarse. |
| Filtrar por un único elemento de filtro (modo predeterminado) | `pivotField.currentPageItem` | establecer en un índice concreto | Por ejemplo, `1` muestra el segundo elemento de la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro | `pivotField.currentPageItem` | establecer en `0x7FFD` | El valor mágico `0x7FFD` (32765 en decimal) es el valor centinela de "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `pivotField.isMultipleItemSelectionAllowed` | establecer en `true` | Necesario antes de que cualquier asignación a `isHidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `pivotItem.isHidden` | establecer por elemento | Al menos un elemento debe seguir visible (`isHidden === false`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si se oculta cada `PivotItem` de un campo de filtro con selección múltiple, Excel se bloquea al abrirse o muestra una tabla dinámica vacía. Construya la lista blanca a partir de los datos de origen para que al menos un elemento siga siendo visible, y los libros de trabajo guardados se abrirán de forma fiable en cualquier equipo.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}