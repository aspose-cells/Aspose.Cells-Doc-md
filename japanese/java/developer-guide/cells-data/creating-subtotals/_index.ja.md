---
title: 小計の作成
type: docs
weight: 50
url: /ja/java/creating-subtotals/
---
{{% alert color="primary" %}}

スプレッドシートで繰り返される値の小計を自動的に作成できます。 Aspose.Cells は、小計をスプレッドシートにプログラムで追加するのに役立つ API 機能を提供します。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel で小計を作成するには:

1. ワークブックの最初のワークシートに簡単なデータ リストを作成し (下図を参照)、ファイルを Book1.xls として保存します。
1. リスト内の任意のセルを選択します。
1. から**データ**メニュー、選択**小計**.
小計ダイアログが表示されます。使用する関数と小計を配置する場所を定義します。

   **小計を追加するデータ範囲の選択**

![todo:画像_代替_文章](creating-subtotals_1.png)

**小計ダイアログ** 

![todo:画像_代替_文章](creating-subtotals_2.png)

## **Aspose.Cells API を使用**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。このクラスは、ワークシートやその他のオブジェクトを管理するための幅広いプロパティとメソッドを提供します。各ワークシートは、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。ワークシートで小計を作成するには、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラスの小計メソッド。メソッドのパラメーターに適切な値を指定して、必要な結果を取得します。

次の例は、Aspose.Cells API を使用して、テンプレート ファイル (Book1.xls) の最初のワークシートに小計を作成する方法を示しています。

コードが実行されると、小計を含むワークシートが作成されます。

**小計の適用** 

![todo:画像_代替_文章](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
