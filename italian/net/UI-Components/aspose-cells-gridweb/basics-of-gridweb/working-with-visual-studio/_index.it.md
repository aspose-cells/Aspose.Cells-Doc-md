---
title: Lavorare con Visual Studio
type: docs
weight: 20
url: /it/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: Questo articolo introduce come utilizzare GridWeb in visual studio.
---

{{% alert color="primary" %}} 

Questo argomento spiega come utilizzare Aspose.Cells.GridWeb nelle applicazioni ASP.NET usando Visual Studio.NET 2005. Questo argomento è utile per gli sviluppatori di livello principiante che lavorano con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Lavorare con Aspose.Cells.GridWeb Utilizzando Visual Studio 2013**
Questo argomento mostra come utilizzare Aspose.Cells.GridWeb creando un sito web di esempio in Visual Studio 2013. Il processo è stato diviso in fasi.
### **Passo 1: Creazione di un nuovo sito web**
1. Apri Visual Studio 2013.
1. Dal menu **File**, seleziona **Nuovo Menu**, quindi **Sito Web**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


Viene aperta la finestra di dialogo Nuovo sito Web. 

1. Seleziona **Sito Web ASP.NET Web Forms** dai modelli installati di Visual Studio.
1. Scegli la modalità HTTP per la posizione del sito web. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Specifica una posizione in cui verranno creati e memorizzati i file del sito web. 
   1. Fai clic su **Sfoglia** nella finestra di dialogo Nuovo sito Web. 

![todo:image_alt_text](working-with-visual-studio_3.png)



Viene visualizzata la finestra di dialogo Scegli posizione. 

1. Fai clic sulla scheda **Local IIS**.
   Vengono visualizzate tutte le cartelle e le applicazioni web memorizzate nella cartella radice di IIS (ad esempio: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Ora crea una nuova applicazione web nel tuo IIS locale dove verranno memorizzati i file del sito web.
   La finestra di dialogo Scegli posizione ti consente di creare ed eliminare applicazioni web o directory virtuali nel tuo IIS locale. Per creare un'applicazione web, fai clic su un pulsante come mostrato di seguito nella figura. 

![todo:image_alt_text](working-with-visual-studio_5.png)



Viene creata una nuova applicazione web con il nome predefinito WebSite. 

1. Rinomina l'applicazione web. L'abbiamo rinominata in GridWebOn2013.
1. Fare clic su **Apri**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Fai clic su **OK** per consentire a Visual Studio di creare un sito web. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Passo 2: Verifica delle viste di origine e design di una pagina web**
Un sito web predefinito sarà stato creato da Visual Studio 2013. Contiene una pagina web default.aspx predefinita con del testo e markup fittizi. 

**Vista origine della pagina default.aspx** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Tutte le pagine web (incluse quelle ASP.NET) possono essere aperte in due modalità. Una è la vista origine che consente ai programmatori di accedere e modificare il codice sorgente. La seconda modalità è la vista design che può essere utilizzata per progettare le pagine web in modo WYSIWYG. La schermata sopra mostra la vista origine della pagina web default.aspx. Per visualizzare la vista design, fai clic su **Design**. 

**Vista del design della pagina default.aspx** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Elimina la pagina Default.aspx aggiunta da Visual Studio e aggiungi una nuova pagina Default.aspx vuota.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Passaggio 3: Aggiunta di Aspose.Cells.GridWeb alla pagina Web**
Puoi semplicemente aggiungere il controllo Aspose.Cells.GridWeb (o GridWeb) a una pagina Web trascinandolo dalla toolbox. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Se non sai come aggiungere Aspose.Cells.GridWeb alla toolbox, fai riferimento a [Integrare i controlli della griglia Aspose.Cells con Visual Studio.NET](/cells/it/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

Una volta aggiunto il controllo GridWeb alla pagina Web, si renderizzerebbe così: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Seleziona l'intero tag. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Passaggio 5: Ridimensionamento del controllo Aspose.Cells.GridWeb**
Puoi cambiare la larghezza e l'altezza del controllo GridWeb dopo averlo trascinato sul sito Web. 

Nel design view, puoi ridimensionare la larghezza e l'altezza del GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Passaggio 6: Configurazione delle proprietà di Aspose.Cells.GridWeb**
Configura le proprietà di Aspose.Cells.GridWeb in WYSIWYG facendo clic sul pulsante **Proprietà** sul lato destro di Visual Studio 2013 IDE. 
Viene visualizzata una finestra di dialogo delle proprietà. 

![todo:image_alt_text](working-with-visual-studio_15.png)



Il riquadro delle proprietà consente di configurare l'aspetto e alcune altre proprietà per controllare il comportamento di GridWeb.
### **Passaggio 7: Esecuzione del primo sito Web contenente Aspose.Cells.GridWeb**
Compila ed esegui il sito Web. 

1. Esegui il sito Web direttamente da Visual Studio premendo Ctrl+F5 o facendo clic su **Avvia debug**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Ora puoi iniziare a giocare con il controllo GridWeb. 

**Controllo GridWeb in azione** 

![todo:image_alt_text](working-with-visual-studio_17.png)
