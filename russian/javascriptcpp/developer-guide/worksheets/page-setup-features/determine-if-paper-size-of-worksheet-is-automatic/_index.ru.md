---
title: Определить автоматически ли выбран размер бумаги листа с помощью JavaScript через C++
linktitle: Определение автоматического размера бумаги листа
type: docs
weight: 90
url: /ru/javascript-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: В этой статье объясняется, как использовать JavaScript API с дополнениями C++ для определения автоматического ли размера бумаги в листе программным путем.
keywords: определить автоматически ли размер бумаги листа JavaScript через C++
---

## **Возможные сценарии использования**

Часто размер бумаги листа устанавливается автоматически. Когда он автоматический, он обычно задан как *Letter*. Иногда пользователь устанавливает размер бумаги по своим требованиям. В этом случае размер бумаги не является автоматическим. Вы можете определить, автоматический ли размер бумаги листа, используя свойство [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isAutomaticPaperSize--).

## **Определение автоматического размера бумаги листа**

В приведенном ниже образце кода загружаются следующие два файлы Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

и определяется, является ли размер бумаги их первого листа автоматическим или нет. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим или нет, через окно настройки страницы, как показано на этом скриншоте.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup IsAutomaticPaperSize</title>
    </head>
    <body>
        <h1>PageSetup IsAutomaticPaperSize Example</h1>
        <p>Select two Excel files to compare the PageSetup.isAutomaticPaperSize property:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx,.csv" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');
            const resultDiv = document.getElementById('result');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Instantiating Workbook objects from uploaded files
            const wb1 = new Workbook(new Uint8Array(arrayBuffer1));
            const wb2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Access first worksheet of both workbooks
            const ws11 = wb1.worksheets.get(0);
            const ws12 = wb2.worksheets.get(0);

            // Read the PageSetup.isAutomaticPaperSize property of both worksheets
            const isAuto1 = ws11.pageSetup.isAutomaticPaperSize;
            const isAuto2 = ws12.pageSetup.isAutomaticPaperSize;

            // Display results
            resultDiv.innerHTML = `
                <p>First Worksheet of First Workbook - IsAutomaticPaperSize: ${isAuto1}</p>
                <p>First Worksheet of Second Workbook - IsAutomaticPaperSize: ${isAuto2}</p>
            `;
        });
    </script>
</html>
```

## **Вывод в консоль**



{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
