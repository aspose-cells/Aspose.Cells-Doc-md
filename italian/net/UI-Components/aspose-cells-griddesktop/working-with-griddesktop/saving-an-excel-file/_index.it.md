---
title: Salvataggio di un file Excel
type: docs
weight: 20
url: /it/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop, salvataggio, file
description: Questo articolo introduce come salvare un file in GridDesktop.
---

{{% alert color="primary" %}} 

Utilizzando il controllo Aspose.Cells.GridDesktop, gli utenti possono non solo creare nuovi file Excel ma gestire anche quelli esistenti. Tuttavia, in entrambi i casi, sarebbe necessario salvare i contenuti del Aspose.Cells.GridDesktop. Quindi, questo è l'argomento della nostra discussione ora per far sapere ai nostri utenti come possono salvare i loro contenuti del Grid come un file Excel.

{{% /alert %}} 
## **Introduzione**
Per salvare il contenuto del controllo Aspose.Cells.GridDesktop come file Excel, Aspose.Cells.GridDesktop fornisce i seguenti metodi.

1. **Salvataggio come file**
1. **Salvataggio come stream**
## **Salvataggio del file**
Creare un'applicazione desktop e aggiungere due pulsanti con un controllo GridControl al form. Impostare le proprietà di testo dei pulsanti rispettivamente come **Salva come file** e **Salva come stream**.
### **Salvataggio come file**
Creare l'evento di clic del pulsante **Salva come file** e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Un punto importante da discutere è che il controllo Aspose.Cells.GridDesktop contiene anche un metodo chiamato SaveToExcel, che è anche utilizzato per caricare i contenuti di un file Excel nel Grid. Tuttavia, questo metodo è ora obsoleto. Pertanto, si consiglia a tutti i programmatori di utilizzare il metodo ExportExcelFile che è più robusto ed efficiente rispetto a quello obsoleto.

{{% /alert %}} 
### **Salvataggio come flusso**
A volte, potrebbe essere richiesto dai programmatori di salvare i contenuti della griglia su uno stream (ad esempio MemoryStream). Per agevolare questo compito, il controllo Aspose.Cells.GridDesktop supporta anche il salvataggio dei dati della griglia su uno stream. Crea l'evento Click del pulsante **Salva come stream** e incolla il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel supporta fogli Excel che possono contenere al massimo 65.536 righe e 256 colonne. Anche Aspose.Cells.GridDesktop segue gli stessi standard. Nel controllo Aspose.Cells.GridDesktop, i programmatori possono creare più righe e colonne rispetto al limite standard, ma quando si salvano i dati della griglia in un file Excel, verrà generata un'eccezione. Ciò significa che solo i dati contenuti nelle 65.536 righe e 256 colonne possono essere salvati in un file Excel utilizzando Aspose.Cells.GridDesktop.

{{% /alert %}}
