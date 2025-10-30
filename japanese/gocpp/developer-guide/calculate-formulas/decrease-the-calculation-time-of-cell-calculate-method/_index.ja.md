---
title: GolangをC++経由でセルのCalculateメソッドの計算時間を短縮する
linktitle: Cell.Calculateの計算時間を短縮
description: Microsoft Excelのセル計算メソッドの計算時間を削減するためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してセル計算メソッドを最適化し、パフォーマンスを改善し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, セル計算メソッド、最適化、パフォーマンス、計算時間の短縮
type: docs
weight: 100
url: /ja/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能な使用シナリオ**

通常、ユーザーには[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)メソッドを一度呼び出し、その後個々のセルの計算済み値を取得することを推奨します。しかし、時にはワークブック全体を計算したくない場合もあります。特定のセルだけを計算したい場合、Aspose.Cellsは[**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)プロパティを提供しており、これを false に設定すると、個々のセルの計算時間を大幅に短縮できます。再帰プロパティがtrueに設定されている場合、すべての依存セルも都度計算されますが、falseに設定すると、依存セルは一度だけ計算され、その後は再計算されません。

## **Cell.Calculate() メソッドの計算時間を短縮する**

以下のサンプルコードは、[**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/)プロパティの使用例を示しています。このコードを[サンプルExcelファイル](5113710.xlsx)で実行し、その結果をコンソールで確認してください。再帰プロパティをfalseに設定すると、計算時間が大幅に短縮されることがわかります。プロパティの理解のためにコメントもご参照ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **コンソール出力**

このコードは、指定された[サンプルExcelファイル](5113710.xlsx)を使用して実行した場合のコンソール出力例です。出力結果は異なる場合がありますが、再帰プロパティをfalseに設定した後の経過時間は常にtrueに設定した場合より短くなります。

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
