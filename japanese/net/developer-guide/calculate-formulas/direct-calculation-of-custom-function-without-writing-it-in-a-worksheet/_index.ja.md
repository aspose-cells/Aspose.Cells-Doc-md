---
title: カスタム関数をワークシートに書かずに直接計算
type: docs
weight: 90
url: /ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **カスタム関数をワークシートに書かずに直接計算**

このトピックでは、最初にカスタム関数をワークシートに記述せずに直接計算する方法について説明します。をご利用ください[**Worksheet.CalculateFormula(文字列式、CalculationOptions オプション)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)この目的のためのメソッド。

このメソッドの使用法を示す次のサンプル コードを参照してください。 MyCompany.CustomFunction() という名前のカスタム関数を使用し、その値を "Aspose.Cells" として計算します。この値は、計算エンジンによって「Welcome to」であるセル A1 の値と自動的に連結され、最終的に計算された値は「Welcome to Aspose.Cells.」として返されます。カスタム関数はワークシートのどこにも記述されておらず、独自のカスタム ロジックによって直接計算されます。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **コンソール出力**

以下は、上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **関連記事**

{{% alert color="primary" %}}

[カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
