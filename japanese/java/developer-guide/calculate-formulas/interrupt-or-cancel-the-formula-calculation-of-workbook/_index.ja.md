---
title: ワークブックの数式計算を中断またはキャンセルする
type: docs
weight: 30
url: /ja/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **考えられる使用シナリオ**

Aspose.Cells は、[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)クラス。これは、ワークブックの数式計算に時間がかかりすぎて処理をキャンセルしたい場合に便利です。

## **ワークブックの数式計算を中断またはキャンセルする**

次のサンプル コードは、[**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) の方法[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)クラス。このメソッド内で、行と列のインデックス パラメータを使用してセル名を見つけます。セル名が B8 の場合、AbstractCalculationMonitor.interrupt() メソッドを呼び出して計算プロセスを中断します。一度、具体的なクラス[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)クラスが実装され、そのインスタンスが割り当てられます[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)財産。ついに、[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) を渡すことによって呼び出されます[**計算オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)パラメータとして。をご覧ください[サンプル Excel ファイル](51740744.xlsx)参照用に以下に示すコードのコンソール出力と同様に、コード内で使用されます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
