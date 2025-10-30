---
title: 塗りつぶし設定
linktitle: 塗りつぶし設定
description: JavaScriptをC++経由で使用してセルの塗りつぶし設定、背景、スタイルをカスタマイズする方法を学ぶ。
keywords: Aspose.Cells、セル、塗りつぶし設定、背景、スタイル、JavaScriptをC++経由
type: docs
weight: 50
url: /ja/javascript-cpp/cells-fill-settings/
---

## **色と背景パターン**

Microsoft Excel では、セルの前景（輪郭）と背景（塗りつぶし）の色、および背景パターンを設定できます。

Aspose.Cells もこれらの機能を柔軟にサポートしています。このトピックでは、Aspose.Cells を使用してこれらの機能を使用する方法について学びます。

### **色と背景パターンの設定**

Aspose.CellsはMicrosoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセス可能な[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションを提供し、[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)には、セルのフォーマットを取得および設定するために使用される[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)プロパティがあります。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)クラスは、セルの前景色と背景色を設定するためのプロパティを提供します。Aspose.Cellsは、以下に示す一連の事前定義された背景パターンタイプを含む[**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype)列挙体を提供します。

|**背景パターン**|**説明**|
| :- | :- |
|DiagonalCrosshatch| 対角線のかすかな格子状のパターンを表します|
|DiagonalStripe| 対角線のストライプパターンを表します|
|Gray6| 6.25% グレーのパターンを表します|
|Gray12| 12.5% グレーのパターンを表します|
|Gray25| 25% グレーのパターンを表します|
|Gray50| 50% グレーのパターンを表します|
|Gray75| 75% グレーのパターンを表します|
|HorizontalStripe|水平ストライプパターンを表します|
|None|背景なしを表します|
|ReverseDiagonalStripe|反対角ストライプパターンを表します|
|Solid|ソリッドパターンを表します|
|ThickDiagonalCrosshatch|太い斜めクロスハッチパターンを表します|
|ThinDiagonalCrosshatch|細い斜めクロスハッチパターンを表します|
|ThinDiagonalStripe|細い斜めストライプパターンを表します|
|ThinHorizontalCrosshatch|細い水平クロスハッチパターンを表します|
|ThinHorizontalStripe|細い水平ストライプパターンを表します|
|ThinReverseDiagonalStripe|細い逆斜めストライプパターンを表します|
|ThinVerticalStripe|細い垂直ストライプパターンを表します|
|VerticalStripe|垂直ストライプパターンを表します|

以下の例では、A1セルの前景色が設定されていますが、A2は前景色と背景色の両方を垂直ストライプの背景パターンで構成するように設定されています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **重要なこと**

{{% alert color="primary" %}}

- セルの前景色または背景色を設定するには、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style) オブジェクトの [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) または [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) プロパティを使用します。どちらも効果を発揮するのは、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style) オブジェクトの [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) プロパティが設定されている場合のみです。
- [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) プロパティはセルのシェード色を設定します。 [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) プロパティは、前景色または背景色に使用される背景パターンの種類を指定します。Aspose.Cells は、背景パターンの事前定義された種類を含む列挙体 [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) を提供します。
- [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) 列挙の *BackgroundType.None* 値を選択すると、前景色は適用されません。同様に、背景色は *BackgroundType.None* または *BackgroundType.Solid* の値を選択した場合に適用されません。
- セルのシェード／塗りつぶし色を取得する場合、[**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) が *BackgroundType.None* であれば、[**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) は *Color.Empty* を返します。

{{% /alert %}}

### **グラデーション塗りつぶし効果の適用**

セルに望ましいグラデーション塗りつぶし効果を適用するには、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style) オブジェクトの [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) プロパティを適切に使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム色も使用できます。カスタム色を使用する前に、まずパレットに色を追加します。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

### **パレットにカスタム色を追加**

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。

Aspose.CellsはMicrosoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、カスタムカラーを追加してパレットを変更するための[**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-)メソッドがあり、引数は次の通りです：

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}
