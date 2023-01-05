---
title: テーブルの作成
type: docs
weight: 40
url: /ja/java/creating-a-list-object/
---
{{% alert color="primary" %}}

スプレッドシートの利点の 1 つは、電話番号リスト、タスク リスト、取引リスト、資産または負債のリストなど、さまざまな種類のリストを作成できることです。複数のユーザーが協力して、さまざまなリストを使用、作成、および維持できます。

Aspose.Cells は、リストの作成と管理をサポートしています。

{{% /alert %}}

## **テーブルの利点**

データのリストを実際のリスト オブジェクトに変換すると、いくつかの利点があります。

- 新しい行と列が自動的に含まれます。
- リストの下部に合計行を簡単に追加して、SUM、AVERAGE、COUNT などを表示できます。
- 右側に追加された列は、List オブジェクトに自動的に組み込まれます。
- 行と列に基づくグラフは自動的に展開されます。
- 行と列に割り当てられた名前付き範囲は、自動的に展開されます。
- リストは、偶発的な行と列の削除から保護されています。

## **Microsoft Excel を使用して表を作成する**

**リスト オブジェクトを作成するためのデータ範囲の選択** 

![todo:画像_代替_文章](creating-a-list-object_1.png)

[リストの作成] ダイアログが表示されます。

**リストの作成ダイアログ** 

![todo:画像_代替_文章](creating-a-list-object_2.png)

List オブジェクトを実装し、Total Row を指定する (Select**データ**、 それから**リスト**、 に続く**合計行**).

**リスト オブジェクトの作成** 

![todo:画像_代替_文章](creating-a-list-object_3.png)

## **Aspose.Cells API を使用してテーブルを作成する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。を作成するには[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)ワークシートで、使用[**リストオブジェクト**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)Worksheet クラスのコレクション プロパティ。各[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)実際には、[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)このクラスは、List オブジェクトを追加し、リストのセル範囲を指定するための add メソッドをさらに提供します。

指定されたセルの範囲に従って、Aspose.Cells によってワークシートに List オブジェクトが作成されます。[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)リストを制御するクラス。

以下の例では、同じものを作成しました[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)上記のセクションで Microsoft Excel を使用して作成したように、Aspose.Cells API を使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
