---
title: 実行中のプログラムの監視
type: docs
weight: 10
url: /ja/python-java/monitor-running-programs/
---

## **実行中のプログラムの監視方法**

次のサンプルコードは、実行中のプログラムを監視する方法を示しています。このコードは、実行中のプログラムを監視するために使用できます。[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)に関連するコードを監視する場合は、[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor)クラスを使用して監視オブジェクトを作成し、[setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor)関数を使用して[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)の実行パラメータに追加し、[startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int))関数を使用して予期される中断時刻（ミリ秒単位）を設定します。監視されているコードの実行時間が予想時間を超えると、プログラムが中断され、例外がスローされます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
