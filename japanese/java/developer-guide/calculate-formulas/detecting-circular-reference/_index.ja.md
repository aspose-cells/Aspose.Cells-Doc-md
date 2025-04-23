---
title: 循環参照の検出
type: docs
weight: 70
url: /ja/java/detecting-circular-reference/
---

## **紹介**

ワークブックには循環参照が存在し、時々、循環参照があるかどうかを検出する必要があります。

## **循環参照の検出の概念**

循環参照は、式が計算される時にのみ検出されます。なぜなら、1つの式の参照は通常、他の部分や他の式の計算結果に依存するからです。そのため、この要件(循環参照を持つセルを収集するための)のために新しいAPIを提供しています。

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): 計算されている1つのセルに関する関連データの計算を表します

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): は、循環参照が発生したときに式計算エンジンによって呼び出されます。列挙子内の要素は、1つのサークル内のすべてのセルを表す[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell)オブジェクトであり、返された値は、この呼び出し後に循環セルを計算する必要があるかどうかを示します。

ユーザーは、[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-)メソッドの実装でこれらの循環参照を収集することができます。

ソースのサンプルファイルは、次のリンクからダウンロードできます:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)クラスから派生した*CircularMonitor*クラスの定義は次のようになります:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
