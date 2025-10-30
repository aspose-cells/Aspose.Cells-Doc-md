---
title: Node.js via C++によるチャート内の図形
linktitle: チャート内の図形
description: Aspose.Cells for Node.js via C++を使ったMicrosoft Excelのチャートコントロールとカスタマイズの方法を学びます。このガイドでは、チャート要素の操作、書式設定、全体的な外観や使いやすさの向上方法を示します。
keywords: Aspose.Cells for Node.js via C++、チャートコントロール、チャートカスタマイズ、Microsoft Excel、チャート要素、書式設定。
type: docs
weight: 70
url: /ja/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
時には、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cellsはランタイムでチャートにコントロールを追加できます。
{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルは、スプレッドシートのコンテンツに関する情報をユーザーに提供する手段を提供します。Aspose.Cellsを使用して、チャートにラベルを追加および操作できます。

クラスには [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-) という名前のメソッドを備えた [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) クラス があります。 このメソッドを使用してチャートにラベルコントロールを追加します。 このメソッドに使用されるパラメータのリストは以下の通りです：

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** - ラベルの幅、チャートエリアの1/4000単位。

このメソッドは [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) オブジェクトを返します。 [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) クラス はチャート内のラベルを表します。 いくつかの重要なメンバを持っています：

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (プロパティ) - ラベルのキャプション文字列を指定します。
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (プロパティ) - 塗りつぶしの色属性を指定します。

以下の例では、チャートにラベルを追加する方法が示されています。 この例では、チャートが含まれたデザイナーファイル（**exp_piechart.xls**）を使用します。 このファイルを使用してチャートにラベルを挿入します。 チャートにラベルを追加するための元のコードは以下の通りです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **チャートにテキストボックスコントロールを追加**

レポートで重要な情報を強調表示する一つの方法は、テキストボックスを使用することです。たとえば、企業名を表示したり、最高の売上地域を示したりするためにテキストを入力します。 [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) クラス には [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) という名前のメソッドがあり、これを使用してチャートにテキストボックスコントロールを追加します。以下は、このメソッドに使用されるパラメータのリストです：

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - テキストボックスの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) オブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) クラスはチャート内のテキストボックスを表します。

下の例は、チャートにテキストボックスを追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートにテキストボックスを挿入してチャートタイトルを表示します。以下は、チャートにテキストボックスを追加するための元のコードです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **チャートに画像を追加する**

Aspose.Cellsを使用すると、チャートに画像を挿入することができます。たとえば、チャートやその内容を強調したり、意味を追加するために画像を追加したり、ブランドのイメージファイルを挿入することができます。

[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) クラスは、画像オブジェクトをチャートに追加するために使用される[**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-)メソッドを提供します。以下は、メソッドに使用されるパラメータのリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) オブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) クラスはチャート内の画像オブジェクトを表します。

下の例は、チャートに画像を追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **チャートにチェックボックスを追加する**

Aspose.Cellsを使用すると、[**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/)列挙型を使用して、チャートシートにチェックボックスを挿入することができます。以下の例では、チャートシートにチェックボックスを追加する方法を示しています。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_1.jpg)

次のコードスニペットによって生成された[出力ファイル](101089316.xlsx)が添付されています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **高度なトピック**
- [ワードアートウォーターマークをグラフに追加する](/cells/ja/nodejs-cpp/add-wordart-watermark-to-chart/)

{{< app/cells/assistant language="nodejs-cpp" >}}
