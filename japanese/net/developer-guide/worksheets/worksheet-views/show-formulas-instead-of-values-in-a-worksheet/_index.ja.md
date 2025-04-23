---
title: ワークシートで値の代わりに数式を表示する
type: docs
weight: 20
url: /ja/net/show-formulas-instead-of-values-in-a-worksheet/
description: この記事では、C# APIまたは.NETライブラリを使用して、Excelワークシートやスプレッドシートで値の代わりに数式をプログラムで表示するためのサンプルコードが提供されています。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**Formulas**リボンから**Show Formulas**オプションを使用して、計算された値の代わりに数式を表示させることが可能です。数式が表示されると、ワークシート内で数式が表示されます。Aspose.Cellsを使用して同じことを実現することができます。

{{% /alert %}}

Aspose.Cellsは[**Worksheet.ShowFormulas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/showformulas)プロパティを提供します。これを**true**に設定することで、Microsoft Excelに数式を表示設定することができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ShowFormulasInsteadOfValues-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
