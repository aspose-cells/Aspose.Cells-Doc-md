---
title: JavaScript を C++ 経由で使用して、Excel ファイルのドキュメントバージョンをBuiltIn Document Properties で指定する
linktitle: ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する
type: docs
weight: 20
url: /ja/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: JavaScript を C++ 経由で使用して、組み込みドキュメントプロパティを用いたExcelファイルのバージョンをプログラム的に指定する方法を学びます。
---

## **可能な使用シナリオ**  

Excelファイルの**バージョン番号**を変更するには、ファイルを右クリックして[プロパティ] > [詳細]を選択し、**バージョン番号**フィールドを編集します。Aspose.Cells APIを使用してプログラム的に変更するには[**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--)プロパティを使用してください。  

## **ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する**  

次のサンプルコードは、ワークブックを作成し、その組み込みドキュメントプロパティ（タイトル、著者、バージョン番号）を変更します。コードで生成された[出力Excelファイル](64716811.xlsx)と、[**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--)プロパティによって修正されたバージョン番号のスクリーンショットを確認してください。  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
