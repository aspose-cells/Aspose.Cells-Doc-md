---
title: Binden des Arbeitsblatts an ein DataSet mithilfe des GridWebs-Arbeitsblatt-Designers
type: docs
weight: 20
url: /de/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 Dieser Artikel beschreibt einen einfachen Ansatz zum Binden von Arbeitsblättern an Datenbanktabellen im GUI-Modus mithilfe eines speziellen Tools, das mit Aspose.Cells.GridWeb, dem Worksheets Designer, geliefert wird.

{{% /alert %}} 
## **Binden eines Arbeitsblatts mit einer Datenbank mithilfe des Arbeitsblatt-Designers**
	**Schritt 1: Erstellen einer Beispieldatenbank**
1. Zuerst erstellen wir die Beispieldatenbank, die in diesem Artikel verwendet wird. Wir verwenden Microsoft Access, um eine Datenbank zu erstellen, die eine Tabelle namens Products enthält. Das Schema ist unten dargestellt.
   **Designinformationen der Produkttabelle** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Der Tabelle Products werden einige Dummy-Datensätze hinzugefügt.
   **Datensätze in der Tabelle Produkte** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Schritt 2: Beispielanwendung entwerfen**
 Eine ASP.NET-Webanwendung wird wie unten gezeigt in Visual Studio.NET erstellt und entworfen.
**Entworfene Beispielanwendung** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Schritt 3: Herstellen einer Verbindung mit der Datenbank mithilfe des Server-Explorers**
 Es ist Zeit, sich mit der Datenbank zu verbinden. Wir können dies ganz einfach mit dem Server Explorer in Visual Studio.NET tun.

1.  Auswählen**Datenverbindung** in**Server-Explorer** und Rechtsklick.
1.  Auswählen**Verbindung hinzufügen** aus dem Menü.
   **Auswahl der Option Verbindung hinzufügen** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 Das Dialogfeld Datenverknüpfungseigenschaften wird angezeigt.
**Das Dialogfeld Datenverknüpfungseigenschaften** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 Mit diesem Dialog können Sie sich mit jeder Datenbank verbinden. Standardmäßig können Sie sich mit einer SQL Server-Datenbank verbinden. Für dieses Beispiel müssen wir eine Verbindung mit einer Microsoft Access-Datenbank herstellen.

1.  Drücke den**Anbieter** Tab.
1.  Auswählen**Microsoft Jet 4.0 OLE DB-Anbieter** von dem**OLE DB-Anbieter** aufführen.
1.  Klicken**Nächste**.
   **Klicken Sie auf Weiter, nachdem Sie einen OLE DB-Anbieter ausgewählt haben** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 Das**Verbindung** Registerkarte wird geöffnet.

1.  Wählen Sie die Access-Datenbankdatei Microsoft (in unserem Fall db.mdb) und klicken Sie auf**OK**.
   **Klicken Sie auf die Schaltfläche OK, nachdem Sie die Datenbankdatei ausgewählt haben** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 Nach dem Anklicken**OK** , wird eine Datenbankverbindung zur Microsoft Access-Datenbank in der erstellt**Server-Explorer**Doppelklicken Sie auf die Verbindung, um alle Tabellen, Ansichten und gespeicherten Prozeduren in der Datenbank anzuzeigen.

{{% /alert %}} 
### **Schritt 4: Datenbankverbindungsobjekte grafisch erstellen**
1.  Durchsuchen Sie die Tabellen in der Datenbank mit der**Server-Explorer**.
 Es gibt nur eine Tabelle, Produkte.
1.  Ziehen Sie die Tabelle Produkte per Drag-and-Drop aus der**Server-Explorer** zum**Web-Formular**.
   **Ziehen Sie die Produkttabelle aus dem Server-Explorer und legen Sie sie im Webformular ab** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Möglicherweise wird ein Dialogfeld angezeigt.
**Dialog zum Bestätigen der Einbeziehung des Datenbankkennworts in die Verbindungszeichenfolge** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Entscheiden Sie, ob Sie ein Datenbankkennwort in die Verbindungszeichenfolge aufnehmen möchten oder nicht. Für dieses Beispiel haben wir ausgewählt**Geben Sie kein Passwort ein**. 
Zwei Datenbankverbindungsobjekte (oleDbConnection1 und oleDbDataAdapter1) wurden erstellt und hinzugefügt.
**Datenbankverbindungsobjekte (oleDbConnection1 & oleDbDataAdapter1) erstellt und angezeigt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Schritt 5: DataSet generieren**
Bisher haben wir Datenbankverbindungsobjekte erstellt, müssen aber nach der Verbindung mit der Datenbank noch Daten speichern. Ein DataSet-Objekt kann Daten genau speichern und wir können es auch einfach mit der VS.NET-IDE generieren.

1.  Auswählen**oleDbDataAdaper1** und Rechtsklick.
1.  Auswählen**Datensatz generieren** Option aus dem Menü.
   **Auswahl der Option DataSet generieren** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 Der Dialog DataSet generieren wird angezeigt.
 Hier kann ein Name für das neu zu erstellende DataSet-Objekt ausgewählt werden und welche Tabellen hinzugefügt werden sollen.

1.  Wähle aus**Fügen Sie dieses Dataset dem Designer hinzu** Möglichkeit.
1.  Klicken**OK**.
   **Klicken Sie auf die Schaltfläche OK, um DataSet zu generieren** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Dem Designer wird ein dataSet11-Objekt hinzugefügt.
**DataSet generiert und Designer hinzugefügt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Schritt 6: Verwenden des Arbeitsblatt-Designers**
 Jetzt ist es an der Zeit, das Geheimnis zu lüften.

1. Wählen Sie das GridWeb-Steuerelement aus, und klicken Sie mit der rechten Maustaste.
1.  Auswählen**Arbeitsblatt-Designer** Option aus dem Menü.

   **Auswählen der Option Arbeitsblatt-Designer** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 Der Worksheet Collection Editor (auch Worksheets Designer genannt) wird angezeigt.
**Dialogfeld Arbeitsblattsammlungs-Editor** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



Das Dialogfeld enthält mehrere Eigenschaften, die konfiguriert werden können, um Sheet1 an eine beliebige Tabelle in der Datenbank zu binden.

1.  Wähle aus**Datenquelle** Eigentum.
 Das im vorherigen Schritt generierte dataSet11-Objekt wird im Menü aufgelistet.
1. Wählen Sie dataSet11.
1.  Drücke den**Datenmitglied** Eigentum.
 Der Worksheets Designer zeigt automatisch eine Liste von Tabellen in dataSet11. Es gibt nur eine Tabelle, Produkte.
1. Wählen Sie die Tabelle Produkte aus.
   **Festlegen von DataSource- und DataMember-Eigenschaften** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  Überprüf den**BindenSpalten** Eigentum.
   **Klicken Sie auf die BindColumns-Eigenschaft** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 Klicken Sie auf die**BindenSpalten** -Eigenschaft öffnet den BindColumn-Auflistungs-Editor.
**Der BindColumn-Auflistungs-Editor** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 Im BindColumn Collection Editor werden alle Spalten der**Produkte** -Tabelle werden automatisch zur BindColumns-Auflistung hinzugefügt.

1. Wählen Sie eine beliebige Spalte aus und passen Sie ihre Eigenschaften an.
 Beispielsweise können Sie jede Spaltenüberschrift ändern.
   **Ändern der Beschriftung der ProductID-Spalte** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  Nachdem Sie Änderungen vorgenommen haben, klicken Sie auf**OK**.
1.  Schließen Sie alle Dialoge durch Anklicken**OK**.
 Schließlich kehren Sie zur Seite WebForm1.aspx zurück.
   **Rückkehr zur Seite WebForm1.aspx nach der Verwendung des Arbeitsblatt-Designers** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 Oben wird der Spaltenname der Tabelle „Products“ angezeigt. Die Breite der Spalten ist gering, sodass die vollständigen Namen einiger Spalten nicht vollständig sichtbar sind.
### **Schritt 7: Hinzufügen von Code zum Page_Load-Ereignishandler**
 Wir haben den Arbeitsblatt-Designer verwendet und müssen jetzt nur noch Code zum Page_Load-Ereignishandler hinzufügen, um das dataSet11-Objekt mit Daten aus der Datenbank zu füllen (unter Verwendung von oleDbDataAdapter1) und das GridWeb-Steuerelement durch Aufrufen seiner DataBind-Methode an dataSet11 zu binden.

1.  Fügen Sie den Code hinzu:

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

1. Überprüfen Sie den Code, der dem Page_Load-Ereignishandler hinzugefügt wurde.
   **Code zum Page_Load-Ereignishandler hinzugefügt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Schritt 8: Ausführen der Anwendung**
 Kompilieren Sie die Anwendung und führen Sie sie aus: Drücken Sie entweder**Strg+F5** oder klicken**Anfang**. 
**Ausführen der Anwendung** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Nach der Kompilierung wird die Seite WebForm1.aspx in einem Browserfenster geöffnet, wobei alle Daten aus der Datenbank geladen werden.
**Daten, die aus der Datenbank in das GridWeb-Steuerelement geladen werden** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Arbeiten mit dem GridWeb Control**
 Wenn Daten in das GridWeb-Steuerelement geladen werden, bietet es Benutzern die Kontrolle über die Daten. GridWeb bietet eine Reihe verschiedener Arten von Datenbearbeitungsfunktionen an.
### **Datenvalidierung**
Aspose.Cells. GridWeb erstellt automatisch geeignete Validierungsregeln für alle gebundenen Spalten gemäß den in der Datenbank definierten Datentypen. Zeigen Sie den Validierungstyp einer Zelle an, indem Sie den Mauszeiger darüber bewegen.
**Überprüfung des Validierungstyps einer Zelle** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Hier enthält die ausgewählte Zelle die**<INT>** Validierung, was bedeutet, dass Benutzer nur ganzzahlige Werte eingeben können. Wenn sie einen anderen Wert eingeben, tritt ein Validierungsfehler auf. Darüber hinaus,**<ERFORDERLICH>** zeigt, dass der Wert Produkt-ID übermittelt werden muss.
### **Zeilen löschen**
 Um eine Zeile zu löschen, wählen Sie eine Zeile (oder eine beliebige Zelle in der Zeile) aus, klicken Sie mit der rechten Maustaste und wählen Sie aus**Zeile löschen**.
**Auswahl der Option Zeile löschen aus dem Menü** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Die Zeile würde sofort gelöscht.
**Rasterdaten (nachdem eine Zeile gelöscht wurde)** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Zeilen bearbeiten**
Bearbeiten Sie Daten in Zellen oder Zeilen und klicken Sie dann auf**Speichern** oder**Einreichen** um die Änderungen zu speichern.
### **Zeilen hinzufügen**
1.  Um eine Zeile hinzuzufügen, klicken Sie mit der rechten Maustaste auf eine Zelle und wählen Sie sie aus**Zeile hinzufügen**.
   **Auswahl der Option Zeile hinzufügen aus dem Menü** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Eine neue Zeile wird dem Blatt am Ende anderer Zeilen hinzugefügt.
**Neue Zeile zum Raster hinzugefügt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 Links neben der neuen Zeile befindet sich ein Sternchen{{< emoticons/cross >}} , was anzeigt, dass die Zeile neu ist.

1. Fügen Sie der neuen Zeile Werte hinzu.
1.  Klicken**Speichern** oder**Einreichen** um die Änderung zu bestätigen.
   **Änderungen an Daten speichern, indem Sie auf *Speichern klicken** Taste*

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Zahlenformat einstellen**
 Im Moment sind die Preise in der**Produktpreis** Spalte werden als numerische Werte angezeigt. Es ist möglich, sie wie eine Währung aussehen zu lassen.

1. Kehren Sie zu Visual Studio.NET zurück.
1. Öffnen Sie den BindColumn-Auflistungs-Editor.
 Das**NumberType** Eigentum der**Produktpreis** Spalte eingestellt ist**Allgemein**.
   **Die NumberType-Eigenschaft ist auf General festgelegt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Klicken**Dropdown-Liste** und auswählen**Währung4** von der Liste.
   **Die NumberType-Eigenschaft wurde in Currency4 geändert** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Führen Sie die Anwendung erneut aus.
 Die Werte in der**Produktpreis** Spalte ist jetzt Währung.
   **Produktpreise im Währungszahlenformat** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Bearbeiten von Daten**
 Die Anwendung erlaubt ihren Benutzern bisher nur das Anzeigen von Tabellendaten. Benutzer können Daten im GridWeb-Steuerelement bearbeiten, aber beim Schließen des Browsers und Öffnen der Datenbank hat sich nichts geändert. Die vorgenommenen Änderungen werden nicht in der Datenbank gespeichert.

 Im folgenden Beispiel wird der Anwendung Code hinzugefügt, sodass GridWeb Änderungen in der Datenbank speichern kann.

1. Öffne das**Eigenschaften** und wählen Sie das SaveCommand-Ereignis des GridWeb-Steuerelements aus der Liste aus.
   **Auswählen des SaveCommand-Ereignisses von GridWeb** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  Doppelklicken Sie auf die**SaveCommand** -Ereignis und VS.NET erstellt den GridWeb1_SaveCommand-Ereignishandler.
1.  Fügen Sie diesem Ereignishandler Code hinzu, der die Datenbank mit allen geänderten Daten im DataSet aktualisiert, die mit oleDbDataAdapter1 an das Arbeitsblatt gebunden sind.

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

Sie können auch den Code überprüfen, der dem Ereignishandler GridWeb1_SaveCommand hinzugefügt wurde
**Code zum GridWeb1_SaveCommand-Ereignishandler hinzugefügt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 Speichern Sie Änderungen in der Datenbank mit der**Speichern** Schaltfläche speichert sie jetzt definitiv.
## **Fazit**
{{% alert color="primary" %}} 

Die Datenbindung ist ein wichtiges Feature von Aspose.Cells.GridWeb. Es ist einfach, Arbeitsblätter mit dem von Aspose.Cells.GridWeb angebotenen Worksheets Designer-Dienstprogramm an eine Datenbank zu binden. Aspose.Cells.GridWeb spart Zeit und Mühe beim Erstellen leistungsstarker Grid-Lösungen.

{{% /alert %}}
