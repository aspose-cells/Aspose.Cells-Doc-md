---
title: 既存のスタイルを修正する
linktitle: 既存のスタイルを修正する
description: Aspose.Cellsは、既存のセルスタイルを変更できるスプレッドシートファイル操作用のC++を使用したJavaScriptライブラリです。この記事では、Aspose.Cellsライブラリを用いて既存のセルスタイルを変更し、セルの外観を必要に応じてカスタマイズする方法を紹介します。
keywords: 既存のスタイルを変更し、アプリケーションの外観と使いやすさをカスタマイズする、ガイド、チュートリアル、ヘルプドキュメント、開発ドキュメント、APIリファレンス、サンプルコード、ダウンロード、サポート。
type: docs
weight: 90
url: /ja/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

セルに同じフォーマットオプションを適用するには、新しいフォーマットスタイルオブジェクトを作成します。フォーマットスタイルオブジェクトは、フォント、フォントサイズ、インデント、数値、罫線、パターンなどのフォーマット特性を組み合わせたものであり、名前が付けられ、セットとして保存されます。適用されると、そのスタイルのすべてのフォーマットが適用されます。

既存のスタイルを使用して、同じ属性で情報にフォーマットを適用することもできます。

セルが明示的にフォーマットされていない場合、**通常**スタイル(ワークブックのデフォルトスタイル)が適用されます。Microsoft Excelでは、通常スタイルに加えてComma、Currency、Percentなどのスタイルがいくつか事前に定義されています。

Aspose.Cellsを使用すると、これらのスタイルのいずれか、または独自の属性で定義したスタイルを修正することができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel 97-2003でスタイルを更新するには:

1. **書式**メニューで **スタイル** をクリックします。
1. **スタイル名** リストから変更したいスタイルを選択します。
1. **変更** をクリックします。
1. 「セルの書式設定」ダイアログのタブを使用して、望むスタイルオプションを選択します。
1. **OK** をクリックします。
1. **スタイルに含まれるもの** で、希望するスタイルの機能を指定します。
1. **OK** をクリックしてスタイルを保存し、選択した範囲に適用します。

## **C++を使用したAspose.Cells for JavaScriptの利用方法**

次の例は[**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--)メソッドの使用方法を示しています。

### **スタイルの作成と変更**

この例では、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを作成し、それをセル範囲に適用し、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを変更します。変更は自動的にセルとスタイルが適用された範囲に反映されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **既存のスタイルの変更**

この例では、範囲にすでに適用されているPercentという名前のスタイルが含まれる単純なテンプレートExcelファイルを使用します。具体的な手順は以下の通りです:

1. スタイルを取得します。
1. スタイルオブジェクトを作成します。
1. スタイルフォーマットを変更します。

変更は自動的に適用された範囲に適用されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
