---
title: ワークブックの数式計算を中断またはキャンセルする
description: この記事では、Aspose.Cells Excel で Aspose.Cells ライブラリを使用してブックの数式計算を中断またはキャンセルする方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用して、数式の計算を中断またはキャンセルして結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /ja/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **考えられる使用シナリオ**

Aspose.Cells は、ワークブックの数式計算を中断またはキャンセルするメカニズムを提供します。[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。これは、ブックの数式計算に時間がかかりすぎて処理をキャンセルしたい場合に便利です。

##  **ワークブックの数式計算を中断またはキャンセルする**

次のサンプル コードは、[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)の方法[**抽象的な計算モニター**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラス。このメソッド内では、行と列のインデックス パラメーターを使用してセル名を検索します。セル名が B8 の場合、関数を呼び出して計算プロセスを中断します。[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。一度、具体的なクラス[**抽象的な計算モニター**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラスが実装され、そのインスタンスが割り当てられます[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)財産。ついに、[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)通りすがりに呼ばれる[**計算オプション**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions)パラメータとして。をご覧ください。[サンプル Excel ファイル](51740731.xlsx)コード内で使用されるほか、参考のために以下に示すコードのコンソール出力も使用されます。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **コンソール出力**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
