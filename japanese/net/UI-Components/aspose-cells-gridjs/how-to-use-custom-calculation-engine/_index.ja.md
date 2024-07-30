---
title: GridJsのためのカスタム計算エンジンの操作
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: この記事では、Aspose.Cells.GridJsライブラリのカスタム計算エンジンの使用方法について説明します。
aliases:
  - /net/aspose-cells-gridjs/customcalculation/
  - /net/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **カスタム計算エンジンの実装**

Aspose.Cells.GridJsには、ほとんどのMicrosoft Excel式を計算できる強力な計算エンジンがあります。 このため、デフォルトの計算エンジンを拡張することができ、より大きな力と柔軟性を得ることができます。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

以下のコードは、カスタム計算エンジンを実装します。 このメソッドは、すべての数式に対して呼び出されるインターフェース [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine) を実装します。 このメソッドでは、**MYTESTFUNC** の数式を取得し、その第1パラメータの値を2倍にします。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

