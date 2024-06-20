---
title: Erstellen einer hierarchischen Ansichtstabelle
type: docs
weight: 30
url: /de/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb, hierarchisch
description: Dieser Artikel zeigt, wie man eine hierarchische Ansicht in GridWeb erstellt.
---

{{% alert color="primary" %}} 

Die Datenbindung ist eine leistungsstarke und benutzerfreundliche Funktion von GridWeb. Daten, die in Datenbanktabellen gespeichert sind, werden in ein DataSet abgerufen und mit Daten gefüllt 

und die Datentabellen darstellen. Mit der Datenbindungs-Funktion können Sie eine hierarchische Ansicht (eine Master-Kind-Ansicht) von verknüpften Daten erstellen und 

sie im Steuerelement anzeigen, um sie eleganter zu gestalten. 

Dieses Thema befasst sich mit der Erstellung einer hierarchischen Ansichtstabelle. Einige der Zeilen in der Tabelle haben Kindansichten. Wenn ein Benutzer auf den Link **Erweitern** in der Zeile klickt

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**Eine Tabelle mit hierarchischer Ansicht** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Relations für DataTables erstellen**
Zum Beispiel verwenden Sie die ADO.Net-API und extrahieren Daten aus den Datenbanktabellen. Um eine hierarchische Ansichtstabelle zu erstellen, müssen Sie ein DataSet entwerfen

Objekt basierend auf einigen Tabellen entwerfen und zunächst eine Beziehung zwischen ihnen herstellen. Verwenden Sie den **DataSet Designer** des VS.NET, um die Beziehung zu erstellen. In 

diesem Beispiel gibt es drei DataTables: Kunden, Aufträge, Auftragsdetails. Die Tabelle zeigt standardmäßig alle Kundeninformationen an. Wenn 

der Benutzer einen Kunden erweitert, zeigt die Tabelle alle Bestellungen an, die dieser Kunde getätigt hat. Wenn der Benutzer eine Bestellung erweitert, zeigt die Tabelle die Details 

dieser Bestellung an. Die Daten sind hierarchisch: Auftragsdetails sind unter Aufträgen und Aufträge sind unter Kunden aufgeführt.

Damit dies funktioniert, müssen die folgenden Beziehungen zwischen den Datentabellen hergestellt werden:

1. Erstellen Sie einen Fremdschlüssel auf der DataTable Orders, das Schlüsselfeld ist CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




2. Erstellen Sie einen Fremdschlüssel auf der DataTable Order Details, das Schlüsselfeld ist OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



Der DataSet Designer sieht jetzt so aus: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Arbeitsblatt binden**
Verwenden Sie nun den **Arbeitsblätter Designer**, um die DataSource und das DataMember für das Arbeitsblatt festzulegen und die Datenfelder zu konfigurieren. 

Die Steuerung fügt automatisch ein + Symbol für jede Zeile hinzu, die einem Datensatz entspricht, dessen Bindungsobjekt (in der Regel ein DataRowView-Objekt) hat 

Kindansichten. Wenn auf das + Symbol geklickt wird, wird der Datensatz erweitert, um die Kindansicht anzuzeigen. Das folgende Beispiel verwendet den **Worksheets Designer**, um die 

Tabelle an das übergeordnete Stamm-Datentabelle Kunden zu binden. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Anpassen der Spalten für gebundene Kindtabellen**
Die Steuerung bietet ein Ereignis namens GridWeb.BindingChildView, das von Entwicklern verwendet wird, um die Spalten für gebundene Kindtabellen anzupassen. Dieses Beispiel 

muss das **UnitPrice**-Feld der Bestelldetails im Währungsformat anzeigen. Fügen Sie einen Ereignishandler hinzu, um das Zahlenformat der gebundenen Spalte zu ändern. 

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
### **Daten aus der Datenbank laden und binden**
Wie in [Arbeitsblattbindung an ein DataSet mithilfe des Worksheet-Designers von GridWeb](/cells/de/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/) beschrieben, müssen Sie
Code zum Laden von Daten aus einer Datenbank in den Page_Load-Block hinzufügen und das DataSet im nächsten Schritt an das Arbeitsblatt binden. 

Der Asppose.Grid.Web.Data.WebWorksheet-Klasse verfügt über einige nützliche Eigenschaften. 

Die Klasse Asppose.Grid.Web.Data.WebWorksheet hat einige nützliche Eigenschaften.

- Beispielsweise wird die Eigenschaft EnableCreateBindColumnHeader verwendet, um die Überschriften der gebundenen Spalte im Arbeitsblatt zu erstellen oder die Spalte

Kopfzeilen zeigen die Namen der gebundenen Spalten. Sie nimmt die Werte **true** oder **false** an. 

- Die Eigenschaften BindStartRow und BindStartColumn geben die Position im Arbeitsblatt des GridWeb-Steuerung an, an die die Quelle gebunden werden soll.
- Die Eigenschaft EnableExpandChildView wird verwendet, um die erweiterte Kindansicht für das Arbeitsblatt zu deaktivieren. Standardmäßig ist sie auf true gesetzt.

Die Klasse hat auch einige nützliche Methoden. 

- Die Methode DataBind() bindet ein Arbeitsblatt mit der Quelle.
- Die Methode CreateNewBindRow() fügt eine neue Zeile hinzu und bindet sie an die Datenquelle.
- Die Methode DeleteBindRow() löscht eine gebundene Zeile.
- Die Methode SetRowExpand() legt die erweiterte Zeile fest und zeigt den Inhalt der untergeordneten Ansicht im Datenbindungsmodus an.
- Die Methode GetRowExpand() gibt einen Booleschen Wert zurück, der angibt, ob die Zeile erweitert ist oder nicht.

Im folgenden Code wird das DataSet-Objekt "dataSet21" basierend auf drei Tabellen mit Daten gefüllt. Die Kunden-Tabelle wird gefiltert, um sie zur ersten Tabelle in der hierarchischen Ansicht zu machen. Ein WebWorksheet-Objekt mit dem Namen "sheet" wird erstellt, das zuerst das Blatt löscht und dann mit der Datenquelle verknüpft. 

**VB.NET** 

mit der Datenquelle verknüpft. 

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
