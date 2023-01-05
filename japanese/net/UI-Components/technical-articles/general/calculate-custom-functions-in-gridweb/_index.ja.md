---
title: GridWeb でカスタム関数を計算する
type: docs
weight: 90
url: /ja/net/calculate-custom-functions-in-gridweb/
---
## **考えられる使用シナリオ**
Aspose.Cells.GridWeb は、GridWeb.CustomCalculationEngine プロパティを使用してカスタム関数の計算をサポートします。このプロパティは、GridAbstractCalculationEngine インターフェイスのインスタンスを取ります。 GridAbstractCalculationEngine インターフェイスを実装し、独自のロジックでカスタム関数を計算してください。
## **GridWeb でカスタム関数を計算する**
次のサンプル コードは、セル B3 に MYTESTFUNC() という名前のカスタム関数を追加します。次に、GridAbstractCalculationEngine インターフェイスを実装して、この関数の値を計算します。パラメータに 2 を掛けて結果を返すように MYTESTFUNC() を計算します。したがって、パラメータが 9 の場合、2*9 = 18 が返されます。
### **サンプルコード**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
