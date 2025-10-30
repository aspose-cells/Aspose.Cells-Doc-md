---
title: Überwachen laufender Programme
type: docs
weight: 10
url: /de/python-java/monitor-running-programs/
---

## **Wie man ein laufendes Programm überwacht**

Der folgende Beispielcode zeigt, wie ein laufendes Programm überwacht werden kann. Dieser Code kann verwendet werden, um das Laufen von [Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)-bezogenem Code zu überwachen. Verwenden Sie einfach die [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor)-Klasse, um ein Überwachungsobjekt zu erstellen, verwenden Sie die [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor)-Funktion, um es zu den Laufparameter der [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) hinzuzufügen, und verwenden Sie dann die [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int))-Funktion, um die erwartete Unterbrechungszeit (in Millisekunden) einzustellen. Wenn die Laufzeit des überwachten Codes die erwartete Zeit überschreitet, wird das Programm unterbrochen und es wird eine Ausnahme ausgelöst.

## **Beispielcode**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
