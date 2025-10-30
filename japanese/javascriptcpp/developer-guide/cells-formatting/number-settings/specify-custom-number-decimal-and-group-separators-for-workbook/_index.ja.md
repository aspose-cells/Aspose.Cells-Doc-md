---
title: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
linktitle: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
type: docs
weight: 110
url: /ja/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: C++を使用したAspose.Cells for JavaScriptでExcelの数字の小数点と桁区切り記号を変更する。
keywords: C++を使用したExcel JavaScriptでカスタム小数点区切り記号、カスタム桁区切り記号を指定し、小数点と桁区切り記号を変更する
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cellsは、[**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-)と[**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-)メソッドを提供し、数値のフォーマッティングやパースのためにカスタムセパレータを設定します。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **C++を使用したAspose.Cells for JavaScriptでカスタム区切り記号の指定**

次のサンプルコードは、Aspose.Cells APIを使用してカスタムセパレータを指定する方法を示しています。これにより、カスタム数値の10進セパレータとグループセパレータを、それぞれドットとスペースに設定します。

### カスタムの数字小数点及び桁区切り記号を指定するJavaScriptコード

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
