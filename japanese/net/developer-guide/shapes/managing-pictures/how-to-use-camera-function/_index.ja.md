---
title: 範囲にカメラを追加する方法
type: docs
weight: 10
url: /ja/net/how-to-add-camera-for-range/
description: この記事では、API Aspose.Cells for .NETの範囲コンテンツにカメラを追加する方法を紹介します。
keywords: カメラ機能の使い方、範囲にカメラを追加する方法、カメラツールの使い方、Excelのカメラ機能、API Aspose.Cells for .NETでのカメラ機能の使い方
---

## **可能な使用シナリオ**
Excelのカメラツールは、隠されたが強力な機能であり、セル範囲のライブリンクされたスナップショットを作成できます。それをいつ、なぜ使うのかをご紹介します。

カメラツールの内容:
1. 選択したセル範囲の"写真"を撮る。
2.この"写真"はライブリンクです。ソースセルが変更されると、画像も自動的に更新されます。
3. 画像はシート内の任意の場所や別のシートに移動またはサイズ変更が可能です。


## **Excelでのカメラ機能の使い方**
こちらは、Excelのカメラツールを使用してセル範囲のライブで動的な画像を作成するための段階的ガイドです。

### カメラツールの有効化

カメラツールはデフォルトでは非表示です。以下の方法で追加します：

1. Excelのクイックアクセスツールバー（左上隅）の下矢印をクリックします。
2.その他のコマンドを選択....
3. ダイアログ内で、「リボンにないコマンド」のドロップダウンから「コマンドの選択」を選び、スクロールして「カメラ」を選択します。「追加>>」をクリックしてツールバーに追加します。
4. OKをクリックします。これでツールバーに小さなカメラアイコンが表示されます。

### カメラツールの使用方法
1. キャプチャしたいセル範囲を選択します（例：A1:C5）。
2. クイックアクセスツールバーのカメラインコンをクリックします。
3. カーソルが十字線に変わります。
4. 画像を配置したいワークシートの任意の場所をクリックします。選択範囲のライブ画像が挿入されます。

### 動的リンク
画像は元のセルにリンクされています。ソース範囲の値や書式が変更されると、画像は自動的に更新されます。


## **範囲のカメラ追加方法について（Aspose.Cells for .NET）**
Aspose.Cellsは、セルまたは範囲の内容を画像の形で表示することをサポートしています。表示したいデータを含むセルまたは範囲に画像をリンクできます。セルまたは範囲がグラフィックオブジェクトにリンクされているため、そのセルまたは範囲のデータを変更すると、自動的にグラフィックオブジェクトに反映されます。 

以下は、サンプルファイル（camera.xlsx）を使用した[カメラ機能の使用例](Aspose.Cells for .NET)の基本的な例です：

1. [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook)クラスを使用してサンプルファイルを読み込む。
1. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)オブジェクトの[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)コレクションの[**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)メソッドを呼び出して、ワークシートに画像を追加します。 
1. [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトの[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)属性を使用してセル範囲を指定します。
1. ワークシート内で選択した図形の値を更新します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **結果出力**
以下のスクリーンショットは、Aspose.Cells for .NETによって作成された範囲（A1:E12）のカメラの出力Excelファイルです。
<br>
データ追加前：
<br>
<img src="1.png" width=70% />
<br>
データ追加後：
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
