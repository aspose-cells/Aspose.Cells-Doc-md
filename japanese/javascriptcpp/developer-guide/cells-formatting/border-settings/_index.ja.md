---
title: 罫線設定
linktitle: 罫線設定
description: Aspose.CellsライブラリをJavaScript経由C++で使用して、セルの境界線のスタイルと色を設定する方法。境界線の幅、スタイル、色を調整することで、セルの見た目と外観をよりコントロールできます。
keywords: Aspose.Cells、セルの境界線設定、JavaScriptをC++経由で、境界線の幅、スタイル、色
type: docs
weight: 40
url: /ja/javascript-cpp/cells-border-settings/
---

## **セルにボーダーを追加する**

Microsoft Excelでは、セルに枠線を追加してセルの書式設定を行えます。枠線の種類は追加場所によって異なります。例えば、上枠線はセルのトップ位置に追加されます。ユーザーは線のスタイルや色も変更可能です。

Aspose.Cells for JavaScriptをC++経由で使用することで、開発者はMicrosoft Excelと同じ柔軟な方法で境界線を追加し、その外観をカスタマイズできます。

### **セルにボーダーを追加する**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトです。

Aspose.Cellsは、[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)プロパティを[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスに提供します。[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)はセルのフォーマットスタイルを設定するために使用されます。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)クラスはセルに境界線を追加するためのプロパティを提供します。

#### **セルに罫線を追加**

開発者は、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)コレクションを使ってセルに枠線を追加できます。枠線のタイプはインデックスとして[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)コレクションに渡します。すべての枠線タイプは事前に定義された[**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype)列挙型に含まれています。

**境界の列挙**

|**境界タイプ**|**説明**|
| :- | :- |
|BottomBorder|下部の境界線
|DiagonalDown|左上から右下への対角線
|DiagonalUp|左下から右上への対角線
|LeftBorder|左側の境界線
|RightBorder|右側の境界線
|TopBorder|上部の境界線

[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)コレクションはすべての枠線を格納します。[**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)コレクション内の各枠線は[**Border**](https://reference.aspose.com/cells/javascript-cpp/border)オブジェクトで表され、二つのプロパティ[**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-)と[**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-)を持ち、枠線の線の色とスタイルをそれぞれ設定できます。

境界線の線の色を設定するには、Color列挙体（JavaScriptの一部）を使用して色を選択し、それをBorderオブジェクトのcolorプロパティに割り当てます。

枠線のラインスタイルは、[**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype)列挙型からスタイルを選択して設定します。

**CellBorderType列挙体**

|**線のスタイル**|**説明**|
| :- | :- |
|DashDot|細い点線のような線
|DashDotDot|細い破線点線のような線
|Dashed|破線のような線
|Dotted|点線のような線
|Double|二重線
|Hair|細い線
|MediumDashDot|中くらいの点線のような線
|MediumDashDotDot|中くらいの破線点線のような線
|MediumDashed|中くらいの破線のような線
|None|線なし
|Medium|中くらいの線
|SlantedDashDot|対角の中くらいの点線のような線
|Thick|太い線
|Thin|細い線
線スタイルを一つ選び、それを[**Border**](https://reference.aspose.com/cells/javascript-cpp/border)オブジェクトの[**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-)プロパティに割り当てます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
線のスタイルと色は同時に設定すべきです。斜めの二つの枠線は同じ線スタイルと色にします。
{{% /alert %}}

#### **セルの範囲に境界線を追加する**

1つのセルだけでなく、範囲に対して枠線を追加することも可能です。そのためには、最初に[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)メソッドを呼び出し、セル範囲を作成します。引数は以下の通りです：

- 最初の行、範囲の最初の行。
- 最初の列、範囲の最初の列を表す。
- 行数、範囲内の行数。
- 列数、範囲内の列数。

[**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)メソッドは、指定されたセル範囲を含む[**Range**](https://reference.aspose.com/cells/javascript-cpp/range)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/javascript-cpp/range)オブジェクトは、範囲に枠線を追加するための引数を取る[**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-)メソッドを提供します：

- **枠線タイプ**：[**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype)列挙型から選ばれる枠線タイプ。
- **ラインスタイル**：枠線のラインスタイル。[**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype)列挙型から選択。
- **色**、Color 列挙型から選択した線の色。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
