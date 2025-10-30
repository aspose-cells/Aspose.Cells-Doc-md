---
title: Borrar filtro en tabla dinámica
type: docs
weight: 130
url: /es/javascript-cpp/clear-filter-in-pivot-table/
description: Cómo limpiar el filtro de tabla dinámica en un campo específico de la tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript vía C++ Excel, biblioteca JavaScript de Excel, limpiar el filtro en la tabla dinámica usando Aspose.Cells for JavaScript vía C++ Excel Library.
---

## **Escenarios de uso posibles**
Cuando crea una tabla dinámica con datos conocidos y desea filtrarla, necesita aprender y usar filtros. Esto puede ayudarle a filtrar eficazmente los datos que desea. Mediante la API Aspose.Cells for JavaScript vía C++, puede operar filtros en los valores de los campos en tablas dinámicas. 

## **Cómo borrar el filtro en una tabla dinámica en Excel**
Limpiar filtro en Tabla Dinámica en Excel, sigue estos pasos:

1. Selecciona la Tabla Dinámica de la que deseas eliminar el filtro. 
2. Haz clic en la flecha desplegable para el filtro que deseas borrar en la tabla dinámica.
3. Selecciona "Limpiar filtro" en el menú desplegable.
<img src="1.png" width=80% />
4. Si deseas borrar todos los filtros de la tabla dinámica, también puedes hacer clic en el botón "Limpiar filtros" en la pestaña Analizar tabla dinámica en la cinta de Excel.
<img src="2.png" width=80% />

## **Cómo limpiar el filtro en la tabla dinámica usando Aspose.Cells for JavaScript vía C++**
Limpiar filtro en la tabla dinámica usando Aspose.Cells for JavaScript vía C++. Consulte el siguiente ejemplo de código. 
1. Establece los datos y crea una tabla dinámica basada en ellos. 
2. Agrega un filtro en el campo de fila de la tabla dinámica. 
3. Guarda el libro en formato XLSX de salida. Después de ejecutar el código de ejemplo, se añade un filtro top10 a la hoja de cálculo. 
4. Elimina el filtro en un campo de la tabla dinámica específico. Después de ejecutar el código para eliminar el filtro, se eliminará el filtro en el campo de la tabla dinámica específico. Por favor, revisa el XLSX de salida.

## **Código de muestra**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkAdd" style="display: none; margin-right: 10px;">Download Pivot Added File</a>
            <a id="downloadLinkDelete" style="display: none;">Download Pivot Filter Cleared File</a>
        </div>
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
            document.getElementById('result').innerHTML = '<p>Running example...</p>';

            // Create a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("A6");
            cell.value = "Guava";
            cell = cells.get("A7");
            cell.value = "Carambola";
            cell = cells.get("A8");
            cell.value = "Banana";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("B6");
            cell.value = 5;
            cell = cells.get("B7");
            cell.value = 2;
            cell = cells.get("B8");
            cell.value = 20;

            // Adding a PivotTable to the worksheet
            const i = ws.pivotTables.add("=A1:B8", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Count");
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;

            const field = pivotTable.rowFields.get(0);
            field.isAutoSort = true;
            field.isAscendSort = false;
            field.autoSortField = 0;

            // Add top10 filter
            const index = pivotTable.pivotFilters.add(field.baseIndex, AsposeCells.PivotFilterType.Count);
            const filter = pivotTable.pivotFilters.get(index);
            filter.autoFilter.filterTop10(0, true, false, 5);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after adding pivot/filter
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLinkAdd = document.getElementById('downloadLinkAdd');
            downloadLinkAdd.href = URL.createObjectURL(blob);
            downloadLinkAdd.download = 'out_add.xlsx';
            downloadLinkAdd.style.display = 'inline-block';
            downloadLinkAdd.textContent = 'Download out_add.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created and top10 filter applied. Download the file with pivot added.</p>';

            // Clear PivotFilter from the specific PivotField
            pivotTable.pivotFilters.clearFilter(field.baseIndex);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after clearing filter
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLinkDelete = document.getElementById('downloadLinkDelete');
            downloadLinkDelete.href = URL.createObjectURL(blob2);
            downloadLinkDelete.download = 'out_delete.xlsx';
            downloadLinkDelete.style.display = 'inline-block';
            downloadLinkDelete.textContent = 'Download out_delete.xlsx';

            document.getElementById('result').innerHTML += '<p style="color: green;">Pivot filter cleared and data recalculated. Download the file with filter removed.</p>';
        });
    </script>
</html>
```
