---
title: Aggiungere GridWeb al modulo Web
type: docs
weight: 10
url: /it/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

Questo argomento fornisce una guida dettagliata di base per i principianti per aiutarli a creare e utilizzare il controllo Aspose.Cells.GridWeb nelle applicazioni Web.

{{% /alert %}} 
## **Creazione e utilizzo di Aspose.Cells.GridWeb Control**
### **Passaggio 1: creazione di un progetto di applicazione Web**
Creare innanzitutto un progetto di applicazione Web in cui utilizzare il controllo Aspose.Cells.GridWeb:

1. Apri VisualStudio.
1.  Dal**File** menù, selezionare**Nuovo** seguito da**Progetto**. 

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_1.png)



Viene visualizzata una finestra di dialogo Nuovo progetto.

1.  Selezionare**ASP.NET Applicazione web** per la lingua desiderata.

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_2.png)

1.  Selezionare**Moduli web** modello.

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_3.png)

1. Aggiungi un nuovo modulo Web al progetto.
### **Passaggio 2: incorporare il controllo nel modulo Web**
 Trascinare e rilasciare il controllo Aspose.Cells.GridWeb dalla casella degli strumenti di Visual Studio al modulo Web.

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 Per informazioni su come aggiungere i controlli griglia Aspose.Cells alla casella degli strumenti di Visual Studio, leggere[Integra i controlli Aspose.Cells.Grid con Visual Studio.NET](/cells/it/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

 Quando il controllo è stato aggiunto al form, viene visualizzato in questo modo:

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_5.png)
### **Passaggio 3: ridimensionamento del controllo**
Il modulo viene visualizzato con una dimensione predefinita. Regola le dimensioni trascinando i bordi o gli angoli.

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_6.png)
### **Passaggio 4: impostazione delle proprietà del controllo**
 Aspose.Cells.Il controllo GridWeb può anche essere configurato utilizzando varie proprietà.

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_7.png)

È possibile regolare molte proprietà del controllo con la finestra di dialogo Proprietà. Le proprietà di base includono altezza, larghezza, colore e stili visivi. Le proprietà avanzate includono la modalità di modifica, la modalità sessione e la modalità doppio clic. Inoltre, è possibile impostare gestori di eventi personalizzati nella finestra di dialogo Proprietà.

Ci sono anche alcuni strumenti di configurazione extra per Aspose.Cells.GridWeb che possono essere visualizzati nella parte inferiore della finestra di dialogo Proprietà come collegamenti ipertestuali o fare clic con il pulsante destro del mouse sul controllo GridWeb per trovarli. Questi strumenti di configurazione includono:

- Pulsanti di comando personalizzati
#### **Pulsanti di comando personalizzati**
Per aprire l'editor dei pulsanti di comando personalizzati:
 Fare clic con il pulsante destro del mouse sul controllo GridWeb e selezionare**Pulsanti di comando personalizzati**. 

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_8.png)



 Viene visualizzata la finestra di dialogo Editor raccolta CustomCommandButton.

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_9.png)

La finestra di dialogo consente agli sviluppatori di aggiungere e rimuovere pulsanti di comando personalizzati nel controllo GridWeb.


### **Importante**
Aspose.Cells.GridWeb fornisce anche i suoi file di risorse con il controllo. Il "acw_client" è una cartella (@ la tua directory di installazione) che contiene file e Aspose.Cells.GridWeb usa questa cartella per gestire la sua configurazione interna e altre funzionalità, ha file di script, file immagine e altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il config viene utilizzato per gestire le risorse client incorporate (immagini, script, ecc.) Inoltre, quando è necessario distribuire l'applicazione Web con controllo GridWeb, è necessario copiare anche il file "acw_client" nella cartella del progetto almeno la tua applicazione web (distribuita sul server) non è riuscita a trovarla. Puoi sempre specificare la cartella delle risorse aggiungendo le seguenti righe di codice nella sezione di configurazione (ad esempio nel file web.config nel tuo Progetto VS.NET):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

Il percorso è sempre correlato alla directory del progetto. Non dovresti usare alcuna directory che sia al di fuori della directory del progetto. Quindi è necessario copiare la directory "acw_client" (@ la cartella di installazione di GridWeb) nella directory/sottodirectory del progetto.

{{% /alert %}}
### **Passaggio 5: esecuzione dell'applicazione Web**
 Eseguire l'applicazione premendo Ctrl+F5 o facendo clic su**Inizio** pulsante.

 Quando l'applicazione viene eseguita in un browser, viene visualizzata la pagina WebForm1.aspx, che ora contiene un controllo Aspose.Cells.GridWeb vuoto. Aggiungi valori alle celle facendo clic su di essi. È anche possibile eseguire altre attività come modificare l'altezza di una riga o la larghezza di una colonna, copiare (Ctrl+C) o tagliare (Ctrl+X) i dati della cella negli appunti e incollare (Ctrl+V) i dati nella cella . Per eseguire più operazioni, fare clic con il pulsante destro del mouse sul controllo per visualizzare l'elenco completo delle opzioni.

**Menu contestuale del controllo GridWeb** 

![cose da fare:immagine_alt_testo](add-gridweb-to-web-form_10.png)
