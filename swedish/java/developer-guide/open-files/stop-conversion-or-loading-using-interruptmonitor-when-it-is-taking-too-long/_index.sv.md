---
title: Stoppa konvertering eller inläsning med avbrottsövervakning när det tar för lång tid
type: docs
weight: 100
url: /sv/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig stoppa omvandlingen av arbetsboken till olika format som PDF, HTML osv. med hjälp av [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)-objektet när det tar för lång tid. Omvandlingsprocessen är ofta både CPU- och minnesintensiv och det är ofta användbart att avbryta den när resurser är begränsade. Du kan använda [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) både för att stoppa omvandlingen och för att stoppa laddningen av stora arbetsböcker. Använd [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)-egenskapen för att stoppa omvandlingen och [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)-egenskapen för att ladda stora arbetsböcker.

## **Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid**

Följande exempelkod förklarar användningen av [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)-objektet. Koden konverterar en ganska stor Excelfil till PDF. Det kommer att ta flera sekunder (dvs. *mer än 30 sekunder*) att konvertera den på grund av dessa kodrader.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Som du ser är **AB1000000** ganska långt bort i XLSX-filen. Dock avbryter *WaitForWhileAndThenInterrupt()*-metoden omvandlingen efter 10 sekunder och programmet avslutas/avslutas. Använd följande kod för att köra exempelkoden.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
