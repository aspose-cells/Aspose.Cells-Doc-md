---
title: セルをロックして保護する方法
type: docs
weight: 130
url: /ja/javascript-cpp/how-to-lock-cells-to-protect-them/
description: この記事では、C++を通じてAspose.Cells for JavaScriptを使ったセルのロックと保護方法についてのコードを紹介します。
keywords: JavaScriptを使ったセルのロックと保護方法、JavaScriptを使用したセルのロックと保護方法、JavaScriptでセルをロックして保護する方法
---

## **可能な使用シナリオ**
セルをロックして保護することは、Microsoft ExcelやGoogle Sheetsなどのスプレッドシートアプリケーションで一般的な慣行であり、重要な理由がいくつかあります：

1. 不慮の変更防止：セルをロックすることで、重要なデータや数式を誤って変更するのを防げます。これは、誤操作による大きなエラーを避けるために複雑なスプレッドシートで特に役立ちます。

1. データの整合性維持：セルをロックすることで、重要なデータが一貫して正確であることを確保できます。これは、財務書類、レポート、その他データの整合性が重要な文書に不可欠です。

1. 制御されたアクセス: コラボレーション環境では、セルをロックすることで、誰がスプレッドシートの特定の部分を編集できるかを制御できます。例えば、特定のチームメンバーだけに特定のセルの編集を許可し、残りのワークシートは保護されたままにしておくことができます。

1. 数式の保護: 数式は計算やデータ分析において重要です。数式を含むセルをロックすると、これらの数式が誤って変更または削除されるのを防ぎ、ワークシート全体の機能を維持します。

1. ビジネスルールの強制: 一部のケースでは、特定のデータの修正を防ぐ必要があるビジネスルールや規制があります。セルをロックすることで、これらの要件を満たすことができます。

1. ユーザーの案内: セルをロックし、編集可能なセルについて明確な指示を提供することで、ユーザーの操作を導き、混乱やエラーを減らすことができます。

## **Excelでセルをロックして保護する方法**
Microsoft Excelでセルをロックする方法は次のとおりです：

1. ロックするセルを選択：ロックしたいセルを選択します。シート全体をロックしたい場合は、このステップをスキップできます。
1. セルの書式設定ダイアログを開く：選択したセルを右クリックし、「セルの書式設定」を選択するか、Ctrl+1を押します。
<br>
<img src="1.png" width=60% />
1. セルをロック：セルの書式設定ダイアログの「保護」タブに移動します。「ロック済み」のチェックボックスをオンにし、「OK」をクリックします。
1. シートを保護：リボンの「校閲」タブに移動し、「シートの保護」をクリックします。パスワード（任意）を設定し、許可したい操作（ロックされたセルの選択、セルの書式設定など）を選び、「OK」をクリックします。
<br>
<img src="2.png" width=60% />

## **JavaScriptを使ってセルをロックして保護する方法**

Aspose.CellsはExcelファイルをプログラムで操作するための強力なライブラリです。Aspose.Cells for JavaScriptを使ってC++でセルをロックするには、次の手順を踏みます：サンプルファイル([sample.xlsx])を読み込み、最初にすべてのセルのロックを解除します（デフォルトではすべてのセルがロックされているが、ワークシートが保護されるまで有効にならないため）、その後、保護したいセルをロックし、最後にワークシートを保護してロックを施行します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **結果出力**
このコードは、指定されたセル（この例ではA1とB2）のみをロックし、シートが保護されていることでこれらの設定を強制します。シートの他のセルはロック解除され、編集可能のままです。

<br>
<img src="3.png" width=60% />
