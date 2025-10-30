---
title: GolangをC++経由で使用してExcel 2016のMINIFSおよびMAXIFS関数を計算する
description: この記事は、C++を使用してMicrosoft Excel 2016でMINIFSおよびMAXIFS関数を計算するためにAspose.Cellsライブラリを使用する方法を紹介します。
keywords: Aspose.Cells, Excel, 2016, MINIFS関数、MAXIFS関数、計算
type: docs
weight: 300
url: /ja/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能な使用シナリオ**
Microsoft Excel 2016はMINIFSおよびMAXIFS関数をサポートしています。これらの関数はExcel 2013以前ではサポートされていません。Aspose.Cellsもこれらの関数の計算をサポートしています。以下のスクリーンショットはこれらの関数の使用例を示しています。スクリーンショット内の赤いコメントを読んで、これらの関数の動作を理解してください。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016のMINIFSおよびMAXIFS関数の計算**
次のサンプルコードは[サンプルExcelファイル](5115149.xlsx)を読み込み、[Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)メソッドを呼び出して数式計算を行い、その結果を[出力PDF](5115154.pdf)に保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}
