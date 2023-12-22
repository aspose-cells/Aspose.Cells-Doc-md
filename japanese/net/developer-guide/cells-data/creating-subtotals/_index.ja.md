---
title: 小計の作成
type: docs
weight: 800
url: /ja/net/creating-subtotals/
description: Aspose.Cells for .NET API を使用して、スプレッドシート内の繰り返し値の小計を作成する方法を学びます。
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

スプレッドシート内の繰り返し値の小計を自動的に作成できます。 Aspose.Cells は、プログラムでスプレッドシートに小計を追加するのに役立つ API 機能を提供します。

{{% /alert %}}

##  **Microsoft Excelの使用**

Microsoft Excel で小計を追加するには:

1. ワークブックの最初のワークシートに単純なデータ リストを作成し (下図を参照)、そのファイルを Book1.xls として保存します。
1. リスト内の任意のセルを選択します。
1. から**データ**メニューで、*小計**を選択します。小計ダイアログが表示されます。使用する関数と小計を配置する場所を定義します。

##  **Aspose.Cells API を使用する**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。このクラスは、ワークシートやその他のオブジェクトを管理するための幅広いプロパティとメソッドを提供します。各ワークシートは、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。ワークシートに小計を追加するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス'[**小計**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。メソッドにパラメーター値を指定して、小計の計算方法と配置方法を指定します。

以下の例では、Aspose.Cells API を使用して、テンプレート ファイル (Book1.xls) の最初のワークシートに小計を追加しました。コードが実行されると、小計を含むワークシートが作成されます。

次のコード スニペットは、Aspose.Cells for .NET を使用してワークシートに小計を追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **アドバンストトピック**
- [詳細の下の概要行の小計の適用と方向の変更](/cells/ja/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
