---
title: スタイルオブジェクトの再利用
linktitle: スタイルオブジェクトの再利用
description: C++を使用したAspose.Cells for JavaScriptで、再利用可能なスタイルオブジェクトを作成して使用することで、スタイル管理を簡素化し、コード効率を向上させることができます。ガイドでは、再利用可能なスタイルオブジェクトのメリットを活かし、アプリケーションに実装する方法を解説します。
keywords: C++を使用したAspose.Cells for JavaScript、スタイルオブジェクトの再利用、スタイル管理、コード効率化、再利用可能なスタイル、アプリケーション開発、APIリファレンス、サンプルコード、ダウンロード、サポート
type: docs
weight: 3000
url: /ja/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
スタイルオブジェクトを再利用することでメモリを節約し、プログラムを高速化できます。  
{{% /alert %}}  

ワークシート内の大きな範囲のセルにフォーマットを適用するには:

1. スタイルオブジェクトを作成します。
1. 属性を指定します。
1. 範囲のセルにスタイルを適用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
[**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)アプローチはメモリ消費が少なく、効率的であるため、不要なメモリを大量に消費していた古いCell.styleプロパティはAspose.Cells 7.1.0のリリースとともに削除されました。  
{{% /alert %}}
