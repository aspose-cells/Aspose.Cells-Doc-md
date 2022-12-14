---
title: Stoppen Sie die Konvertierung oder das Laden mit InterruptMonitor, wenn es zu lange dauert
type: docs
weight: 100
url: /de/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Konvertierung der Arbeitsmappe in verschiedene Formate wie PDF, HTML usw. zu stoppen, indem Sie die verwenden[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)Objekt, wenn es zu lange dauert. Der Konvertierungsprozess ist häufig sowohl CPU- als auch speicherintensiv und es ist oft sinnvoll, ihn anzuhalten, wenn die Ressourcen begrenzt sind. Sie können verwenden[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)sowohl zum Stoppen der Konvertierung als auch zum Stoppen des Ladens riesiger Arbeitsmappen. Bitte verwende[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)Eigenschaft zum Stoppen der Konvertierung und[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)Eigenschaft zum Laden einer riesigen Arbeitsmappe.

## **Stoppen Sie die Konvertierung oder das Laden mit InterruptMonitor, wenn es zu lange dauert**

Der folgende Beispielcode erläutert die Verwendung von[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)Objekt. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert einige Sekunden (z*mehr als 30 Sekunden*), um es aufgrund dieser Codezeilen konvertieren zu lassen.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Wie du siehst**AB1000000**ist eine ziemlich weiter entfernte Zelle in der XLSX-Datei. Allerdings ist die*WaitForWhileAndThenInterrupt()*Methode unterbricht die Konvertierung nach 10 Sekunden und Programm endet/beendet. Bitte verwenden Sie den folgenden Code, um den Beispielcode auszuführen.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
