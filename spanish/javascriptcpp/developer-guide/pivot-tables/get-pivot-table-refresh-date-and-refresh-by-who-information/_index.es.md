---
title: Obtener la fecha de actualización de la tabla dinámica e información de quién la actualizó
type: docs
weight: 100
url: /es/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Cómo obtener la fecha de actualización de la tabla dinámica y quién la actualizó con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript Excel, biblioteca JavaScript de Excel, obtener la fecha de actualización de la tabla dinámica y quién la actualizó usando Aspose.Cells for JavaScript Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript vía C++ ahora soporta obtener la fecha de actualización y quién la actualizó desde un libro de trabajo.

{{% /alert %}}

## **Cómo obtener la fecha de actualización de la tabla dinámica y la información sobre quién la actualizó**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) devuelve la fecha en la que se actualizó por última vez el informe de la tabla dinámica. De manera similar, la propiedad [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) devuelve el nombre del usuario que actualizó el informe la última vez. El siguiente ejemplo demuestra esta característica y el archivo de ejemplo se puede descargar desde el siguiente enlace.

[SourcePivotTable.xlsx](77496335.xlsx)

**Código de Ejemplo**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
