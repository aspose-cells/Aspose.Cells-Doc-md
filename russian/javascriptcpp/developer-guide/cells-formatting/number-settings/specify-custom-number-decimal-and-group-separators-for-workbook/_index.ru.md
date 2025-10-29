---
title: Укажите пользовательский разделитель десятичной и разрядной группы для книги
linktitle: Укажите пользовательский разделитель десятичной и разрядной группы для книги
type: docs
weight: 110
url: /ru/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Изменение разделителей десятичных и групповых чисел в Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: укажите пользовательский десятичный разделитель excel JavaScript через C++, укажите пользовательский групповой разделитель excel JavaScript через C++, изменение разделителя десятичных и групповых чисел excel JavaScript через C++
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете указать пользовательские разделители десятичной точки и тысячи вместо использования системных разделителей из **Расширенных опций Excel**, как показано на скриншоте ниже.

Aspose.Cells предоставляет методы [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) и [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) для установки пользовательских разделителей для форматирования/парсинга чисел.

{{% /alert %}}

## **Указание пользовательских разделителей, используя Microsoft Excel**

На следующем скриншоте показаны **Расширенные параметры Excel** и выделена секция для указания **Пользовательских разделителей**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Указание пользовательских разделителей с помощью Aspose.Cells for JavaScript через C++**

Приведенный ниже образец кода иллюстрирует, как указать пользовательские разделители с помощью API Aspose.Cells. Он указывает пользовательские разделители для десятичных и групповых чисел как точку и пробел соответственно.

### JavaScript код для указания пользовательских разделителей чисел и групп

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
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

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as pdf
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
