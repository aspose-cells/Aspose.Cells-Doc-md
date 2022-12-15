---
title: Skapa hierarkiskt vyblad
type: docs
weight: 30
url: /sv/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 Databindning är en kraftfull och användarvänlig GridWeb-funktion. Data som lagras i databastabeller hämtas till en datauppsättning och fylls med data

 representerar datatabellerna. Med hjälp av databindningsfunktionen kan du skapa en hierarkisk vy (en master-child-vy) av sammanlänkade data och

 visa den i kontrollen för att göra den mer elegant.

 Det här ämnet diskuterar att skapa ett hierarkiskt vyblad. Några av raderna i arket har barnvyer. När en användare klickar på radens**Bygga ut**

 knapp{{< emoticons/cross >}} , expanderas den underordnade vytabellen för den raden nedåt. Den här funktionen är mycket användbar för att skapa en hierarkisk vyrapport.

**En tabell med en hierarkisk vy** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Skapa relationer för datatabeller**
Till exempel använder du ADO.Net API och extraherar data från databastabellerna. För att skapa hierarkiskt vyblad måste du designa en datauppsättning

 objekt baserat på vissa tabeller och skapa en relation mellan dem först. Använd VS.NET**Dataset designer** att skapa relationen. I

 I det här exemplet finns det tre datatabeller: kunder, beställningar, beställningsdetaljer. Arket visar all kundinformation som standard. När

 användaren utökar en kund, rutnätet visar alla beställningar som kunden har lagt. När användaren utökar en beställning visar rutnätet detaljerna

av den ordningen. Uppgifterna är hierarkiska: beställningsdetaljer listas under beställningar och beställningar under kunder.

För att detta ska fungera måste följande till relationer upprättas mellan datatabellerna:

1.  Skapa en främmande nyckel på DataTable Orders, nyckelfältet är CustomerID

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Skapa en främmande nyckel på DataTable Order Details, nyckelfältet är OrderID.

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



 DataSet Designer ser nu ut så här:

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Bind arbetsblad**
 Använd nu**Arbetsbladsdesigner** för att ställa in DataSource och DataMember för kalkylbladet och konfigurera datafältets bindningskolumner.

 Kontrollen lägger automatiskt till en +-ikon för varje rad som motsvarar en post vars bindningsobjekt (vanligtvis ett DataRowView-objekt) har

 barns synpunkter. När du klickar på +-ikonen expanderas posten för att visa barnvyn. I exemplet nedan används**Arbetsbladsdesigner** att binda

 kalkylblad till rotöverordnade DataTable-kunder.

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Anpassa underordnade tabeller Bind kolumner**
 Kontrollen tillhandahåller en händelse som heter GridWeb.BindingChildView som utvecklare använder för att anpassa de underordnade tabellernas bindningskolumner. Detta exempel

 måste visa beställningsinformationen'**Enhetspris** fältet i ett valutaformat. Lägg till en händelsehanterare för att ändra bindkolumns nummerformat.

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
### **Ladda data från databas och bindning**
Som beskrivs i[Bindning av kalkylblad till en datauppsättning med hjälp av GridWebs kalkylbladsdesigner](/cells/sv/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 du måste lägga till kod i blocket Page_Load för att ladda data till datamängden från en databas och binda datamängden till bladet i

 Nästa steg.

Klassen Asppose.Grid.Web.Data.WebWorksheet har några användbara egenskaper.

- Till exempel, egenskapen EnableCreateBindColumnHeader används för att skapa rubrikerna för den bundna kolumnen i arket, eller kolumnen

 rubriker visar de bundna kolumnnamnen. Det tar värdena**Sann** eller**falsk**. 

- Egenskaperna BindStartRow och BindStartColumn anger positionen i arket GridWeb-kontroll som källan ska vara bunden till.
- Egenskapen EnableExpandChildView används för att inaktivera den utökade underordnade vyn för kalkylbladet. Som standard är det satt till sant.

 Klassen har också några användbara metoder.

- Metoden DataBind() binder ett ark med källan.
- CreateNewBindRow() lägger till en ny rad och binder den till datakällan.
- DeleteBindRow() tar bort en bunden rad.
- Metoden SetRowExpand() ställer in den utökade raden och visar innehållet i den underordnade vyn i databindningsläget.
- Metoden GetRowExpand() får ett booleskt värde som indikerar om raden expanderas eller inte.

 I koden nedan är DataSet-objektet "dataSet21" fyllt med data baserat på tre tabeller. Kundtabellen filtreras för att göra den till

 första tabellen i den hierarkiska displayen. Ett WebWorksheet-objekt med namnet "sheet" skapas, vilket rensar arket först och sedan ställer in det

 kopplat till datakällan.

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

 Private Sub Page_Load(ByVal avsändare Som System.Object, ByVal e As System.EventArgs) Hanterar MyBase.Load

 'Sätt in användarkod för att initiera sidan här

 Om inte IsPostBack Då

 BindWithoutInSheetHeaders()

 Avsluta om

Avsluta Sub

Private Sub BindWithoutInSheetHeaders()

 Dim db As DemoDatabase2 = New DemoDatabase2()

Dim sökväg As String = MapPath(".")

 path = path.Substring(0, path.LastIndexOf("\"))

 path = path.Substring(0, path.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Datakälla=" + sökväg + "\Databas\Northwind.mdb"

 Prova

 ' Ansluter till databasen och hämtar data.

 ' Kundtabell.

 db.OleDbDataAdapter1.Fill(DataSet21)

 ' Beställningstabell.

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' OrderDetailTable.

 db.OleDbDataAdapter3.Fill(DataSet21)

 ' Filtrera data

 DataSet21.Customers.DefaultView.RowFilter = "Kund-ID<'BSAAA'"

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
