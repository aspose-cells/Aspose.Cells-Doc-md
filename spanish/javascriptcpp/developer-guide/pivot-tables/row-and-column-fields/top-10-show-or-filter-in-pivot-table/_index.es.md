---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con la clasificación más alta o más baja de un campo de tabla dinámica en Aspose.Cells for JavaScript via C++. Este artículo explica las propiedades AutoShow de Excel 97-2003 (isAutoShow y otras propiedades similares), la lectura de las opciones y el filtro de los 10 principales de Excel 2007-365 mediante filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, tabla dinámica, 10 principales, AutoShow, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /es/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede resultar difícil de leer cuando el campo contiene decenas de miembros. Un informe de los 10 principales conserva únicamente los elementos con la clasificación más alta o más baja, exactamente lo que necesitan los informes de clasificación: «5 productos principales por ingresos» o «3 regiones inferiores por número de ventas». Aspose.Cells admite dos mecanismos para ello, que corresponden a dos generaciones de Microsoft Excel.
- **AutoShow de Excel 97-2003** — las cuatro propiedades de `PivotField`: `isAutoShow`, `isAscendShow`, `autoShowCount` y `autoShowField`. Esta es la configuración clásica «Mostrar los N elementos principales/inferiores», almacenada directamente en el campo de tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como modernas, porque forma parte del formato original de tabla dinámica.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.filterTop10()`. Este es el filtro moderno de valores «10 principales», disponible en «Filtros de valores» del menú del campo. Se almacena como un objeto `PivotFilter` asociado al campo y ofrece una clasificación basada en el número de elementos o en porcentajes.

## **Mostrar los 10 principales en Excel 97-2003 (AutoShow)**
El AutoShow clásico se configura mediante cuatro asignaciones de propiedades en `PivotField`:
- `isAutoShow` — habilita o deshabilita la configuración de AutoShow en el campo.
- `isAscendShow` — `false` conserva los elementos con mayor clasificación (Principales), mientras que `true` conserva los de menor clasificación (Inferiores).
- `autoShowCount` — el número de elementos que se conservan, por ejemplo, 10 para un informe clásico de los 10 principales.
- `autoShowField` — el índice de base cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos por el propio campo.
La clasificación puede estar determinada por un campo de valores o por el propio campo. Hay dos variantes habituales, que se muestran a continuación.

### **Clasificar por un campo de valores**
Clasifique los elementos del campo de fila por un campo de valores convencional, como «Suma de ventas». El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y después muestra los 2 deportes con mayor volumen de ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos que ocupa el índice 0.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Mostrar los 2 elementos principales clasificados por "Suma de ventas" (índice del campo de datos 0)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Clasificar por el propio campo**
También es posible clasificar un campo por sí mismo: pase -1 a `autoShowField`. Esta variante no necesita ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con menor clasificación según el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y al leer `autoShowField`, se obtiene -1.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Mostrar los 3 elementos inferiores clasificados por el propio campo (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Leer las opciones actuales de AutoShow**
Las propiedades de `PivotField` (`isAutoShow`, `isAscendShow`, `autoShowCount` y `autoShowField`) exponen las opciones de AutoShow almacenadas actualmente en el campo. Úselas para comprobar cómo se muestran los elementos en un libro de trabajo existente o en una tabla dinámica recién configurada, incluidos los libros de trabajo cargados desde un archivo.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

Las cuatro propiedades se corresponden con los atributos clásicos de AutoShow que se escriben en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que todas las versiones de Excel respetarán los valores leídos.

## **Nota**

{{% alert color="primary" %}}
- Después de cambiar cualquier propiedad de AutoShow, vuelva a llamar a `pivotTable.calculateData()`. La configuración solo se refleja en el diseño después del siguiente recálculo.
- La configuración de AutoShow funciona con campos de fila y columna. Un campo que se encuentra únicamente en el área de página (filtro) no se puede clasificar de esta manera porque sus elementos no aparecen en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (filterTop10)**
Las versiones modernas de Excel ofrecen los 10 principales como un filtro de valores en el menú del campo (Filtros de valores, 10 principales...). Aspose.Cells lo representa mediante el método `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`, que devuelve el `PivotFilter` creado:
- `valueFieldIndex` — el índice de base cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — el significado de `itemCount`. `PivotFilterType.Count` conserva un número fijo de elementos (la opción «Elementos» del cuadro de diálogo). `PivotFilterType.Percent` conserva un porcentaje de los elementos, de modo que `itemCount` es el propio porcentaje: 30 conserva el 30 % de los elementos con mayor clasificación. `PivotFilterType.Sum` clasifica los elementos según la cobertura acumulativa de los valores.
- `isTop` — `true` para principales y `false` para inferiores.
- `itemCount` — el valor N en «N principales»; su unidad depende de `type`.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Las propiedades de AutoShow y `filterTop10` son dos mecanismos distintos. AutoShow escribe el atributo clásico `autoShow` en el campo de tabla dinámica y se respeta en todas las versiones de Excel desde Excel 97. `filterTop10` escribe una entrada moderna de `PivotFilter`, que requiere Excel 2007 o posterior. Cuando un libro de trabajo se abre en una versión anterior de Excel, una tabla dinámica que utiliza el filtro moderno vuelve a mostrar todos los elementos. Para los documentos que deben procesarse con herramientas heredadas sin perder fidelidad, prefiera las propiedades de AutoShow; para los libros de trabajo modernos, prefiera `filterTop10` porque se integra con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de una tabla dinámica](/cells/es/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}