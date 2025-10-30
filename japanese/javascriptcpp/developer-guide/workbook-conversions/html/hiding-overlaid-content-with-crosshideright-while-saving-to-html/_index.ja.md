---
title: HTML保存時にOverlaid ContentをCrossHideRightで非表示にします JavaScript via C++
linktitle: HTMLで保存する際のCrossHideRightでオーバーレイされたコンテンツを非表示にする
type: docs
weight: 100
url: /ja/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際、セル文字列に対して異なるクロスタイプを指定できます。デフォルトでは、Aspose.CellsはMicrosoft Excelに従ってHTMLを生成しますが、[**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)にクロスタイプを設定すると、セルの右側に重ね合わされたり重複したセル文字列がある場合、その文字列を非表示にします。

## **CrossHideRightを使用してオーバーレイコンテンツを非表示にする**

次のサンプルコードは、[サンプルExcelファイル](64716894.xlsx)を読み込み、[**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--)を[**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)に設定した後、[出力HTML](64716893.zip)に保存します。スクリーンショットは、[**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)がどのように出力に影響するかを示しています。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To Html</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To Html</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;

            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
