---
title: Modificar la disposición de los campos de página en una tabla dinámica
linktitle: Modificar la disposición de los campos de página en una tabla dinámica
description: Aprenda a controlar la disposición del área de campos de página de una tabla dinámica con Aspose.Cells for JavaScript via C++, incluidos el orden de visualización, el número de campos por fila o columna antes del ajuste y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells for JavaScript via C++, hoja de cálculo, tabla dinámica, campo de página, orden de campos de página, número de campos de página antes del ajuste, mover campos de página
type: docs
weight: 191
url: /es/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Este artículo es una continuación del tema **Agregar un campo de página en una tabla dinámica**. Demuestra cómo controlar la disposición del área de campos de página (la franja de controles de filtrado situada en la parte superior de una tabla dinámica), incluidos el orden de visualización, el número de campos por fila o columna antes del ajuste y la reordenación de los campos.
{{% /alert %}}

## **Introducción**
Una tabla dinámica de Microsoft Excel ofrece un **área de campos de página** dedicada, situada encima del cuerpo de filas, columnas y datos de la tabla. Esta área se representa como una franja de controles de filtrado desplegables, uno por cada campo de página, en la que los usuarios finales hacen clic para filtrar la tabla dinámica según criterios como el año o la región. Aspose.Cells modela esta área mediante la colección `pivotTable.pageFields` y expone tres propiedades que controlan cómo se organiza visualmente la franja:
- `pivotTable.pageFieldOrder` (un valor de `Aspose.Cells.PrintOrderType`) determina si los campos de página adicionales se colocan *junto a* los existentes o *debajo* de ellos.
- `pivotTable.pageFieldWrapCount` establece cuántos campos de página se colocan en cada fila o columna antes de pasar a la siguiente.
- `pivotTable.pageFields.move(currIndex, destIndex)` reordena los campos de página sin cambiar el modo de orden.
Este artículo presenta tres ejemplos de código que demuestran estas operaciones con un conjunto de datos común, para que pueda comparar las disposiciones resultantes en paralelo.

## **Datos de origen**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Las ocho filas están rellenadas con datos en todos los ejemplos de código y mantienen el mismo orden, por lo que los datos de origen no varían entre los escenarios; solo cambian las propiedades de disposición de los campos de página.

## **Ejemplo 1: Primero en horizontal y luego en vertical**
En el primer escenario, configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **uno junto al otro en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, colocamos `Year` primero y `Region` segundo en el eje de campos de página (el orden de las llamadas `addFieldToArea` determina el índice inicial), añadimos `Amount` (`Sum`) como campo de datos y, a continuación, establecemos `pivotTable.pageFieldOrder` en `PrintOrderType.OverThenDown` y `pivotTable.pageFieldWrapCount` en `2`. Con `OverThenDown` y `pivotTable.pageFieldWrapCount` igual a `2`, los dos campos de página se colocan horizontalmente, uno junto al otro, en una sola fila en la parte superior de la tabla dinámica; por lo tanto, la franja ocupa una fila con dos campos.

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
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // Encabezados (fila 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Fila 1: Manzana, 2022, Norte, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Fila 2: Manzana, 2023, Norte, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Fila 3: Plátano, 2022, Sur, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Fila 4: Plátano, 2023, Sur, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Fila 5: Cereza, 2022, Este, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Fila 6: Cereza, 2023, Este, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Fila 7: Uva, 2022, Oeste, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Fila 8: Uva, 2023, Oeste, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // Agregar la hoja PivotTableReport
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // Crear una tabla dinámica con origen PivotData!A1:D9 y colocarla en A1 de PivotTableReport
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Agregar campos
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruta
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Año
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Región
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Importe
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Configurar el diseño del área de campos de página: colocar los campos de página horizontalmente primero y ajustar después de cada 2
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Actualizar y calcular
            pivotTable.calculateData();
            // Guardar
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Ejemplo 2: Primero en vertical y luego en horizontal**
En este ejemplo, colocamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de campos de página (con `Year` primero) y `Amount` (`Sum`) como campo de datos, exactamente como en el ejemplo 1. A continuación, establecemos `pivotTable.pageFieldOrder` en `PrintOrderType.DownThenOver` y `pivotTable.pageFieldWrapCount` en `2`. Con `DownThenOver` y `pivotTable.pageFieldWrapCount` igual a `2`, los dos campos de página se apilan verticalmente (`Year` arriba y `Region` justo debajo), formando una sola columna en la parte superior de la tabla dinámica. Por tanto, la franja ocupa dos filas con un campo cada una, a diferencia del ejemplo 1.

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
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Ejemplo 3: Mover un campo de página**
En el tercer escenario, mantenemos este conjunto de datos y esta asignación de campos, establecemos una disposición neutral (`OverThenDown` con `pivotTable.pageFieldWrapCount` igual a `2`) y, a continuación, demostramos la operación `pivotTable.pageFields.move`. La llamada `move(0, 1)` mueve el campo de página situado en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) pasa a la posición 0. Después de esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El ajuste y el modo de orden no cambian, por lo que la franja sigue presentándose horizontalmente, con los dos campos uno junto al otro; solo se ha intercambiado el orden de los dos controles desplegables.

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
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Artículos relacionados**
- [Agregar un campo de página en una tabla dinámica](/cells/es/javascript-cpp/add-page-field-in-pivot-table/) — el artículo principal que presenta cómo agregar campos de página a una tabla dinámica.
- [Administrar campos de valor en una tabla dinámica](/cells/es/javascript-cpp/manage-value-fields/) — explica cómo configurar el área de datos (valores), incluida la agregación `Sum` utilizada en este artículo.
- [Aplicar estilo a una tabla dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica después de disponer la franja de campos de página.

{{< app/cells/assistant language="javascript-cpp" >}}