---
title: Establecer el Comentario de la Tabla u Objeto de Lista dentro de la Hoja de Cálculo con JavaScript vía C++
linktitle: Establecer el comentario de una tabla o un objeto de lista dentro de la hoja de cálculo
type: docs
weight: 40
url: /es/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Aprenda a establecer el comentario de la tabla u objeto de lista dentro de la hoja usando Aspose.Cells for JavaScript vía C++. 
---

{{% alert color="primary" %}}

Puede establecer el comentario de la Tabla u Objeto de Lista dentro de la hoja de cálculo usando la propiedad [**ListObject.comment**](https://reference.aspose.com/cells/javascript-cpp/listobject/#comment--). El comentario será visible dentro del archivo xl/tables/tableName.xml.

{{% /alert %}}

## **Establecer el Comentario de la Tabla o Objeto de Lista dentro de la Hoja de Cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de origen](5115514.xlsx), establece el comentario de la primera tabla u objeto de lista dentro de la hoja de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Comment of Table/ListObject</title>
    </head>
    <body>
        <h1>Set Comment of Table/ListObject</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first list object or table.
            const lstObj = worksheet.listObjects.get(0);

            // Set the comment of the list object
            lstObj.comment = "This is Aspose.Cells comment.";

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetCommentOfTableOrListObject_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
