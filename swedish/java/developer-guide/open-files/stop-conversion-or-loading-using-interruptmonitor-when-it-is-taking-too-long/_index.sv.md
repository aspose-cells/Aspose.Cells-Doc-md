---
title: Stoppa konvertering eller laddning med InterruptMonitor när det tar för lång tid
type: docs
weight: 100
url: /sv/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Möjliga användningsscenarier**

Aspose.Cells låter dig stoppa konverteringen av arbetsboken till olika format som PDF, HTML, etc. med hjälp av[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)objekt när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minnesintensiv och det är ofta användbart att stoppa den när resurserna är begränsade. Du kan använda[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)både för att stoppa konverteringen och för att sluta ladda en enorm arbetsbok. Snälla använd[**Arbetsbok.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)egendom för att stoppa konvertering och[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)egendom för att ladda enorm arbetsbok.

## **Stoppa konvertering eller laddning med InterruptMonitor när det tar för lång tid**

Följande exempelkod förklarar användningen av[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)objekt. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (dvs.*mer än 30 sekunder*) för att få det konverterat på grund av dessa kodrader.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Som du ser**AB1000000**är en ganska längre cell i XLSX-filen. Men den*WaitForWhileAndThenInterrupt()*metoden avbryter konverteringen efter 10 sekunder och programmet avslutas/avslutas. Använd följande kod för att köra exempelkoden.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
