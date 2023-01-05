---
title: Associazione del foglio di lavoro a un oggetto raccolta personalizzato utilizzando GridWeb
type: docs
weight: 130
url: /it/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Il framework Microsoft .NET offre molte classi di raccolta ma a volte non soddisfano i requisiti di sviluppo, quindi gli sviluppatori creano**collezioni personalizzate**e potrebbe essere necessario associare tali raccolte personalizzate a Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Associare un foglio di lavoro con una raccolta personalizzata**
Per illustrare questa funzionalità, questo articolo spiega come creare un'applicazione di esempio, passo dopo passo. Innanzitutto, crea una raccolta personalizzata e quindi utilizza tale raccolta per associare con un foglio di lavoro.
### **Passaggio 1: creazione di un record personalizzato**
Prima di creare una raccolta personalizzata, creare una classe per contenere i record personalizzati che verranno archiviati nella raccolta. Lo scopo di questo articolo è dare un'idea di come creare le tue raccolte personalizzate e associarle a Aspose.Cells.GridWeb, quindi come creare il record personalizzato dipende da te.

L'esempio seguente utilizza la classe MyCustomRecord che contiene cinque campi privati e cinque proprietà pubbliche che controllano l'accesso ai campi privati. Ecco la struttura delle proprietà:

-  La proprietà StringField1 da leggere e scrivere**campostringa1** (corda).
-  La proprietà ReadonlyField2 di sola lettura**campostringa2** (corda).
-  Proprietà DateField1 da leggere e scrivere**campodata1** (Appuntamento).
-  La proprietà IntField1 da leggere e scrivere**intfield1** (numero intero).
-  La proprietà DoubleField1 da leggere e scrivere**doublefield1** (Doppio).

**C#**

{{< highlight "csharp" >}}

 //Creating a class that will act as record for the custom collection

public class MyCustomRecord

{

    //Private data members

    private string stringfield1;

    private string stringfield2 = "ABC";

    private DateTime datefield1;

    private int intfield1;

    private double doublefield1;

    //Creating a string property

    public string StringField1

    {

        get { return stringfield1; }

        set { stringfield1 = value; }

    }

    //Creating a readonly string property

    public string ReadonlyField2

    {

        get { return stringfield2; }

    }

    //Creating a DateTime property

    public DateTime DateField1

    {

        get { return datefield1; }

        set { datefield1 = value; }

    }

    //Creating an int property

    public int IntField1

    {

        get { return intfield1; }

        set { intfield1 = value; }

    }

    //Creating a double property

    public double DoubleField1

    {

        get { return doublefield1; }

        set { doublefield1 = value; }

    }

}

{{< /highlight >}}
### **Passaggio 2: creazione di una raccolta personalizzata**
Ora, crea una raccolta personalizzata a cui aggiungere i record dei clienti e da cui accedervi. Per semplificare, questo esempio utilizza la classe MyCollection che contiene un indicizzatore di sola lettura. Utilizzando questo indicizzatore, possiamo ottenere qualsiasi record personalizzato archiviato nella raccolta.

**C#**

{{< highlight "csharp" >}}

 //Creating a custom collection

public class MyCollection : CollectionBase

{

    //Leaving the collection constructor empty

    public MyCollection()

    {

    }

    //Creating a readonly property for custom collection. This Item property is used by GridWeb control to

    //determine the collection's type

    public MyCustomRecord this[int index]

    {

        get { return (MyCustomRecord)this.List[index]; }

    }

}

{{< /highlight >}}
### **Passaggio 3: associazione di un foglio di lavoro con una raccolta personalizzata**
Il processo di creazione di una raccolta personalizzata è completo. Utilizzare ora la raccolta personalizzata per associare a un foglio di lavoro in Aspose.Cells.GridWeb . Per prima cosa crea un modulo Web, aggiungi il controllo GridWeb e aggiungi del codice.

Per utilizzare la raccolta personalizzata per l'associazione, creare innanzitutto un oggetto della classe MyCollection (creata nel passaggio precedente).
Quindi creare e aggiungere oggetti MyCustomRecord all'oggetto MyCollection.

{{% alert color="primary" %}} 

Ti stai chiedendo perché non c'era un metodo nella classe MyCollection per aggiungere un oggetto MyCustomRecord alla collezione. Dai un'altra occhiata al codice sopra e noterai che la classe MyCollection è ereditata dalla classe CollectionBase (che ha implementato l'interfaccia IList che fornisce un metodo Add per aggiungere un oggetto alla collezione). Utilizzare il metodo Add della classe IList eseguendo l'upcast dell'oggetto MyCollection in IList.

{{% /alert %}} 

Infine, imposta l'oggetto MyCollection come origine dati del foglio di lavoro e associa il foglio di lavoro alla raccolta. A questo punto, puoi anche creare regole di convalida per le colonne associate del foglio di lavoro.

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

    {

        //Creating an object of custom collection

        MyCollection list = new MyCollection();

        //Creating an instance of Random class

        System.Random rand = new System.Random();

        //Creating a loop that will run 5 times

        for (int i = 0; i < 5; i++)

        {

            //Creating an object of Custom Record

            MyCustomRecord rec = new MyCustomRecord();

            //Initializing all properties of Custom Record

            rec.DateField1 = DateTime.Now;

            rec.DoubleField1 = rand.NextDouble() * 10;

            rec.IntField1 = rand.Next(20);

            rec.StringField1 = "ABC_" + i;

            //Adding Custom Record to Collection

            ((IList)list).Add(rec);

        }

        //Accessing a desired worksheet

        GridWorksheet sheet = GridWeb1.WorkSheets[0];

        //Setting the Data Source of worksheet

        sheet.DataSource = list;

        //Creating columns automatically

        sheet.CreateAutoGenratedColumns();

        //Setting the validation type of value to DateTime

        sheet.BindColumns[2].Validation.ValidationType = ValidationType.DateTime;

        //Binding worksheet

        sheet.DataBind();

        //Assigning an event handler to InitializeNewBindRow event of the worksheet

        //sheet.InitializeNewBindRow += new InitializeNewBindRowHandler(GridWeb1_InitializeNewBindRow);

    }

}

{{< /highlight >}}
### **Passaggio 4: gestione dell'evento InitializeNewBindRow del foglio di lavoro**
Nel codice precedente, potresti aver notato una riga di codice aggiuntiva utilizzata per assegnare il gestore dell'evento GridWeb1_InitializeNewBindRow all'InitializeNewBindRow del foglio di lavoro. Questo evento viene attivato ogni volta che una nuova riga associata viene aggiunta al foglio di lavoro. Abbiamo creato un gestore eventi per questo evento a causa della proprietà DateField1 dell'oggetto MyCustomRecord.

 Aspose.Cells.GridWeb si inizializza automaticamente**int** e**Doppio** valori con**zero (0)**ogni volta che una nuova riga associata viene aggiunta al controllo GridWeb. Per le date, vorremmo che il controllo GridWeb aggiungesse automaticamente la data corrente dal sistema. Per fare ciò, abbiamo creato il gestore dell'evento GridWeb1_InitializeNewBindRow per l'evento InitializeNewBindRow.

Accedere a una particolare istanza della classe MyCustomRecord da GridWeb utilizzando l'argomento bindObject e quindi assegnare la data di sistema corrente alla relativa proprietà DateField1.

**C#**

{{< highlight "csharp" >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **Passaggio 5: eseguire l'applicazione**
 Eseguire l'applicazione premendo uno dei due**Ctrl+F5** o facendo clic sul**Inizio** pulsante in VS.NET. Il modulo Web viene aperto in una nuova finestra del browser.

**Foglio di lavoro rilegato con una raccolta personalizzata** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Fare clic con il pulsante destro del mouse sul controllo GridWeb per aggiungere o eliminare un record. Ad esempio, aggiungi un nuovo record al foglio di lavoro selezionando**Aggiungi riga** opzione.

**Selezionando l'opzione Aggiungi riga dal menu** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 Quando una nuova riga viene aggiunta al foglio di lavoro, le celle contengono dati predefiniti inclusa la data di sistema corrente.

**Nuova riga aggiunta al foglio di lavoro con dati predefiniti** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Dopo aver apportato modifiche ai dati, fare clic su**Salva** o**Invia** per salvare le modifiche.

**Salvataggio delle modifiche facendo clic sul pulsante Salva** 

![cose da fare:immagine_alt_testo](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Conclusione**
{{% alert color="primary" %}} 

Questo articolo ha mostrato come associare un foglio di lavoro a una raccolta personalizzata creata. Utilizzando Aspose.Cells.GridWeb, gli sviluppatori possono associare i fogli di lavoro a un database o a raccolte personalizzate tramite Worksheets Designer in modalità GUI o tramite codifica. Ciò offre agli sviluppatori un'ampia gamma di opzioni per la creazione di applicazioni.

{{% /alert %}}
