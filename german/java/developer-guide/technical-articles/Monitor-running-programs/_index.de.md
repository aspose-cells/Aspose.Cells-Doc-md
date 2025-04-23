---
title: Überwachen laufender Programme
type: docs
weight: 20
url: /de/java/Monitor-running-programs/
---

## **Wie man ein laufendes Programm überwacht**

Der folgende Beispielcode zeigt, wie ein laufendes Programm überwacht werden kann. Dieser Code kann verwendet werden, um die Ausführung von [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/)-bezogenem Code zu überwachen. Verwenden Sie einfach die Klasse [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/), um ein Überwachungsobjekt zu erstellen, verwenden Sie die Funktion [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-), um es zu den Laufparametern von [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/) hinzuzufügen, und verwenden Sie dann die Funktion [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-), um die erwartete Unterbrechungszeit (in Millisekunden) festzulegen. Falls die Laufzeit des überwachten Codes die erwartete Zeit überschreitet, wird das Programm unterbrochen und eine Ausnahme ausgelöst.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
