---
title: Как добавить/вставить TextBox в лист с помощью JavaScript через C++
linktitle: Добавить текстовое поле на лист
type: docs
weight: 10
url: /ru/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Как добавить/вставить TextBox в лист в Aspose.Cells for JavaScript через C++.
keywords: добавление/вставка текста в TextBox на листе Excel с помощью Aspose JavaScript через C++
---

## Добавление текстового поля в лист Excel

В программе Excel (версия 07 и выше) есть два места, куда можно вставлять текстовые поля. Одно в "insert-shapes", другое — справа от верхнего меню опции "Insert".

### метод первый:

![1](1.png)

### метод второй:

![2](2.png)

## Как создать

Вы можете создавать текстовые поля с горизонтальным или вертикальным текстом.

- Выберите соответствующую опцию (горизонтальную или вертикальную)
- Щелкните левой кнопкой мыши на странице
- Удерживайте левую кнопку и перетаскивайте на странице
- Отпустите левую кнопку

Теперь у вас есть текстовое поле.

## Добавить TextBox на лист в Aspose.Cells for JavaScript через C++

Когда необходимо массово вставлять TextBox в лист, ручной метод вставки очевидно неудобен. Если это вас беспокоит, данный документ вам поможет. [Aspose.Cells](https://products.aspose.com/cells/) предоставляет API для быстрой массовой вставки в вашем коде.

В следующем примере кода создается текстовое поле.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Вы получите файл, похожий на [итоговый файл](result.xlsx). В файле вы увидите следующее:

![](52449.png)
