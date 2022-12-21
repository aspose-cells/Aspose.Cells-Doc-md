---
title: ワークブックの数式計算を中断またはキャンセルする
type: docs
weight: 50
url: /ja/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **考えられる使用シナリオ**

Aspose.Cells は、ワークブックの数式計算を中断またはキャンセルするメカニズムを提供します。[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。これは、ワークブックの数式計算に時間がかかりすぎて処理をキャンセルしたい場合に便利です。

## **ワークブックの数式計算を中断またはキャンセルする**

次のサンプル コードは、[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)方法[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラス。このメソッド内で、行と列のインデックス パラメータを使用してセル名を見つけます。セル名が B8 の場合、関数を呼び出して計算プロセスを中断します。[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。一度、具体的なクラス[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)クラスが実装され、そのインスタンスが割り当てられます[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)財産。ついに、[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)渡すことによって呼び出されます[**計算オプション**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions)パラメータとして。をご覧ください[サンプル Excel ファイル](51740731.xlsx)参照用に以下に示すコードのコンソール出力と同様に、コード内で使用されます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
