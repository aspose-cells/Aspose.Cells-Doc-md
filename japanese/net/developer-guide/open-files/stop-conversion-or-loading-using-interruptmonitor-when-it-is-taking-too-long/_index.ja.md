---
title: 時間がかかりすぎる場合は、InterruptMonitor を使用して変換またはロードを停止します
type: docs
weight: 100
url: /ja/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用すると、PDF、HTML などのさまざまな形式への Workbook の変換を停止できます。[**割り込みモニター**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)時間がかかりすぎる場合はオブジェクト。多くの場合、変換プロセスは CPU とメモリの両方を集中的に使用するため、リソースが限られている場合に停止すると便利な場合がよくあります。使用できます[**割り込みモニター**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)変換を停止するためと、巨大なワークブックのロードを停止するための両方です。使ってください[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor)変換を停止するプロパティと[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor)巨大なワークブックをロードするためのプロパティ。

## **時間がかかりすぎる場合は、InterruptMonitor を使用して変換またはロードを停止します**

次のサンプル コードは、[**割り込みモニター**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)物体。このコードは、非常に大きな Excel ファイルを PDF に変換します。数秒かかります (つまり、*30秒以上*）これらのコード行のために変換する必要があります。

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

ご覧のとおり**J1000000** XLSX ファイルのかなり遠いセルです。しかし**WaitForWhileAndThenInterrupt()**メソッドは 10 秒後に変換を中断し、プログラムは終了/終了します。サンプルコードを実行するには、次のコードを使用してください。

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
