---
title: Binden des Arbeitsblatts an ein benutzerdefiniertes Sammlungsobjekt mithilfe von GridWeb
type: docs
weight: 130
url: /de/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Das Microsoft .NET Framework bietet viele Sammlungsklassen, aber manchmal erfüllen sie nicht die Entwicklungsanforderungen, die Entwickler erstellen**benutzerdefinierte Sammlungen**, und erfordert möglicherweise, solche benutzerdefinierten Sammlungen mit Aspose.Cells.GridWeb zu binden.

{{% /alert %}} 
## **Binden eines Arbeitsblatts mit einer benutzerdefinierten Sammlung**
Um diese Funktion zu veranschaulichen, wird in diesem Artikel Schritt für Schritt beschrieben, wie Sie eine Beispielanwendung erstellen. Erstellen Sie zuerst eine benutzerdefinierte Sammlung und verwenden Sie diese Sammlung dann zum Binden mit einem Arbeitsblatt.
### **Schritt 1: Erstellen eines benutzerdefinierten Datensatzes**
Erstellen Sie vor dem Erstellen einer benutzerdefinierten Sammlung eine Klasse für die benutzerdefinierten Datensätze, die in der Sammlung gespeichert werden. Der Zweck dieses Artikels besteht darin, Ihnen eine Vorstellung davon zu vermitteln, wie Sie Ihre eigenen benutzerdefinierten Sammlungen erstellen und sie mit Aspose.Cells.GridWeb binden können. Wie Sie den benutzerdefinierten Datensatz erstellen, liegt also bei Ihnen.

Das folgende Beispiel verwendet die MyCustomRecord-Klasse, die fünf private Felder und fünf öffentliche Eigenschaften enthält, die den Zugriff auf die privaten Felder steuern. Hier ist die Struktur der Eigenschaften:

-  Die StringField1-Eigenschaft zum Lesen und Schreiben**Zeichenkettenfeld1** (Schnur).
-  Die ReadonlyField2-Eigenschaft, die nur gelesen werden soll**Zeichenfolgenfeld2** (Schnur).
-  Die DateField1-Eigenschaft zum Lesen und Schreiben**Datumsfeld1** (Terminzeit).
-  Die IntField1-Eigenschaft zum Lesen und Schreiben**intfield1** (ganze Zahl).
-  Die DoubleField1-Eigenschaft zum Lesen und Schreiben**Doppelfeld1** (doppelt).

**C#**

{{< highlight "csharp" >}}

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
### **Schritt 2: Erstellen einer benutzerdefinierten Sammlung**
Erstellen Sie jetzt eine benutzerdefinierte Sammlung, um Kundendatensätze hinzuzufügen und darauf zuzugreifen. Der Einfachheit halber verwendet dieses Beispiel die MyCollection-Klasse, die einen schreibgeschützten Indexer enthält. Mit diesem Indexer können wir jeden benutzerdefinierten Datensatz abrufen, der in der Sammlung gespeichert ist.

**C#**

{{< highlight "csharp" >}}

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
### **Schritt 3: Binden eines Arbeitsblatts mit einer benutzerdefinierten Sammlung**
Der Vorgang zum Erstellen einer benutzerdefinierten Sammlung ist abgeschlossen. Verwenden Sie nun die benutzerdefinierte Sammlung zum Binden an ein Arbeitsblatt in Aspose.Cells.GridWeb . Erstellen Sie zuerst ein Webformular, fügen Sie das GridWeb-Steuerelement hinzu und fügen Sie etwas Code hinzu.

Um die benutzerdefinierte Sammlung für die Bindung zu verwenden, erstellen Sie zunächst ein Objekt der MyCollection-Klasse (im obigen Schritt erstellt).
Erstellen Sie dann MyCustomRecord-Objekte und fügen Sie sie dem MyCollection-Objekt hinzu.

{{% alert color="primary" %}} 

Fragen Sie sich, warum es in der MyCollection-Klasse keine Methode zum Hinzufügen eines MyCustomRecord-Objekts zur Sammlung gab. Wenn Sie sich den obigen Code noch einmal ansehen, werden Sie feststellen, dass die MyCollection-Klasse von der CollectionBase-Klasse geerbt ist (die die IList-Schnittstelle implementiert hat, die eine Add-Methode zum Hinzufügen eines Objekts zur Sammlung bereitstellt). Verwenden Sie die Add-Methode der IList-Klasse, indem Sie das MyCollection-Objekt in IList umwandeln.

{{% /alert %}} 

Legen Sie abschließend das MyCollection-Objekt als Datenquelle des Arbeitsblatts fest und binden Sie das Arbeitsblatt an die Sammlung. An dieser Stelle können Sie auch Validierungsregeln für die gebundenen Spalten des Arbeitsblatts erstellen.

**C#**

{{< highlight "csharp" >}}

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
### **Schritt 4: Behandeln des InitializeNewBindRow-Ereignisses des Arbeitsblatts**
Im obigen Code ist Ihnen möglicherweise eine zusätzliche Codezeile aufgefallen, mit der der Ereignishandler GridWeb1_InitializeNewBindRow der InitializeNewBindRow des Arbeitsblatts zugewiesen wird. Dieses Ereignis wird ausgelöst, wenn dem Arbeitsblatt eine neue gebundene Zeile hinzugefügt wird. Wir haben für dieses Ereignis aufgrund der DateField1-Eigenschaft des MyCustomRecord-Objekts eine Ereignisbehandlungsroutine erstellt.

 Aspose.Cells. GridWeb wird automatisch initialisiert**int** und**doppelt** Werte mit**Null (0)**immer dann, wenn dem GridWeb-Steuerelement eine neue gebundene Zeile hinzugefügt wird. Für Datumsangaben möchten wir, dass das GridWeb-Steuerelement automatisch das aktuelle Datum aus dem System hinzufügt. Dazu haben wir den Ereignishandler GridWeb1_InitializeNewBindRow für das Ereignis InitializeNewBindRow erstellt.

Greifen Sie mit dem bindObject-Argument auf eine bestimmte Instanz der MyCustomRecord-Klasse aus dem GridWeb zu, und weisen Sie dann das aktuelle Systemdatum der DateField1-Eigenschaft zu.

**C#**

{{< highlight "csharp" >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **Schritt 5: Ausführen der Anwendung**
 Führen Sie die Anwendung aus, indem Sie entweder drücken**Strg+F5** oder klicken Sie auf die**Anfang** Taste in VS.NET. Das Webformular wird in einem neuen Browserfenster geöffnet.

**Arbeitsblatt mit einer benutzerdefinierten Sammlung gebunden** 

![todo: Bild_alt_Text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Klicken Sie mit der rechten Maustaste auf das GridWeb-Steuerelement, um einen Datensatz hinzuzufügen oder zu löschen. Fügen Sie dem Arbeitsblatt beispielsweise einen neuen Datensatz hinzu, indem Sie auswählen**Zeile hinzufügen** Möglichkeit.

**Wählen Sie die Option Zeile hinzufügen aus dem Menü** 

![todo: Bild_alt_Text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 Wenn dem Arbeitsblatt eine neue Zeile hinzugefügt wird, enthalten die Zellen Standarddaten, einschließlich des aktuellen Systemdatums.

**Neue Zeile mit Standarddaten zum Arbeitsblatt hinzugefügt** 

![todo: Bild_alt_Text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Nachdem Sie Änderungen an den Daten vorgenommen haben, klicken Sie auf**Speichern** oder**Einreichen** um Ihre Änderungen zu speichern.

**Speichern Sie die Änderungen, indem Sie auf die Schaltfläche Speichern klicken** 

![todo: Bild_alt_Text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Fazit**
{{% alert color="primary" %}} 

In diesem Artikel wurde gezeigt, wie Sie ein Arbeitsblatt an eine erstellte benutzerdefinierte Sammlung binden. Mit Aspose.Cells.GridWeb können Entwickler Arbeitsblätter über den Worksheets Designer in einem GUI-Modus oder durch Codierung entweder an eine Datenbank oder an benutzerdefinierte Sammlungen binden. Dies bietet Entwicklern eine breite Palette von Optionen zum Erstellen von Anwendungen.

{{% /alert %}}
