---
title: Überwachen laufender Programme
type: docs
weight: 20
url: /de/net/Monitor-running-programs/
---

## **Wie man ein laufendes Programm überwacht**

Im folgenden Beispielcode wird gezeigt, wie man ein laufendes Programm überwachen kann. Dieser Code kann verwendet werden, um den Ablauf von [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)-bezogenem Code zu überwachen. Verwenden Sie einfach die Klasse [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) um ein Überwachungsobjekt zu erstellen, die Funktion [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) um es den laufenden Parametern von [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/) hinzuzufügen und die Funktion [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) um die erwartete Unterbrechungszeit (in Millisekunden) festzulegen. Wenn die Laufzeit des überwachten Codes die erwartete Zeit überschreitet, wird das Programm unterbrochen und es wird eine Ausnahme ausgelöst.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
