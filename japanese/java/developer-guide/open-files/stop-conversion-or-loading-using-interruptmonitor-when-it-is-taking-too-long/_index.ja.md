---
title: 時間がかかりすぎる場合は、InterruptMonitor を使用して変換またはロードを停止します
type: docs
weight: 100
url: /ja/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用すると、ワークブックから PDF、HTML などのさまざまな形式への変換を停止できます。[**割り込みモニター**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)時間がかかりすぎる場合はオブジェクト。多くの場合、変換プロセスは CPU とメモリの両方を集中的に使用するため、リソースが限られている場合に停止すると便利な場合がよくあります。使用できます[**割り込みモニター**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)変換を停止するためと、巨大なワークブックのロードを停止するための両方です。使ってください[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)変換を停止するプロパティと[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)巨大なワークブックをロードするためのプロパティ。

## **時間がかかりすぎる場合は、InterruptMonitor を使用して変換またはロードを停止します**

次のサンプル コードは、[**割り込みモニター**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)物体。このコードは、非常に大きな Excel ファイルを PDF に変換します。数秒かかります（つまり*30秒以上*）これらのコード行のために変換する必要があります。

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

ご覧のとおり**AB1000000**XLSX ファイルではかなり遠いセルです。しかし*WaitForWhileAndThenInterrupt()*メソッドは 10 秒後に変換を中断し、プログラムは終了/終了します。サンプルコードを実行するには、次のコードを使用してください。

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
