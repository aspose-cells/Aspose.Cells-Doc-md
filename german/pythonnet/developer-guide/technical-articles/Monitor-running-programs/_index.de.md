---
title: Überwachen laufender Programme
type: docs
weight: 20
url: /de/python-net/monitor-running-programs/
---

## **Wie man ein laufendes Programm überwacht**

Der folgende Beispielscode zeigt, wie ein laufendes Programm überwacht werden kann. Dieser Code kann verwendet werden, um den Ablauf von [Arbeitsmappe](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)zu überwachen. Verwenden Sie einfach die [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) Klasse, um ein Überwachungsobjekt zu erstellen, verwenden Sie die [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) Funktion, um es den Laufparametern hinzuzufügen, und verwenden Sie dann die [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) Funktion, um die erwartete Unterbrechungszeit (in Millisekunden) festzulegen. Wenn die Laufzeit des überwachten Codes die erwartete Zeit überschreitet, wird das Programm unterbrochen und eine Ausnahme ausgelöst.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
{{< app/cells/assistant language="python-net" >}}
