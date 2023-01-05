---
title: Esporta file Excel Microsoft
type: docs
weight: 50
url: /it/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

È possibile creare nuovi file Excel Microsoft esistenti o manipolarli sui siti Web in modalità GUI utilizzando il controllo Aspose.Cells.GridWeb. I file possono quindi essere salvati in file Excel. Aspose.Cells.GridWeb funge efficacemente da editor di fogli di calcolo online. Questo argomento descrive come salvare il contenuto della griglia in file Excel.

{{% /alert %}} 
## **Esporta file Excel**
### **Esporta come file**
Per salvare il contenuto del controllo Aspose.Cells.GridWeb come file Excel:

1. Aggiungere il controllo Aspose.Cells.GridWeb al modulo Web.
1. Salva il tuo lavoro come file Excel in un percorso specificato.
1. Eseguire l'applicazione.

{{% alert color="primary" %}} 

 Se non sai come aggiungere il controllo Aspose.Cells.GridWeb al tuo modulo web, dovresti fare riferimento a[Aggiungere GridWeb al modulo Web](/cells/it/net/add-gridweb-to-web-form/)

{{% /alert %}} 

Quando il controllo Aspose.Cells.GridWeb viene aggiunto a un Windows Form, il controllo viene automaticamente istanziato e aggiunto al form con una dimensione predefinita. Non devi creare un oggetto di controllo Aspose.Cells.GridWeb, tutto ciò che devi fare è trascinare e rilasciare il controllo e iniziare a usarlo.

L'esempio di codice seguente illustra come salvare il contenuto della griglia in un file Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Se il tuo file system è NTFS, concedi l'accesso in lettura/scrittura agli account utente ASPNET o Everyone o otterrai un'eccezione di accesso negato in fase di esecuzione.

{{% /alert %}} 

Il suddetto frammento di codice può essere utilizzato in diversi modi. Un modo comune consiste nell'aggiungere un pulsante che salva il contenuto della griglia in un file Excel quando viene fatto clic. Aspose.Cells.GridWeb offre un approccio più semplice per l'attività. Aspose.Cells.GridWeb ha un evento chiamato SaveCommand. Il suddetto frammento di codice può essere aggiunto al gestore dell'evento dell'evento SaveCommand che consente agli utenti di salvare il proprio lavoro facendo clic su Aspose.Cells.GridWeb's in-built**Salva** pulsante.

**L'evento SaveCommand di GridWeb** 

![cose da fare:immagine_alt_testo](export-microsoft-excel-file_1.jpg)

**Salvataggio del contenuto della griglia in Excel facendo clic sul pulsante Salva integrato di GridWeb** 

![cose da fare:immagine_alt_testo](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 Se stai lavorando in Visual Studio puoi facilmente creare il gestore eventi dell'evento SaveCommand facendo doppio clic sull'evento nel**Proprietà** Pannello. Per saperne di più su questo, fare riferimento a[Utilizzo degli eventi GridWeb](/cells/it/net/working-with-gridweb-events/)

{{% /alert %}} 
### **Esporta come flusso**
È anche possibile salvare il contenuto della griglia in un flusso (ad esempio MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
