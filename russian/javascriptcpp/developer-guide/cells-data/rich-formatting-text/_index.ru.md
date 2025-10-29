---
title: Доступ и обновление частей форматированного текста ячейки
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 40
url: /ru/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Изучите, как получать доступ и обновлять части формата текста ячейки через API Aspose.Cells for JavaScript с использованием C++.
keywords: Получить доступ и обновить обогащенный текст ячейки, получить обогащенный текст ячейки, отредактировать обогащенный текст ячейки, получить доступ к обогащенному тексту ячейки, обновить обогащенный текст ячейки, изменить обогащенный текст ячейки
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript через C++ позволяет вам получать доступ и обновлять части богатого текста ячейки. Для этой цели вы можете использовать свойства [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) и [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). Эти свойства возвращают и принимают массив объектов [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting), которые можно использовать для доступа и обновления различных свойств шрифта, таких как название шрифта, цвет шрифта, жирность и т.д.

{{% /alert %}}

## **Доступ и обновление частей Rich Text ячейки**

Следующий код демонстрирует использование свойств [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) и [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) с помощью исходного файла Excel ([source excel file](5112369.xlsx), который можно скачать по предоставленной ссылке). Исходный файл содержит богатый текст в ячейке A1. В нем три части, каждая с разным шрифтом. Этот код получает эти части и обновляет первую часть с новым названием шрифта. В итоге он сохраняет книгу как [output excel file](5112366.xlsx). После открытия вы увидите, что шрифт первой части текста изменился на **"Arial"**.

### JavaScript код для доступа и обновления частей богатого текста ячейки

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Вывод консоли, сгенерированный примерным кодом



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
