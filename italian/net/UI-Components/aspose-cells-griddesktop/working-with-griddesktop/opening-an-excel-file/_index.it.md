---
title: Apertura di un file Excel
type: docs
weight: 10
url: /it/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Una caratteristica unica di Aspose.Cells Grid Suite è la sua compatibilità con i file Excel. In questo argomento, dimostreremo come gli utenti possono aprire i file Excel nelle loro applicazioni Windows utilizzando il controllo Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **introduzione**
 Per aprire un file Excel utilizzando Aspose.Cells.GridDesktop devi creare un'applicazione desktop con GridDesktop Control al suo interno. Se non sai come aggiungere il controllo Aspose.Cells.GridDesktop al tuo Windows Form, dovresti fare riferimento a[Come usare Aspose.Cells.GridDesktop](/cells/it/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop offre tre modi diversi per aprire un file Excel.

1. **Apertura da un file**
1. **Apertura di un file CSV**
1. **Apertura da un flusso**
## **Apertura del file Excel**
In questo esempio creare un'applicazione desktop e procedere come segue.

- Aggiungere un controllo GridControl al form.
- Aggiungi tre pulsanti con le proprietà del testo impostate come segue:
  - **Apri File Excel**
  - **Apri il file CSV**
  - **Apri da Stream**
### **Apertura da un file**
 Per caricare il contenuto da un file Excel nel controllo Aspose.Cells.GridDesktop, sarà necessario chiamare un metodo del controllo per specificare il percorso del file Excel. Successivamente, il controllo Aspose.Cells.GridDesktop troverà automaticamente il file dal percorso specificato e ne visualizzerà il contenuto. Il frammento di codice per caricare il contenuto di un file Excel è fornito nell'esempio seguente. Crea l'evento Click di**Apri File Excel** pulsante e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Il suddetto frammento di codice può essere utilizzato dagli sviluppatori in qualsiasi modo desiderino. Ad esempio, se vuoi caricare automaticamente un file Excel quando viene caricato un Windows Form, puoi aggiungere questo codice sotto l'evento Load del tuo Form.
### **Apertura di un file CSV**
Aspose.Cells. Il controllo GridDesktop supporta anche il caricamento del file CSV. Crea l'evento Click di**Apri il file CSV** pulsante e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Apertura da un flusso**
 Nella nostra discussione precedente, abbiamo discusso del caricamento di un file Excel utilizzando il relativo percorso file, ma il controllo Aspose.Cells.GridDesktop supporta anche il caricamento di file Excel da un flusso. Crea l'evento Click di**Apri da Stream** pulsante e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



L'utilizzo di file come flusso è un approccio migliore per vietare qualsiasi tipo di accesso ai file o problemi di violazione della condivisione perché questo approccio garantisce la chiusura di tutte le connessioni ai file chiudendo il flusso.

{{% alert color="primary" %}} 

IMPORTANTE: un punto importante da discutere è che il controllo Aspose.Cells.GridDesktop contiene anche un metodo denominato LoadFromExcel, utilizzato anche per caricare il contenuto di un file Excel nella griglia. Ma questo metodo è ormai obsoleto. Pertanto, si consiglia a tutti gli sviluppatori di utilizzare il metodo ImportExcelFile che è più robusto ed efficiente di quello obsoleto.

{{% /alert %}}
