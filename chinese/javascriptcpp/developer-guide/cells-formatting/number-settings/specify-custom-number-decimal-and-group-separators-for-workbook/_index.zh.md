---
title: 为工作簿指定自定义数字小数点和分组分隔符
linktitle: 为工作簿指定自定义数字小数点和分组分隔符
type: docs
weight: 110
url: /zh/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: 使用C++通过Aspose.Cells for JavaScript更改Excel中的数字十进制和分组分隔符。
keywords: 用C++指定自定义小数点分隔符和自定义分组分隔符，支持Excel JavaScript，修改十进制和分组分隔符
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以在“高级Excel选项”中指定自定义十进制和千位分隔符，而不是使用系统分隔符，如下面的屏幕截图所示。

Aspose.Cells 提供 [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) 和 [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) 方法，用于设置数字格式化/解析的自定义分隔符。

{{% /alert %}}

## **使用Microsoft Excel指定自定义分隔符**

下面的屏幕截图显示了“高级Excel选项”，并突出显示了指定“自定义分隔符”的部分。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **使用C++通过Aspose.Cells for JavaScript指定自定义分隔符**

下面的示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。它将十进制和组分隔符分别指定为点和空格。

### JavaScript代码示例：指定自定义数字十进制和分组分隔符

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
