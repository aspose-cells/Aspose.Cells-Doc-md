---
title: Associare un foglio di lavoro al database utilizzando Worksheets Designer in VS.Net 2005
type: docs
weight: 40
url: /it/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 Questo articolo discute un approccio più semplice per associare fogli di lavoro con tabelle di database**Visual Studio.Net 2005** utilizzando uno strumento speciale fornito con Aspose.Cells.GridWeb denominato as**Progettista di fogli di lavoro** . Questo articolo ti farebbe sicuramente sentire quanto sia più facile utilizzare la funzione di associazione dei dati in Aspose.Cells.GridWeb con l'aiuto di**Progettista di fogli di lavoro** .

{{% /alert %}}

## **Associare un foglio di lavoro al database utilizzando Worksheets Designer in VS.Net 2005**

 Lo scopo di questo articolo è consentire a tutti gli sviluppatori di apprendere come creare un'applicazione di data binding in**VS.Net 2005** e comprendere l'uso e il ruolo di**Progettista di fogli di lavoro** editore. Il modo migliore per imparare e capire qualsiasi cosa è attraverso esempi. Quindi, in questo articolo, sarebbe anche meglio per noi creare un'applicazione di esempio per dimostrare l'uso di**Progettista di fogli di lavoro**in fogli di lavoro vincolanti con database. Creiamo un'applicazione passo dopo passo.

### **Passaggio 1: creazione di un database di esempio**

 Prima di tutto creeremo un database di esempio che verrà utilizzato in questo articolo. Abbiamo utilizzato MS Access per creare un database di esempio contenente**Prodotti** tabella il cui schema è riportato di seguito:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**Figura:** Informazioni di progettazione di**Prodotti** tavolo

 Alcuni record fittizi vengono aggiunti al file**Prodotti** tabella come mostrato di seguito nella figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**Figura:** Registra in**Prodotti** tavolo

### **Passaggio 2: progettazione dell'applicazione di esempio**

 Un**ASP.NET Applicazione web** è creato e progettato in Visual Studio.NET 2005 come mostrato nelle figure seguenti. Queste schermate sono utili per quegli sviluppatori che non hanno molta familiarità con l'utilizzo di Aspose.Cells.GridWeb in Visual Studio.Net 2005.

Primo avvio VS.Net 2005.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**Figura:** Avvio di VS.Net 2005

Crea un nuovo sito Web dal menu File|Nuovo|Sito Web....

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**Figura:** Creazione di un nuovo sito web

 Dopo aver fatto clic sull'opzione di menu File|Nuovo|Sito Web...,**Nuovo sito web** viene visualizzata la finestra di dialogo. Clicca il**Navigare** pulsante al suo interno.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**Figura:**Finestra di dialogo Nuovo sito Web

 Dopo aver cliccato sul**Navigare** pulsante, scegliere la cartella di posizione nell'IIS locale. È possibile creare una nuova cartella e renderla come cartella virtuale come mostrato nella figura.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**Figura:** Creazione di una nuova cartella


 Dopo aver cliccato sul**Aprire** pulsante nel**Scegli Posizione** dialogo,**Nuovo sito web** sarà simile alla finestra di dialogo.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**Figura:** Impostazione della posizione del progetto

Ora il progetto è creato

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**Figura:** Progetto creato

### **Modalità XHTML e HTML**

**Aspose.Cells.GridWeb** supporta completamente la modalità XHTML che è implementata per impostazione predefinita in VS.Net 2005 dal**Modalità Xhtml** proprietà del**GrigliaWeb** il controllo è impostato su**Vero** per impostazione predefinita quando si posiziona il controllo sulla pagina Web. Ma se vuoi implementare la modalità HTML per il controllo in VS.Net 2005, puoi farlo abbastanza facilmente. Devi modificare il**<!DOCTYPE>** tagga un po' nel codice sorgente della pagina web e imposta il file**Modalità Xhtml** proprietà del**GrigliaWeb** controllo a**Falso** .

#### **In questo argomento utilizzeremo la modalità HTML per il controllo. Quindi segui i passaggi seguenti**

##### **1. Passare alla vista Sorgente della pagina web e trovare il seguente tag <!DOCTYPE> nel codice sorgente.**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

Una volta trovato quel tag, seleziona quel tag completo nel codice sorgente come mostrato di seguito.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**Figura:** Selezione**tag <!DOCTYPE>**

 Sostituisci il**<!DOCTYPE>** tag dal tuo codice sorgente con il seguente.

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**Figura:** Modifica**tag <!DOCTYPE>**

##### **2. Dopo aver aggiunto il controllo GridWeb al modulo web. È necessario selezionare il controllo e scegliere la proprietà XhtmlMode dalla finestra Proprietà per impostarla su False.**

**Aggiunta di GridWeb al WebForm** 

 Fare clic con il tasto destro su**Cassetta degli attrezzi** e seleziona**Scegli gli articoli...** dal menù.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**Figura:** Scelta degli articoli

 Ora seleziona**GrigliaWeb** componente e fare clic**OK**

{{% alert color="primary" %}}

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**Figura:** Selezione**GrigliaWeb** componente nella finestra di dialogo del componente

 Ora il**GrigliaWeb** viene aggiunto come mostrato nella figura sottostante.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**Figura:** **GrigliaWeb** viene aggiunto nella casella degli strumenti

 Posiziona il**GrigliaWeb** sul modulo web come mostrato di seguito.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**Figura:** Posizionamento**GrigliaWeb** sulla pagina web

{{% /alert %}} {{% alert color="primary" %}}

**Procedura** : Seleziona il controllo, Ora, scegli il**Modalità Xhtml** proprietà dal**Proprietà** finestra e impostarlo su**Falso** valore.

{{% /alert %}}

##### **Passaggio 3: connessione al database tramite Esplora server e impostazione dell'oggetto di connessione**

 Per prima cosa aggiungiamo il database MS Access al progetto che abbiamo precedentemente creato**Passo 1** . Potresti vederlo**db.mdb** il file viene aggiunto al progetto.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**Figura:** Database aggiunto alla cartella del progetto

 Ora, andiamo a**Progettista di componenti** finestra del modulo Web utilizzando l'opzione del menu di scelta rapida della pagina Web.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**Figura:** Selezione**Visualizza Progettazione componenti** opzione

La finestra Component Designer è mostrata come sotto.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**Figura:** Finestra Progettazione componenti

 Fare doppio clic su**Connessione OleDb** componente dal pannello Dati per posizionare l'oggetto oleDbConnection1 nella finestra.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**Figura:** oggetto oleDbConnection1

 Ora è il momento di connettersi con il database. Possiamo farlo facilmente usando**Esplora server** in Visual Studio.NET 2005. Basta selezionare**Connessione dati** in**Esplora server** e clic destro. Vedrai apparire un menu contestuale davanti a te. Selezionare**Aggiungi connessione...**opzione dal menu come mostrato di seguito nella figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**Figura:** Selezione**Aggiungi connessione...** opzione dal menu


 Dopo aver selezionato**Aggiungi connessione...** opzione dal menu,**Aggiungi connessione** si aprirà la finestra di dialogo e**Navigare** per selezionare il file del database come mostrato di seguito.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**Figura:** Selezione del file di database

Puoi testare la connessione.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**Figura:** Testare la connessione

Puoi sfogliare la connessione per controllare la tabella e i suoi campi.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**Figura:** Controllo della tabella e dei relativi campi della connessione

 Ora se selezioni**oleDbConnection1** oggetto nel**Progettista di componenti** è possibile selezionare la stringa di connessione relativa alla connessione esistente appena creata, è presente nella proprietà "ConnectionString" del**oleDbConnection1** oggetto nella finestra Proprietà.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**Figura:** Selezione della stringa di connessione per l'oggetto

 Infine il modificatore dell'oggetto viene cambiato in**Protetto** per una migliore accessibilità.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**Figura:** Impostazione del modificatore dell'oggetto

##### **Passaggio 4: configurazione dell'oggetto adattatore dati**

 Ora, aggiungi un**OleDbDataAdapter** componente dal pannello Dati nella casella degli strumenti per configurarlo. Fare doppio clic su**OleDbDataAdapter** nel pannello Dati del toolbox, avvierà la sua procedura guidata di configurazione e selezionerà la connessione esistente come mostrato in figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**Figura:** Procedura guidata di configurazione dell'adattatore dati

 Dopo aver cliccato**Prossimo** pulsante, fare clic sul**Costruttore di query** per aggiungere il**Prodotti** tabella, selezionare Tutte le colonne e fare clic**OK** pulsante.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**Figura:** Aggiunta della tabella dei prodotti

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**Figura:** Costruttore di query

 Ora fai clic**Fine** pulsante per terminare la procedura guidata.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**Figura:** Finire la procedura guidata

 Dopo aver configurato la procedura guidata, oleDbDataAdapter1 viene aggiunto automaticamente alla finestra come mostrato di seguito. Inoltre, puoi impostare il suo modificatore su**Protetto**.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**Figura:** Recupero dell'oggetto OleDbDataAdapter nella finestra di progettazione

##### **Passaggio 5: generazione del set di dati**

 Poiché abbiamo creato la connessione al database e gli oggetti dell'adattatore dati, abbiamo ancora bisogno di qualcosa in cui possiamo archiviare i dati dopo la connessione al database. UN**Set di dati**oggetto può memorizzare i dati con precisione e possiamo anche generarli facilmente utilizzando VS.NET 2005 IDE. Per farlo, seleziona**oleDbDataAdaper1** e clic destro. Verrà visualizzato un menu contestuale con alcune opzioni. Selezionare**creare** **Set di dati...** opzione dal menu come mostrato sotto nella figura.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**Figura:** Selezione**creare** **Set di dati...** opzione dal menu

 Dopo aver selezionato**creare** **Set di dati...** opzione dal menu, a**Genera set di dati** si aprirà la finestra di dialogo. Usando questa finestra di dialogo, possiamo selezionare quale sarebbe il nome del nuovo**Set di dati** oggetto da creare e a quali tabelle aggiungere**Set di dati** . Dai un'occhiata**Aggiungi questo set di dati a designer** opzione e fare clic**OK** pulsante come mostrato sotto nella figura.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**Figura:** Cliccando**OK** pulsante per generare**Set di dati**

 Ora puoi vedere a**dataSet11** oggetto aggiunto al designer come mostrato di seguito nella figura. Imposta il modificatore oggetto su**Protetto**.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**Figura:** **Set di dati** generato e aggiunto alla finestra del designer

Determinato codice viene generato automaticamente nella connessione correlata al file .cs, nell'adattatore dati, nell'oggetto set di dati.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**Figura:** Codice generato

##### **Passaggio 6: utilizzo di Designer di fogli di lavoro**

 Ora è il momento di aprire il segreto. Selezionare il controllo e fare clic con il tasto destro. Si aprirà un menu contestuale. Selezionare l'opzione Worksheets Designer... dal menu come mostrato di seguito nella figura.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**Figura:** Selezione**Progettista di fogli di lavoro...** opzione dal menu

 Dopo di che**Editor della raccolta di fogli di lavoro** dialogo (chiamato anche**Progettista di fogli di lavoro** ) verrà aperto, puoi vedere diverse proprietà che possono essere configurate per associare il file**Foglio1** con qualsiasi tabella nel database. Selezioniamo**Fonte di dati** proprietà. Scrivere**dataSet11** in esso (che abbiamo generato e aggiunto alla finestra del designer nel passaggio precedente). Quindi fare clic su**DataMember** proprietà. Scrivere**Prodotti** come nome di tabella qui come mostrato di seguito nella figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**Figura:** Ambientazione**Fonte di dati** e**DataMember** proprietà

 Ora puoi configurare**Associa colonne** proprietà. Dopo aver fatto clic su di esso, ora puoi aggiungere le colonne di rilegatura e impostare il file**Didascalia** , **Campo dati** (Dovrebbe essere uguale a**Prodotti** campi tabella) e altre proprietà. Puoi impostare il**È creato automaticamente** a**VERO** e applicare**Convalida** e impostare il**NumeroTipo**di diversi campi per le vostre esigenze.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**Figura:** Cliccando**Associa colonne** proprietà

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**Figura:** **Editor della raccolta BindColumn** dialogo

##### **Passaggio 7: aggiunta di alcune righe di codice per la pagina Web**

 Abbiamo usato**Progettista di fogli di lavoro** facilmente e ora non ci resta che aggiungere alcune righe di codice

 Per prima cosa aggiungeremo**OnInit** codice relativo all'evento da inizializzare**InizializzaComponente** metodo per inizializzare e creare oggetti connessione, comando, dataadapter e set di dati. Queste righe di codice non vengono aggiunte con il codice generato automaticamente, quindi dobbiamo aggiungerle manualmente.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**Figura:** Aggiunta di codice1

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**Figura:** Aggiunta di codice2

 Ora aggiungiamo del codice nel file**Pagina_Carica** gestore di eventi per il riempimento**dataSet11** oggetto con dati dal database (utilizzando**oleDbDataAdapter1** ) e vincolante**GrigliaWeb** controllare con**dataSet11** chiamando il suo**DataBind** metodo.

{{% alert color="primary" %}}   {{% /alert %}}

##### **Esempio:**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing Page_Load event handler

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub

{{< /highlight >}}

 Puoi anche controllare il codice aggiunto a**Pagina_Carica** gestore di eventi come mostrato di seguito nella figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**Figura:** Codice aggiunto a**Pagina_Carica** gestore di eventi

Di gran lunga, abbiamo creato un'applicazione di database molto utile. Ma questa applicazione ti consente solo di visualizzare i dati della tabella. Sebbene sia possibile modificare i dati in**GrigliaWeb** controllo ma quando chiuderai la finestra del browser e aprirai il tuo database. Scoprirai che non è cambiato nulla. Significa che le modifiche apportate non vengono salvate nel database. Quindi, c'è qualcosa che devi fare.

 Ora aggiungeremo del codice alla nostra applicazione in modo che**GrigliaWeb** può salvare le sue modifiche al database effettivo. Apriamo**Proprietà** riquadro e selezionare**SalvaComando** evento del**GrigliaWeb** controllo dall'elenco dei relativi eventi. Se fai doppio clic su**SalvaComando** evento quindi VS.NET 2005 IDE creerà**GridWeb1_SaveCommand** gestore di eventi per te. Aggiungi del codice a questo gestore di eventi per l'aggiornamento del database con i dati modificati contenuti in**Set di dati** (legato con il foglio di lavoro) utilizzando**oleDbDataAdapter1**.

##### **Esempio:**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub

{{< /highlight >}}

 Puoi anche controllare il codice aggiunto a**GridWeb1_SaveCommand** gestore di eventi come mostrato di seguito nella figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**Figura:** Codice aggiunto a**GridWeb1_SaveCommand** gestore di eventi

 Ora, se salverai le modifiche al database utilizzando**Salva** pulsante del**GrigliaWeb** , sarebbero sicuramente salvati.

##### **Passaggio 8: eseguire l'applicazione**

 Infine, possiamo compilare ed eseguire la nostra applicazione premendo entrambi**Ctrl+F5** o facendo clic**Inizio** pulsante. Nella finestra di dialogo di debug, è possibile specificare l'opzione di debug appropriata e fare clic**OK** pulsante come mostrato sotto nella figura.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**Figura:** Applicazione in esecuzione

 Dopo la compilazione,**Predefinito.aspx** pagina della nostra applicazione web verrà aperta in una nuova finestra del browser in cui possiamo vedere tutti i dati caricati dal database come mostrato di seguito:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**Figura:** Dati caricati in**GrigliaWeb** controllo dal database

 Quando i dati vengono caricati in**GrigliaWeb** control allora sentiresti che Aspose.Cells.GridWeb fornisce un controllo implicito dei dati ai suoi utenti. Controlliamo che tipo di funzionalità di manipolazione dei dati sono offerte da**GrigliaWeb** ai suoi utenti.

##### **Convalida dei dati**

Aspose.Cells.GridWeb crea automaticamente regole di convalida appropriate per tutte le colonne associate in base ai tipi di dati definiti nel database. Puoi vedere il tipo di convalida di una cella passando il puntatore del mouse su di essa come mostrato di seguito nella figura:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**Figura:**Verifica del tipo di convalida di una cella

 Nella figura sopra, possiamo vedere che la cella selezionata contiene**\<INT>** tipo di convalida, il che significa che gli utenti possono inserire solo un valore intero, altrimenti si verificherà un errore di convalida. Inoltre,**\<OBBLIGATORIO>** mostra che il valore di**numero identificativo del prodotto** deve essere inviato dall'utente.

##### **Eliminazione di righe**

 Per eliminare una riga, devi prima selezionare una riga (o qualsiasi cella della riga) e selezionare**Elimina riga** opzione dal menu di scelta rapida come mostrato di seguito:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**Figura:** Selezione**Elimina riga** opzione dal menu

 Dopo aver selezionato**Elimina riga** dal menu, la riga viene eliminata dal file**GrigliaWeb** . Ora fai clic**Salva** pulsante del**GrigliaWeb** per eliminare quel record nella tabella del database originale.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**Figura:** Dati della griglia (dopo l'eliminazione di una riga)

##### **Modifica righe**

 Puoi anche modificare i dati in celle o righe e quindi fare clic**Salva** pulsante per salvare le modifiche.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**Figura:** Dati griglia (Editing Record1)

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**Figura:** Dati griglia (Editing Record2)

##### **Aggiunta di righe**

 Per aggiungere una riga, seleziona**Aggiungi riga** opzione dal menu di scelta rapida come mostrato di seguito:

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**Figura:** Selezione**Aggiungi riga** opzione dal menu

Una nuova riga verrà aggiunta al foglio alla fine delle righe dopo la selezione**Aggiungi riga** opzione dal menu. A sinistra della riga appena aggiunta, noterai un**asterisco** segno, che indica che la riga è stata aggiunta di recente.

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**Figura:** Nuova riga aggiunta a Grid

 Dopo aver inserito i valori nella nuova riga, fare clic su**Salva** pulsante per confermare le modifiche nella tabella del database originale come mostrato di seguito

![cose da fare:immagine_alt_testo](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**Figura:** Salvataggio delle modifiche alla tabella del database facendo clic**Salva** pulsante

{{% alert color="primary" %}}   {{% /alert %}}

##### **Conclusione**

{{% alert color="primary" %}}

**Associazione dati** è una caratteristica importante di Aspose.Cells.GridWeb . È davvero facile per gli sviluppatori associare i propri fogli di lavoro al database utilizzando**Progettista di fogli di lavoro** utilità offerta da Aspose.Cells.GridWeb . Aspose.Cells.GridWeb è molto utile per gli sviluppatori per risparmiare tempo e sforzi nella creazione di potenti soluzioni Grid.

{{% /alert %}}
