---
title: JavaScriptを使用して図形をロックまたはロック解除（C++経由）
linktitle: 形状のロックまたはロック解除
type: docs
weight: 200
url: /ja/javascript-cpp/lock-or-unlock-shapes/
description: この記事は、C++経由のAspose.Cellsライブラリを使用して図形をロックまたはロック解除し、保護する方法を説明したコード例を示しています。
keywords: JavaScriptからC++経由で図形をロックし保護します。図形のロック・ロック解除方法について説明します。
---

## **可能な使用シナリオ**

場合によっては、特定のワークシート内のすべての形状を保護して、望ましくない状況によって破壊されるのを防ぐ必要があります。その場合は、指定されたワークシート内のすべての形状をロックする必要があります。 

スプレッドシートやドキュメント内の図形をロックすることは、いくつかの理由で有益です：
1. 偶発的な変更を防ぐ：図形をロックすることで、ユーザーによる誤った移動やサイズ変更、削除を防ぎます。特に複雑なドキュメントでは、図形が注釈やイラスト、またはドキュメントのデザインの一部として使われる場合に重要です。
1. レイアウトとデザインの維持：図形はドキュメントのレイアウトやビジュアルデザインにおいて重要な役割を果たします。それらをロックすることで、意図した外観を維持し、ドキュメントの専門性と視覚的魅力を保ちます。
1. データの整合性：スプレッドシートでは、図形を使って重要なデータポイントを強調したり、コメントを追加したり、ビジュアルな説明を提供したりします。これらの図形をロックすることで、提供される文脈情報の正確性と完全性を確保します。
1. 共有ドキュメントの一貫性：複数のユーザーがドキュメントで共同作業する際、それぞれの技術レベルは異なる場合があります。図形をロックすることで、予期しない変更を防ぎ、ドキュメントの一貫性を維持します。
1. セキュリティ：敏感なドキュメントでは、図形をロックすることは情報保護の一環となります。例えば、財務報告書や法的文書において、ロックされた図形は重要な注釈やハイライトを安全に保護するために使われます。

時には、特定の保護されたワークシートで特定の図形を変更できる必要があり、その場合これらの図形のロック解除が必要です。この記事では、指定した図形のロックとロック解除の方法を詳しく紹介します。

## **Excelで図形をロックする方法**

Microsoft Excelでセルをロックする方法は次のとおりです：

1. Excelファイルを開く：ロックしたい図形を含むExcelファイルを開きます。

1. 図形を選択：ロックしたい図形をクリックします。複数の図形を選択するには、Ctrlキーを押しながら各図形をクリックします。

1. 図形の書式設定パネルを開く：選択した図形上で右クリックし、「サイズとプロパティ」を選択します。あるいは、リボンの「書式」タブに移動し、「サイズ」グループのダイアログランチャー（小さな矢印）をクリックして「図形の書式設定」パネルを開きます。
1. 図形をロック： 「図形の書式設定」パネルの「サイズとプロパティ」タブ（四角形と矢印のアイコン）に移動します。「プロパティ」セクションで、「ロック」のチェックボックスをオンにします。
<br>
<img src="1.png" width=60% />
1. シートを保護：リボンの「校閲」タブに移動し、「シートの保護」をクリックします。パスワード（任意）を設定し、許可したい操作（ロックされたセルの選択、セルの書式設定など）を選び、「OK」をクリックします。
<br>
<img src="2.png" width=60% />

## **指定したワークシート内の全ての図形をロックする方法**

指定したワークシートのすべての図形を保護するには、`worksheet.protect(ProtectionType.Objects)`メソッドを使用します。以下のサンプルコードを参照してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **保護されたワークシート内の指定した図形のアンロック方法**

保護されたワークシート内の特定の図形のロック解除には、`shape.isLocked`を使用します。以下のサンプルコードをご覧ください。

注意：`shape.isLocked`は、ワークシートが保護されている場合のみ有効です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
