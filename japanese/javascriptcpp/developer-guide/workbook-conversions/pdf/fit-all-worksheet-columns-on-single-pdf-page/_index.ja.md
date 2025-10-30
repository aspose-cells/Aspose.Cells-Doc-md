---
title: JavaScriptを使ってC++経由で単一のPDFページにすべてのワークシートの列をフィットさせる
linktitle: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 160
url: /ja/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

時々、ワークシートの全列を1ページに収めたPDFファイルを生成したいことがあります。[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--)プロパティはその機能を非常に簡単に使用できます。ワークシートのデータに基づいて、出力PDFの高さや幅などの複雑な計算は内部で処理されます。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--)は、ワークシート内のすべての列を単一のPDFページにレンダリングし、行はワークシート内のデータに応じて複数ページに拡張されることを保証します。

以下のサンプルコードは、100列の大きなワークシートをレンダリングするために[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--)プロパティを使用する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Create and initialize an instance of Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and initialize an instance of PdfSaveOptions
            const saveOptions = new PdfSaveOptions();
            // Set AllColumnsInOnePagePerSheet to true (converted from setter to property)
            saveOptions.allColumnsInOnePagePerSheet = true;

            // Save Workbook to PDF format by passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされたPDFファイルでは内容が非常に小さくなる場合があります。Acrobat Readerなどの閲覧アプリケーションで拡大するとまだ読める場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
