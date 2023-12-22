---
title: ガントチャートの作成方法
linktitle: ガントチャートの作成方法
type: docs
weight: 72
url: /ja/net/how-to-create-gantt-chart/
description: Aspose.Cellsのガントチャートの作成方法。
keywords: create/insert Gantt Chart Excel Aspose
---
## ガントチャートとは

ガント チャートは、プロジェクト タスクのスケジュールを設定し、進捗状況を追跡するのに役立ちます。

##  Excelにガントチャートを追加する

単純なプロジェクト スケジュールのステータスをガント チャートで表示する必要がありますか? Excel には事前定義されたガント チャートの種類はありませんが、次のように積み上げ棒グラフをカスタマイズしてタスクの開始日と終了日を表示することで、ガント チャートをシミュレートできます。

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## 作成方法

- グラフ化したいデータを選択します。この例では、B1:B7 に続いて挿入します。**積み上げバー**チャート。

![todo:image_alt_text](1.png)

- チャートを選択し、**データを選択**->****を追加し、**シリーズ名を設定します**そして**系列値**次のように

![todo:image_alt_text](2.png)

- チャートを選択し、編集します**横(カテゴリ)軸ラベル**

![todo:image_alt_text](3.png)

- **軸のフォーマット**Y軸、選択**逆順のカテゴリ**
- を選択します**ブルーシリーズ**そして、**塗りつぶし -> 塗りつぶしなし**
- **軸のフォーマット** 軸、*最小値と最大値**を設定します(1/5/2019:43470、1/30/2019:43494)

![todo:image_alt_text](4.png)

- **データファイルの追加**チャート用
これでガントチャートが作成できました。

## Aspose.Cells にガント チャートを追加

次のサンプル コードでは、[サンプルファイル](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

次のようなファイルが得られます[結果ファイル](result.xlsx)ファイルには次の内容が表示されます。

![todo:image_alt_text](5.png)

