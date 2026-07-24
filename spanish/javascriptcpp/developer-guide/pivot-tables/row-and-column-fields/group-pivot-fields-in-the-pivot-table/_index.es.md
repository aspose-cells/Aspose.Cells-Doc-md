---
title: Agrupar campos de pivote en la tabla dinámica
type: docs
weight: 80
url: /es/javascript-cpp/group-pivot-fields-in-the-pivot-table/
description: Cómo agrupar campos pivote en la tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript vía C++ Excel, biblioteca JavaScript de Excel, cómo agrupar campos pivote en la tabla dinámica usando Aspose.Cells for JavaScript vía C++ Excel Library.
---

## **Escenarios de uso posibles**

Microsoft Excel te permite agrupar campos de tabla dinámica en la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo de tabla dinámica, a menudo es útil agruparlos en secciones. Aspose.Cells for JavaScript vía C++ también ofrece esta función usando el método [**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **Cómo agrupar campos de tabla dinámica en la tabla dinámica**

El siguiente código de muestra carga el [archivo Excel de muestra](64716818.xlsx) y realiza agrupaciones en el primer campo de tabla dinámica utilizando el método [**PivotTable.groupBy()**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). Luego actualiza y calcula los datos de la tabla dinámica y guarda la hoja de cálculo como [archivo Excel de salida](64716817.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, el primer campo de tabla dinámica está ahora agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Example</title>
    </head>
    <body>
        <h1>Group Pivot Fields in PivotTable</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotGroupByType } = AsposeCells;

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

            // Load workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the second worksheet
            const ws = wb.worksheets.get(1);

            // Access the pivot table
            const pt = ws.pivotTables.get(0);

            // Specify the start and end date time
            const dtStart = new Date(2008, 1, 1);
            const dtEnd = new Date(2008, 9, 5);

            // Specify the group type list, we want to group by months and quarters
            const groupTypeList = [PivotGroupByType.Months, PivotGroupByType.Quarters];

            // Apply the grouping on first pivot field
            const field = pt.rowFields.get(0);
            field.groupBy(dtStart, dtEnd, groupTypeList, 1, true);

            // Refresh and calculate pivot table
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGroupPivotFieldsInPivotTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
