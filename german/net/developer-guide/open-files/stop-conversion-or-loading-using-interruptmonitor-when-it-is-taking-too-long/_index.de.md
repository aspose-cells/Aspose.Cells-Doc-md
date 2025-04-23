---
title: Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert
type: docs
weight: 100
url: /de/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Konvertierung einer Arbeitsmappe in verschiedene Formate wie PDF, HTML usw. mit dem [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)-Objekt zu stoppen, wenn es zu lange dauert. Der Konvertierungsprozess ist oft sowohl rechen- als auch speicherintensiv und es ist oft nützlich, ihn zu stoppen, wenn die Ressourcen begrenzt sind. Sie können [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) sowohl zum Stoppen der Konvertierung als auch zum Stoppen des Ladens großer Arbeitsmappen verwenden. Verwenden Sie das [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor)-Eigenschaft zum Stoppen der Konvertierung und das [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor)-Eigenschaft zum Laden großer Arbeitsmappen.

## ** Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert**

Der folgende Beispielscode erläutert die Verwendung des [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)-Objekts. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert einige Sekunden (d.h. *mehr als 30 Sekunden*), um sie zu konvertieren, aufgrund dieser Codezeilen.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Wie Sie sehen, ist **J1000000** in der XLSX-Datei recht weit entfernt. Die Methode **WaitForWhileAndThenInterrupt()** unterbricht die Konvertierung nach 10 Sekunden und das Programm endet/terminiert. Verwenden Sie bitte den folgenden Code, um den Beispielscode auszuführen.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
