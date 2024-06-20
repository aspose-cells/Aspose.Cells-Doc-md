---
title: Associazione del Foglio di Lavoro a un Oggetto di Collezione Personalizzato utilizzando GridWeb
type: docs
weight: 130
url: /it/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: Questo articolo introduce come associare un foglio di lavoro a una collezione in GridWeb. 
---

{{% alert color="primary" %}} 

Il framework Microsoft .NET offre molte classi di collezioni ma talvolta non soddisfano i requisiti di sviluppo, quindi gli sviluppatori creano **collezioni personalizzate**, e è possibile associare un foglio di lavoro a tali collezioni personalizzate in GridWeb.

{{% /alert %}} 
## **Associazione di un foglio di lavoro con una raccolta personalizzata**
Per illustrare questa funzionalità, questo articolo illustra come creare un'applicazione di esempio passo dopo passo. Prima, creare una raccolta personalizzata e poi utilizzare quella raccolta per associarla a un foglio di lavoro.
### **Passaggio 1: Creazione di un record personalizzato**
Prima di creare una raccolta personalizzata, creare una classe per contenere i record personalizzati che verranno memorizzati nella raccolta. Lo scopo di questo articolo è quello di dare un'idea su come creare le tue raccolte personalizzate e associarle a GridWeb, quindi come crei il record personalizzato dipende da te.

L'esempio di seguito utilizza la classe MyCustomRecord che contiene cinque campi privati e cinque proprietà pubbliche che controllano l'accesso ai campi privati. Ecco la struttura delle proprietà:

- La proprietà StringField1 per leggere e scrivere **stringfield1** (stringa).
- La proprietà ReadonlyField2 per leggere solo **stringfield2** (stringa).
- La proprietà DateField1 per leggere e scrivere **datefield1** (DateTime).
- La proprietà IntField1 per leggere e scrivere **intfield1** (intero).
- La proprietà DoubleField1 per leggere e scrivere **doublefield1** (double).

**C#**

{{< highlight csharp >}}

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
### **Passaggio 2: Creazione di una raccolta personalizzata**
Ora, creare una raccolta personalizzata a cui aggiungere i record dei clienti e accedervi. Per semplificare, questo esempio utilizza la classe MyCollection che contiene un indice di sola lettura. Utilizzando questo indice, possiamo ottenere qualsiasi record personalizzato memorizzato nella raccolta.

**C#**

{{< highlight csharp >}}

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
### **Passaggio 3: Associazione di un foglio di lavoro con una raccolta personalizzata**
Il processo di creazione di una raccolta personalizzata è completo. Ora utilizzare la raccolta personalizzata per associarla a un foglio di lavoro in Aspose.Cells.GridWeb. Prima creare un modulo web, aggiungere il controllo GridWeb ad esso e aggiungere del codice.

Per utilizzare la raccolta personalizzata per l'associazione, creare prima un oggetto della classe MyCollection (creato nel passaggio precedente).
Quindi creare e aggiungere gli oggetti MyCustomRecord all'oggetto MyCollection.

{{% alert color="primary" %}} 

Ti stai chiedendo perché nella classe MyCollection non c'era un metodo per aggiungere un oggetto MyCustomRecord alla raccolta. Dai un'altra occhiata al codice sopra e noterai che la classe MyCollection eredita dalla classe CollectionBase (che ha implementato l'interfaccia IList che fornisce un metodo Add per aggiungere un oggetto alla raccolta). Utilizza il metodo Add della classe IList tramite l'upcasting dell'oggetto MyCollection a IList.

{{% /alert %}} 

Infine, impostare l'oggetto MyCollection come origine dati del foglio di lavoro e associare il foglio di lavoro alla raccolta. A questo punto, è anche possibile creare regole di convalida per le colonne associate del foglio di lavoro.

**C#**

{{< highlight csharp >}}

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
### **Passaggio 4: Gestione dell'evento InitializeNewBindRow del foglio di lavoro**
Nel codice sopra, potresti aver notato una riga di codice aggiuntiva utilizzata per assegnare l'handler event GridWeb1_InitializeNewBindRow al InitializeNewBindRow del foglio di lavoro. Questo evento viene attivato ogni volta che viene aggiunta una nuova riga associata al foglio di lavoro. Abbiamo creato un gestore dell'evento per questo evento a causa della proprietà DateField1 dell'oggetto MyCustomRecord.

Aspose.Cells.GridWeb inizializza automaticamente i valori **int** e **double** con **zero (0)** ogniqualvolta viene aggiunta una nuova riga vincolata al controllo GridWeb. Per le date, vogliamo che il controllo GridWeb aggiunga automaticamente la data corrente dal sistema. A tal scopo, abbiamo creato l'handler dell'evento GridWeb1_InitializeNewBindRow per l'evento InitializeNewBindRow.

Accedi a un'istanza particolare della classe MyCustomRecord da GridWeb utilizzando l'argomento bindObject e quindi assegna la data corrente di sistema alla proprietà DateField1.

**C#**

{{< highlight csharp >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **Passo 5: Esecuzione dell'Applicazione**
Esegui l'applicazione premendo **Ctrl+F5** o facendo clic sul pulsante **Start** in VS.NET. Il modulo web viene aperto in una nuova finestra del browser. 

**Foglio di lavoro vincolato con una collezione personalizzata** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



Fai clic con il pulsante destro del mouse sul controllo GridWeb per aggiungere o eliminare un record. Ad esempio, aggiungi un nuovo record al foglio di lavoro selezionando l'opzione **Aggiungi Riga**. 

**Selezionare l'opzione Aggiungi Riga dal menu** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



Quando viene aggiunta una nuova riga al foglio di lavoro, le celle contengono dati predefiniti inclusa la data corrente di sistema. 

**Nuova riga aggiunta al foglio di lavoro con dati predefiniti** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Dopo aver apportato modifiche ai dati, fare clic su **Salva** o **Invia** per salvare le modifiche. 

**Salvataggio delle modifiche cliccando sul pulsante Salva** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Conclusioni**
{{% alert color="primary" %}} 

Questo articolo ha mostrato come vincolare un foglio di lavoro a una collezione personalizzata creata. Utilizzando Aspose.Cells.GridWeb, gli sviluppatori possono vincolare i fogli di lavoro sia a un database che a collezioni personalizzate tramite il Designer dei Fogli di Lavoro in modalità GUI o tramite codice. Questo fornisce una vasta gamma di opzioni agli sviluppatori per la creazione di applicazioni.

{{% /alert %}}
