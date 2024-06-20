---
title: ピボットテーブルとソースデータ
type: docs
weight: 30
url: /ja/python-net/pivot-table-and-source-data/
description: この記事は、Aspose.Cells for Python via .NETを使用したピボットテーブルのソースデータの変更方法を示しています。
keywords: Aspose.Cells for Python via .NETを使用したPivot Tableのソースデータの変更方法。
---

## **Pivot Tableのソースデータ**

デザイン時にはわからない異なるデータソース（たとえばデータベースなど）からデータを取るピボットテーブルを作成したいときがあります。この記事では、ピボットテーブルのデータソースを動的に変更するアプローチについて説明します。

### **ピボットテーブルのデータソースを変更する**

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

以下のコード例を実行すると、ピボットテーブルのソースデータが変更されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

