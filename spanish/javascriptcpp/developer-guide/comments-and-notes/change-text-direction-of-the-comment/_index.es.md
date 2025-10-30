---
title: Cambiar la dirección del texto del comentario con JavaScript vía C++
linktitle: Cambiar la dirección del texto del comentario
type: docs
weight: 10
url: /es/javascript-cpp/change-text-direction-of-the-comment/
description: Aprende cómo cambiar la dirección del texto de los comentarios usando Aspose.Cells for JavaScript vía C++. Personaliza eficazmente la configuración del alineamiento del comentario.
---

{{% alert color="primary" %}}

 Microsoft Excel permite a los usuarios agregar comentarios a las celdas para proporcionar información adicional y resaltar datos. Los desarrolladores pueden necesitar personalizar el comentario para especificar la configuración del alineamiento y la dirección del texto. Aspose.Cells for JavaScript a través de C++ proporciona API para realizar esta tarea.

{{% /alert %}}

 Aspose.Cells for JavaScript vía C++ proporciona una propiedad [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) para establecer la dirección del texto en un comentario. El siguiente código de ejemplo demuestra el uso de la propiedad [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) para configurar la dirección del texto en un comentario.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment Shape</title>
    </head>
    <body>
        <h1>Add Comment Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, TextDirectionType } = AsposeCells;

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
            // Instantiate a new Workbook
            const wb = new Workbook();

            // Get the first worksheet
            const sheet = wb.worksheets.get(0);

            // Add a comment to A1 cell
            const commentIndex = sheet.comments.add("A1");
            const comment = sheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set its horizontal alignment setting
            comment.commentShape.textHorizontalAlignment = TextAlignmentType.Right;

            // Set the Text Direction - Right-to-Left
            comment.commentShape.textOrientationType = TextDirectionType.RightToLeft;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is test";

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutCommentShape.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
