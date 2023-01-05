---
title: リスト オブジェクトの書式設定 - テーブル
type: docs
weight: 50
url: /ja/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

関連するデータのグループを管理および分析するために、セルの範囲をリスト オブジェクト (Excel テーブルとも呼ばれます) に変換することができます。テーブルは、他の行や列のデータとは独立して管理される関連データを含む一連の行と列です。既定では、テーブルのすべての列のヘッダー行でフィルター処理が有効になっているため、リスト オブジェクト データをすばやくフィルター処理または並べ替えることができます。各合計行セルの集計関数のドロップダウン リストを提供するリスト オブジェクトに、合計行 (数値データの操作に役立つ集計関数の選択を提供するリスト内の特別な行) を追加できます。 Aspose.Cells は、リスト (またはテーブル) を作成および管理するためのオプションを提供します。

{{% /alert %}}

## **リスト オブジェクトの書式設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。を作成するには[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)ワークシートで、使用[**リストオブジェクト**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)のコレクション プロパティ[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。各[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)実際には、[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)このクラスは、List オブジェクトを追加し、それが包含するセルの範囲を指定する add メソッドをさらに提供します。指定されたセル範囲に従って、[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)は Aspose.Cells によってワークシートに作成されます。属性を使用します (たとえば、[**表スタイルの種類**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) の[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)クラスを使用して、要件に合わせてテーブルをフォーマットします。

以下の例では、サンプル データをワークシートに追加し、[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)デフォルトのスタイルを適用します。[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)スタイルは、Microsoft Excel 2007/2010 でサポートされています。

コードを実行すると、次の出力が生成されます。

**書式設定されたテーブルがワークシートに作成されます** 

![todo:画像_代替_文章](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
