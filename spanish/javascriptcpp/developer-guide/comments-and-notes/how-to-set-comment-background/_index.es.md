---
title: Cómo cambiar el fondo de un comentario en Excel con JavaScript vía C++
linktitle: Fondo del comentario
type: docs
weight: 190
url: /es/javascript-cpp/how-to-set-comment-background/
description: Cómo cambiar el color en un comentario e insertar una imagen o imagen en el comentario en Excel usando Aspose.Cells for JavaScript vía C++.
keywords: agregar imagen insetada, color del comentario, fondo en Excel JavaScript vía C++
---

{{% alert color="primary" %}}
Los comentarios se añaden a las celdas para registrar observaciones, desde los detalles de cómo funciona una fórmula, el origen de un valor o preguntas de los revisores. Los comentarios juegan un papel muy importante cuando varias personas discuten o revisan el mismo documento en diferentes momentos. ¿Cómo distinguir los comentarios de diferentes personas? Sí, podemos establecer un color de fondo diferente para cada comentario. Pero cuando necesitamos procesar muchos documentos y un gran número de comentarios, hacerlo manualmente es un caos. Afortunadamente, [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) proporciona una API que te permite hacer esto en código.
{{% /alert %}}

## **Cómo cambiar el color en el comentario en Excel**

Cuando no necesitas el color de fondo predeterminado para los comentarios, tal vez quieras reemplazarlo por un color de tu interés. ¿Cómo cambio el color de fondo del cuadro de Comentarios en Excel?

El siguiente código le guiará sobre cómo usar [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) para agregar su color de fondo favorito a los comentarios de su elección.

Aquí hemos preparado un [archivo de ejemplo](exmaple.xlsx) para ti. Este archivo se usa para inicializar el objeto Workbook en el código a continuación.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change Comment Background Color Example</title>
    </head>
    <body>
        <h1>Change Comment Background Color Example</h1>
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

            // Initialize a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the newly added comment
            const comment = workbook.worksheets.get(0).comments.get(0);

            // change background color
            const shape = comment.commentShape;
            shape.fill.solidFill.color = AsposeCells.Color.Red;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment background color changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Ejecute el código anterior y obtendrá un [archivo de salida](result.xlsx).

## **Cómo insertar una imagen en el comentario en Excel**

Microsoft Excel permite a los usuarios personalizar el aspecto de las hojas de cálculo en gran medida. Incluso es posible agregar imágenes de fondo a los comentarios. Agregar una imagen de fondo puede ser una opción estética o usarse para reforzar la marca.

El código de ejemplo a continuación crea un archivo XLSX desde cero usando la API de [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/), y agrega un comentario con fondo de imagen en la celda A1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Comment with Picture Example</h1>
        <p>
            Select an existing Excel file (optional) and an image file to attach to a comment in cell A1.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert in comment (required):</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the comment.</p>';
                return;
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get comments collection for the first sheet
            const comments = worksheet.comments;

            // Add a comment to cell A1 (row 0, column 0)
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set comment text and font name (converted from setters to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load the selected image file and set it to the comment's shape fill imageData
            const imageFile = imageInput.files[0];
            const imgArrayBuffer = await imageFile.arrayBuffer();
            const imageData = new Uint8Array(imgArrayBuffer);

            comment.commentShape.fill.imageData = imageData;

            // Save the workbook to a blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'commentwithpicture1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Comment with picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</body>
</html>
```
