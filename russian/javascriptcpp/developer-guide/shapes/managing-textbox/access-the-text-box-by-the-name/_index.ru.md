---
title: Доступ к текстовому полю по имени с помощью JavaScript через C++
linktitle: Доступ к текстовому полю по имени
type: docs
weight: 230
url: /ru/javascript-cpp/access-the-text-box-by-the-name/
description: Узнайте, как получить доступ к текстовому полю по имени из коллекции в Aspose.Cells for JavaScript через C++. 
---

## Доступ к текстовому полю по имени

Ранее текстовые поля получали по индексу из коллекции [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--), но теперь их также можно получить по имени из этой коллекции. Это удобный и быстрый способ доступа к вашему текстовому полю, если вы уже знаете его имя.

Приведенный ниже образец кода сначала создает текстовое поле и назначает ему некоторый текст и имя. Затем в следующих строках мы получаем доступ к тому же текстовому полю по его имени и печатаем его текст.

### JavaScript код для доступа к текстовому полю по имени

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### Вывод консоли, сгенерированный примерным кодом



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
