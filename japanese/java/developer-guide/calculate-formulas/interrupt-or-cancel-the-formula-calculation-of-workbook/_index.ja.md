---
title: ワークブックの数式計算を中断またはキャンセルする
type: docs
weight: 30
url: /ja/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsは、ワークブックの数式計算を中断またはキャンセルするためのAbstractCalculationMonitorクラスのinterrupt()メソッドを使用できます。これは、ワークブックの数式計算にかかる時間が長い場合に処理をキャンセルしたい場合に便利です。

## **ワークブックの数式計算を中断またはキャンセルする**

次のサンプルコードはAbstractCalculationMonitor.interrupt()メソッドを実装しています。このメソッド内で、行と列のインデックスパラメータを使用してセル名を見つけます。セル名がB8の場合、AbstractCalculationMonitor.interrupt()メソッドを呼び出して計算プロセスを中断します。AbstractCalculationMonitorクラスの具象クラスが実装されると、そのインスタンスがAbstractCalculationMonitor.interrupt()プロパティに割り当てられます。最後に、[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-)をパラメータとして渡して[**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)を呼び出します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **コンソール出力**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
