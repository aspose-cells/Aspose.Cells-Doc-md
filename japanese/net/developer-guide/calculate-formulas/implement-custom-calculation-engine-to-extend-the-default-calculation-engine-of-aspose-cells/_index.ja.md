---
title: Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する
description: Aspose.Cellsライブラリを使用してカスタム計算エンジンを実装し、デフォルトの計算エンジンを拡張する方法について説明します。既存のExcelファイルを読み込むか、新しいファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してカスタム計算エンジンを実装し、結果を取得し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, カスタム計算エンジン、デフォルト計算エンジンの拡張
type: docs
weight: 80
url: /ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **カスタム計算エンジンの実装**

Aspose.CellsにはほとんどすべてのMicrosoft Excel式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、より大きな力と柔軟性を提供します。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

以下のコードは、カスタム計算エンジンを実装しています。そのエンジンは[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)インターフェースを実装しており、[**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)メソッドを持っています。このメソッドはすべての数式に対して呼び出されます。このメソッド内で、**TODAY**関数をキャプチャし、システムの日付に1日を追加します。したがって、現在の日付が2023年07月27日である場合、カスタムエンジンはTODAY()を2023年07月28日として計算します。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタムエンジンを使用した場合、A1の値（日時）はカスタムエンジンを使用しなかった場合の結果よりも1日後になるはずです。

### **関連記事**

{{% alert color="primary" %}}

[ワークブックの数式計算を書き込むことなく直接計算するカスタム関数](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
