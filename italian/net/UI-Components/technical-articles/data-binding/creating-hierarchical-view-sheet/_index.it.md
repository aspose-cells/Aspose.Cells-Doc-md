---
title: Creazione della visualizzazione gerarchica del foglio
type: docs
weight: 30
url: /it/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb, gerarchico
description: Questo articolo presenta come creare una visualizzazione gerarchica in GridWeb.
---

{{% alert color="primary" %}} 

Il data binding è una potente e user-friendly caratteristica di GridWeb. I dati memorizzati nelle tabelle del database vengono recuperati in un DataSet e popolati con dati 

rappresentando le tabelle dei dati. Utilizzando la funzionalità di data binding, è possibile creare una visualizzazione gerarchica (una visualizzazione padre-figlio) di dati interconnessi e 

mostrarla nel controllo per renderla più elegante. 

Questo argomento discute la creazione di un foglio con visualizzazione gerarchica. Alcune delle righe nel foglio hanno visualizzazioni figlio. Quando un utente fa clic su **Espandi** della riga

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**Una tabella con una visualizzazione gerarchica** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Creare relazioni per i DataTable**
Ad esempio, si utilizza l'API ADO.Net ed estrarre dati dalle tabelle del database. Per creare un foglio con visualizzazione gerarchica, è necessario progettare un DataSet

oggetto basato su alcune tabelle e creare una relazione tra di esse prima. Utilizzare il **DataSet Designer** di VS.NET per creare la relazione. In 

In questo esempio, ci sono tre DataTables: Clienti, Ordini, Dettagli ordine. Il foglio mostra tutte le informazioni dei clienti per impostazione predefinita. Quando 

l'utente espande un cliente, la griglia mostra tutti gli ordini che quel cliente ha effettuato. Quando l'utente espande un ordine, la griglia mostra i dettagli 

di quell'ordine. I dati sono gerarchici: i dettagli dell'ordine sono elencati sotto gli ordini e gli ordini sono elencati sotto i clienti.

Per far funzionare questo, è necessario stabilire le seguenti relazioni tra le tabelle:

1. Creare una chiave esterna su DataTable Ordini, il campo chiave è CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Creare una chiave esterna su DataTable Dettagli ordine, il campo chiave è OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



Il DataSet Designer sembra ora così: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Collegare il foglio di lavoro**
Ora utilizza il **Worksheets Designer** per impostare il DataSource e il DataMember per il foglio di lavoro e configurare le colonne del binding dei campi dati. 

Il controllo aggiunge automaticamente un'icona + per ogni riga corrispondente a un record il cui oggetto di binding (generalmente un oggetto DataRowView) ha 

viste figlio. Quando si fa clic sull'icona +, il record si espande per mostrare la vista figlio. L'esempio di seguito utilizza il **Worksheets Designer** per collegare il 

foglio di lavoro al DataTable genitore radice Clienti. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Personalizzare le colonne di binding delle tabelle figlio**
Il controllo fornisce un evento chiamato GridWeb.BindingChildView che gli sviluppatori utilizzano per personalizzare le colonne di binding delle tabelle figlio. In questo esempio 

deve mostrare il campo **UnitPrice** dei dettagli dell'ordine in un formato di valuta. Aggiungere un gestore di eventi per cambiare il formato numerico della colonna di binding. 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Carica dati dal database e collegamento**
Come descritto in [Collegare il foglio di lavoro a un DataSet utilizzando il Worksheets Designer di GridWeb](/cells/it/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
è necessario aggiungere del codice al blocco Page_Load per caricare i dati nel DataSet da un database e collegare il DataSet al foglio nel 

passo successivo. 

La classe Asppose.Grid.Web.Data.WebWorksheet ha alcune proprietà utili.

- Ad esempio, la proprietà EnableCreateBindColumnHeader viene utilizzata per creare gli intesinti della colonna collegata all'interno del foglio, o la colonna

intestazioni visualizza i nomi delle colonne collegate. Assuma i valori **true** o **false**. 

- Le proprietà BindStartRow e BindStartColumn specificano la posizione nel foglio di controllo GridWeb in cui il sorgente deve essere collegato.
- La proprietà EnableExpandChildView viene utilizzata per disabilitare la vista figlio espansa per il foglio di lavoro. Per impostazione predefinita è impostata su true.

La classe ha anche alcuni metodi utili. 

- Il metodo DataBind() collega un foglio con il sorgente.
- Il metodo CreateNewBindRow() aggiunge una nuova riga e la collega al sorgente dati.
- Il metodo DeleteBindRow() elimina una riga collegata.
- Il metodo SetRowExpand() imposta la riga espansa e mostra il contenuto della vista figlio in modalità di binding dei dati.
- Il metodo GetRowExpand() ottiene un valore booleano che indica se la riga è espansa o meno.

Nel codice sottostante, l'oggetto DataSet "dataSet21" è riempito con dati basati su tre tabelle. La tabella dei clienti è filtrata per renderla la 

prima tabella nella visualizzazione gerarchica. Viene creato un oggetto WebWorksheet chiamato "foglio", che cancella prima il foglio e poi lo imposta 

collegato al sorgente dati. 

**C#**

{{< highlight csharp >}}

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

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

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

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

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
