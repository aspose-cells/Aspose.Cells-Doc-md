---
title: ピボットテーブルとソースデータ
type: docs
weight: 30
url: /ja/python-net/pivot-table-and-source-data/
description: この記事では、ピボット テーブルのソース データを Aspose.Cells for Python via .NET で変更する方法を示します。
keywords: Change Pivot Table's Source Data
---
##  **ピボットテーブルのソースデータ**

設計時には不明なさまざまなデータ ソース (データベースなど) からデータを取得するピボット テーブルを含む Microsoft Excel レポートを作成したい場合があります。この記事では、ピボット テーブルのデータ ソースを動的に変更する方法を説明します。

###  **ピボットテーブルのソースデータの変更**

1. 新しいデザイナーテンプレートを作成します。
 1. 以下のスクリーンショットのように、新しいデザイナー テンプレート ファイルを作成します。
 1. 次に、このセル範囲を参照する名前付き範囲 *DataSource** を定義します。

      **デザイナー テンプレートの作成と名前付き範囲、DataSource の定義** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)
   
1. この名前付き範囲に基づいてピボット テーブルを作成します。
1. Microsoft Excel で、**データ**、次に**ピボットテーブル**および *ピボットグラフ レポート**。
 1. 最初の手順で作成した名前付き範囲に基づいてピボット テーブルを作成します。

      **名前付き範囲 DataSource に基づいてピボット テーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

   
1. 対応するフィールドをピボット テーブルの行と列にドラッグし、以下のスクリーンショットのような結果のピボット テーブルを作成します。

   **対応するフィールドに基づいてピボット テーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

   
1. ピボット テーブルを右クリックし、[*テーブル オプション**] を選択します。
 1. チェック**開くときに更新**で**データオプション**設定。

      **ピボットテーブルオプションの設定** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


これで、このファイルをデザイナー テンプレート ファイルとして保存できます。

1. 新しいデータを入力し、ピボット テーブルのソース データを変更します。
 1. デザイナー テンプレートが作成されたら、次のコードを使用してピボット テーブルのソース データを変更します。

以下のサンプルコードを実行すると、ピボットテーブルのソースデータが変更されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

