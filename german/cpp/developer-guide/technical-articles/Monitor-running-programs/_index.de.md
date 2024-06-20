---
title: Überwachen laufender Programme
type: docs
weight: 20
url: /de/cpp/Monitor-running-programs/
---

## **Wie man ein laufendes Programm überwacht**

Der folgende Beispielcode zeigt, wie man ein laufendes Programm überwachen kann. Dieser Code kann verwendet werden, um die Ausführung des mit [Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) zusammenhängenden Codes zu überwachen. Verwenden Sie einfach die Klasse [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) , um ein Überwachungsobjekt zu erstellen, verwenden Sie die Funktion [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) , um es zu den Laufparametern von [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) hinzuzufügen, und verwenden Sie dann die Funktion [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) , um die erwartete Unterbrechungszeit (in Millisekunden) festzulegen. Wenn die Laufzeit des überwachten Codes die erwartete Zeit überschreitet, wird das Programm unterbrochen und es wird eine Ausnahme ausgelöst.

## **Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
