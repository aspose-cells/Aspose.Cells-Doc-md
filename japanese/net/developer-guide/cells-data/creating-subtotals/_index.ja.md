---
title: 小計の作成
type: docs
weight: 800
url: /ja/net/creating-subtotals/
---
{{% alert color="primary" %}}

スプレッドシートで繰り返される値の小計を自動的に作成できます。 Aspose.Cells は、小計をプログラムでスプレッドシートに追加するのに役立つ API 機能を提供します。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel で小計を追加するには:

1. ワークブックの最初のワークシートに簡単なデータ リストを作成し (下図を参照)、ファイルを Book1.xls として保存します。
1. リスト内の任意のセルを選択します。
1. から**データ**メニュー、選択**小計**.小計ダイアログが表示されます。使用する関数と小計を配置する場所を定義します。

## **Aspose.Cells API を使用する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。このクラスは、ワークシートやその他のオブジェクトを管理するための幅広いプロパティとメソッドを提供します。各ワークシートは、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。小計をワークシートに追加するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス'[**小計**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法。メソッドにパラメーター値を指定して、小計の計算方法と配置方法を指定します。

以下の例では、Aspose.Cells API を使用して、テンプレート ファイル (Book1.xls) の最初のワークシートに小計を追加しています。コードを実行すると、小計を含むワークシートが作成されます。

次のコード スニペットは、Aspose.Cells for .NET を使用して小計をワークシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **先行トピック**
- [小計の適用と詳細の下のアウトライン集計行の方向の変更](/cells/ja/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
