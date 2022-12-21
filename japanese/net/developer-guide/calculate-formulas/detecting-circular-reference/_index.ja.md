---
title: 循環参照の検出
type: docs
weight: 70
url: /ja/net/detecting-circular-reference/
---
## **序章**

ワークブックには循環参照が含まれている可能性があり、循環参照が存在するかどうかを検出する必要がある場合があります。

## **循環参照の検出の背後にある概念**

循環参照は、式が計算されたときにのみ検出できます。これは、1 つの式の参照は通常、他の部分または他の式の計算結果に依存するためです。そのため、式の計算の過程でこの要件 (循環参照を含むセルを収集する) に対応する新しい API を提供します。

[**計算セル**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)計算中の 1 つのセルに関する関連データの計算を表します

[**AbstractCalculationMonitor.OnCircular(IEnumerator circleCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)循環参照に遭遇すると、数式計算エンジンによって呼び出されます。列挙子の要素は[**計算セル**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) つの円内のすべてのセルを表すオブジェクト。返される値は、この呼び出しの後に数式エンジンがこれらのセルを循環的に計算する必要があるかどうかを示します。

ユーザーは、これらの循環参照を次の実装で収集できます。[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)方法。

ソース サンプル ファイルは、次のリンクからダウンロードできます。

[循環式.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

の定義*円形モニター*から派生したクラス[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラスは次のとおりです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
