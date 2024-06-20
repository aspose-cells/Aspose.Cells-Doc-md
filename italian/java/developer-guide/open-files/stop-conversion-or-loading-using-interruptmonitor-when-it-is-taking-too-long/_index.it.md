---
title: Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando ci vuole troppo tempo
type: docs
weight: 100
url: /it/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di interrompere la conversione di un foglio di lavoro in vari formati come PDF, HTML, ecc. utilizzando l'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) quando ci vuole troppo tempo. Il processo di conversione è spesso intensivo in termini di CPU e memoria ed è utile interromperlo quando le risorse sono limitate. Puoi utilizzare [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) sia per interrompere la conversione che per interrompere il caricamento di un foglio di lavoro enorme. Utilizza la proprietà [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) per interrompere la conversione e la proprietà [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) per caricare un foglio di lavoro enorme.

## **Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo**

Il seguente codice di esempio spiega l'uso dell'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor). Il codice converte un file Excel piuttosto grande in PDF. Ci vorranno diversi secondi (cioè *più di 30 secondi*) per convertirlo a causa di queste righe di codice.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Come puoi vedere **AB1000000** è una cella piuttosto lontana nel file XLSX. Tuttavia, il metodo *WaitForWhileAndThenInterrupt()* interrompe la conversione dopo 10 secondi e il programma termina. Utilizza il codice seguente per eseguire il codice di esempio.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
