---
title: GridWebでカスタム関数を計算する
type: docs
weight: 90
url: /ja/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: この記事では、GridWebでのカスタム関数の機能について紹介します。
---


## **可能な使用シナリオ**
Aspose.Cells.GridWebは、GridWeb.CustomCalculationEngineプロパティを使用してカスタム関数の計算をサポートしています。このプロパティはGridAbstractCalculationEngineインターフェースのインスタンスを取ります。GridAbstractCalculationEngineインターフェースを実装し、独自のロジックでカスタム関数を計算してください。
## **GridWebでカスタム関数を計算する**
次のサンプルコードは、セル B3 に MYTESTFUNC() というカスタム関数を追加します。次に、GridAbstractCalculationEngine インターフェースを実装して、この関数の値を計算します。MYTESTFUNC()は、そのパラメータを2倍にして結果を返すように計算されます。そのため、パラメータが9の場合、2*9 = 18 を返します。
### **サンプルコード**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
