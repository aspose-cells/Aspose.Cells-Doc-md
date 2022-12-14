---
title: Stoppa konvertering eller laddning med InterruptMonitor när det tar för lång tid
type: docs
weight: 100
url: /sv/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Möjliga användningsscenarier**

Aspose.Cells låter dig stoppa konverteringen av Workbook till olika format som PDF, HTML etc. med hjälp av[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) objekt när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minnesintensiv och det är ofta användbart att stoppa den när resurserna är begränsade. Du kan använda[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) både för att stoppa konverteringen och för att sluta ladda en enorm arbetsbok. Snälla använd[**Arbetsbok.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) egendom för att stoppa konvertering och[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) egendom för att ladda enorm arbetsbok.

## **Stoppa konvertering eller laddning med InterruptMonitor när det tar för lång tid**

Följande exempelkod förklarar användningen av[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) objekt. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (dvs*mer än 30 sekunder*) för att få det konverterat på grund av dessa kodrader.

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

 Som du ser**J1000000** är en ganska längre cell i XLSX-fil. Men den**WaitForWhileAndThenInterrupt()**metoden avbryter konverteringen efter 10 sekunder och programmet avslutas/avslutas. Använd följande kod för att köra exempelkoden.

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
