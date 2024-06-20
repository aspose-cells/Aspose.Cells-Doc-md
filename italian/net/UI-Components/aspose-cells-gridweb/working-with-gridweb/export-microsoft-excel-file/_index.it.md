---
title: Esporta file Microsoft Excel
type: docs
weight: 50
url: /it/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb, esportare
description: Questo articolo introduce come esportare file in GridWeb.
---

{{% alert color="primary" %}} 

È possibile creare nuovi, o manipolare esistenti file Microsoft Excel, su siti web in modalità GUI utilizzando il controllo Aspose.Cells.GridWeb. I file possono poi essere salvati come file Excel. Aspose.Cells.GridWeb funziona efficacemente come un editor di fogli di calcolo online. Questo argomento descrive come salvare i contenuti del foglio elettronico come file Excel.

{{% /alert %}} 
## **Esporta file Excel**
### **Esporta come file**
Per salvare il contenuto del controllo Aspose.Cells.GridWeb come file Excel:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Salva il tuo lavoro come file Excel in un percorso specificato.
1. Eseguire l'applicazione.

{{% alert color="primary" %}} 

Se non sai come aggiungere il controllo Aspose.Cells.GridWeb al tuo modulo web, dovresti fare riferimento a [Aggiungi GridWeb al modulo web](/cells/it/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

Quando il controllo Aspose.Cells.GridWeb viene aggiunto a un modulo di Windows, il controllo viene istanziato automaticamente e aggiunto al modulo con una dimensione predefinita. Non è necessario creare un oggetto controllo Aspose.Cells.GridWeb, tutto ciò che devi fare è trascinare e rilasciare il controllo e iniziare ad usarlo.

L'esempio di codice sottostante illustra come salvare i contenuti della griglia in un file Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Se il tuo sistema di file è NTFS, concedi l'accesso in lettura/scrittura agli account utente ASPNET o Everyone o otterrai un'eccezione di accesso negato durante l'esecuzione.

{{% /alert %}} 

Il frammento di codice sopra può essere usato in vari modi. Un modo comune è aggiungere un pulsante che salva il contenuto del foglio elettronico in un file Excel quando viene premuto. Aspose.Cells.GridWeb offre un approccio più semplice per questa operazione. Aspose.Cells.GridWeb ha un evento chiamato SaveCommand. Il frammento di codice sopra può essere aggiunto all'elaboratore dell'evento del SaveCommand che consente agli utenti di salvare il proprio lavoro premendo il pulsante **Salva** integrato in Aspose.Cells.GridWeb.

**Evento SaveCommand di GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Salvataggio dei contenuti del foglio elettronico in Excel premendo il pulsante Salva integrato di GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Se stai lavorando in Visual Studio, puoi facilmente creare l'elaboratore dell'evento SaveCommand facendo doppio clic sull'evento nel riquadro **Proprietà**. Per saperne di più, consulta [Working with GridWeb Events](/cells/it/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **Esporta come un flusso**
È anche possibile salvare il contenuto della griglia su un flusso (ad esempio MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
