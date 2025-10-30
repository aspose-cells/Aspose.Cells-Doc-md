---
title: ワークシートに条件付き書式設定を適用する
linktitle: ワークシートに条件付き書式設定を適用する
description: Aspose.Cellsライブラリを使ってJavaScript経由C++でワークシートに条件付き書式を適用し、セルの見た目をよりコントロールできる方法。
keywords: Aspose.Cells、条件付き書式、JavaScript経由C++、ワークシート、書式設定
type: docs
weight: 130
url: /ja/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

この記事では、ワークシートのセル範囲に条件付き書式設定を追加する方法について詳しく説明しています。

条件付き書式設定は、Microsoft Excelの高度な機能であり、セルの値や数式の値に応じて書式を適用し、その書式を変更することを可能にします。たとえば、セルの背景が赤くなるとマイナスの値が強調表示されたり、テキストの色が緑色になるとプラスの値が強調表示されます。セルの値が条件を満たしている場合、書式が適用されます。セルの値が条件を満たしていない場合、セルのデフォルトの書式が使用されます。

Microsoft Office Automationで条件付き書式設定を適用することは可能ですが、その欠点があります。たとえば、セキュリティ、安定性、拡張性、速度などの理由や問題が存在します。他のソリューションを探す主な理由は、Microsoft自体がソフトウェアソリューション向けにOffice Automationを強く推奨していないことです。

この記事では、Aspose.Cells APIを使って最も簡単なコード行でセルに条件付き書式を追加するウェブアプリケーションの作成方法を紹介します。

{{% /alert %}}

## **セルの値に基づいた条件付き書式を適用するためのAspose.Cellsの使用**

1. **Aspose.Cellsをダウンロードしてインストールします。**
   1. Aspose.Cells for JavaScriptをC++でダウンロードします。
1. 開発コンピュータにインストールします。
   すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。
1. **プロジェクトを作成します**。
   この例では、ブラウザベースのウェブアプリケーションでの使用方法を示し、JavaScriptプロジェクトを開始します。
1. **参照を追加します。**
   プロジェクトにAspose.Cellsを参照として追加します。例えば、次のようにライブラリを含めることができます：
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

上記のコードを実行すると、最初のワークシートのセル「A1」に条件付き書式が適用されます。A1に適用される条件付き書式はセルの値に依存します。A1の値が50から100の範囲内なら、条件付き書式により背景色が赤になります。

## **Aspose.Cellsを使用してセルの値に基づいた条件付き書式を適用する**

1. 数式に応じて条件付き書式を適用する（コードスニペット）
   以下はそのタスクを達成するためのコードです。B3に条件付き書式を適用します。
