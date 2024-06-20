---
title: Arbeitsblatt an ein DataSet binden mit dem Arbeitsblätter Designer von GridWeb
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: In diesem Artikel wird erläutert, wie Arbeitsblätter Designer verwendet werden, um ein Arbeitsblatt an ein DataSet in GridWeb zu binden.
---

{{% alert color="primary" %}} 

Dieser Artikel diskutiert einen einfachen Ansatz zum Binden von Arbeitsblättern an Datenbanktabellen im GUI-Modus unter Verwendung eines speziellen Tools, das mit Aspose.Cells.GridWeb mitgeliefert wird, dem Arbeitsblätter-Designer. 

{{% /alert %}} 
## **Ein Arbeitsblatt mit einer Datenbank mit dem Arbeitsblätter-Designer binden**
	**Schritt 1: Erstellen einer Beispieldatenbank**
1. Zunächst erstellen wir die Beispieldatenbank, die in diesem Artikel verwendet wird. Wir verwenden Microsoft Access, um eine Datenbank zu erstellen, die eine Tabelle namens Produkte enthält. Ihre Struktur wird unten dargestellt.
   **Entwurfsinformationen der Produkte Tabelle** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Einige Dummy-Datensätze werden der Produkte-Tabelle hinzugefügt.
   **Datensätze in der Produkte-Tabelle** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Schritt 2: Entwurf der Beispielanwendung**
Eine ASP.NET-Webanwendung wird erstellt und im Visual Studio .NET entworfen, wie unten gezeigt. 
**Entworfene Beispielanwendung** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Schritt 3: Verbindung mit der Datenbank über den Server-Explorer**
Es ist Zeit, sich mit der Datenbank zu verbinden. Wir können dies ganz einfach über den Server-Explorer in Visual Studio .NET tun. 

1. Wählen Sie **Datenverbindung** im **Server-Explorer** aus und klicken Sie mit der rechten Maustaste.
1. Wählen Sie **Verbindung hinzufügen** im Menü aus.
   **Auswählen der Option Verbindung hinzufügen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



Der Dialogfeld Eigenschaften für Datenverbindungen wird angezeigt. 
**Das Dialogfeld Eigenschaften für Datenverbindungen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



Mit diesem Dialog können Sie sich mit einer beliebigen Datenbank verbinden. Standardmäßig können Sie sich mit einer SQL Server-Datenbank verbinden. Für dieses Beispiel müssen wir uns jedoch mit einer Microsoft Access-Datenbank verbinden. 

1. Klicken Sie auf die Registerkarte **Provider**.
1. Wählen Sie **Microsoft Jet 4.0 OLE DB Provider** aus der Liste der **OLE DB-Anbieter**.
1. Klicken Sie auf **Weiter**.
   **Klicken Sie auf Weiter, nachdem Sie einen OLE DB-Anbieter ausgewählt haben** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


Die Registerkarte **Verbindung** wird geöffnet. 

1. Wählen Sie die Microsoft Access-Datenbankdatei (in unserem Fall db.mdb) aus und klicken Sie auf **OK**.
   **Klicken Sie auf die Schaltfläche OK, nachdem Sie die Datenbankdatei ausgewählt haben** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

Nach dem Klicken auf **OK** wird eine Datenbankverbindung zur Microsoft Access-Datenbank im **Server-Explorer** erstellt. Doppelklicken Sie auf die Verbindung, um alle Tabellen, Ansichten und gespeicherten Prozeduren in der Datenbank anzuzeigen.

{{% /alert %}} 
### **Schritt 4: Erstellen von Datenbankverbindungsobjekten grafisch**
1. Durchsuchen Sie die Tabellen in der Datenbank mit dem **Server Explorer**.
   Es gibt nur eine Tabelle, Produkte. 
1. Ziehen Sie die Tabelle Produkte aus dem **Server-Explorer** auf das **Webformular** und lassen Sie sie dort fallen.
   **Ziehen der Tabelle Produkte aus dem Server-Explorer und Ablegen im Webformular** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Ein Dialog kann angezeigt werden.
**Dialog zum Bestätigen der Einschließung des Datenbankpassworts im Verbindungsskript** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Entscheiden Sie, ob Sie ein Datenbankpasswort im Verbindungsskript einschließen möchten oder nicht. Für dieses Beispiel haben wir **Passwort nicht einschließen** ausgewählt. 
Zwei Datenbankverbindungsobjekte (oleDbConnection1 und oleDbDataAdapter1) wurden erstellt und hinzugefügt.
**Datenbankverbindungsobjekte (oleDbConnection1 & oleDbDataAdapter1) wurden erstellt und angezeigt** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Schritt 5: Generierung des DataSets**
Bisher haben wir Datenbankverbindungsobjekte erstellt, benötigen jedoch immer noch einen Ort, um Daten nach der Verbindung mit der Datenbank zu speichern. Ein DataSet-Objekt kann Daten präzise speichern und wir können es auch einfach mit der VS.NET-IDE generieren. 

1. Wählen Sie **oleDbDataAdaper1** aus und klicken Sie mit der rechten Maustaste.
1. Wählen Sie **DataSet generieren** aus dem Menü.
   **Auswählen der Option DataSet generieren** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



Der Dialog zur Generierung des DataSets wird angezeigt. 
Hier ist es möglich, einen Namen für das neu zu erstellende DataSet-Objekt auszuwählen und welche Tabellen hinzugefügt werden sollen. 

1. Wählen Sie die Option **Dieses Dataset zum Designer hinzufügen** aus.
1. Klicken Sie auf **OK**.
   **Klicken Sie auf die OK-Schaltfläche, um DataSet zu generieren** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Ein dataSet11-Objekt wird dem Designer hinzugefügt.
**DataSet generiert und zum Designer hinzugefügt** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Schritt 6: Verwenden des Worksheets Designers**
Jetzt ist es an der Zeit, das Geheimnis zu lüften. 

1. Wählen Sie die GridWeb-Steuerung aus und klicken Sie mit der rechten Maustaste.
1. Wählen Sie die Option **Arbeitsblatt-Designer** im Menü aus. 

   **Auswahl der Option Arbeitsblatt-Designer** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



Der Arbeitsblattsammlungs-Editor (auch Arbeitsblatt-Designer genannt) wird angezeigt. 
**Arbeitsblattsammlungs-Editor-Dialog** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



Der Dialog enthält verschiedene Eigenschaften, die konfiguriert werden können, um Sheet1 mit einer Tabelle in der Datenbank zu verbinden.

1. Wählen Sie die **Datenquelle**-Eigenschaft aus.
   Das im vorherigen Schritt generierte Objekt dataSet11 wird im Menü aufgelistet. 
1. Wählen Sie dataSet11 aus.
1. Klicken Sie auf die **DataMember**-Eigenschaft.
   Der Arbeitsblatt-Designer zeigt automatisch eine Liste von Tabellen in dataSet11 an. Es gibt nur eine Tabelle, Produkte.
1. Wählen Sie die Tabelle Produkte aus.
   **Setzen der DataSource- und DataMember-Eigenschaften** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. Überprüfen Sie die **BindColumns**-Eigenschaft.
   **Klicken der BindColumns-Eigenschaft** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



Durch Klicken der **BindColumns**-Eigenschaft wird der BindColumn-Editor geöffnet.
**Der BindColumn-Editor** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



Im BindColumn-Editor werden automatisch alle Spalten der Tabelle **Produkte** zur BindColumns-Sammlung hinzugefügt. 

1. Wählen Sie eine beliebige Spalte aus und passen Sie ihre Eigenschaften an.
   Sie können beispielsweise jede Spaltenüberschrift anpassen.
   **Anpassen der Überschrift der Spalte ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. Nachdem Sie Änderungen vorgenommen haben, klicken Sie auf **OK**.
1. Schließen Sie alle Dialogfelder, indem Sie auf **OK** klicken.
   Schließlich kehren Sie zur Seite WebForm1.aspx zurück. 
   **Zurück zur Seite WebForm1.aspx nach Verwendung des Arbeitsblattdesigners** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Oben wird der Spaltenname der Tabelle 'Products' angezeigt. Die Spaltenbreite ist klein, sodass die vollständigen Namen einiger Spalten nicht vollständig sichtbar sind. 
### **Schritt 7: Hinzufügen von Code zum Page_Load-Ereignishandler**
Wir haben den Arbeitsblattdesigner verwendet und müssen jetzt nur noch Code zum Page_Load-Ereignishandler hinzufügen, um das Objekt 'dataSet11' mit Daten aus der Datenbank (mit 'oleDbDataAdapter1') zu füllen und das Steuerelement 'GridWeb' an 'dataSet11' zu binden, indem Sie seine DataBind-Methode aufrufen. 

1. Fügen Sie den Code hinzu: 

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

1. Überprüfen Sie den zum Page_Load-Ereignishandler hinzugefügten Code.
   **Zum Page_Load-Ereignishandler hinzugefügter Code** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Schritt 8: Ausführen der Anwendung**
Kompilieren und starten Sie die Anwendung: drücken Sie entweder **Strg+F5** oder klicken Sie auf **Start**. 
**Ausführen der Anwendung** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Nach dem Kompilieren wird die Seite WebForm1.aspx in einem Browserfenster geöffnet, und alle Daten aus der Datenbank werden geladen.
**Daten in das Steuerelement 'GridWeb' aus der Datenbank geladen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Arbeiten mit dem Steuerelement 'GridWeb'**
Wenn Daten in das Steuerelement 'GridWeb' geladen werden, bietet es den Benutzern die Kontrolle über die Daten. Das 'GridWeb' bietet eine Reihe unterschiedlicher Arten von Datenmanipulationsfunktionen. 
### **Datenüberprüfung**
Aspose.Cells.GridWeb erstellt automatisch geeignete Validierungsregeln für alle gebundenen Spalten gemäß den in der Datenbank definierten Datentypen. Sehen Sie sich den Validierungstyp einer Zelle an, indem Sie mit dem Cursor darüber fahren.
**Überprüfen des Validierungstyps einer Zelle** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Zeilen löschen**
Um eine Zeile zu löschen, wählen Sie eine Zeile (oder eine Zelle in der Zeile) aus, klicken Sie mit der rechten Maustaste und wählen Sie **Zeile löschen**.
**Auswählen der Option Zeile löschen im Menü** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Die Zeile wird sofort gelöscht.
**Rasterdaten (nachdem eine Zeile gelöscht wurde)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Bearbeiten von Zeilen**
Bearbeiten Sie Daten in Zellen oder Zeilen und klicken Sie dann auf **Speichern** oder **Senden**, um die Änderungen zu speichern. 
### **Zeilen hinzufügen**
1. Um eine Zeile hinzuzufügen, klicken Sie mit der rechten Maustaste auf eine Zelle und wählen Sie **Zeile hinzufügen**.
   **Auswählen der Option Zeile hinzufügen im Menü** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Eine neue Zeile wird am Ende der anderen Zeilen dem Blatt hinzugefügt.
**Neue Zeile dem Raster hinzugefügt** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Werte zur neuen Zeile hinzufügen.
1. Klicken Sie auf **Speichern** oder **Senden**, um die Änderung zu bestätigen.
   **Änderungen an den Daten durch Klicken auf die *Speichern**-Schaltfläche speichern* 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Nummernformat festlegen**
Derzeit werden die Preise in der Spalte **Produktpreis** als numerische Werte angezeigt. Es ist möglich, sie wie Währung aussehen zu lassen.

1. Zurück zu Visual Studio.NET gehen.
1. Öffnen Sie den BindColumn Collection Editor.
   Die Eigenschaft **NumberType** der Spalte **Product Price** ist auf **Allgemein** eingestellt.
   Die Eigenschaft NumberType ist auf Allgemein eingestellt 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. Klicken Sie auf **DropDownList** und wählen Sie **Currency4** aus der Liste aus.
   Die Eigenschaft NumberType wurde auf Currency4 geändert 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Starten Sie die Anwendung erneut.
   Die Werte in der Spalte **Product Price** sind jetzt in Währung.
   **Produktpreise im Währungsnummerformat** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Daten bearbeiten**
Die Anwendung erlaubt bisher nur das Anzeigen von Tabellendaten. Benutzer können Daten im GridWeb-Control bearbeiten, aber beim Schließen des Browsers und Öffnen der Datenbank hat sich nichts geändert. Die vorgenommenen Änderungen werden nicht in der Datenbank gespeichert. 

Das folgende Beispiel fügt Code zur Anwendung hinzu, damit das GridWeb Änderungen in der Datenbank speichern kann. 

1. Öffnen Sie das **Eigenschaften**-Fenster und wählen Sie das **SaveCommand**-Ereignis des GridWeb-Controls aus der Liste aus.
   **Auswahl des SaveCommand-Ereignisses von GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. Doppelklicken Sie auf das **SaveCommand**-Ereignis, und VS.NET erstellt den Ereignishandler GridWeb1_SaveCommand.
1. Fügen Sie diesem Ereignishandler Code hinzu, der die Datenbank mit allen geänderten Daten im an das Arbeitsblatt gebundenen DataSet unter Verwendung von oleDbDataAdapter1 aktualisiert. 

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

Sie können auch den zum GridWeb1_SaveCommand-Ereignishandler hinzugefügten Code überprüfen
**Zum GridWeb1_SaveCommand-Ereignishandler hinzugefügter Code** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Änderungen an der Datenbank mit der **Speichern**-Schaltfläche jetzt definitiv speichern.
## **Fazit**
{{% alert color="primary" %}} 

Datenbindung ist eine wichtige Funktion von Aspose.Cells.GridWeb. Es ist einfach, Arbeitsblätter mithilfe des von Aspose.Cells.GridWeb angebotenen Worksheets Designer-Dienstprogramms an eine Datenbank zu binden. Aspose.Cells.GridWeb spart Zeit und Mühe bei der Erstellung leistungsfähiger Rasterlösungen. 

{{% /alert %}}
