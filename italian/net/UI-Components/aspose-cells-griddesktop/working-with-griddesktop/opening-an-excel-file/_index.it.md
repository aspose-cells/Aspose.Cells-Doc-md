---
title: Apertura di un file di Excel
type: docs
weight: 10
url: /it/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop,apri,file
description: Questo articolo introduce come aprire un file in GridDesktop.
---

{{% alert color="primary" %}} 

Una caratteristica unica della suite di griglie Aspose.Cells è la sua compatibilità con i file di Excel. In questo argomento, dimostreremo come gli utenti possano aprire file di Excel nelle loro applicazioni Windows utilizzando il controllo Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Introduzione**
Per aprire un file di Excel utilizzando Aspose.Cells.GridDesktop è necessario creare un'applicazione desktop con il controllo GridDesktop al suo interno. Se non sai come aggiungere il controllo Aspose.Cells.GridDesktop al tuo modulo Windows, dovresti fare riferimento a [Come usare Aspose.Cells.GridDesktop](/cells/it/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop fornisce tre diversi modi per aprire un file di Excel.

1. **Apertura da un file**
1. **Apertura di un file CSV**
1. **Apertura da un flusso**
## **Apertura file Excel**
In questo esempio, creare un'applicazione desktop e eseguire le seguenti operazioni.

- Aggiungi un controllo GridControl al modulo.
- Aggiungi tre pulsanti con le loro proprietà di testo impostate come segue:
  - **Apri file di Excel**
  - **Apri file CSV**
  - **Apri da un flusso**
### **Apertura da un file**
Per caricare il contenuto da un file Excel nel controllo Aspose.Cells.GridDesktop, sarà necessario chiamare un metodo del controllo per specificare il percorso del file Excel. Dopo di che, il controllo Aspose.Cells.GridDesktop troverà automaticamente il file dal percorso specificato e ne visualizzerà i contenuti. Il frammento di codice per caricare i contenuti di un file Excel è fornito nel seguente esempio. Creare l'evento di clic del pulsante **Apri file Excel** e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Il frammento di codice sopra può essere utilizzato dai programmatori in qualsiasi modo desiderino. Ad esempio, se si desidera caricare automaticamente un file Excel quando un form di Windows si avvia, è possibile aggiungere questo codice nell'evento di caricamento del form.
### **Apertura di un file CSV**
Il controllo Aspose.Cells.GridDesktop supporta anche il caricamento di file CSV. Creare l'evento di clic del pulsante **Apri file CSV** e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Apertura da uno stream**
Nella nostra precedente discussione, abbiamo parlato del caricamento di un file Excel utilizzando il suo percorso ma il controllo Aspose.Cells.GridDesktop supporta anche il caricamento di file Excel da uno stream. Creare l'evento di clic del pulsante **Apri da Stream** e incollare il seguente codice al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Utilizzare un file come stream è un approccio migliore per evitare problemi di accesso o condivisione del file in quanto questo approccio garantisce la chiusura di tutte le connessioni ai file chiudendo lo stream.

{{% alert color="primary" %}} 

IMPORTANTE: Un punto importante da discutere è che il controllo Aspose.Cells.GridDesktop contiene anche un metodo chiamato LoadFromExcel, che è anche utilizzato per caricare i contenuti di un file Excel nel Grid. Tuttavia, questo metodo è ora obsoleto. Pertanto, si consiglia a tutti i programmatori di utilizzare il metodo ImportExcelFile che è più robusto ed efficiente rispetto a quello obsoleto.

{{% /alert %}}
