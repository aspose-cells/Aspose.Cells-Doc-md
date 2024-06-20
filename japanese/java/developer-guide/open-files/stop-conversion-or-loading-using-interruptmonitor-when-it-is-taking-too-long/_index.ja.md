---
title: 時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください
type: docs
weight: 100
url: /ja/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用すると、リソースが限られている場合に変換プロセスを中止したり、大きなワークブックの読み込みを中止したりすることができます。変換プロセスはCPUおよびメモリを多く使用し、リソースが限られている場合に中止することは役立ちます。中断するためには[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)オブジェクトを使用し、大きなワークブックの読み込みを停止するためにも[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)を使用することができます。変換を停止する場合は[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)プロパティ、大きなワークブックの読み込みを中止する場合は[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)プロパティを使用してください。

## **時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください**

以下のサンプルコードでは、[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)オブジェクトの使用方法について説明しています。コードは非常に大きなExcelファイルをPDFに変換します。これはコードの行のために時間がかかります（つまり*30秒以上*）。

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

AB1000000はXLSXファイルの相当するセルで、*WaitForWhileAndThenInterrupt()*メソッドは10秒後に変換を中断し、プログラムを終了/終了します。以下のコードを使用して、サンプルコードを実行してください。

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
