---
title: Node.jsとC++を使用したワークシートのスケール方法
linktitle: ワークシートを縮尺する方法
type: docs
weight: 130
url: /ja/nodejs-cpp/how-to-scale-a-worksheet/
description: この記事では、Aspose.Cells for Node.js via C++を使用してワークシートをスケールする方法を解説したコードを示します。
keywords: Node.jsでワークシートをスケールする方法、Node.jsを使用してワークシートをスケールする方法（C++経由）、Node.jsでワークシートを拡大縮小
---

## **可能な使用シナリオ**
ワークシートの縮尺は、作業するコンテキストによってさまざまな理由で便利です。一般的な理由をいくつか挙げます：
1. ページに収める：印刷時にすべての内容が1ページまたは指定したページ数に収まるようにし、読みやすさと管理の容易さを確保します。

1. プレゼンテーション：シートをより整理されたプロフェッショナルな外観にし、会議やレポートで他者と共有しやすくします。

1. 可読性：文字や他の要素のサイズを調整して、特に小さなフォントの読みづらさを感じる人々にとっても読みやすくします。

1. スペース管理：シート上のスペースの最適化を図り、不必要な空白を避け、重要な情報が過剰なスクロールなしで見えるようにします。

1. データビジュアル化：チャートやグラフの場合、適切なスペースに収めるためにサイズを調整し、見やすさを向上させることができます。

1. 一貫性：複数のシートやドキュメント間で見た目の一貫性を保つために、特にプロフェッショナルや教育環境で重要です。

## **Excelでワークシートを縮尺する方法**
Excelでシートをスケールすることで、印刷時にコンテンツを単一ページや指定したページ数に収めることができます。手順は次のとおりです：

1. シートを開く：スケールしたいExcelシートを開きます。

1. ページレイアウトタブへ移動：「リボン」内の「ページレイアウト」タブをクリックします。

1. スケール調整グループ：「ページレイアウト」タブ内の「スケール調整」グループを見つけます。ここでスケーリングの調整が行えます。幅：印刷されるシートの横幅ページ数を指定します。高さ：縦方向のページ数を指定します。スケール：カスタムの割合を設定することも可能です。
<br>
<img src="1.png" width=60% />

1. 幅と高さの設定：希望のページ数に設定します。例えば、シートを1ページに収めたい場合は両方とも1に設定します。

1. スケーリング割合の調整（必要に応じて）：特定の割合に設定したい場合は、Scaleボックスを調整します。例えば50%に設定すると、すべてが半分の大きさになります。


## **Node.jsとC++を使用したワークシートのスケーリング方法**
Aspose.Cells for Node.js via C++は、Excelファイルをプログラムで操作する強力なライブラリです。Aspose.Cellsを使用してワークシートをスケールするには、次の手順に従います：[サンプルファイル](sample.xlsx)を読み込み、内容が希望のページ数または特定のパーセンテージに収まるように印刷設定を調整してください。

### **例：ページに収める**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the worksheet to fit to 1 page wide and 1 page tall
pageSetup.setFitToPagesWide(1);
pageSetup.setFitToPagesTall(1);

// Save the modified workbook
workbook.save("output_fit_to_page.xlsx");
```
<br>
<img src="3.png" width=60% />

### **例：パーセンテージにスケール**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the scaling to a specific percentage (e.g., 75%)
pageSetup.setZoom(75);

// Save the modified workbook
workbook.save("output_scaled_percentage.xlsx");
```
<br>
<img src="2.png" width=60% />
