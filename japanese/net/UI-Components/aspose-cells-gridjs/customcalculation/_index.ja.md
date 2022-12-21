---
title: GridJs のカスタム計算エンジンの操作
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/customcalculation/
description: この記事では、Aspose.Cells.GridJs ライブラリのカスタム計算エンジンを使用する方法について説明します。
---
## **カスタム計算エンジンの実装**

Aspose.Cells.GridJs には、Microsoft の Excel 数式のほぼすべてを計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することもでき、より優れた機能と柔軟性を提供します。

この機能の実装には、次のプロパティとクラスが使用されます。

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

次のコードは、カスタム計算エンジンを実装します。インターフェースを実装します**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**を持っている**[Calculate(GridCalculationData データ)](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)**方法。このメソッドは、すべての数式に対して呼び出されます。このメソッド内で、**MYTESTFUNC**式を作成し、その最初のパラメーター値に 2 を掛けます。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
