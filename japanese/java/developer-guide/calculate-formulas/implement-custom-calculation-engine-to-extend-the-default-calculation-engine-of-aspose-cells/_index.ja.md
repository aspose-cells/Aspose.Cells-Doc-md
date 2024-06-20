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
以下のコードは、カスタム計算エンジンの実装を示しています。それは[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) インタフェースを実装し、ただ1つの[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)) メソッドを持っています。このメソッドはすべての式に対して呼び出されます。このメソッド内で、**TODAY**関数を捕捉し、システム日付に1日加えます。したがって、現在の日付が2023年07月27日の場合、カスタムエンジンはTODAY()を2023年07月28日として計算します。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタムエンジンを使用した場合、A1の値（日時）はカスタムエンジンを使用しなかった場合の結果よりも1日後になるはずです。

### **関連記事**
{{% alert color="primary" %}} 

- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
