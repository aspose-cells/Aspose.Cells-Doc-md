---
title: Чтение подзаголовка диаграммы из ODS файла с помощью JavaScript через C++
linktitle: Чтение подзаголовка диаграммы из файла ODS
description: Узнайте, как использовать Aspose.Cells for JavaScript через C++ для чтения подзаголовка диаграммы из файла OpenDocument Spreadsheet (ODS). Наш гайд покажет, как извлечь и получить доступ к подзаголовку диаграммы для дальнейшего анализа или отображения.
keywords: Aspose.Cells for JavaScript через C++, Чтение подзаголовка диаграммы, OpenDocument Spreadsheet, ODS файл, Выделение диаграммы, Анализ данных.
type: docs
weight: 160
url: /ru/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **Чтение подзаголовка диаграммы из файла ODS**

Aspose.Cells позволяет вам читать подписи диаграмм в файлах ODS с помощью свойства [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--). Следующий пример кода загружает [пример файла ODS](89620481.ods) и читает подпись диаграммы, используя свойство [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--), и выводит ее в Консольное окно. Пожалуйста, смотрите вывод кода ниже для справки.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **Вывод в консоль**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
