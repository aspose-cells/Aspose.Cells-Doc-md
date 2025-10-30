---
title: Built InドキュメントプロパティのScaleCropとLinksUpToDateのプロパティをJavaScriptをC++経由で設定する方法
linktitle: ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する
type: docs
weight: 320
url: /ja/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for JavaScriptをC++で使用して、ビルトインドキュメントプロパティのScaleCropとLinksUpToDateプロパティを設定する方法を学びます。
---

## **可能な使用シナリオ**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) と [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) は、OpenXml 形式内に定義された2つの拡張された組み込みドキュメントプロパティです。これらのプロパティの目的は次のとおりです。

## **1) ScaleCrop**
この要素は、ドキュメントサムネイルの表示モードを示します。この要素を**TRUE**に設定すると、ドキュメントサムネイルを表示に合わせてスケーリングします。この要素を**FALSE**に設定すると、ドキュメントサムネイルを表示に合わせてクロップします。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新であるかどうかを示します。この要素を**TRUE**に設定すると、ハイパーリンクが更新されていることを示します。この要素を**FALSE**に設定すると、ハイパーリンクが更新されていないことを示します。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **これらのプロパティを示すスクリーンショット**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する**
次のサンプルコードは、ブックの [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) と [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) 拡張組み込みドキュメントプロパティを設定します。このコードで生成された [出力Excelファイル](5115500.xlsx) を確認し、その拡張子を .zip に変更して内容を抽出し、スクリーンショットのように app.xml を表示してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
