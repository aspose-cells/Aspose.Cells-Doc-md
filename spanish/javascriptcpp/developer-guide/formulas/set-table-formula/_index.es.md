---
title: Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas con JavaScript a través de C++
linktitle: Establecer fórmula de tabla
type: docs
weight: 260
url: /es/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Aprende cómo propagar automáticamente fórmulas en tablas u objetos de lista al ingresar datos en nuevas filas usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**
A veces, quieres que una fórmula en tu Tabla u Objeto de Lista se propague automáticamente a nuevas filas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr la misma funcionalidad con Aspose.Cells for JavaScript a través de C++, por favor usa la propiedad [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--).

## **Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea una Tabla u Objeto de Lista de tal manera que la fórmula en la columna B se propagará automáticamente a filas nuevas cuando ingreses nuevos datos. Por favor, revisa el [archivo Excel de salida](5115469.xlsx) generado con este código. Si ingresas cualquier número en la celda A3, verás que la fórmula en la celda B2 se propagará automáticamente a la celda B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
