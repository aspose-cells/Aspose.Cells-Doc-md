---
title: Обновление значений связанных фигур с помощью JavaScript через C++
linktitle: Обновить значения связанных форм
type: docs
weight: 3200
url: /ru/javascript-cpp/refresh-values-of-linked-shapes/
description: Узнайте, как обновлять значения связанных фигур в Excel при помощи Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}

Иногда в вашем файле Excel есть связанная фигура, которая связана с некоторой ячейкой. В Microsoft Excel изменение значения связанной ячейки также изменяет значение связанной фигуры. Это также работает в Aspose.Cells for JavaScript через C++, если вы хотите сохранить рабочую книгу в формате XLS или XLSX. Однако, если вы хотите сохранить рабочую книгу в формате PDF или HTML, тогда вам придется вызвать метод [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) для обновления значения связанной фигуры.

{{% /alert %}}

## Пример

Следующий скриншот показывает исходный файл Excel, использованный в приведенном ниже примере кода. В нем есть связанная картинка, связанная с ячейками A1 до E4. Мы изменим значение ячейки B4 с помощью Aspose.Cells и вызовем метод [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) для обновления значения картинки и сохранения его в PDF-формате.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Вы можете скачать [исходный файл Excel](95584291.xlsx) и [итоговый PDF](95584292.pdf) по указанным ссылкам.

### JavaScript код для обновления значений связанных фигур

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
