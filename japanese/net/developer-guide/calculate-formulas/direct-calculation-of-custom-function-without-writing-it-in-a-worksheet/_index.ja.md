---
title: ワークシートに書き込まずにカスタム関数を直接計算する
description: Microsoft Excelでワークシートに関数を記述せずにカスタム関数を直接計算するためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してカスタム関数を計算し、結果を取得し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, カスタム関数、直接計算、ワークシートに記述不要
type: docs
weight: 90
url: /ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **ワークシートに書き込まずにカスタム機能を直接計算する**

ワークシートに関数を最初に記述せずにカスタム関数を直接計算する方法を説明します。この目的のためには[**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)メソッドを使用してください。

このメソッドの利用法を示す次のサンプルコードをご覧ください。私たちは自社のカスタム関数MyCompany.CustomFunction()を使用し、計算エンジンによって"Aspose.Cells."としてその値を計算し、最終的な計算値として"Welcome to Aspose.Cells."が返されます。コードに示されている通り、カスタム機能をワークシートに書き込んでいないことがわかりますが、カスタムロジックで直接計算されています。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **コンソール出力**

上記のサンプルコードのコンソール出力は以下の通りです。

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **関連記事**

{{% alert color="primary" %}}

[Aspose.Cellsのデフォルト計算エンジンを拡張するカスタム計算エンジンの実装](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
