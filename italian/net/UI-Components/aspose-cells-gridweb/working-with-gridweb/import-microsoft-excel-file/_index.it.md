---
title: Importa file Microsoft Excel
type: docs
weight: 40
url: /it/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Come Aspose.Cells.GridDesktop, il controllo Aspose.Cells.GridWeb può aprire e caricare file Microsoft Excel - completi di dati, formattazione, grafici, immagini ecc. - ma in applicazioni web. Questo argomento spiega come.

{{% /alert %}} 
## **Importa file Excel**
### **Importa da file**
Per aprire un file Excel utilizzando il controllo Aspose.Cells.GridWeb:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Importa il file Excel specificando il percorso del file.
1. Eseguire l'applicazione.

{{% alert color="primary" %}} 

 Se non sai come aggiungere il controllo a un modulo Web, fai riferimento a[Aggiungere GridWeb al modulo Web](/cells/it/net/add-gridweb-to-web-form/).

{{% /alert %}} 

Quando il controllo Aspose.Cells.GridWeb viene aggiunto a un modulo Web, il controllo viene automaticamente istanziato e aggiunto al modulo con una dimensione predefinita. Non devi creare un oggetto di controllo Aspose.Cells.GridWeb, tutto ciò che devi fare è trascinare e rilasciare il controllo e iniziare a usarlo.

Tuttavia, per caricare il contenuto da un file Excel nel controllo Aspose.Cells.GridWeb, è necessario chiamare il metodo ImportExcelFile per specificare il percorso del file Excel. Successivamente, il controllo Aspose.Cells.GridWeb troverà automaticamente il file dal percorso specificato e ne visualizzerà il contenuto. Di seguito viene fornito uno snippet di codice che carica il contenuto di un file Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Lo snippet di codice sopra può essere utilizzato come preferisci. Ad esempio, per caricare automaticamente un file Excel quando viene caricato un modulo Web, aggiungi questo codice all'evento Page_Load del modulo. Se vuoi aprire un file quando si fa clic su un pulsante, aggiungi un pulsante al modulo Web e scrivi il codice sopra riportato sotto l'evento Click del pulsante.

**Un file Excel viene caricato quando si fa clic su un pulsante** 

![cose da fare:immagine_alt_testo](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Se il file system è NTFS, è necessario concedere l'autorizzazione di accesso in lettura agli account utente ASPNET o Everyone o si otterrà un'eccezione di accesso negato in fase di esecuzione.

{{% /alert %}} 
### **Importa da Stream**
Oltre ad aprire file Excel da file, il controllo Aspose.Cells.GridWeb può caricare file Excel da un flusso. L'utilizzo di file come flusso è un approccio migliore per vietare qualsiasi tipo di accesso ai file o problemi di violazione della condivisione perché questo approccio garantisce la chiusura di tutte le connessioni ai file chiudendo il flusso.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
