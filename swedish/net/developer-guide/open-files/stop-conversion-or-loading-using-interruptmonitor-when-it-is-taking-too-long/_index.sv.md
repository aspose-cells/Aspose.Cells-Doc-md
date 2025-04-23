---
title: Stoppa konvertering eller inläsning med avbrottsövervakning när det tar för lång tid
type: docs
weight: 100
url: /sv/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att stoppa konverteringen av arbetsbok till olika format som PDF, HTML etc. med hjälp av [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) -objektet när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minnesintensiv och det är ofta användbart att avbryta den när resurserna är begränsade. Du kan använda [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) både för att stoppa konverteringen och för att stoppa inläsning av stora arbetsböcker. Använd [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) -egenskapen för att stoppa konvertering och [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) -egenskapen för att ladda stora arbetsböcker.

## **Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid**

Följande kodexempel förklarar användningen av [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) -objektet. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (det vill säga *mer än 30 sekunder*) att konvertera den på grund av dessa kodrader.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Som du ser är **J1000000** ganska långt bort cell i XLSX-fil. Dock avbryter **WaitForWhileAndThenInterrupt()** -metoden konverteringen efter 10 sekunder och programmet avslutas/avslutas. Vänligen använd följande kod för att exekvera exempelkod.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
