---
title: Управление текстовыми полями с помощью JavaScript через C++
linktitle: Управление текстовым полем
type: docs
weight: 50
url: /ru/javascript-cpp/managing-textbox-of-excel/
description: Узнайте, как управлять TextBox в Excel с помощью Aspose.Cells for JavaScript через C++. 
keywords: Управление TextBox в Excel с помощью JavaScript через C++
---

## **Возможные сценарии использования**
Существуют ситуации, когда вам может понадобиться добавлять, обновлять или управлять объектами TextBox внутри листа Excel. Это может быть полезно для добавления аннотаций, руководящих текстов или любой дополнительной информации, которая помогает в представлении данных. Aspose.Cells for JavaScript через C++ предоставляет надежный функционал для управления TextBox в документах Excel. 

## **Управление TextBox с помощью Aspose.Cells for JavaScript через C++**
Этот пример показывает, как:

1. Создайте новую книгу.
2. Добавьте фигуру TextBox.
3. При необходимости измените свойства TextBox.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Этот код демонстрирует, как создавать и настраивать текстовое поле в листе Excel, показывая, как изменять его размер, положение и оформлять в соответствии с требованиями.

 Учтите, что взаимодействие с текстовыми полями может различаться в зависимости от конкретных сценариев использования, поэтому обращайтесь к документации Aspose.Cells for JavaScript через C++ для получения дополнительных методов и свойств.
