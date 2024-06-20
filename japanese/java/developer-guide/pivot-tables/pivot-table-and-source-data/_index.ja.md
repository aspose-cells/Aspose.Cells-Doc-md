---
title: ピボットテーブルとソースデータ
type: docs
weight: 110
url: /ja/java/pivot-table-and-source-data/
---

## **Pivot Tableのソースデータ**
ピボットテーブルのデータソースを動的に変更する
## **ピボットテーブルのデータソースを変更する**
1. 新しいデザイナーテンプレートを作成します。
   1. 以下のスクリーンショットに示すように、新しいデザイナーテンプレートファイルを作成します。
   1. その後、**DataSource**という名前の範囲を定義します。この範囲はこれらのセルの範囲を参照します。 

      **デザイナーテンプレートの作成と名前付き範囲の定義、DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. この名前付き範囲に基づいてPivot Tableを作成します。
   1. Microsoft Excelで**データ**、**ピボットテーブル**、**ピボットテーブルおよびピボットチャートレポート**を選択します。
   1. 最初のステップで作成した名前付き範囲に基づいてピボットテーブルを作成します。 

      **DataSourceに基づいてピボットテーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

1. 対応するフィールドをピボットテーブルの行と列にドラッグし、スクリーンショットに示されているような結果のピボットテーブルを作成します。 

   **対応するフィールドに基づいてピボットテーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

設計したピボットテーブルが以下に示されています。
   1. **データオプション**の設定で**開くときに更新**をチェックします。 

      **ピボットテーブルオプションの設定** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)



これで、このファイルをデザイナーテンプレートファイルとして保存できます。

1. 新しいデータを埋め込んでピボットテーブルのソースデータを変更します。
   1. デザイナーテンプレートが作成されたら、次のコードを使用してピボットテーブルのソースデータを変更します。

以下に示す例のコードを実行すると、ピボットテーブルのソースデータが変更され、ピボットテーブルが以下のようになります。

**動的に変更されたピボットテーブル** 

![todo:image_alt_text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
