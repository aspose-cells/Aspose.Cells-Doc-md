---
title: 実行中のプログラムの監視
type: docs
weight: 20
url: /ja/java/Monitor-running-programs/
---

## **実行中のプログラムの監視方法**

以下のサンプルコードは実行中のプログラムを監視する方法を示しています。このコードは、[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/)関連のコードを監視するために使用できます。単に[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/)クラスを使用して監視オブジェクトを作成し、[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/)の実行パラメータに追加するために[SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-)関数を使用し、それから[StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-)関数を使用して期待される中断時間（ミリ秒単位）を設定します。監視対象のコードの実行時間が期待時間を超過した場合、プログラムは中断され、例外がスローされます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
