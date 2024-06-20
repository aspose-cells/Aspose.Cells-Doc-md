---
title: Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert
type: docs
weight: 100
url: /de/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Konvertierung von Arbeitsmappen in verschiedene Formate wie PDF, HTML usw. mit dem [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)-Objekt zu stoppen, wenn es zu lange dauert. Der Konvertierungsprozess ist oft sowohl CPU- als auch speicherintensiv und es ist oft nützlich, ihn anzuhalten, wenn die Ressourcen begrenzt sind. Sie können [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) sowohl zum Stoppen der Konvertierung als auch zum Stoppen des Ladens riesiger Arbeitsmappen verwenden. Verwenden Sie [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) Eigenschaft, um die Konvertierung zu stoppen, und [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) Eigenschaft, um riesige Arbeitsmappen zu laden.

## ** Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert**

Der folgende Beispielcode erläutert die Verwendung des [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)-Objekts. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert mehrere Sekunden (d. h. *länger als 30 Sekunden*), um sie zu konvertieren, weil diese Zeilen Code vorhanden sind.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Wie Sie sehen, befindet sich **AB1000000** ziemlich weit entfernt in der XLSX-Datei. Die *WaitForWhileAndThenInterrupt()*-Methode unterbricht jedoch die Konvertierung nach 10 Sekunden, und das Programm endet/terminiert. Bitte verwenden Sie den folgenden Code, um den Beispielcode auszuführen.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
