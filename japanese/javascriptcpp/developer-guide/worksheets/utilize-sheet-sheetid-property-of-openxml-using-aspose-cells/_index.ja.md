---
title: OpenXmlのSheet.SheetIdプロパティをAspose.Cells for JavaScriptとC++を用いて利用
linktitle: Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する
type: docs
weight: 200
url: /ja/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: この記事は、C++を使用してAspose.Cells for JavaScript経由でOpenXmlのSheet.SheetIdプロパティをExcel操作で活用する方法を示しています。
keywords: SheetのIDプロパティをOpenXml JavaScript経由でC++を使用して操作し、ExcelのシートIDをJavaScriptで制御します。
---

## **可能な使用シナリオ**

*Sheet.SheetId*プロパティは*DocumentFormat.OpenXml.Spreadsheet*モジュール内で利用可能で、OpenXmlの一部です。このプロパティとその値は、以下のスクリーンショットのように*workbook.xml*内で確認できます。Aspose.Cellsは、これと同等のプロパティを[**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--)として提供します。

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **C++を使用してAspose.Cells for JavaScript経由でOpenXmlのSheet.SheetIdプロパティを活用します。**

次のサンプルコードは、[サンプルExcelファイル](51740716.xlsx)をロードし、そのシートまたはタブIDを読み取り、それに新しいタブIDを割り当てて[出力Excelファイル](51740717.xlsx)として保存します。以下に示すコードのコンソール出力も参照してください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
