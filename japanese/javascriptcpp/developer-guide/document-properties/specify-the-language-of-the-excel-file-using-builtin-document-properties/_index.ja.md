---
title: JavaScript を C++ 経由で使用して、BuiltIn Document Properties を用いてExcelファイルの言語を指定する
linktitle: ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する
type: docs
weight: 30
url: /ja/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **可能な使用シナリオ**

 Excelファイルの言語を右クリックして「プロパティ」>「詳細」を選択し、「言語」フィールドを編集して変更できます。プログラム的に変更するには [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) プロパティを使用し、Aspose.Cells for JavaScript 経由の C++ API を利用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する**

このコードは、ワークブックを作成し、その組み込みドキュメントプロパティである言語を変更します。コードで生成されたExcelファイルと修正された言語フィールドのスクリーンショットは[**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--)プロパティによります。

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
