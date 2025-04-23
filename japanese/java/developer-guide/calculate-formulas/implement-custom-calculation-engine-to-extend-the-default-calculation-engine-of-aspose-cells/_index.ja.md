---
title: Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する
type: docs
weight: 590
url: /ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.CellsにはほとんどすべてのMicrosoft Excel式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、より大きな力と柔軟性を提供します。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **カスタム計算エンジンの実装**
以下のコードは、カスタム計算エンジンを実装しています。インターフェース [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) を実装し、その中のメソッド [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate-com.aspose.cells.CalculationData-) を呼び出しています。このメソッドは、すべての数式に対して呼び出され、**TODAY**関数をキャプチャし、システム日付に1日加算します。つまり、現在の日付が 27/07/2023 の場合、カスタムエンジンは TODAY() を 28/07/2023 と計算します。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタムエンジンを使用した場合、A1の値（日時）はカスタムエンジンを使用しなかった場合の結果よりも1日後になるはずです。

### **関連記事**
{{% alert color="primary" %}} 

- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
