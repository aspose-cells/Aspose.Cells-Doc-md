---
title: テーブルの作成
type: docs
weight: 40
url: /ja/java/creating-a-list-object/
---

{{% alert color="primary" %}}

スプレッドシートの利点の1つは、電話リスト、タスクリスト、取引のリスト、資産リスト、負債リストなど、さまざまなタイプのリストを作成できることです。複数のユーザーが協力して、さまざまなリストを利用、作成、維持することができます。

Aspose.Cellsはリストの作成と管理をサポートしています。

{{% /alert %}}

## **テーブルの利点**

実際のリストオブジェクトにデータリストを変換すると、いくつかの利点があります:

- 新しい行や列が自動的に含まれます。
- リストの最下部に合計、平均、カウントなどを表示するために総合行を簡単に追加できます。
- 右に追加された列は自動的にリストオブジェクトに取り込まれます。
- 行と列に基づくチャートは自動的に拡張されます。
- 行と列に割り当てられた名前付き範囲は自動的に拡張されます。
- リストは誤って行や列が削除されないように保護されています。

## **Microsoft Excelを使用して表を作成する**

リストオブジェクトを作成するためのデータ範囲の選択 

![todo:image_alt_text](creating-a-list-object_1.png)

これにより、リストの作成ダイアログが表示されます。

リストの作成ダイアログ 

![todo:image_alt_text](creating-a-list-object_2.png)

リストオブジェクトの実装と合計行を指定する（**データ**を選択し、**リスト**、次に**合計行**を選択）。

リストオブジェクトを作成する 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Aspose.Cells APIを使用して表を作成する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが提供されています。 ワークシート内に[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)を作成するには、ワークシートクラスの[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)コレクションプロパティを使用します。 各[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)クラスのオブジェクトであり、さらにはリストオブジェクトを追加し、リストオブジェクトの範囲を指定するためのaddメソッドを提供しています。

指定したセル範囲に応じて、Aspose.Cellsによってワークシートにリストオブジェクトが作成されます。 テーブルをコントロールするための[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)クラスの属性（ShowTotals、ListColumnsなど）を使用します。

以下の例では、上のセクションでMicrosoft Excelを使用して作成したものと同じ[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)をAspose.Cells APIを使用して作成しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
