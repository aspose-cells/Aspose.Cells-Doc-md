---
title: Aggiungi GridWeb a Web Form
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: Questo articolo introduce come lavorare con il modulo web in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento fornisce una guida passo passo di base per i principianti per aiutarli a creare e utilizzare il controllo Aspose.Cells.GridWeb nelle applicazioni web.

{{% /alert %}} 
## **Creazione e Utilizzo del Controllo Aspose.Cells.GridWeb**
### **Passo 1: Creazione di un Progetto di Applicazione Web**
Prima, creare un progetto di applicazione web in cui utilizzare il controllo Aspose.Cells.GridWeb:

1. Aprire Visual Studio.
1. Dal menu **File**, selezionare **Nuovo** seguito da **Progetto**. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



Compare una finestra di dialogo Nuovo progetto.

1. Selezionare il modello **Applicazione Web ASP.NET** per il linguaggio desiderato. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. Selezionare il template **Moduli Web**. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Aggiungere un nuovo modulo web al progetto.
### **Passo 2: Incorporare il Controllo nel Modulo Web**
Trascinare e rilasciare il controllo Aspose.Cells.GridWeb dalla casella degli strumenti di Visual Studio al modulo web. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

Per sapere come aggiungere i controlli Aspose.Cells Grid alla casella degli strumenti di Visual Studio, leggere [Integrare i controlli Aspose.Cells.Grid con Visual Studio.NET](/cells/it/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

Quando il controllo è stato aggiunto al modulo, viene visualizzato in questo modo: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Passo 3: Ridimensionamento del Controllo**
Il modulo viene visualizzato con una dimensione predefinita. Regolare le dimensioni trascinando i bordi o gli angoli. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Passo 4: Impostazione delle Proprietà del Controllo**
Il controllo Aspose.Cells.GridWeb può anche essere configurato utilizzando diverse proprietà. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

È possibile regolare molte proprietà del controllo con la finestra di dialogo Proprietà. Le proprietà di base includono altezza, larghezza, colore e stili visivi. Le proprietà avanzate includono la modalità di modifica, la modalità di sessione e la modalità doppio clic. Inoltre, è possibile impostare gestori di eventi personalizzati nella finestra di dialogo Proprietà.

Ci sono anche alcuni strumenti di configurazione aggiuntivi per Aspose.Cells.GridWeb che possono essere visti nella parte inferiore della finestra di dialogo Proprietà come collegamenti ipertestuali o fare clic con il pulsante destro del mouse sul controllo GridWeb per trovarli. Questi strumenti di configurazione includono:

- Pulsanti di comando personalizzati
#### **Pulsanti di comando personalizzati**
Per aprire l'editor dei pulsanti di comando personalizzati:
Fare clic con il pulsante destro del mouse sul controllo GridWeb e selezionare **Pulsanti di comando personalizzati**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



Viene visualizzata la finestra di dialogo Editor Collezione Pulsante di Comando Personalizzato. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

La finestra di dialogo consente ai programmatori di aggiungere e rimuovere pulsanti di comando personalizzati nel controllo GridWeb.


### **Importante**
Aspose.Cells.GridWeb fornisce anche i file di risorse con il controllo. La "acw_client" è una cartella (@ la tua directory di installazione) che contiene file e Aspose.Cells.GridWeb utilizza questa cartella per gestire la sua configurazione interna e altre funzionalità, ha file di script, file di immagine e altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il file di configurazione viene utilizzato per gestire le risorse client incorporate (immagini, script, ecc.). Inoltre, quando è necessario distribuire l'applicazione web con il controllo GridWeb, è necessario copiare anche la directory "acw_client" nella tua cartella del progetto altrimenti la tua applicazione web (distribuita sul server) non riuscirà a trovarla. È sempre possibile specificare la cartella delle risorse aggiungendo le seguenti righe di codice nella sezione di configurazione (ad esempio nel file web.config nel tuo progetto VS.NET):



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

Il percorso è sempre relativo alla directory del progetto. Non è necessario utilizzare alcuna directory che si trovi al di fuori della directory del progetto. Quindi è necessario copiare la directory "acw_client" (@ la tua cartella di installazione di GridWeb) nella directory/sottodirectory del progetto.

{{% /alert %}}
### **Passo 5: Eseguire l'applicazione web**
Eseguire l'applicazione premendo Ctrl+F5 o facendo clic sul pulsante **Start**. 

Quando l'applicazione viene eseguita in un browser, viene visualizzata la pagina WebForm1.aspx, ora contenente un controllo Aspose.Cells.GridWeb vuoto. Aggiungi valori alle celle facendo clic su di esse. È anche possibile eseguire altre attività come modificare l'altezza di una riga o la larghezza di una colonna, copiare (Ctrl+C) o tagliare (Ctrl+X) dati della cella negli appunti e incollare (Ctrl+V) dati nella cella. Per eseguire più operazioni, fare clic con il pulsante destro del mouse sul controllo per vedere l'elenco completo delle opzioni. 

**Menu contestuale del controllo GridWeb** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
