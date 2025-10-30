---
title: GolangをC++経由でAspose.Cellsのデフォルト計算エンジンを拡張するためのカスタム計算エンジンを実装する
linktitle: カスタム計算エンジンの実装
description: この記事では、GolangをC++経由でAspose.Cellsライブラリを使用してカスタム計算エンジンを実装し、デフォルトの計算エンジンを拡張する方法について説明します。既存のExcelファイルを読み込むか、新規に作成し、Aspose.Cellsが提供するメソッドを使用してカスタム計算エンジンを実装し、結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、カスタム計算エンジン、既定の計算エンジンを拡張、C++
type: docs
weight: 80
url: /ja/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **カスタム計算エンジンの実装**

Aspose.CellsにはほとんどすべてのMicrosoft Excel式を計算できる強力な計算エンジンがあります。それにもかかわらず、デフォルトの計算エンジンを拡張することが可能であり、より大きな力と柔軟性を提供します。

この機能の実装に使用される次のプロパティとクラスは次のとおりです。

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

以下のコードは、カスタム計算エンジンを実装しています。そのエンジンは[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)インターフェースを実装しており、[**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/)メソッドを持っています。このメソッドはすべての数式に対して呼び出されます。このメソッド内で、**TODAY**関数をキャプチャし、システムの日付に1日を追加します。したがって、現在の日付が2023年07月27日である場合、カスタムエンジンはTODAY()を2023年07月28日として計算します。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **結果**

上記のサンプルコードのコンソール出力を確認してください。カスタムエンジンを使用した場合、A1の値（日時）はカスタムエンジンを使用しなかった場合の結果よりも1日後になるはずです。

### **関連記事**

{{% alert color="primary" %}}

[ワークシートに書き込まずにカスタム関数を直接計算する](/cells/ja/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
