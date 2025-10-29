---
title: Обрезайте ведущие пустые строки и столбцы при экспорте таблиц в формат CSV с помощью JavaScript на C++
linktitle: Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV
type: docs
weight: 100
url: /ru/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Узнайте, как обрезать ведущие пустые строки и столбцы при экспорте таблиц в формат CSV с помощью Script Aspose.Cells for Java на C++.
---

## **Возможные сценарии использования**

Иногда ваш файл Excel или CSV имеет ведущие пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, то Microsoft Excel отбрасывает эти ведущие пустые строки и столбцы.

 По умолчанию Script Aspose.Cells for Java на C++ не удаляет ведущие пустые столбцы и строки при сохранении, но если вы хотите удалить их, как в Microsoft Excel, то Aspose.Cells предоставляет свойство [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--). Установите его в **true**, и все ведущие пустые строки и столбцы будут игнорироваться при сохранении.

{{% alert color="primary" %}}

 Перед выпуском Script Aspose.Cells for Java на C++ 20.4 значение [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) по умолчанию было **false**. Начиная с версии 20.4, значение [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) по умолчанию — **true.**

{{% /alert %}}

## **Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Следующий пример кода загружает [исходный Excel-файл](sampleTrimBlankColumns.xlsx), который содержит два ведущих пустых столбца. Он сначала сохраняет файл в формате CSV без изменений, затем устанавливает свойство [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) в **true** и сохраняет файл снова. Скриншоты показывают [исходный файл Excel](sampleTrimBlankColumns.xlsx), [выходной CSV без обрезки](outputWithoutTrimBlankColumns.csv) и [обрезанный CSV](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
