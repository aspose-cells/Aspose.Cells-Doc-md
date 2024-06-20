---
title: Skapa hierarkisk vyark
type: docs
weight: 30
url: /sv/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb, hierarkisk
description: Denna artikel introducerar hur man skapar hierarkisk vy i GridWeb.
---

{{% alert color="primary" %}} 

Data binding är en kraftfull och användarvänlig GridWeb-funktion. Data som lagras i databastabeller hämtas till en DataSet och fylls med data 

som representerar datatabellerna. Genom att använda data bindning-funktionen kan du skapa en hierarkisk vy (en huvud-barnvy) av sammanlänkade data och 

visa den i kontrollen för att göra den mer elegant. 

I detta ämne diskuteras skapandet av ett hierarkiskt vyblad. Några av raderna i bladet har underordnade vyer. När en användare klickar på radens **Expand**

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**En tabell med en hierarkisk vy** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Skapa relationer för datatabeller**
Till exempel kan du använda ADO.Net API och extrahera data från databastabellerna. För att skapa hierarkisk vy måste du designa en DataSet

objekt baserat på några tabeller och skapa en relation mellan dem först. Använd VS.NET's **DataSet Designer** för att skapa relationen. I 

detta exempel finns det tre DataTables: Customers, Orders, Order Details. Bladet visar all kundinformation som standard. När 

användaren expanderar en kund visar griden alla ordrar som kunden har lagt. När användaren expanderar en order visar griden detaljerna 

av den ordern. Datat är hierarkiskt: orderdetaljer listas under ordrar, och ordrar listas under kunder.

För att detta ska fungera, måste följande relationer etableras mellan datatabellerna:

1. Skapa en främmande nyckel på DataTable Orders; nyckelfältet är CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Skapa en främmande nyckel på DataTable Order Details; nyckelfältet är OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



DataSet Designer ser nu ut så här: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Binda kalkylblad**
Använd nu **Worksheets Designer** för att ställa in DataKällan och DataMedlem för kalkylarket och konfigurera datafältsbindningskolumner. 

Kontrollen lägger automatiskt till en + ikon för varje rad som motsvarar en post vars bindande objekt (vanligtvis en DataRowView-objekt) har 

underordnade vyer. När + ikonen klickas expanderas posten för att visa underordnad vy. Exemplet nedan använder **Worksheets Designer** för att binda 

kalkylarket till huvudförälder DataTable Customers. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Anpassa de underordnade tabellernas bindningskolumner**
Kontrollen tillhandahåller ett event med namnet GridWeb.BindingChildView som utvecklare använder för att anpassa de underordnade tabellernas bindningskolumner. Detta exempel 

behöver visa orderdetaljernas **UnitPrice**-fält i valutaformat. Lägg till en händelsehanterare för att ändra bindningskolumnens nummerformat. 

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
### **Ladda data från databasen och binda**
Som beskrivet i [Bindning kalkylblad till en DataSet med hjälp av GridWeb's Worksheets Designer](/cells/sv/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
du behöver lägga till kod i Page_Load-blocket för att ladda data till DataSet från en databas och binda DataSet till arket i 

nästa steg. 

Klassen Asppose.Grid.Web.Data.WebWorksheet har några användbara egenskaper.

- Till exempel används egenskapen EnableCreateBindColumnHeader för att skapa rubrikerna för den bundna kolumnen inom arket, eller kolumn

huvuden visar de bundna kolumnnamnen. Den tar värdena **true** eller **false**. 

- Egenskaperna BindStartRow och BindStartColumn specificerar positionen i GridWeb-kontrollens ark som källan ska bindas till.
- Egenskapen EnableExpandChildView används för att inaktivera den utökade underordnade vyn för arbetsbladet. Som standard är den inställd på true.

Klassen har också några användbara metoder. 

- DataBind() - metoden binder ett ark med källan.
- Metoden CreateNewBindRow() lägger till en ny rad och binder den till datakällan.
- Metoden DeleteBindRow() tar bort en bunden rad.
- Metoden SetRowExpand() anger den utökade raden och visar innehållet i barnvyn i databindningsläge.
- Metoden GetRowExpand() returnerar ett Booleskt värde som indikerar om raden är utökad eller inte.

I koden nedan fylls DataSet-objektet "dataSet21" med data baserat på tre tabeller. Kund-tabellen filtreras för att göra den till 

första tabellen i den hierarkiska visningen. Ett WebWorksheet-objekt med namnet "sheet" skapas, som rensar arket först och sedan sätter det 

länkas till datakällan. 

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
