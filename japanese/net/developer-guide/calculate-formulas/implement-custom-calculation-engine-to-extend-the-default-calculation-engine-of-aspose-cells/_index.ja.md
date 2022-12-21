---
title: カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します
type: docs
weight: 80
url: /ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **カスタム計算エンジンの実装**

Aspose.Cells には、ほとんどすべての Microsoft Excel 数式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することもでき、より優れた機能と柔軟性を提供します。

この機能の実装には、次のプロパティとクラスが使用されます。

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[計算データ](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

次のコードは、カスタム計算エンジンを実装します。インターフェースを実装します**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**を持っている**[Calculate(CalculationData データ)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)**方法。このメソッドは、すべての数式に対して呼び出されます。このメソッド内で、**和**したがって、Aspose.Cells の計算値が 20 の場合、カスタム エンジンは 30 を加算して 50 にします。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **コンソール出力**

上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **関連記事**

{{% alert color="primary" %}}

[カスタム関数をワークシートに書かずに直接計算](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
