---
title: Stoppen Sie die Konvertierung oder das Laden mit InterruptMonitor, wenn es zu lange dauert
type: docs
weight: 100
url: /de/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Konvertierung der Arbeitsmappe in verschiedene Formate wie PDF, HTML usw. zu stoppen[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) Objekt, wenn es zu lange dauert. Der Konvertierungsprozess ist häufig sowohl CPU- als auch speicherintensiv und es ist oft sinnvoll, ihn anzuhalten, wenn die Ressourcen begrenzt sind. Sie können verwenden[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)sowohl zum Stoppen der Konvertierung als auch zum Stoppen des Ladens riesiger Arbeitsmappen. Bitte verwende[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) Eigenschaft zum Stoppen der Konvertierung und[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) Eigenschaft zum Laden einer riesigen Arbeitsmappe.

## **Stoppen Sie die Konvertierung oder das Laden mit InterruptMonitor, wenn es zu lange dauert**

Der folgende Beispielcode erläutert die Verwendung von[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) Objekt. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert einige Sekunden (dh*mehr als 30 Sekunden*), um es aufgrund dieser Codezeilen konvertieren zu lassen.

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

 Wie du siehst**J1000000** ist eine ziemlich weiter entfernte Zelle in der Datei XLSX. Allerdings ist die**WaitForWhileAndThenInterrupt()**Methode unterbricht die Konvertierung nach 10 Sekunden und Programm endet/beendet. Bitte verwenden Sie den folgenden Code, um den Beispielcode auszuführen.

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
