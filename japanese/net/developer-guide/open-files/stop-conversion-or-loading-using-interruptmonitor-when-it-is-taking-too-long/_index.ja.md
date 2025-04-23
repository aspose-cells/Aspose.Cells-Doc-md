---
title: 時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください
type: docs
weight: 100
url: /ja/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用すると、リソースが限られている場合に変換を停止するために、[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)オブジェクトを使用できます。変換プロセスはCPUおよびメモリの両方を多く使用するため、リソースが制限されているときに中断すると便利です。変換と巨大なワークブックの読み込みの両方を停止するために、[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)を使用できます。変換を中止する場合は[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor)プロパティを、巨大なワークブックの読み込みを中止する場合は[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor)プロパティを使用してください。

## **時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください**

次のサンプルコードでは、[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)オブジェクトの使用方法について説明しています。多大なExcelファイルをPDFに変換します。このコードは、これらのコードの行のために変換が数秒かかります（すなわち*30秒以上*）。

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

**J1000000** はXLSXファイルでかなり遠いセルであることがわかります。ただし、**WaitForWhileAndThenInterrupt()** メソッドを使用すると、10秒後に変換が中断され、プログラムが終了します。次のコードを使用して、サンプルコードを実行してください。

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
