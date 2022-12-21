---
title: カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します
type: docs
weight: 590
url: /ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells には、ほとんどすべての Microsoft Excel 数式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することもでき、より優れた機能と柔軟性を提供します。

この機能の実装には、次のプロパティとクラスが使用されます。

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [計算データ](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **カスタム計算エンジンの実装**
次のコードは、カスタム計算エンジンを実装します。インターフェースを実装します[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)メソッドが 1 つしかない[calculate(CalculationData データ)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)）。このメソッドは、すべての数式に対して呼び出されます。このメソッド内で、**和**したがって、Aspose.Cells の計算値が 20 の場合、カスタム エンジンは 30 を加算して 50 にします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **コンソール出力**
上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **関連記事**
{{% alert color="primary" %}} 

- [カスタム関数をワークシートに書かずに直接計算](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
