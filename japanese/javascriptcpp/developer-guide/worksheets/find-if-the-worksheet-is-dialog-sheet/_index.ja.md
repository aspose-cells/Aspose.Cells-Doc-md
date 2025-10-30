---
title: JavaScriptを使用してワークシートがダイアログシートかどうかを検出する方法
linktitle: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 90
url: /ja/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: この資料では、C++経由のAspose.Cells for JavaScriptを使用してExcelワークシートがダイアログシートかどうかをプログラムで判断するための手順とサンプルコードを提供します。
keywords: C++経由のAspose.Cells for JavaScriptを使用してExcelワークシートのダイアログタイプを見つける方法
---

## **可能な使用シナリオ**

ダイアログシートは古い形式のシートで、ダイアログボックスを含みます。例えば、Microsoft Excelの古いバージョン（例：2003）で挿入されたものです。新しいバージョン（例：Microsoft Excel 2016）でもVBAを使って挿入可能です。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

シートがダイアログシートか他のタイプのシートかを確認するには、Aspose.Cells for JavaScriptによって提供される[**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--)プロパティを使用します。もし列挙値[**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype)を返した場合、それはダイアログシートであることを意味します。

## **ワークシートがダイアログシートであるかを検索する**

次のサンプルコードは、ダイアログシートを含むサンプルExcelファイル（64716820.xlsx）を読み込み、[**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--)プロパティを確認し、それを[**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype)と比較してメッセージを出力します。詳細は以下のコンソール出力を参照してください。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
