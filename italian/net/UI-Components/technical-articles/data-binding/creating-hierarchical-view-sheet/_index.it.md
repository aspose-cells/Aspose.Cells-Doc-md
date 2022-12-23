---
title: Creazione di un foglio di visualizzazione gerarchico
type: docs
weight: 30
url: /it/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 L'associazione dati è una funzionalità GridWeb potente e intuitiva. I dati archiviati nelle tabelle del database vengono recuperati in un DataSet e riempiti con i dati

 che rappresentano le tabelle di dati. Utilizzando la funzione di associazione dati, è possibile creare una vista gerarchica (una vista master-figlio) di dati interconnessi e

 visualizzarlo nel controllo per renderlo più elegante.

 Questo argomento illustra la creazione di un foglio di visualizzazione gerarchico. Alcune delle righe nel foglio hanno visualizzazioni figlio. Quando un utente fa clic sulla riga**Espandere**

 pulsante{{< emoticons/cross >}} , la tabella di visualizzazione figlio di tale riga viene espansa verso il basso. Questa funzione è molto utile per la creazione di un rapporto di visualizzazione gerarchico.

**Una tabella con una vista gerarchica** 

![cose da fare:immagine_alt_testo](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Creare relazioni per DataTable**
Ad esempio, utilizzi ADO.Net API ed estrai i dati dalle tabelle del database. Per creare un foglio di visualizzazione gerarchico, è necessario progettare un DataSet

 oggetto basato su alcune tabelle e creare prima una relazione tra di esse. Usa i VS.NET**Progettazione set di dati** per creare la relazione. In

 In questo esempio sono presenti tre DataTable: Customers, Orders, Order Details. Il foglio mostra tutte le informazioni del cliente per impostazione predefinita. quando

 l'utente espande un cliente, la griglia mostra tutti gli ordini che il cliente ha effettuato. Quando l'utente espande un ordine, la griglia mostra i dettagli

di quell'ordine. I dati sono gerarchici: i dettagli dell'ordine sono elencati sotto gli ordini e gli ordini sono elencati sotto i clienti.

Affinché ciò funzioni, è necessario stabilire le seguenti relazioni tra le tabelle di dati:

1.  Crea una chiave esterna su DataTable Orders, il campo chiave è CustomerID

![cose da fare:immagine_alt_testo](creating-hierarchical-view-sheet_2.png)




1. Crea una chiave esterna su DataTable Order Details, il campo chiave è OrderID.

![cose da fare:immagine_alt_testo](creating-hierarchical-view-sheet_3.png)



 Il DataSet Designer ora ha questo aspetto:

![cose da fare:immagine_alt_testo](creating-hierarchical-view-sheet_4.png)
### **Associa foglio di lavoro**
 Ora usa il**Progettista di fogli di lavoro** per impostare DataSource e DataMember per il foglio di lavoro e configurare le colonne di binding del campo dati.

 Il controllo aggiunge automaticamente un'icona + per ogni riga che corrisponde a un record il cui oggetto di associazione (generalmente un oggetto DataRowView) ha

 punti di vista del bambino. Quando si fa clic sull'icona +, il record si espande per mostrare la vista figlio. L'esempio seguente utilizza il**Progettista di fogli di lavoro** legare il

 foglio di lavoro al padre principale DataTable Customers.

![cose da fare:immagine_alt_testo](creating-hierarchical-view-sheet_5.png)
### **Personalizza le colonne di associazione delle tabelle figlie**
 Il controllo fornisce un evento denominato GridWeb.BindingChildView che gli sviluppatori usano per personalizzare le colonne di associazione delle tabelle figlio. Questo esempio

 deve visualizzare i dettagli dell'ordine'**Prezzo unitario** campo in un formato valuta. Aggiungere un gestore eventi per modificare il formato numerico della colonna di associazione.

**C#**

{{< highlight "csharp" >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Carica dati da database e associazione**
Come descritto in[Associare un foglio di lavoro a un set di dati utilizzando la finestra di progettazione dei fogli di lavoro di GridWeb](/cells/it/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 è necessario aggiungere codice al blocco Page_Load per caricare i dati nel DataSet da un database e associare il DataSet al foglio nel

 passo successivo.

La classe Asppose.Grid.Web.Data.WebWorksheet ha alcune proprietà utili.

- Ad esempio, la proprietà EnableCreateBindColumnHeader viene utilizzata per creare le intestazioni della colonna associata all'interno del foglio o la colonna

 headers visualizza i nomi delle colonne associate. Prende i valori**VERO** o**falso**. 

- Le proprietà BindStartRow e BindStartColumn specificano la posizione nel foglio del controllo GridWeb a cui deve essere associata l'origine.
- La proprietà EnableExpandChildView viene utilizzata per disabilitare la visualizzazione figlio espansa per il foglio di lavoro. Per impostazione predefinita è impostato su true.

 La classe ha anche alcuni metodi utili.

- Il metodo DataBind() associa un foglio con l'origine.
- CreateNewBindRow() aggiunge una nuova riga e la associa all'origine dati.
- DeleteBindRow() elimina una riga associata.
- Il metodo SetRowExpand() imposta la riga espansa e mostra il contenuto della visualizzazione figlio nella modalità di associazione dati.
- Il metodo GetRowExpand() ottiene un valore booleano che indica se la riga è espansa o meno.

 Nel codice seguente, l'oggetto DataSet "dataSet21" è riempito con dati basati su tre tabelle. La tabella Clienti viene filtrata per renderla la

 prima tabella nella visualizzazione gerarchica. Viene creato un oggetto WebWorksheet denominato "foglio", che prima cancella il foglio e poi lo imposta

 collegato all'origine dati.

**C#**

{{< highlight "csharp" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

 'Inserisci qui il codice utente per inizializzare la pagina

 If Not IsPostBack Then

 BindWithoutInSheetHeaders()

 Finisci se

Fine Sub

Private Sub BindWithoutInSheetHeaders()

 Dim db As DemoDatabase2 = Nuovo DemoDatabase2()

Dim percorso As String = MapPath(".")

 percorso = percorso.Substring(0, percorso.LastIndexOf("\"))

 percorso = percorso.Substring(0, percorso.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Origine dati=" + percorso + "\Database\Northwind.mdb"

 Provare

 ' Si connette al database e recupera i dati.

 ' Tabella Clienti.

 db.OleDbDataAdapter1.Fill(DataSet21)

 ' Tabella degli ordini.

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' OrderDetailTable.

 db.OleDbDataAdapter3.Fill(DataSet21)

 ' Filtra i dati

 DataSet21.Customers.DefaultView.RowFilter = "ID cliente<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
