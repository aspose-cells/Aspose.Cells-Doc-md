---
title: Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando ci vuole troppo tempo
type: docs
weight: 100
url: /it/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di interrompere la conversione del Workbook in vari formati come PDF, HTML ecc. utilizzando l'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) quando richiede troppo tempo. Il processo di conversione è spesso intensivo sia per la CPU che per la memoria ed è utile interromperlo quando le risorse sono limitate. Puoi usare [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) sia per interrompere la conversione che per impedire il caricamento di un ampio workbook. Usa la proprietà [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) per interrompere la conversione e la proprietà [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) per il caricamento di un ampio workbook.

## **Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo**

Il seguente codice di esempio illustra l'uso dell'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor). Il codice converte un file Excel abbastanza grande in PDF. Ci vorranno diversi secondi (più di 30 secondi) per completare la conversione a causa di queste righe di codice.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Come si può vedere **J1000000** è una cella piuttosto lontana nel file XLSX. Tuttavia, il metodo **WaitForWhileAndThenInterrupt()** interrompe la conversione dopo 10 secondi e il programma termina. Utilizzare il seguente codice per eseguire il codice di esempio.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
