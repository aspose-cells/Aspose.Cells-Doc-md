---
title: Collegare un foglio di lavoro a un set di dati utilizzando il designer dei fogli di lavoro di GridWeb
type: docs
weight: 20
url: /it/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: Questo articolo introduce come utilizzare il designer dei fogli di lavoro per collegare un foglio di lavoro a un set di dati in GridWeb.
---

{{% alert color="primary" %}} 

Questo articolo discute un approccio semplice per collegare i fogli di lavoro alle tabelle del database in modalità GUI utilizzando uno strumento speciale fornito con Aspose.Cells.GridWeb, il designer dei fogli di lavoro. 

{{% /alert %}} 
## **Collegamento di un foglio di lavoro con il database utilizzando il designer dei fogli di lavoro**
	**Passo 1: Creare un Database di Esempio**
1. Per prima cosa, creiamo il database di esempio che verrà utilizzato in questo articolo. Utilizziamo Microsoft Access per creare un database che contiene una tabella chiamata Prodotti. Il suo schema è mostrato di seguito.
   **Informazioni di progettazione della tabella Prodotti** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Vengono aggiunti alcuni record di esempio alla tabella Prodotti.
   **Record nella tabella Prodotti** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Passo 2: Progettazione dell'Applicazione di Esempio**
Viene creata e progettata un'applicazione web ASP.NET in Visual Studio.NET come mostrato di seguito. 
**Applicazione di esempio progettata** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Passo 3: Connettersi al Database Usando Server Explorer**
È ora di connettersi al database. Possiamo farlo facilmente utilizzando il Server Explorer in Visual Studio.NET. 

1. Seleziona **Connessione Dati** in **Server Explorer** e fai clic con il pulsante destro del mouse.
1. Seleziona **Aggiungi Connessione** dal menu.
   **Selezione dell'opzione Aggiungi Connessione** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



Viene visualizzata la finestra di dialogo Proprietà del collegamento dati. 
**La finestra di dialogo Proprietà del collegamento dati** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



Utilizzando questa finestra di dialogo, è possibile connettersi a qualsiasi database. Per impostazione predefinita, consente di connettersi a un database SQL Server. Per questo esempio, è necessario connettersi a un database Microsoft Access. 

1. Fare clic sulla scheda **Provider**.
1. Selezionare **Microsoft Jet 4.0 OLE DB Provider** dall'elenco **Provider OLE DB**.
1. Fare clic su **Avanti**.
   **Fare clic su Avanti dopo aver selezionato un provider OLE DB** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


La pagina della scheda **Connessione** è aperta. 

1. Seleziona il file del database Microsoft Access (nel nostro caso, db.mdb) e fai clic su **OK**.
   **Cliccando sul pulsante OK dopo aver selezionato il file del database** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

Dopo aver cliccato su **OK**, verrà creata una connessione al database Microsoft Access nell'**Esplora server**. Fai doppio clic sulla connessione per vedere tutte le tabelle, le viste e le stored procedure nel database.

{{% /alert %}} 
### **Passo 4: Creazione di oggetti di connessione al database in modo grafico**
1. Sfoglia le tabelle nel database utilizzando l'**Esplora server**.
   C'è solo una tabella, Products. 
1. Trascina e rilascia la tabella Products dall'**Esplora server** al **Modulo Web**.
   **Trascinando la tabella Products dall'Esplora server e rilasciandola nel modulo Web** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Potrebbe comparire una finestra di dialogo.
**Finestra di dialogo per confermare l'inclusione della password del database nella stringa di connessione** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Decidi se vuoi includere una password del database nella stringa di connessione o no. Per questo esempio, abbiamo selezionato **Non includere la password**. 
Sono stati creati e aggiunti due oggetti di connessione al database (oleDbConnection1 e oleDbDataAdapter1).
**Oggetti di connessione al database (oleDbConnection1 e oleDbDataAdapter1) creati e visualizzati** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Passo 5: Generazione DataSet**
Finora abbiamo creato gli oggetti di connessione al database ma abbiamo ancora bisogno di un posto dove memorizzare i dati dopo la connessione al database. Un oggetto DataSet può memorizzare i dati in modo preciso e possiamo anche generarli facilmente usando l'IDE di VS.NET. 

1. Seleziona **oleDbDataAdaper1** e fai clic destro.
1. Seleziona l'opzione **Genera DataSet** dal menu.
   **Selezionare l'opzione Genera DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



Viene visualizzata la finestra di dialogo Genera DataSet. 
Qui è possibile selezionare un nome per il nuovo oggetto DataSet da creare e quali tabelle aggiungervi. 

1. Seleziona l'opzione **Aggiungi questo dataset al designer**.
1. Fai clic su **OK**.
   **Cliccando il pulsante OK per generare il DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Un oggetto dataSet11 viene aggiunto al designer.
**DataSet generato e aggiunto al designer** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Passo 6: Utilizzo di Worksheets Designer**
Ora è arrivato il momento di aprire il segreto. 

1. Seleziona il controllo GridWeb e fai clic con il tasto destro.
1. Seleziona l'opzione **Worksheets Designer** dal menu. 

   **Selezione dell'opzione Worksheets Designer** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



Viene visualizzato l'Editor della Raccolta dei Fogli di Lavoro (detto anche il Worksheets Designer). 
**Finestra di dialogo dell'Editor della Raccolta dei Fogli di Lavoro** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



La finestra di dialogo contiene diverse proprietà che possono essere configurate per collegare Sheet1 a qualsiasi tabella nel database.

1. Seleziona la proprietà **DataSource**.
   L'oggetto dataSet11 generato nel passaggio precedente è elencato nel menu. 
1. Seleziona dataSet11.
1. Fai clic sulla proprietà **DataMember**.
   Il Worksheets Designer mostra automaticamente un elenco di tabelle in dataSet11. C'è solo una tabella, Products.
1. Seleziona la tabella Products.
   **Impostazione delle proprietà DataSource e DataMember** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. Verificare la proprietà **BindColumns**.
   **Clicca sulla proprietà BindColumns** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



Cliccando sulla proprietà **BindColumns** si apre il BindColumn Collection Editor.
**Il BindColumn Collection Editor** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



Nel BindColumn Collection Editor, tutte le colonne della tabella **Products** vengono automaticamente aggiunte alla collezione BindColumns. 

1. Selezionare una qualsiasi colonna e personalizzarne le proprietà.
   Ad esempio, è possibile modificare la didascalia di ciascuna colonna.
   **Modifica della didascalia della colonna ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. Dopo aver apportato le modifiche, fare clic su **OK**.
1. Chiudere tutte le finestre di dialogo facendo clic su **OK**.
   Infine, ti verrà restituita la pagina WebForm1.aspx. 
   **Ritorno alla pagina WebForm1.aspx dopo aver usato il Worksheets Designer** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Sopra viene mostrato il nome della colonna della tabella Products. La larghezza delle colonne è ridotta, quindi i nomi completi di alcune colonne non sono completamente visibili. 
### **Passo 7: Aggiunta del codice all'event handler Page_Load**
Abbiamo utilizzato il Worksheets Designer e ora dobbiamo solo aggiungere il codice all'event handler Page_Load per riempire l'oggetto dataSet11 con i dati dal database (utilizzando oleDbDataAdapter1) e collegare il controllo GridWeb a dataSet11 chiamando il suo metodo DataBind. 

1. Aggiungere il codice: 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

1. Verificare il codice aggiunto all'event handler Page_Load.
   **Codice aggiunto all'event handler Page_Load** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Passaggio 8: Esecuzione dell'applicazione**
Compilare ed eseguire l'applicazione: premere **Ctrl+F5** o fare clic su **Start**. 
**Esecuzione dell'applicazione** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Dopo la compilazione, la pagina WebForm1.aspx viene aperta in una finestra del browser con tutti i dati caricati dal database.
**Dati caricati nel controllo GridWeb dal database** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Lavorare con il controllo GridWeb**
Quando i dati vengono caricati nel controllo GridWeb, fornisce agli utenti il controllo sui dati. Il GridWeb offre un certo numero di diverse funzionalità di manipolazione dei dati. 
### **Convalida Dati**
Aspose.Cells.GridWeb crea automaticamente regole di convalida appropriate per tutte le colonne associate in base ai tipi di dati definiti nel database. Vedere il tipo di convalida di una cella passando il cursore sopra di essa.
**Verifica del tipo di convalida di una cella** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Eliminazione delle righe**
Per eliminare una riga, selezionare una riga (o qualsiasi cella nella riga), fare clic con il pulsante destro del mouse e selezionare **Elimina riga**.
**Selezione dell'opzione Elimina riga dal menu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


La riga verrebbe eliminata istantaneamente.
**Dati della griglia (dopo l'eliminazione di una riga)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Modifica delle righe**
Modificare i dati nelle celle o nelle righe e quindi fare clic su **Salva** o **Invia** per salvare le modifiche. 
### **Aggiunta di righe**
1. Per aggiungere una riga, fare clic con il pulsante destro del mouse su una cella e selezionare **Aggiungi riga**.
   **Selezione dell'opzione Aggiungi riga dal menu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Viene aggiunta una nuova riga al foglio alla fine delle altre righe.
**Nuova riga aggiunta a Grid** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Aggiungi valori alla nuova riga.
1. Fare clic su **Salva** o **Invia** per confermare la modifica.
   **Salvataggio delle modifiche ai dati cliccando il pulsante *Salva*** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Impostazione del formato numero**
Al momento, i prezzi nella colonna **Prezzo Prodotto** sono mostrati come valori numerici. È possibile farli apparire come valuta.

1. Torna a Visual Studio.NET.
1. Apri l'Editor della Raccolta BindColumn.
   La proprietà **NumberType** della colonna **Prezzo Prodotto** è impostata su **Generale**.
   **La proprietà NumberType impostata su Generale** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. Fare clic su **DropDownList** e selezionare **Valuta4** dalla lista.
   **La proprietà NumberType modificata in Valuta4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Eseguire nuovamente l'applicazione.
   I valori nella colonna **Prezzo Prodotto** sono ora in valuta.
   **Prezzi dei prodotti in formato Numero di valuta** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Modifica dei dati**
Finora l'applicazione consente solo ai suoi utenti di visualizzare i dati della tabella. Gli utenti possono modificare i dati nel controllo GridWeb ma, quando si chiude il browser e si apre il database, nulla è cambiato. Le modifiche apportate non vengono salvate nel database. 

Nell'esempio seguente viene aggiunto del codice all'applicazione in modo che GridWeb possa salvare le modifiche nel database. 

1. Apri il riquadro delle **Proprietà** e seleziona l'evento SaveCommand del controllo GridWeb dall'elenco.
   **Selezione dell'evento SaveCommand di GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. Fare doppio clic sull'evento **SaveCommand** e VS.NET crea l'handler dell'evento GridWeb1_SaveCommand.
1. Aggiungi del codice a questo gestore dell'evento che aggiornerà il database con eventuali dati modificati nel DataSet vincolato al foglio di lavoro utilizzando oleDbDataAdapter1. 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

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

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

È inoltre possibile verificare il codice aggiunto al gestore dell'evento GridWeb1_SaveCommand
**Codice aggiunto al gestore dell'evento GridWeb1_SaveCommand** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Salvare le modifiche al database utilizzando il pulsante **Salva** ora le salva definitivamente.
## **Conclusioni**
{{% alert color="primary" %}} 

Il data binding è una caratteristica importante di Aspose.Cells.GridWeb. È facile vincolare i fogli di lavoro a un database utilizzando l'utility Worksheets Designer offerta da Aspose.Cells.GridWeb. Aspose.Cells.GridWeb risparmia tempo e sforzi nella creazione di potenti soluzioni di griglia. 

{{% /alert %}}
