---
title: Importa File Microsoft Excel
type: docs
weight: 40
url: /it/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb, importazione
description: Questo articolo introduce come importare file in GridWeb.
---

{{% alert color="primary" %}} 

Come Aspose.Cells.GridDesktop, il controllo Aspose.Cells.GridWeb può aprire e caricare file di Microsoft Excel - completi di dati, formattazione, grafici, immagini ecc. - ma nelle applicazioni web. Questo argomento spiega come.

{{% /alert %}} 
## **Importa File Excel**
### **Importa da File**
Per aprire un file Excel utilizzando il controllo Aspose.Cells.GridWeb:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo web.
1. Importa il file Excel specificando il percorso del file.
1. Eseguire l'applicazione.

{{% alert color="primary" %}} 

Se non sai come aggiungere il controllo a un modulo web, consulta [Aggiungi GridWeb a un Modulo Web](/cells/it/net/aspose-cells-gridweb/add-gridweb-to-web-form/).

{{% /alert %}} 

Quando il controllo Aspose.Cells.GridWeb viene aggiunto a un modulo web, il controllo viene istanziato automaticamente e aggiunto al modulo con una dimensione predefinita. Non devi creare un oggetto controllo Aspose.Cells.GridWeb, devi solo trascinare e rilasciare il controllo e iniziare a usarlo.

Tuttavia, per caricare il contenuto da un file Excel al controllo Aspose.Cells.GridWeb, devi chiamare il metodo ImportExcelFile per specificare il percorso del file Excel. Dopo di che, il controllo Aspose.Cells.GridWeb troverà automaticamente il file dal percorso specificato e ne visualizzerà i contenuti. Di seguito è fornito un frammento di codice che carica i contenuti di un file Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Il frammento di codice sopra può essere utilizzato come si desidera. Ad esempio, per caricare un file Excel automaticamente quando un modulo web si carica, aggiungi questo codice all'evento Page_Load del modulo. Se desideri aprire un file quando viene cliccato un pulsante, aggiungi un pulsante al modulo web e scrivi il codice sopra sotto l'evento Click del pulsante.

**Un file Excel viene caricato quando viene cliccato un pulsante** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Se il tuo sistema di file è NTFS, dovresti concedere l'autorizzazione di lettura agli account utente ASPNET o Everyone o otterrai un'eccezione di accesso negato durante l'esecuzione.

{{% /alert %}} 
### **Importa da Stream**
Oltre ad aprire file Excel da file, il controllo Aspose.Cells.GridWeb può caricare file Excel da uno stream. Utilizzare un file come stream è un approccio migliore per vietare qualsiasi tipo di problema di accesso o violazione della condivisione dei file perché questo approccio assicura la chiusura di tutte le connessioni ai file chiudendo lo stream.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
