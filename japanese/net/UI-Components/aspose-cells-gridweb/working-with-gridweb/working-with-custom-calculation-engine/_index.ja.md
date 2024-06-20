---
title: カスタム計算エンジンを使用する
type: docs
weight: 70
url: /ja/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb,custom,calculation,CalculationEngine,GridAbstractCalculationEngine
description: この記事では、GridAbstractCalculationEngine を使用して GridWeb で計算プロセスをカスタマイズする方法を紹介します。
---

## **カスタム計算エンジンの実装**

Aspose.Cells.Gridweb には、ほとんどすべての Microsoft Excel の数式を計算できる強力な計算エンジンがあります。 これにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、これによりより大きなパワーと柔軟性が提供されます。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

以下のコードは、カスタム計算エンジンを実装します。 このメソッドは、すべての数式に対して呼び出されるインターフェース [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) を実装します。 このメソッドでは、**MYTESTFUNC** の数式を取得し、その第1パラメータの値を2倍にします。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

