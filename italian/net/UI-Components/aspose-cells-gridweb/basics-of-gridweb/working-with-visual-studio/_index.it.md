---
title: Lavorare con Visual Studio
type: docs
weight: 20
url: /it/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

Questo argomento spiega come usare Aspose.Cells.GridWeb nelle applicazioni ASP.NET usando Visual Studio.NET 2005. Questo argomento è utile per gli sviluppatori di livello principiante che lavorano con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Utilizzo di Aspose.Cells.GridWeb utilizzando Visual Studio 2013**
Questo argomento illustra come usare Aspose.Cells.GridWeb creando un sito Web di esempio in Visual Studio 2013. Il processo è stato suddiviso in passaggi.
### **Passaggio 1: creazione di un nuovo sito Web**
1. Apri Visual Studio 2013.
1.  Dal**File** menù, selezionare**Nuovo Menù** , poi**Sito web**. 

![cose da fare:immagine_alt_testo](working-with-visual-studio_1.png)


 Viene aperta la finestra di dialogo Nuovo sito Web.

1.  Selezionare**Sito di moduli Web ASP.NET** dai modelli installati di Visual Studio.
1.  Scegli la modalità HTTP per la posizione del sito web.

![cose da fare:immagine_alt_testo](working-with-visual-studio_2.png)




1.  Specificare una posizione in cui verranno creati e archiviati i file del sito Web.
 1. Fare clic**Navigare** nella finestra di dialogo Nuovo sito Web.

![cose da fare:immagine_alt_testo](working-with-visual-studio_3.png)



 Viene visualizzata la finestra di dialogo Scegli posizione.

1.  Clicca il**IIS locale** scheda.
 Vengono visualizzate tutte le cartelle e le applicazioni Web memorizzate nella cartella principale di IIS (ad esempio: C:\Inetpub\wwwroot).

![cose da fare:immagine_alt_testo](working-with-visual-studio_4.png)




1. Ora crea una nuova applicazione Web nel tuo IIS locale in cui verranno archiviati i file del sito Web.
 La finestra di dialogo Scegli posizione consente di creare ed eliminare applicazioni Web o directory virtuali nell'IIS locale. Per creare un'applicazione Web, fare clic su un pulsante come mostrato di seguito nella figura.

![cose da fare:immagine_alt_testo](working-with-visual-studio_5.png)



 Viene creata una nuova applicazione Web con il nome predefinito WebSite.

1. Rinomina l'applicazione web. L'abbiamo rinominato GridWebOn2013.
1.  Clic**Aprire**. 

![cose da fare:immagine_alt_testo](working-with-visual-studio_6.png)



 Si torna alla finestra di dialogo Nuovo sito Web. Il percorso della posizione del sito Web è impostato su<http://localhost/GridWebOn2013>. 

1.  Clic**OK** per consentire a Visual Studio di creare un sito Web.

![cose da fare:immagine_alt_testo](working-with-visual-studio_7.png)
### **Passaggio 2: controllo delle visualizzazioni di origine e progettazione di una pagina Web**
 Un sito Web predefinito sarà stato creato da Visual Studio 2013. Contiene una pagina Web default.aspx con testo fittizio e markup.

**Vista di origine della pagina default.aspx** 

![cose da fare:immagine_alt_testo](working-with-visual-studio_8.png)



Tutte le pagine Web (incluso ASP.NET) possono essere aperte in due modalità. Uno è la visualizzazione del codice sorgente che consente agli sviluppatori di accedere e modificare il codice sorgente. La seconda modalità è la visualizzazione del design che può essere utilizzata per progettare pagine Web in modo WYSIWYG. Lo screenshot sopra mostra una vista sorgente della pagina Web default.aspx. Per visualizzare la vista struttura, fare clic su**Disegno**. 

**Visualizzazione struttura della pagina default.aspx** 

![cose da fare:immagine_alt_testo](working-with-visual-studio_9.png)




Eliminare la pagina Default.aspx aggiunta da Visual Studio e aggiungere una nuova pagina Default.aspx vuota.

![cose da fare:immagine_alt_testo](working-with-visual-studio_10.png)
### **Passaggio 3: aggiunta di Aspose.Cells.GridWeb alla pagina Web**
 Puoi semplicemente aggiungere il controllo Aspose.Cells.GridWeb (o GridWeb) a una pagina Web trascinandolo dalla casella degli strumenti.

![cose da fare:immagine_alt_testo](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Se non sai come aggiungere Aspose.Cells.GridWeb alla casella degli strumenti, fai riferimento a[Integra i controlli griglia Aspose.Cells con Visual Studio.NET](/cells/it/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 Una volta che il controllo GridWeb viene rilasciato nella pagina Web, verrà visualizzato in questo modo:

![cose da fare:immagine_alt_testo](working-with-visual-studio_12.png)



### **Passaggio 4: modificare il tag <!DOCTYPE>**
1.  Passa alla visualizzazione sorgente e trova quanto segue**<!DOCTYPE>** tag nel codice sorgente:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  Seleziona il tag completo.

![cose da fare:immagine_alt_testo](working-with-visual-studio_13.png)




1.  Conservare, modificare o eliminare il<!DOCTYPE>etichetta.
1.  Oppure modificare il file<!DOCTYPE> contrassegnare con il seguente:

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Passaggio 5: ridimensionamento di Aspose.Cells.GridWeb Control**
 È possibile modificare la larghezza e l'altezza del controllo GridWeb dopo averlo trascinato nel sito Web.

 Nella visualizzazione struttura è possibile ridimensionare la larghezza e l'altezza di GridWeb.

![cose da fare:immagine_alt_testo](working-with-visual-studio_14.png)



### **Passaggio 6: configurazione delle proprietà di Aspose.Cells.GridWeb**
 Configurare le proprietà Aspose.Cells.GridWeb in WYSIWYG facendo clic su**Proprietà** pulsante sul lato destro dell'IDE di Visual Studio 2013.
 Viene visualizzata una finestra di dialogo Proprietà.

![cose da fare:immagine_alt_testo](working-with-visual-studio_15.png)



Il riquadro Proprietà consente di configurare l'aspetto di GridWeb e alcune altre proprietà per controllare il comportamento di GridWeb.
### **Passaggio 7: eseguire il primo sito Web contenente Aspose.Cells.GridWeb**
 Costruisci ed esegui il sito web.

1.  Eseguire il sito Web direttamente da Visual Studio premendo Ctrl+F5 o facendo clic**Avvia il debug**. 

![cose da fare:immagine_alt_testo](working-with-visual-studio_16.png)

 Ora puoi iniziare a giocare con il controllo GridWeb.

**Controllo GridWeb in azione** 

![cose da fare:immagine_alt_testo](working-with-visual-studio_17.png)
