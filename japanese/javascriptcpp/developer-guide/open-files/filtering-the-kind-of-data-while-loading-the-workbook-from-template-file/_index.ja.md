---
title: JavaScriptとC++を使用してテンプレートファイルからワークブックを読み込む際にデータの種類をフィルタリングする
linktitle: テンプレートファイルからワークブックをロードする際にデータの種類をフィルタリングする
type: docs
weight: 400
url: /ja/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
時には、テンプレートファイルからワークブックを作成する際に読み込むデータの種類を指定したい場合があります。読み込むデータをフィルターすることで、特定の用途でのパフォーマンスを向上させることができます。特に [LightCells API](/cells/ja/javascript-cpp/using-lightcells-api/) を使用する場合に有効です。この目的のために [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) プロパティを使用してください。
{{% /alert %}}

以下のサンプルコードは、ダウンロードリンクから取得したテンプレートファイル（5115552.xlsx）を読み込む際に、シェイプオブジェクトのみをロードします。スクリーンショットは、テンプレートファイルの内容と、赤色と黄色の背景のデータが[**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--)プロパティを[**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/)に設定しているために読み込まれないことを示しています。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

[指定されたリンク](5115555.pdf)からダウンロードできる出力PDFです。ここでは、赤色および黄色の背景のデータが存在しない一方、すべての形状が存在することが分かります。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Set the load options, we only want to load shapes and do not want to load data
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Create workbook object from uploaded excel file using load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterChars_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
