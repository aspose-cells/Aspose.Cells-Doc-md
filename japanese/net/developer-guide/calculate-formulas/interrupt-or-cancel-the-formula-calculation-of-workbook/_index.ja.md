---
title: ワークブックの数式計算を中断またはキャンセルする
description: Microsoft Excelのワークブックの数式計算を中断またはキャンセルするためにAspose.Cellsライブラリを使用する方法について紹介します。既存のExcelファイルを読み込むか、新しいファイルを作成することで、Aspose.Cellsが提供するメソッドを使用して数式計算を中断またはキャンセルし、その結果を取得し、最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, ワークブック、数式計算、中断、キャンセル
type: docs
weight: 50
url: /ja/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) メソッドを使用して、ワークブックの数式計算を中断またはキャンセルするメカニズムを提供します。これは、ワークブックの数式計算にかかる時間が長い場合に便利です。

## **ワークブックの数式計算を中断またはキャンセルする**

次のサンプルコードは、[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) クラスの [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) メソッドを実装しています。このメソッド内で、行および列のインデックスパラメータを使用してセルの名前を見つけます。セルの名前がB8の場合、[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) メソッドを呼び出すことで計算プロセスを中断します。一度、[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) クラスの具象クラスが実装されると、そのインスタンスは [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor) プロパティに割り当てられます。最後に、[**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) をパラメータとして渡して [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) が呼び出されます。参考のために、コード内で使用される [サンプル Excelファイル](51740731.xlsx) および以下に示すコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **コンソール出力**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
