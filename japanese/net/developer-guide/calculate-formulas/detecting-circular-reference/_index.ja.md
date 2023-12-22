---
title: 循環参照の検出
description: この記事では、Aspose.Cells Excel で循環参照を検出するために Aspose.Cells ライブラリを使用する方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用して循環参照を検出し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /ja/net/detecting-circular-reference/
---
##  **導入**

ワークブックには循環参照が含まれる場合があり、循環参照が存在するかどうかを検出する必要がある場合があります。

##  **循環参照検出の考え方**

ある式の参照は通常、他の部分または他の式の計算結果に依存するため、循環参照は式の計算時にのみ検出できます。そこで、数式計算のプロセスでこの要件 (循環参照を持つセルを収集するため) に対応する新しい API を提供します。

[**計算セル**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)計算中の 1 つのセルに関する関連データの計算を表します

[**AbstractCalculationMonitor.OnCircular(IEnumeratorcircularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): 循環参照が発生すると、数式計算エンジンによって呼び出されます。列挙子の要素は次のとおりです。[**計算セル**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) 1 つの円内のすべてのセルを表すオブジェクト。戻り値は、この呼び出し後に数式エンジンがそれらのセルを循環的に計算する必要があるかどうかを示します。

ユーザーは、の実装においてそれらの循環参照を収集できます。[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)方法。

ソース サンプル ファイルは次のリンクからダウンロードできます。

[循環式.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

の定義*円形モニター*から派生したクラス[**抽象的な計算モニター**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラスは次のとおりです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
