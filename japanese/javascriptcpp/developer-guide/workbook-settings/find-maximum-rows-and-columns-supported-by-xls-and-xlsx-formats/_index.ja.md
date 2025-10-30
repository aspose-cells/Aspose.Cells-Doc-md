---
title: JavaScriptでXLSおよびXLSXフォーマットがサポートする最大行数と列数を見つける（C++経由）
linktitle: XLSおよびXLSX形式がサポートする最大行数および列数を検索する
type: docs
weight: 20
url: /ja/javascript-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **可能な使用シナリオ**  

Excelフォーマットでは、サポートされる行数と列数が異なります。例えば、XLSは65536行と256列をサポートし、XLSXは1048576行と16384列をサポートします。特定のフォーマットでサポートされる行数と列数を知りたい場合は、[**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--)と[**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--)プロパティを使用します。  

## **XLSおよびXLSX形式がサポートする最大行数および列数を検索する**  

次のサンプルコードは、最初にXLS形式でワークブックを作成し、その後XLSX形式で作成します。作成後、[**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--)と[**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--)の値を出力します。以下のコードのコンソール出力をご参照ください。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Maximum Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, Utils } = AsposeCells;

        const runBtn = document.getElementById('runExample');
        const resultDiv = document.getElementById('result');

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runBtn.disabled = false;
        });

        runBtn.addEventListener('click', async () => {
            // Print message about XLS format.
            resultDiv.innerHTML = '<p>Maximum Rows and Columns supported by XLS format.</p>';

            // Create workbook in XLS format.
            let wb = new Workbook(AsposeCells.FileFormatType.Excel97To2003);

            // Print the maximum rows and columns supported by XLS format.
            let maxRows = wb.settings.maxRow + 1;
            let maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
            resultDiv.innerHTML += '<hr/>';

            // Print message about XLSX format.
            resultDiv.innerHTML += '<p>Maximum Rows and Columns supported by XLSX format.</p>';

            // Create workbook in XLSX format.
            wb = new Workbook(AsposeCells.FileFormatType.Xlsx);

            // Print the maximum rows and columns supported by XLSX format.
            maxRows = wb.settings.maxRow + 1;
            maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
        });
    </script>
</html>
```  

## **コンソール出力**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}
