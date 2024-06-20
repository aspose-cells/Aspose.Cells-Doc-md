---
title: 実行中のプログラムの監視
type: docs
weight: 20
url: /ja/net/Monitor-running-programs/
---

## **実行中のプログラムの監視方法**

次のサンプルコードは、実行中のプログラムを監視する方法を示しています。このコードは、[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)関連コードの実行を監視するために使用できます。[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/)クラスを使用して監視オブジェクトを作成し、[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/)の実行パラメータに追加するために[SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/)関数を使用し、それから[StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/)関数を使用して期待される中断時間（ミリ秒単位）を設定します。監視されているコードの実行時間が想定時間を超えると、プログラムは中断され、例外がスローされます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
