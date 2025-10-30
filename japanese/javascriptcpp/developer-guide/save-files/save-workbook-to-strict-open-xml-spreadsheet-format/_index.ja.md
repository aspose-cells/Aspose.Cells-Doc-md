---
title: JavaScript経由でC++を使用してワークブックをStrict Open XMLスプレッドシート形式で保存
linktitle: 厳密なOpen XMLスプレッドシート形式へのブックの保存
type: docs
weight: 150
url: /ja/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Aspose.Cells for JavaScriptを使用してワークブックをStrict Open XMLスプレッドシート形式で保存する方法を学びます。
---

## **可能な使用シナリオ**

C++を使用してAspose.Cells for JavaScriptはワークブックを*Strict Open XMLスプレッドシート*形式で保存できます。そのために、[**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--)プロパティを提供します。その値を[**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance)に設定すると、出力されたExcelファイルはStrict Open XMLスプレッドシート形式で保存されます。

## **ストリクトなOpen XMLスプレッドシート形式でワークブックを保存**

次のサンプルコードは、Workbookを作成し、[**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--)プロパティの値を[**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance)に設定して、[出力Excelファイル](67338272.xlsx)として保存します。Microsoft Excelで出力されたExcelファイルを開き、「名前を付けて保存...」ダイアログを開くと、その形式が*Strict Open XML Spreadsheet*として表示されることがこのスクリーンショットに示されています。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to Strict Open XML Spreadsheet Format</title>
    </head>
    <body>
        <h1>Save Workbook to Strict Open XML Spreadsheet Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlCompliance, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Specify - Strict Open XML Spreadsheet - Format.
            workbook.settings.compliance = OoxmlCompliance.Iso29500_2008_Strict;

            // Access first worksheet and set value in B4
            const worksheet = workbook.worksheets.get(0);
            const b4 = worksheet.cells.get("B4");
            b4.value = "This Excel file has Strict Open XML Spreadsheet format.";

            // Save to output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved to Strict Open XML Spreadsheet format. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
