---
title: Associazione del foglio di lavoro a un set di dati utilizzando GridWebs Worksheets Designer
type: docs
weight: 20
url: /it/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 Questo articolo illustra un approccio semplice per associare i fogli di lavoro alle tabelle del database in modalità GUI utilizzando uno strumento speciale fornito con Aspose.Cells.GridWeb, la finestra di progettazione dei fogli di lavoro.

{{% /alert %}} 
## **Associare un foglio di lavoro al database utilizzando Worksheets Designer**
	**Passaggio 1: creazione di un database di esempio**
1. Innanzitutto, creiamo il database di esempio che verrà utilizzato in questo articolo. Stiamo usando Microsoft Access per creare un database che contiene una tabella chiamata Prodotti. Il suo schema è mostrato di seguito.
   **Informazioni di progettazione della tabella Prodotti** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Alcuni record fittizi vengono aggiunti alla tabella Prodotti.
   **Record nella tabella Prodotti** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Passaggio 2: progettazione dell'applicazione di esempio**
 Un'applicazione Web ASP.NET viene creata e progettata in Visual Studio.NET come illustrato di seguito.
**Applicazione di esempio progettata** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Passaggio 3: connessione al database tramite Esplora server**
 È ora di connettersi al database. Possiamo farlo facilmente utilizzando il Server Explorer in Visual Studio.NET.

1.  Selezionare**Connessione dati** in**Esplora server** e fare clic con il pulsante destro del mouse.
1.  Selezionare**Aggiungi connessione** dal menù.
   **Selezionando l'opzione Aggiungi connessione** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 Viene visualizzata la finestra di dialogo Proprietà collegamento dati.
**La finestra di dialogo Proprietà collegamento dati** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 Usando questa finestra di dialogo, puoi connetterti a qualsiasi database. Per impostazione predefinita, consente di connettersi a un database SQL Server. Per questo esempio, dobbiamo connetterci con un database di Microsoft Access.

1.  Clicca il**Fornitore** scheda.
1.  Selezionare**Provider Microsoft Jet 4.0 OLE DB** dal**Provider OLE DB** elenco.
1.  Clic**Prossimo**.
   **Facendo clic su Avanti dopo aver selezionato un provider OLE DB** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 Il**Connessione** si apre la scheda.

1.  Selezionare il file del database di Microsoft Access (nel nostro caso, db.mdb) e fare clic**OK**.
   **Facendo clic sul pulsante OK dopo aver selezionato il file di database** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 Dopo aver cliccato**OK** , verrà creata una connessione di database al database di Microsoft Access nel file**Esplora server**Fare doppio clic sulla connessione per visualizzare tutte le tabelle, le viste e le procedure memorizzate nel database.

{{% /alert %}} 
### **Passaggio 4: creazione grafica di oggetti di connessione al database**
1.  Sfoglia le tabelle nel database utilizzando il file**Esplora server**.
 C'è solo una tabella, Prodotti.
1.  Trascina e rilascia la tabella Prodotti dal file**Esplora server** al**Modulo web**.
   **Trascinando la tabella Prodotti da Esplora server e rilasciandola nel modulo web** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Potrebbe apparire una finestra di dialogo.
**Finestra di dialogo per confermare l'inclusione della password del database nella stringa di connessione** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Decidi se vuoi includere o meno una password del database nella stringa di connessione. Per questo esempio, abbiamo selezionato**Non includere la password**. 
Sono stati creati e aggiunti due oggetti di connessione al database (oleDbConnection1 e oleDbDataAdapter1).
**Oggetti di connessione al database (oleDbConnection1 e oleDbDataAdapter1) creati e visualizzati** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Passaggio 5: generazione del set di dati**
Finora, abbiamo creato oggetti di connessione al database, ma abbiamo ancora bisogno di un posto dove archiviare i dati dopo la connessione al database. Un oggetto DataSet può memorizzare i dati con precisione e possiamo anche generarli facilmente utilizzando VS.NET IDE.

1.  Selezionare**oleDbDataAdaper1** e fare clic con il pulsante destro del mouse.
1.  Selezionare**Genera set di dati** opzione dal menu.
   **Selezionando l'opzione Genera set di dati** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 Viene visualizzata la finestra di dialogo Genera set di dati.
 Qui è possibile selezionare un nome per il nuovo oggetto DataSet da creare e quali tabelle aggiungervi.

1.  Seleziona il**Aggiungi questo set di dati a designer** opzione.
1.  Clic**OK**.
   **Facendo clic sul pulsante OK per generare DataSet** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Un oggetto dataSet11 viene aggiunto alla finestra di progettazione.
**DataSet generato e aggiunto alla finestra di progettazione** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Passaggio 6: utilizzo di Designer di fogli di lavoro**
 Ora è il momento di aprire il segreto.

1. Selezionare il controllo GridWeb e fare clic con il pulsante destro del mouse.
1.  Selezionare**Progettista di fogli di lavoro** opzione dal menu.

   **Selezione dell'opzione Designer fogli di lavoro** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 Viene visualizzato l'Editor della raccolta di fogli di lavoro (chiamato anche Progettazione fogli di lavoro).
**Finestra di dialogo Editor raccolta fogli di lavoro** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



La finestra di dialogo contiene diverse proprietà che possono essere configurate per associare Sheet1 a qualsiasi tabella nel database.

1.  Seleziona il**Fonte di dati** proprietà.
L'oggetto dataSet11 generato nel passaggio precedente è elencato nel menu.
1. Seleziona DataSet11.
1.  Clicca il**DataMember** proprietà.
 Worksheets Designer mostra automaticamente un elenco di tabelle in dataSet11. C'è solo una tabella, Prodotti.
1. Seleziona la tabella Prodotti.
   **Impostazione delle proprietà DataSource e DataMember** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  Controlla il**Associa colonne** proprietà.
   **Facendo clic sulla proprietà BindColumns** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 Facendo clic sul**Associa colonne** La proprietà apre l'editor della raccolta BindColumn.
**L'editor della raccolta BindColumn** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 Nell'editor della raccolta BindColumn, tutte le colonne del file**Prodotti** table vengono aggiunte automaticamente alla raccolta BindColumns.

1. Seleziona qualsiasi colonna e personalizza le sue proprietà.
 Ad esempio, puoi modificare ogni didascalia di colonna.
   **Modifica della colonna Caption of ProductID** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  Dopo aver apportato le modifiche, fare clic su**OK**.
1.  Chiudere tutte le finestre di dialogo facendo clic**OK**.
 Infine, si torna alla pagina WebForm1.aspx.
   **Ritorno alla pagina WebForm1.aspx dopo aver utilizzato Progettazione fogli di lavoro** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Sopra, viene mostrato il nome della colonna della tabella Prodotti. La larghezza delle colonne è piccola, quindi i nomi completi di alcune colonne non sono completamente visibili.
### **Passaggio 7: aggiunta di codice al gestore dell'evento Page_Load**
 Abbiamo utilizzato Worksheets Designer e ora dobbiamo solo aggiungere il codice al gestore dell'evento Page_Load per riempire l'oggetto dataSet11 con i dati del database (utilizzando oleDbDataAdapter1) e associare il controllo GridWeb a dataSet11 chiamando il relativo metodo DataBind.

1.  Aggiungi il codice:

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

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

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

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

1. Controlla il codice aggiunto al gestore dell'evento Page_Load.
   **Codice aggiunto al gestore dell'evento Page_Load** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Passaggio 8: eseguire l'applicazione**
 Compilare ed eseguire l'applicazione: premere**Ctrl+F5** o clicca**Inizio**. 
**Esecuzione dell'applicazione** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Dopo la compilazione, la pagina WebForm1.aspx viene aperta in una finestra del browser con tutti i dati caricati dal database.
**Dati caricati nel controllo GridWeb dal database** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Utilizzo del controllo GridWeb**
Quando i dati vengono caricati nel controllo GridWeb, fornisce agli utenti il controllo sui dati. GridWeb offre diversi tipi di funzionalità di manipolazione dei dati.
### **Convalida dei dati**
Aspose.Cells.GridWeb crea automaticamente regole di convalida appropriate per tutte le colonne associate in base ai tipi di dati definiti nel database. Visualizza il tipo di convalida di una cella passando il cursore su di essa.
**Verifica del tipo di convalida di una cella** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Qui, la cella selezionata contiene il file**<INT>** convalida, il che significa che gli utenti possono inserire solo valori interi in esso. Se immettono un altro valore, si verifica un errore di convalida. Inoltre,**<OBBLIGATORIO>** mostra che deve essere inviato il valore Product ID.
### **Eliminazione di righe**
 Per eliminare una riga, seleziona una riga (o qualsiasi cella nella riga), fai clic con il pulsante destro del mouse e seleziona**Elimina riga**.
**Selezionando l'opzione Elimina riga dal menu** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


La riga verrebbe eliminata all'istante.
**Dati della griglia (dopo l'eliminazione di una riga)** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Modifica righe**
 Modificare i dati in celle o righe e quindi fare clic**Salva** o**Invia**per salvare le modifiche.
### **Aggiunta di righe**
1.  Per aggiungere una riga, fai clic con il pulsante destro del mouse su una cella e seleziona**Aggiungi riga**.
   **Selezionando l'opzione Aggiungi riga dal menu** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Una nuova riga viene aggiunta al foglio alla fine delle altre righe.
**Nuova riga aggiunta a Grid** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 A sinistra della nuova riga c'è un asterisco{{< emoticons/cross >}} , a indicare che la riga è nuova.

1. Aggiungi valori alla nuova riga.
1.  Clic**Salva** o**Invia** per confermare la modifica.
   **Salvataggio delle modifiche ai dati facendo clic su *Salva** pulsante*

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Impostazione del formato del numero**
 Al momento, i prezzi in**Prezzo del prodotto** colonna vengono visualizzati come valori numerici. È possibile farli sembrare valuta.

1. Ritorna a Visual Studio.NET.
1. Apri l'editor della raccolta BindColumn.
 Il**NumeroTipo** proprietà del**Prezzo del prodotto** colonna è impostata su**Generale**.
   **La proprietà NumberType impostata su Generale** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Clic**Menu `A tendina** e seleziona**Valuta4** dalla lista.
   **La proprietà NumberType è stata modificata in Currency4** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Eseguire nuovamente l'applicazione.
 I valori in**Prezzo del prodotto** colonna è ora valuta.
   **Prezzi dei prodotti in valuta Formato numerico** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Modifica dei dati**
L'applicazione finora consente solo ai suoi utenti di visualizzare i dati della tabella. Gli utenti possono modificare i dati nel controllo GridWeb ma, chiudendo il browser e aprendo il database, non è cambiato nulla. Le modifiche apportate non vengono salvate nel database.

 L'esempio seguente aggiunge codice all'applicazione in modo che GridWeb possa salvare le modifiche apportate al database.

1.  Apri il**Proprietà** riquadro e selezionare l'evento SaveCommand del controllo GridWeb dall'elenco.
   **Selezione dell'evento SaveCommand di GridWeb** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  Fare doppio clic su**SalvaComando** event e VS.NET crea il gestore dell'evento GridWeb1_SaveCommand.
1.  Aggiungere codice a questo gestore eventi che aggiornerà il database con tutti i dati modificati nel DataSet associato al foglio di lavoro utilizzando oleDbDataAdapter1.

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

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

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

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

Puoi anche controllare il codice aggiunto al gestore dell'evento GridWeb1_SaveCommand
**Codice aggiunto al gestore dell'evento GridWeb1_SaveCommand** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 Salva le modifiche al database utilizzando il file**Salva** pulsante ora li salva definitivamente.
## **Conclusione**
{{% alert color="primary" %}} 

Il data binding è una caratteristica importante di Aspose.Cells.GridWeb. È facile associare fogli di lavoro a un database utilizzando l'utilità Worksheets Designer offerta da Aspose.Cells.GridWeb. Aspose.Cells.GridWeb consente di risparmiare tempo e fatica durante la creazione di potenti soluzioni Grid.

{{% /alert %}}
