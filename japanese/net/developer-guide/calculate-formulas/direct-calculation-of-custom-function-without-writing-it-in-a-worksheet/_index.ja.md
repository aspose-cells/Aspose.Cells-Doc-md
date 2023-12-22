---
title: カスタム関数をワークシートに記述せずに直接計算
description: この記事では、Aspose.Cells ライブラリを使用して、ワークシートに関数を記述せずに、Microsoft Excel でカスタム関数を直接計算する方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用してカスタム関数を計算し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **カスタム関数をワークシートに記述せずに直接計算**

このトピックでは、最初にワークシートにカスタム関数を記述せずに、カスタム関数を直接計算する方法について説明します。をご利用ください。[**Worksheet.CalculateFormula(文字列式、CalculationOptions オプション)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)この目的のためのメソッド。

このメソッドの使用法を示す次のサンプル コードを参照してください。 MyCompany.CustomFunction() という名前のカスタム関数を使用し、その値は「Aspose.Cells」として計算されます。その後、この値は計算エンジンによって「ようこそ」であるセル A1 の値と自動的に連結され、最終的に計算された値は「Aspose.Cells へようこそ」として返されます。カスタム関数はワークシートのどこにも記述されておらず、独自のカスタム ロジックによって直接計算されます。

###  **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **コンソール出力**

以下は、上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **関連記事**

{{% alert color="primary" %}}

[カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します。](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
