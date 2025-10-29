---
title: Вставить привязанное изображение с веб адреса с помощью JavaScript через C++
linktitle: Вставить связанное изображение из веб адреса
type: docs
weight: 450
url: /ru/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Узнайте, как вставить привязанное изображение с веб адреса в рабочий лист с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}
Иногда необходимо вставить изображение из интернета (http://) в лист. Для этого укажите URL изображения, и изображение будет загружено каждый раз при открытии файла в Excel. Изображение не встроено физически в документ Excel, а указывает на веб-ресурс.
{{% /alert %}}

## **Использование Microsoft Excel**

В Microsoft Excel (например, 2007 год):

1. Нажмите меню **Вставка** и выберите **Изображение**.  
1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения.

## **Использование Aspose.Cells for JavaScript через C++**

Aspose.Cells for JavaScript через C++ поддерживает добавление привязанного изображения с помощью [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). Метод возвращает объект [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

Следующий пример показывает, как добавить связанное изображение из веб-адреса в лист.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Insert Linked Picture Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length) {
                // If file provided, use it as the base workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Otherwise create a new workbook
                var workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a linked picture (from Web Address) to B2 Cell.
            const pic = worksheet.shapes.addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");

            // Set the height and width of the inserted image.
            pic.heightInch = 1.04;
            pic.widthInch = 2.6;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outLinkedPicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Linked picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
