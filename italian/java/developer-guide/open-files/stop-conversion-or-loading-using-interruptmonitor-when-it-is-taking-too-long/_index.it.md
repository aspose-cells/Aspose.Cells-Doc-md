---
title: Interrompi la conversione o il caricamento utilizzando InterruptMonitor quando impiega troppo tempo
type: docs
weight: 100
url: /it/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Possibili scenari di utilizzo**

Aspose.Cells consente di interrompere la conversione della cartella di lavoro in vari formati come PDF, HTML, ecc. utilizzando il[**Monitor di interruzione**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)oggetto quando ci vuole troppo tempo. Il processo di conversione è spesso intensivo sia per la CPU che per la memoria ed è spesso utile interromperlo quando le risorse sono limitate. Puoi usare[**Monitor di interruzione**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)sia per interrompere la conversione che per interrompere il caricamento di un'enorme cartella di lavoro. Si prega di utilizzare[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)proprietà per interrompere la conversione e[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)proprietà per il caricamento di una cartella di lavoro enorme.

## **Interrompi la conversione o il caricamento utilizzando InterruptMonitor quando impiega troppo tempo**

Il seguente codice di esempio spiega l'utilizzo di[**Monitor di interruzione**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)oggetto. Il codice converte un file Excel piuttosto grande in PDF. Ci vorranno diversi secondi (es*più di 30 secondi*) per convertirlo a causa di queste righe di codice.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Come vedi**AB1000000**è piuttosto una cella più lontana nel file XLSX. in ogni caso, il*WaitForWhileAndThenInterrupt()*Il metodo interrompe la conversione dopo 10 secondi e il programma termina/termina. Utilizzare il codice seguente per eseguire il codice di esempio.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
