---
title: Hierarchisches Ansichtsblatt erstellen
type: docs
weight: 30
url: /de/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 Die Datenbindung ist eine leistungsstarke und benutzerfreundliche GridWeb-Funktion. In Datenbanktabellen gespeicherte Daten werden in ein DataSet geholt und mit Daten gefüllt

 die Datentabellen darstellen. Mit der Datenbindungsfunktion können Sie eine hierarchische Ansicht (eine Master-Child-Ansicht) von miteinander verknüpften Daten erstellen und

 Zeigen Sie es im Steuerelement an, um es eleganter zu machen.

 In diesem Thema wird das Erstellen eines hierarchischen Ansichtsblatts erläutert. Einige der Zeilen im Blatt haben untergeordnete Ansichten. Wenn ein Benutzer auf die Zeile klickt**Erweitern**

 Taste{{< emoticons/cross >}} , wird die untergeordnete Ansichtstabelle dieser Zeile nach unten erweitert. Diese Funktion ist sehr hilfreich beim Erstellen eines hierarchischen Ansichtsberichts.

**Eine Tabelle mit einer hierarchischen Ansicht** 

![todo: Bild_alt_Text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Erstellen Sie Beziehungen für DataTables**
Sie verwenden beispielsweise ADO.Net API und extrahieren Daten aus den Datenbanktabellen. Um ein hierarchisches Ansichtsblatt zu erstellen, müssen Sie ein DataSet entwerfen

 Objekt basierend auf einigen Tabellen und erstellen Sie zuerst eine Beziehung zwischen ihnen. Verwenden Sie die VS.NET**DataSet-Designer** um die Beziehung herzustellen. Im

 In diesem Beispiel gibt es drei DataTables: Kunden, Bestellungen, Bestelldetails. Das Blatt zeigt standardmäßig alle Kundeninformationen an. Wann

 erweitert der Benutzer einen Kunden, zeigt das Raster alle Bestellungen, die der Kunde aufgegeben hat. Wenn der Benutzer eine Bestellung erweitert, zeigt das Raster die Details an

dieser Reihenfolge. Die Daten sind hierarchisch: Bestelldetails werden unter Bestellungen und Bestellungen unter Kunden aufgelistet.

Damit dies funktioniert, müssen folgende Beziehungen zwischen den Datentabellen hergestellt werden:

1.  Erstellen Sie einen Fremdschlüssel für DataTable Orders, das Schlüsselfeld ist CustomerID

![todo: Bild_alt_Text](creating-hierarchical-view-sheet_2.png)




1. Erstellen Sie einen Fremdschlüssel für DataTable Order Details, das Schlüsselfeld ist OrderID.

![todo: Bild_alt_Text](creating-hierarchical-view-sheet_3.png)



 Der DataSet Designer sieht nun so aus:

![todo: Bild_alt_Text](creating-hierarchical-view-sheet_4.png)
### **Arbeitsblatt binden**
 Verwenden Sie jetzt die**Arbeitsblatt-Designer** , um die DataSource und DataMember für das Arbeitsblatt festzulegen und die Datenfeldbindungsspalten zu konfigurieren.

 Das Steuerelement fügt automatisch ein +-Symbol für jede Zeile hinzu, die einem Datensatz entspricht, dessen Bindungsobjekt (im Allgemeinen ein DataRowView-Objekt) hat

 kindliche Ansichten. Wenn auf das Symbol + geklickt wird, wird der Datensatz erweitert, um die untergeordnete Ansicht anzuzeigen. Das folgende Beispiel verwendet die**Arbeitsblatt-Designer** zu binden

 Arbeitsblatt zum übergeordneten Root DataTable Customers.

![todo: Bild_alt_Text](creating-hierarchical-view-sheet_5.png)
### **Passen Sie die Bindungsspalten der untergeordneten Tabellen an**
 Das Steuerelement stellt ein Ereignis namens GridWeb.BindingChildView bereit, das Entwickler verwenden, um die Bindungsspalten der untergeordneten Tabellen anzupassen. Dieses Beispiel

 muss die Bestelldetails anzeigen**Stückpreis** Feld in einem Währungsformat. Fügen Sie einen Ereignishandler hinzu, um das Zahlenformat der Bindungsspalte zu ändern.

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
### **Daten aus Datenbank und Bindung laden**
Wie beschrieben in[Binden des Arbeitsblatts an ein DataSet mit dem Arbeitsblatt-Designer von GridWeb](/cells/de/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 Sie müssen dem Page_Load-Block Code hinzufügen, um Daten aus einer Datenbank in das DataSet zu laden, und das DataSet an das Blatt in der binden

 nächster Schritt.

Die Klasse Asppose.Grid.Web.Data.WebWorksheet hat einige nützliche Eigenschaften.

- Beispielsweise wird die Eigenschaft EnableCreateBindColumnHeader verwendet, um die Überschriften der gebundenen Spalte innerhalb des Blatts oder der Spalte zu erstellen

 headers zeigt die gebundenen Spaltennamen an. Es nimmt die Werte**Stimmt** oder**FALSCH**. 

- Die Eigenschaften BindStartRow und BindStartColumn geben die Position im Blatt des GridWeb-Steuerelements an, an das die Quelle gebunden werden soll.
- Die Eigenschaft EnableExpandChildView wird verwendet, um die erweiterte untergeordnete Ansicht für das Arbeitsblatt zu deaktivieren. Standardmäßig ist es auf true gesetzt.

 Die Klasse hat auch einige nützliche Methoden.

- Die Methode DataBind() bindet ein Blatt an die Quelle.
- Die CreateNewBindRow() fügt eine neue Zeile hinzu und bindet sie an die Datenquelle.
- DeleteBindRow() löscht eine gebundene Zeile.
- Die Methode SetRowExpand() legt die erweiterte Zeile fest und zeigt den Inhalt der untergeordneten Ansicht im Datenbindungsmodus an.
- Die Methode GetRowExpand() erhält einen booleschen Wert, der angibt, ob die Zeile erweitert ist oder nicht.

 Im folgenden Code wird das DataSet-Objekt „dataSet21“ mit Daten gefüllt, die auf drei Tabellen basieren. Die Customers-Tabelle wird gefiltert, um sie zu machen

 erste Tabelle in der hierarchischen Darstellung. Ein WebWorksheet-Objekt mit dem Namen "sheet" wird erstellt, das das Blatt zuerst löscht und dann festlegt

 mit der Datenquelle verknüpft.

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

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Behandelt MyBase.Load

 'Benutzercode zum Initialisieren der Seite hier eingeben

 Wenn nicht IsPostBack Then

 BindWithoutInSheetHeaders()

 Ende Wenn

End Sub

Private UnterbindungOhneInSheetHeaders()

 Dim db As DemoDatabase2 = Neue DemoDatabase2()

Dim path As String = MapPath(".")

 path = path.Substring(0, path.LastIndexOf("\"))

 path = path.Substring(0, path.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Datenquelle=" + Pfad + "\Database\Northwind.mdb"

 Versuchen

 ' Stellt eine Verbindung zur Datenbank her und ruft Daten ab.

 ' Kundentabelle.

 db.OleDbDataAdapter1.Fill(DataSet21)

 ' Bestelltabelle.

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' OrderDetailTable.

 db.OleDbDataAdapter3.Fill(DataSet21)

 ' Daten filtern

 DataSet21.Customers.DefaultView.RowFilter = "Kunden-ID<'BSAAA'"

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
