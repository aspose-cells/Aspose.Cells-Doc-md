---
title: Получить предупреждения при загрузке файла Excel с помощью JavaScript через C++
linktitle: Получать предупреждения при загрузке файла Excel
type: docs
weight: 110
url: /ru/javascript-cpp/get-warnings-while-loading-excel-file/
description: Узнайте, как улавливать предупреждения при загрузке файла Excel с помощью Script Aspose.Cells for Java через C++. Эффективно обрабатывайте поврежденные, но загружаемые рабочие книги.
---

## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая несколько повреждена, но все же загружается. В таких случаях Aspose.Cells выбрасывает предупреждения при загрузке. Вы можете ловить эти предупреждения, реализовав интерфейс [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) и установив свойство [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--).

## **Получение предупреждений при загрузке файла Excel**

Следующий пример кода показывает, как получать предупреждения при загрузке файла Excel. Код загружает [пример файла excel](sampleDuplicateDefinedName.xlsx), который вызывает предупреждение [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) при загрузке. Это предупреждение перехватывается методом [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-), который выводит сообщения предупреждений в консоль. Затем рабочая книга сохраняется как [выходной файл excel](outputDuplicateDefinedName.xlsx). Если открыть исходный файл в Microsoft Excel, он также отобразит это предупреждение, как показано на скриншоте. Также рекомендуем проверить вывод в консоль для лучшего понимания.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **Вывод в консоль**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
