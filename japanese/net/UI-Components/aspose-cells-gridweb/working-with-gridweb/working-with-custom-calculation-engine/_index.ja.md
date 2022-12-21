---
title: カスタム計算エンジンの操作
type: docs
weight: 70
url: /ja/net/working-with-custom-calculation-engine/
---
## **カスタム計算エンジンの実装**

Aspose.Cells.Gridweb には、Microsoft Excel の数式のほぼすべてを計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することもでき、より優れた機能と柔軟性を提供します。

この機能の実装には、次のプロパティとクラスが使用されます。

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

次のコードは、カスタム計算エンジンを実装します。インターフェースを実装します**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**を持っている**[Calculate(GridCalculationData データ)](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)**方法。このメソッドは、すべての数式に対して呼び出されます。このメソッド内で、**MYTESTFUNC**式を作成し、その最初のパラメーター値に 2 を掛けます。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

