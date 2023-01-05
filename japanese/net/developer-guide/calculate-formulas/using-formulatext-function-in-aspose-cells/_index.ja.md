---
title: Aspose.Cells で FormulaText 関数を使用する
type: docs
weight: 60
url: /ja/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText は Excel 2013 以降の関数です。 Excel 2010 や 2007 などの以前のバージョンではサポートされていません。その名前が示すように、特定のセルに存在する数式のテキストを出力します。この記事では、Aspose.Cells を使用してこの機能を利用する方法を紹介します。

{{% /alert %}} 

次のサンプル コードは、Aspose.Cells を使用した FormulaText の使用法を示しています。このコードは、最初にセル A1 に数式を書き込み、次にセル A2 の FormulaText を使用して数式のテキストを出力します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **コンソール出力**
上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
