---
title: Salvataggio di un file Excel
type: docs
weight: 20
url: /it/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Utilizzando il controllo Aspose.Cells.GridDesktop, gli utenti non possono solo creare nuovi file Excel, ma anche gestire quelli esistenti. Ma, in entrambi i casi, sarebbe necessario salvare il contenuto del Aspose.Cells.GridDesktop. Quindi, questo è l'argomento della nostra discussione ora per far sapere ai nostri utenti come possono salvare i loro contenuti Grid come file Excel.

{{% /alert %}} 
## **introduzione**
Per salvare il contenuto del controllo Aspose.Cells.GridDesktop come file Excel, Aspose.Cells.GridDesktop fornisce i seguenti metodi.

1. **Salvataggio come file**
1. **Salvataggio come flusso**
## **Salvataggio file**
 Creare un'applicazione desktop e aggiungere al form due pulsanti con un controllo GridControl. Imposta le proprietà del testo dei pulsanti come**Salva come file** e**Salva come flusso** rispettivamente.
### **Salvataggio come file**
 Crea l'evento Click di**Salva come file** pulsante e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: un punto importante da discutere è che il controllo Aspose.Cells.GridDesktop contiene anche un metodo denominato SaveToExcel , utilizzato anche per caricare il contenuto di un file Excel nella griglia. Ma questo metodo è ormai obsoleto. Pertanto, si consiglia a tutti gli sviluppatori di utilizzare il metodo ExportExcelFile che è più robusto ed efficiente di quello obsoleto.

{{% /alert %}} 
### **Salvataggio come flusso**
 A volte, potrebbe essere richiesto dagli sviluppatori di salvare i propri contenuti Grid in un flusso (ad esempio, MemoryStream). Per facilitare questa attività, il controllo Aspose.Cells.GridDesktop supporta anche il salvataggio dei dati Grid in un flusso. Crea l'evento Click di**Salva come flusso** pulsante e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel supporta i fogli Excel che possono contenere 65.536 righe e 256 colonne al massimo. Anche Aspose.Cells.GridDesktop segue gli stessi standard. Nel controllo Aspose.Cells.GridDesktop, gli sviluppatori possono creare più righe e colonne rispetto al limite standard, ma quando si salvano i dati della griglia in un file Excel, verrà generata un'eccezione. Significa che solo i dati contenuti nelle 65.536 righe e 256 colonne possono essere salvati in un file Excel utilizzando Aspose.Cells.GridDesktop.

{{% /alert %}}
