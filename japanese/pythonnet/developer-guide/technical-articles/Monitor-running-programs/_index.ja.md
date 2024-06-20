---
title: 実行中のプログラムの監視
type: docs
weight: 20
url: /ja/python-net/monitor-running-programs/
---

## **実行中のプログラムの監視方法**

次のサンプルコードは、実行中のプログラムを監視する方法を示しています。このコードは、[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)関連コードの実行を監視するために使用できます。[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/)クラスを使用して監視オブジェクトを作成し、[LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/)の実行パラメータに追加するために[setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/)関数を使用し、[startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int)関数を使用して、予想される中断時間（ミリ秒単位）を設定します。監視されたコードの実行時間が予想時間を超えると、プログラムが中断され、例外がスローされます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
