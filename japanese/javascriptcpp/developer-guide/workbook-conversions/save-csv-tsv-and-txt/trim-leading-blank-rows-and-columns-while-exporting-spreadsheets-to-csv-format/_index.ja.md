---
title: スプレッドシートをCSV形式にエクスポートする際、先頭の空白行と列をトリムする
linktitle: スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします
type: docs
weight: 100
url: /ja/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for JavaScriptを使用して、スプレッドシートをCSVフォーマットにエクスポートする際に先頭の空白行と列をトリムする方法を学びます。
---

## **可能な使用シナリオ**

ExcelまたはCSVファイルには先行する空白の列または行が含まれている場合があります。 たとえば、この行を考えてみてください

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の3つのセルまたは列が空白です。 このようなCSVファイルをMicrosoft Excelで開くと、Microsoft Excelはこれらの先行する空白行と列を破棄します。

デフォルトでは、C++を使用したAspose.Cells for JavaScriptは保存時に先頭の空白列と行を削除しませんが、Microsoft Excelと同じように削除したい場合は、Aspose.Cellsは[**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--)プロパティを提供します。これを**true**に設定すると、保存時にすべての先頭の空白列と行が削除されます。

{{% alert color="primary" %}}

C++を使用したAspose.Cells for JavaScript 20.4リリース以前のデフォルト値は**false**でした。20.4リリース以降、[**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--)のデフォルト値は**true**です。

{{% /alert %}}

## **スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。**

以下のサンプルコードは、先頭に空白列が二つある [ソース excel ファイル](sampleTrimBlankColumns.xlsx) を読み込みます。最初は変更なしで CSV 形式で保存し、その後 [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) プロパティを **true** に設定して再保存します。スクリーンショットは、[ソース excel ファイル](sampleTrimBlankColumns.xlsx)、トリミングなしの [出力 CSV ファイル](outputWithoutTrimBlankColumns.csv)、およびトリミング後の [出力 CSV ファイル](outputTrimBlankColumns.csv) を示しています。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **サンプルコード**

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
