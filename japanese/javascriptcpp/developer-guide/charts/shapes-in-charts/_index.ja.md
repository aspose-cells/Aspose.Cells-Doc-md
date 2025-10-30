---
title: JavaScript を使用したチャート内のシェイプ（C++ 経由）
linktitle: チャート内の図形
description: Microsoft Excel でチャートやコントロールを追加・カスタマイズするために C++ 経由の Aspose.Cells for JavaScript の使い方を学習します。このガイドでは、チャートの要素を操作し、書式設定を調整し、チャートの外観や操作性を向上させる方法を示します。
keywords: C++ での Aspose.Cells for JavaScript、チャートコントロール、チャートのカスタマイズ、Microsoft Excel、チャート要素、書式設定
type: docs
weight: 70
url: /ja/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
時には、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cellsはランタイムでチャートにコントロールを追加できます。
{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルは、スプレッドシートのコンテンツに関する情報をユーザーに提供する手段を提供します。Aspose.Cellsを使用して、チャートにラベルを追加および操作できます。

クラスには [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-) という名前のメソッドを備えた [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) クラス があります。 このメソッドを使用してチャートにラベルコントロールを追加します。 このメソッドに使用されるパラメータのリストは以下の通りです：

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** - ラベルの幅、チャートエリアの1/4000単位。

このメソッドは [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) オブジェクトを返します。 [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) クラス はチャート内のラベルを表します。 いくつかの重要なメンバを持っています：

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) (プロパティ) - ラベルのキャプション文字列を指定します。
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--) (プロパティ) - 塗りつぶしの色属性を指定します。

以下の例では、チャートにラベルを追加する方法が示されています。 この例では、チャートが含まれたデザイナーファイル（**exp_piechart.xls**）を使用します。 このファイルを使用してチャートにラベルを挿入します。 チャートにラベルを追加するための元のコードは以下の通りです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Label In Chart Example</title>
    </head>
    <body>
        <h1>Add Label In Chart Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new label to the chart.
            const label = chart.shapes.addLabelInChart(100, 100, 350, 900);

            // Set the caption of the label.
            label.text = "A Label In Chart";

            // Set the Placement Type, the way the Label is attached to the cells.
            label.placement = AsposeCells.PlacementType.FreeFloating;

            // Save the excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Label added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **チャートにテキストボックスコントロールを追加**

レポートで重要な情報を強調表示する一つの方法は、テキストボックスを使用することです。たとえば、企業名を表示したり、最高の売上地域を示したりするためにテキストを入力します。 [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) クラス には [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) という名前のメソッドがあり、これを使用してチャートにテキストボックスコントロールを追加します。以下は、このメソッドに使用されるパラメータのリストです：

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - テキストボックスの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) オブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) クラスはチャート内のテキストボックスを表します。

下の例は、チャートにテキストボックスを追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートにテキストボックスを挿入してチャートタイトルを表示します。以下は、チャートにテキストボックスを追加するための元のコードです。

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new textbox to the chart.
            const textbox0 = chart.shapes.addTextBoxInChart(100, 1100, 350, 2550);

            // Fill the text.
            textbox0.text = "Sales By Region";

            // Get the textbox text frame.
            // const textframe0 = textbox0.textFrame;

            // Set the textbox to adjust it according to its contents.
            // textframe0.autoSize = true;

            // Set the font color.
            textbox0.font.color = AsposeCells.Color.Maroon;

            // Set the font to bold.
            textbox0.font.isBold = true;

            // Set the font size.
            textbox0.font.size = 14;

            // Set font attribute to italic.
            textbox0.font.isItalic = true;

            // Get the fill format of the textbox.
            const fillformat = textbox0.fill;

            // Get the line format type of the textbox.
            const lineformat = textbox0.line;

            // Set the line weight.
            lineformat.weight = 2;

            // Set the dash style to solid.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **チャートに画像を追加する**

Aspose.Cellsを使用すると、チャートに画像を挿入することができます。たとえば、チャートやその内容を強調したり、意味を追加するために画像を追加したり、ブランドのイメージファイルを挿入することができます。

[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) クラスは、画像オブジェクトをチャートに追加するために使用される[**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-)メソッドを提供します。以下は、メソッドに使用されるパラメータのリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) オブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) クラスはチャート内の画像オブジェクトを表します。

下の例は、チャートに画像を追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture to Chart</title>
    </head>
    <body>
        <h1>Add Picture to Chart Example</h1>
        <p>Select an Excel file and an image to add to the first chart in the first worksheet.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            if (!fileInput.files.length || !imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file and an image file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const imageFile = imageInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const imageBuffer = await imageFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first sheet.
            const sheet = workbook.worksheets.get(0);
            const chart = sheet.charts.get(0);

            // Add a new picture to the chart.
            const pic0 = chart.shapes.addPictureInChart(50, 50, new Uint8Array(imageBuffer), 40, 40);

            // Get the lineformat type of the picture.
            const lineformat = pic0.line;

            // Set the dash style.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Set the line weight.
            lineformat.weight = 4;

            // Save the modified Excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Picture added to chart successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **チャートにチェックボックスを追加する**

Aspose.Cellsを使用すると、[**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/)列挙型を使用して、チャートシートにチェックボックスを挿入することができます。以下の例では、チャートシートにチェックボックスを追加する方法を示しています。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_1.jpg)

次のコードスニペットによって生成された[出力ファイル](101089316.xlsx)が添付されています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Checkbox in Chart Sheet Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Insert Checkbox in Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            // This example creates a new workbook and inserts a chart sheet with a checkbox in the chart.
            // The file input is optional for this example (a new workbook is created regardless).

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a chart sheet to the workbook
            const index = workbook.worksheets.add(AsposeCells.SheetType.Chart);

            // Access the newly added chart sheet
            const sheet = workbook.worksheets.get(index);

            // Add a floating column chart to the chart sheet
            sheet.charts.addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);

            // Add nSeries to the chart (single series with values 1,2,3)
            sheet.charts.get(0).nSeries.add("{1,2,3}", false);

            // Add checkbox to the chart
            sheet.charts.get(0).shapes.addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);

            // Set text of the checkbox shape
            sheet.charts.get(0).shapes.get(0).text = "CheckBox 1";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertCheckboxInChartSheet_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart sheet with checkbox created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [ワードアートウォーターマークをグラフに追加する](/cells/ja/javascript-cpp/add-wordart-watermark-to-chart/)
