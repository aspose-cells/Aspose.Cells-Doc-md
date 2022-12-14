---
title: Binden eines Arbeitsblatts mit einer Datenbank mithilfe des Arbeitsblatt-Designers in VS.Net 2005
type: docs
weight: 40
url: /de/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 Dieser Artikel beschreibt einen einfachsten Ansatz zum Binden von Arbeitsblättern mit Datenbanktabellen**Visual Studio.Net 2005** mit einem speziellen Tool, das mit Aspose.Cells.GridWeb mit dem Namen as geliefert wird**Arbeitsblatt-Designer** . Dieser Artikel würde Ihnen definitiv das Gefühl geben, wie einfach es ist, die Datenbindungsfunktion in Aspose.Cells.GridWeb mit Hilfe von zu verwenden**Arbeitsblatt-Designer** .

{{% /alert %}}

## **Binden eines Arbeitsblatts mit einer Datenbank mithilfe des Arbeitsblatt-Designers in VS.Net 2005**

 Der Zweck dieses Artikels besteht darin, allen Entwicklern zu zeigen, wie Sie eine Datenbindungsanwendung in erstellen können**VS.Net 2005** und verstehen Sie die Verwendung und Rolle von**Arbeitsblatt-Designer** Editor. Der beste Weg, etwas zu lernen und zu verstehen, ist durch Beispiele. Daher erstellen wir in diesem Artikel am besten auch eine Beispielanwendung, um die Verwendung von zu demonstrieren**Arbeitsblatt-Designer**in verbindlichen Arbeitsblättern mit Datenbank. Lassen Sie uns Schritt für Schritt eine Anwendung erstellen.

### **Schritt 1: Erstellen einer Beispieldatenbank**

 Zunächst erstellen wir eine Beispieldatenbank, die in diesem Artikel verwendet wird. Wir haben MS Access verwendet, um eine Beispieldatenbank zu erstellen, die Folgendes enthält**Produkte** Tabelle, deren Schema unten gezeigt wird:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**Figur:** Designinformationen von**Produkte** Tisch

 Dem werden einige Dummy-Datensätze hinzugefügt**Produkte** Tabelle wie unten in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**Figur:** Aufzeichnungen ein**Produkte** Tisch

### **Schritt 2: Beispielanwendung entwerfen**

 Ein**ASP.NET Webanwendung** wird in Visual Studio.NET 2005 erstellt und entworfen, wie in den Abbildungen unten gezeigt. Diese Screenshots sind nützlich für Entwickler, die mit Aspose.Cells.GridWeb in Visual Studio.Net 2005 nicht sehr vertraut sind.

Starten Sie zuerst VS.Net 2005.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**Figur:** Ab VS.Net 2005

Erstellen Sie über das Menü Datei|Neu|Website... eine neue Website.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**Figur:** Erstellen einer neuen Website

 Nachdem Sie auf die Menüoption Datei|Neu|Website... geklickt haben,**Neue Website** Dialog angezeigt. Drücke den**Durchsuche** Knopf darin.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**Figur:**Dialogfeld „Neue Website“.

 Nach dem Anklicken der**Durchsuche** Wählen Sie den Standortordner im lokalen IIS aus. Sie können einen neuen Ordner erstellen und ihn wie in der Abbildung gezeigt zu einem virtuellen Ordner machen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**Figur:** Erstellen eines neuen Ordners


 Nach dem Anklicken der**Offen** Schaltfläche in der**Ort wählen** Dialog,**Neue Website** Dialog wird aussehen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**Figur:** Projektspeicherort festlegen

Jetzt wird das Projekt erstellt

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**Figur:** Erstelltes Projekt

### **XHTML- und HTML-Modi**

**Aspose.Cells.GridWeb** unterstützt vollständig den XHTML-Modus, der seit dem standardmäßig in VS.Net 2005 implementiert ist**XhtmlMode** Eigentum der**GridWeb** Steuerung eingestellt ist**WAHR** standardmäßig, wenn Sie das Steuerelement auf der Webseite platzieren. Wenn Sie jedoch den HTML-Modus für das Steuerelement in VS.Net 2005 implementieren möchten, können Sie dies ganz einfach tun. Sie müssen die ändern**<!DOCTYPE>** Tag ein bisschen im Quellcode der Webseite und setze das**XhtmlMode** Eigentum der**GridWeb** Kontrolle zu**FALSCH** .

#### **In diesem Thema verwenden wir den HTML-Modus für das Steuerelement. Befolgen Sie daher die folgenden Schritte**

##### **1. Wechseln Sie zur Quellansicht der Webseite und suchen Sie das folgende <!DOCTYPE>-Tag im Quellcode.**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

Sobald Sie dieses Tag gefunden haben, wählen Sie dieses vollständige Tag im Quellcode aus, wie unten gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**Figur:** Auswählen**<!DOCTYPE>-Tag**

 Ersetze das**<!DOCTYPE>** -Tag aus Ihrem Quellcode mit dem folgenden.

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**Figur:** Ändern**<!DOCTYPE>-Tag**

##### **2. Nachdem Sie das GridWeb-Steuerelement zum Webformular hinzugefügt haben. Sie sollten das Steuerelement auswählen und die XhtmlMode-Eigenschaft im Eigenschaftenfenster auswählen, um sie auf False zu setzen.**

**Hinzufügen von GridWeb zum WebForm** 

 Klicken Sie mit der rechten Maustaste auf**Werkzeugkasten** und auswählen**Artikel auswählen...** aus dem Menü.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**Figur:** Artikel auswählen

 Wählen Sie nun aus**GridWeb** Komponente und klicken Sie**OK**

{{% alert color="primary" %}}

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**Figur:** Auswählen**GridWeb** Komponente im Komponentendialog

 Jetzt die**GridWeb** wird hinzugefügt, wie in der Abbildung unten gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**Figur:** **GridWeb** wird in der Toolbox hinzugefügt

 Stelle das**GridWeb** im Webformular wie unten gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**Figur:** Platzierung**GridWeb** auf der Webseite

{{% /alert %}} {{% alert color="primary" %}}

**Verfahren** : Wählen Sie das Steuerelement aus. Wählen Sie nun das aus**XhtmlMode** Eigentum aus der**Eigenschaften** Fenster und stellen Sie es ein**FALSCH** Wert.

{{% /alert %}}

##### **Schritt 3: Herstellen einer Verbindung mit der Datenbank mithilfe des Server-Explorers und Festlegen des Verbindungsobjekts**

 Zuerst fügen wir die MS Access-Datenbank dem Projekt hinzu, in dem wir zuvor erstellt haben**Schritt 1** . Sie können das sehen**db.mdb** Datei wird dem Projekt hinzugefügt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**Figur:** Datenbank zum Projektordner hinzugefügt

 Nun gehen wir zu**Komponentendesigner** Fenster des Webformulars mit der Rechtsklick-Menüoption der Webseite.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**Figur:** Auswählen**Komponenten-Designer anzeigen** Möglichkeit

Das Fenster „Komponenten-Designer“ wird wie folgt angezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**Figur:** Komponenten-Designer-Fenster

 Doppelklicken Sie auf die**OleDbConnection** Komponente aus dem Datenbereich, um das oleDbConnection1-Objekt im Fenster zu platzieren.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**Figur:** oleDbConnection1-Objekt

 Jetzt ist es an der Zeit, sich mit der Datenbank zu verbinden. Wir können es einfach tun, indem wir verwenden**Server-Explorer** in Visual Studio.NET 2005. Einfach auswählen**Datenverbindung** in**Server-Explorer** und Rechtsklick. Vor Ihnen erscheint ein Kontextmenü. Auswählen**Verbindung hinzufügen...**Option aus dem Menü, wie unten in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**Figur:** Auswählen**Verbindung hinzufügen...** Option aus dem Menü


 Nach der Auswahl**Verbindung hinzufügen...** Option aus dem Menü,**Verbindung hinzufügen** Dialog wird geöffnet und**Durchsuche** , um die Datenbankdatei wie unten gezeigt auszuwählen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**Figur:** Auswahl der Datenbankdatei

Sie können die Verbindung testen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**Figur:** Testen der Verbindung

Sie können die Verbindung durchsuchen, um die Tabelle und ihre Felder zu überprüfen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**Figur:** Überprüfen der Tabelle und ihrer Felder der Verbindung

 Wenn Sie jetzt auswählen**oleDbConnection1** Objekt in der**Komponentendesigner** Fenster können Sie die Verbindungszeichenfolge auswählen, die sich auf die vorhandene Verbindung bezieht, die gerade erstellt wird. Sie befindet sich dort in der Eigenschaft "ConnectionString" der**oleDbConnection1** Objekt im Eigenschaftenfenster.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**Figur:** Auswählen der Verbindungszeichenfolge für das Objekt

 Schließlich wird der Modifikator des Objekts geändert zu**Geschützt** für eine bessere Erreichbarkeit.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**Figur:** Festlegen des Modifikators des Objekts

##### **Schritt 4: Datenadapterobjekt konfigurieren**

 Fügen Sie nun ein hinzu**OleDbDataAdapter** Komponente aus dem Datenbereich in der Toolbox, um sie zu konfigurieren. Doppelklicken Sie auf die**OleDbDataAdapter** Im Datenbereich der Toolbox startet es seinen Konfigurationsassistenten und wählt die vorhandene Verbindung aus, wie in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**Figur:** Konfigurationsassistent für Datenadapter

 Nach dem Anklicken**Nächste** klicken Sie auf die Schaltfläche**Abfrage Ersteller** um die hinzuzufügen**Produkte** Tabelle, wählen Sie Alle Spalten und klicken Sie auf**OK** Taste.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**Figur:** Produkttabelle hinzufügen

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**Figur:** Abfrage Ersteller

 Jetzt klicken**Fertig** Schaltfläche, um den Assistenten zu beenden.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**Figur:** Den Assistenten beenden

 Nach der Konfiguration des Assistenten wird oleDbDataAdapter1 automatisch zum Fenster hinzugefügt, wie unten gezeigt. Außerdem können Sie den Modifikator auf setzen**Geschützt**.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**Figur:** Abrufen des OleDbDataAdapter-Objekts im Designerfenster

##### **Schritt 5: DataSet generieren**

 Da wir Datenbankverbindungs- und Datenadapterobjekte erstellt haben, brauchen wir dennoch etwas, wo wir Daten speichern können, nachdem wir uns mit der Datenbank verbunden haben. EIN**Datensatz**Objekt kann Daten genau speichern und wir können sie auch einfach mit VS.NET 2005 IDE generieren. Wählen Sie dazu aus**oleDbDataAdaper1** und Rechtsklick. Ein Kontextmenü mit einigen Optionen wird angezeigt. Auswählen**Generieren** **Datensatz...** Option aus dem Menü, wie unten in der Abbildung gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**Figur:** Auswählen**Generieren** **Datensatz...** Option aus dem Menü

 Nach der Auswahl**Generieren** **Datensatz...** Option aus dem Menü, a**Datensatz generieren** Dialog geöffnet würde. Mit diesem Dialog können wir den Namen des neuen auswählen**Datensatz** zu erstellendes Objekt und welche Tabellen hinzugefügt werden sollen**Datensatz** . Prüfen**Fügen Sie dieses Dataset dem Designer hinzu** Option und klicken Sie auf**OK** Taste wie unten in der Abbildung gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**Figur:** Klicken**OK** Schaltfläche zum Generieren**Datensatz**

 Jetzt sieht man a**Datensatz11** Objekt, das dem Designer hinzugefügt wurde, wie unten in der Abbildung gezeigt. Stellen Sie den Objektmodifikator auf ein**Geschützt**.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**Figur:** **Datensatz** generiert und dem Designerfenster hinzugefügt

Bestimmter Code wird automatisch in der .cs-dateibezogenen Verbindung, dem Datenadapter und dem Datensatzobjekt generiert.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**Figur:** Generierter Code

##### **Schritt 6: Verwenden des Arbeitsblatt-Designers**

 Jetzt ist es an der Zeit, das Geheimnis zu lüften. Wählen Sie das Steuerelement aus und klicken Sie mit der rechten Maustaste. Ein Kontextmenü würde geöffnet werden. Wählen Sie die Option Arbeitsblatt-Designer... aus dem Menü, wie unten in der Abbildung gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**Figur:** Auswählen**Arbeitsblatt-Designer...** Option aus dem Menü

 Danach**Editor für Arbeitsblattsammlungen** Dialog (auch genannt**Arbeitsblatt-Designer** ) geöffnet wird, können Sie mehrere Eigenschaften sehen, die konfiguriert werden können, um die**Blatt1** mit jeder Tabelle in der Datenbank. Lassen Sie uns auswählen**Datenquelle** Eigentum. Schreiben**Datensatz11** darin (das wir im vorherigen Schritt generiert und zum Designerfenster hinzugefügt haben). Dann klicken Sie auf**Datenmitglied** Eigentum. Schreiben**Produkte** als Tabellenname hier, wie unten in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**Figur:** Einstellung**Datenquelle** und**Datenmitglied** Eigenschaften

 Jetzt können Sie konfigurieren**BindenSpalten** Eigentum. Nachdem Sie darauf geklickt haben, können Sie jetzt die Bindungsspalten hinzufügen und festlegen**Bildbeschriftung** , **Datenfeld** (Sollte gleich sein**Produkte** Tabellenfelder) und andere Eigenschaften. Sie können die einstellen**Wird automatisch erstellt** zu**Stimmt** und bewerben**Validierung** und setze die**NumberType**aus verschiedenen Feldern für Ihre Anforderungen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**Figur:** Klicken**BindenSpalten** Eigentum

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**Figur:** **BindColumn-Auflistungs-Editor** Dialog

##### **Schritt 7: Hinzufügen einiger Codezeilen für die Webseite**

 Wir haben benutzt**Arbeitsblatt-Designer** einfach und jetzt müssen wir nur noch ein paar Codezeilen hinzufügen

 Zuerst werden wir hinzufügen**OnInit** ereignisbezogener Code zum Initialisieren**Initialisieren der Komponente** Methode zum Initialisieren und Erstellen von Verbindungs-, Befehls-, Datenadapter- und Datensatzobjekten. Diese Codezeilen werden nicht mit dem automatisch generierten Code hinzugefügt, daher müssen wir sie manuell hinzufügen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**Figur:** Etwas Code hinzufügen1

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**Figur:** Etwas Code hinzufügen2

 Jetzt fügen wir etwas Code in die hinzu**Seite_Laden** Ereignishandler zum Füllen**Datensatz11** Objekt mit Daten aus der Datenbank (mit**oleDbDataAdapter1** ) und verbindlich**GridWeb** Kontrolle mit**Datensatz11** indem Sie es anrufen**DataBind** Methode.

{{% alert color="primary" %}}   {{% /alert %}}

##### **Beispiel:**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

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

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

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

 Sie können auch den hinzugefügten Code überprüfen**Seite_Laden** Ereignishandler wie unten in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**Figur:** Code hinzugefügt**Seite_Laden** Ereignishandler

Bei weitem haben wir eine sehr nützliche Datenbankanwendung erstellt. Mit dieser Anwendung können Sie jedoch nur die Daten der Tabelle anzeigen. Obwohl Sie Daten in bearbeiten können**GridWeb** steuern, sondern wenn Sie Ihr Browserfenster schließen und Ihre Datenbank öffnen. Sie würden feststellen, dass sich nichts geändert hat. Das bedeutet, dass die von Ihnen vorgenommenen Änderungen nicht in der Datenbank gespeichert werden. Es gibt also etwas, das Sie tun müssen.

 Jetzt werden wir unserer Anwendung etwas Code hinzufügen, damit**GridWeb** kann seine Änderungen in der aktuellen Datenbank speichern. Öffnen wir es**Eigenschaften** Bereich und wählen Sie aus**SaveCommand** Veranstaltung der**GridWeb** Steuerung aus der Liste seiner Ereignisse. Wenn Sie auf doppelklicken**SaveCommand** Ereignis dann VS.NET 2005 IDE erstellen**GridWeb1_SaveCommand** Event-Handler für Sie. Fügen Sie diesem Ereignishandler Code hinzu, um die Datenbank mit den darin enthaltenen geänderten Daten zu aktualisieren**Datensatz** (mit dem Arbeitsblatt verbunden) verwenden**oleDbDataAdapter1**.

##### **Beispiel:**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

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

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

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

 Sie können auch den hinzugefügten Code überprüfen**GridWeb1_SaveCommand** Ereignishandler wie unten in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**Figur:** Code hinzugefügt**GridWeb1_SaveCommand** Ereignishandler

 Wenn Sie nun Ihre Änderungen in der Datenbank speichern, verwenden Sie**Speichern** Knopf der**GridWeb** , sie würden definitiv gerettet werden.

##### **Schritt 8: Ausführen Ihrer Anwendung**

 Schließlich können wir unsere Anwendung kompilieren und ausführen, indem wir entweder drücken**Strg+F5** oder klicken**Anfang** Taste. Im Debugging-Dialogfeld können Sie die entsprechende Debugging-Option angeben und klicken**OK** Taste wie unten in der Abbildung gezeigt.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**Figur:** Laufende Anwendung

 Nach der Zusammenstellung**Default.aspx** Die Seite unserer Webanwendung wird in einem neuen Browserfenster geöffnet, in dem wir alle aus der Datenbank geladenen Daten wie unten gezeigt sehen können:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**Figur:** Daten geladen in**GridWeb** Steuerung aus der Datenbank

 Wenn Daten in geladen werden**GridWeb** Kontrolle, dann würden Sie das Gefühl haben, dass Aspose.Cells.GridWeb seinen Benutzern eine implizite Kontrolle über die Daten bietet. Lassen Sie uns überprüfen, welche Art von Datenbearbeitungsfunktionen angeboten werden**GridWeb** an seine Benutzer.

##### **Datenvalidierung**

Aspose.Cells. GridWeb erstellt automatisch geeignete Validierungsregeln für alle gebundenen Spalten gemäß ihren in der Datenbank definierten Datentypen. Sie können den Validierungstyp einer Zelle sehen, indem Sie Ihren Mauszeiger darauf bewegen, wie unten in der Abbildung gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**Figur:**Überprüfung des Validierungstyps einer Zelle

 In der obigen Abbildung können wir sehen, dass die ausgewählte Zelle enthält**\<INT>** Typ der Validierung, was bedeutet, dass Benutzer nur einen ganzzahligen Wert eingeben können, da sonst ein Validierungsfehler auftritt. Darüber hinaus,**\<ERFORDERLICH>** zeigt, dass der Wert von**Produkt ID** muss vom Benutzer eingereicht werden.

##### **Zeilen löschen**

 Um eine Zeile zu löschen, sollten Sie zuerst eine Zeile (oder eine beliebige Zelle der Zeile) auswählen und auswählen**Zeile löschen** Option aus dem Rechtsklickmenü wie unten gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**Figur:** Auswählen**Zeile löschen** Option aus dem Menü

 Nach der Auswahl**Zeile löschen** aus dem Menü wird die Zeile aus dem gelöscht**GridWeb** . Jetzt klicken**sparen** Knopf der**GridWeb** um diesen Datensatz in der ursprünglichen Datenbanktabelle zu löschen.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**Figur:** Rasterdaten (nachdem eine Zeile gelöscht wurde)

##### **Zeilen bearbeiten**

 Sie können auch Daten in Zellen oder Zeilen bearbeiten und dann klicken**Speichern** Schaltfläche, um Ihre Änderungen zu speichern.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**Figur:** Rasterdaten (Bearbeiten von Datensatz 1)

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**Figur:** Rasterdaten (Bearbeiten von Datensatz2)

##### **Zeilen hinzufügen**

 Um eine Zeile hinzuzufügen, wählen Sie aus**Zeile hinzufügen** Option aus dem Rechtsklickmenü wie unten gezeigt:

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**Figur:** Auswählen**Zeile hinzufügen** Option aus dem Menü

Nach der Auswahl wird dem Blatt am Ende der Zeilen eine neue Zeile hinzugefügt**Zeile hinzufügen** Option aus dem Menü. Auf der linken Seite der neu hinzugefügten Zeile würden Sie ein bemerken**Sternchen** Markierung, die angibt, dass die Zeile neu hinzugefügt wurde.

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**Figur:** Neue Zeile zum Raster hinzugefügt

 Nachdem Sie die Werte in die neue Zeile eingegeben haben, klicken Sie auf**Speichern** Schaltfläche, um die Änderungen in der ursprünglichen Datenbanktabelle wie unten gezeigt zu bestätigen

![todo: Bild_alt_Text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**Figur:** Änderungen an Datenbanktabelle speichern durch Anklicken**Speichern** Taste

{{% alert color="primary" %}}   {{% /alert %}}

##### **Fazit**

{{% alert color="primary" %}}

**Datenbindung** ist ein wichtiges Feature von Aspose.Cells.GridWeb . Es ist wirklich mühelos für Entwickler, ihre Arbeitsblätter mit der Datenbank zu binden**Arbeitsblatt-Designer** Dienstprogramm angeboten von Aspose.Cells.GridWeb . Aspose.Cells.GridWeb ist sehr hilfreich für die Entwickler, um ihre Zeit und Mühe bei der Erstellung leistungsstarker Grid-Lösungen zu sparen.

{{% /alert %}}
