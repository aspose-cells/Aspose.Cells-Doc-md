---
title: Cell.Calculateメソッドの計算時間の短縮
description: Microsoft Excelのセル計算メソッドの計算時間を削減するためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してセル計算メソッドを最適化し、パフォーマンスを改善し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, セル計算メソッド、最適化、パフォーマンス、計算時間の短縮
type: docs
weight: 100
url: /ja/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能な使用シナリオ**

通常、ユーザーには[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)メソッドを一度呼び出し、個々のセルの計算値を取得することをお勧めします。しかし、時々、ユーザーはブック全体を計算したくない場合があります。単に個々のセルを計算したいだけです。Aspose.Cellsは、[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) プロパティを提供しており、これを**false**に設定すると、個々のセルの計算時間が大幅に短縮されます。**true**にプロパティが設定されている場合、セルの依存関係は各呼び出しに対して再計算されますが、**false**にプロパティが設定されている場合、依存するセルは1度だけ計算され、次回以降に再計算されません。

## **Cell.Calculate() メソッドの計算時間を短縮する**

次のサンプルコードは、[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)プロパティの使用法を示しています。指定された[サンプルExcelファイル](5113710.xlsx) を使用してこのコードを実行し、コンソール出力を確認してください。[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive)プロパティを**false**に設定すると、計算時間が大幅に短縮されることがわかります。このプロパティの理解を深めるためにコメントもお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **コンソール出力**

上記のサンプルコードを指定された[サンプルExcelファイル](5113710.xlsx) で実行した際のコンソール出力です。出力は異なる可能性がありますが、再帰プロパティを**false**に設定した後の経過時間は常に**true**に設定するよりも少なくなります。

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
