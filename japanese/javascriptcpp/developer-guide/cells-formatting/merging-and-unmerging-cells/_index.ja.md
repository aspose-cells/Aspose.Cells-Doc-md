---
title: JavaScript経由のC++でセルの結合と解除
linktitle: セルの結合と解除
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのJavaScriptライブラリで、セルの結合と解除をサポートしています。この記事では、Aspose.Cellsライブラリを使用したセルの結合と解除の方法と、結合セルのスタイルのカスタマイズオプションについて紹介します。
keywords: Aspose.Cells、JavaScriptライブラリ、スプレッドシート、セルの結合、解除、スタイル設定、カスタムスタイル
type: docs
weight: 190
url: /ja/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cellsはこの機能をサポートし、ワークシート内でセルを結合することもできます。 結合されたセルは解除することもできます。 結合されたセルのセル参照は、元の選択範囲の左上のセルの参照です。

{{% /alert %}} 
## **紹介**
すべての行や列に常に同じ数のセルを必ずしも欲しいわけではありません。 たとえば、複数の列にまたがるタイトルを置きたい場合があります。 または、請求書を作成する場合、合計に対して少ない列を望むことがあります。 セルを1つに結合してみてください。 Microsoft Excelは、ユーザーがファイルを選択して自分の望むようにスプレッドシートの構造を結合できます。

{{% alert color="primary" %}} 

セルをマージすると、左上のセルのデータだけが保持されます。範囲内の他のセルにデータがある場合は、そのデータは削除されます。書式設定も参照セルの基準に基づいて行われ、セルのマージ時には範囲内の左上セルの書式設定が適用されます。セルの分割時には、新しいセルは元の書式設定を保持します。

{{% /alert %}} 
## **ワークシート内でセルを結合する**
### **Microsoft Excelでセルを結合する**
以下の手順では、MS Excelを使用してワークシート内のセルを結合する方法について説明します。

1. 範囲内で左上のセルにデータをコピーします。
1. 結合したいセルを選択します。
1. 行または列内のセルを結合してセルの内容を中央に配置するには、**書式設定**ツールバーの**結合して中央配置**アイコンをクリックします。

### **Aspose.Cellsでセルの結合**
Aspose.Cells.Cellsクラスにはこの作業に役立つ便利なメソッドがあります。例えば、merge()メソッドは特定の範囲内のセルを1つのセルに結合します。

以下の例は、ワークシート内のセル(C6:E7)を結合する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **結合されたセルの結合解除（分割）**
### **Microsoft Excel の使用**
以下の手順では、Microsoft Excelを使用して結合されたセルを分割する方法について説明します。

1. 結合されたセルを選択します。
   セルが結合されている場合、**結合して中央配置**が**書式設定**ツールバーで選択されます。
1. **書式設定**ツールバーで**結合して中央配置**をクリックします。

### **Aspose.Cellsの使用**
Aspose.Cells.Cellsクラスには、セルを元の状態に分割する`unmerge()`メソッドもあります。これはセルの参照を使用してセルを分割します。

以下の例は、結合されたセル(C6)を分割する方法を示しています。 この例では、前の例で作成されたファイルを使用し、結合されたセルを分割しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [ワークシート内の結合セルを検出する](/cells/ja/javascript-cpp/detect-merged-cells-in-a-worksheet/)
