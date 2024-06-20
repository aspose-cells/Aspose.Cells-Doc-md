---
title: 実行中のプログラムの監視
type: docs
weight: 20
url: /ja/cpp/Monitor-running-programs/
---

## **実行中のプログラムの監視方法**

次のサンプルコードは、実行中のプログラムを監視する方法を示しています。このコードは、[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) に関連するコードの実行を監視するために使用できます。単純に [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) クラスを使用して監視オブジェクトを作成し、[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) の実行パラメータに追加するために [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) 関数を使用し、その後 [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) 関数を使用して期待される中断時刻（ミリ秒単位）を設定します。監視されているコードの実行時間が期待される時間を超過すると、プログラムが中断されて例外がスローされます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
