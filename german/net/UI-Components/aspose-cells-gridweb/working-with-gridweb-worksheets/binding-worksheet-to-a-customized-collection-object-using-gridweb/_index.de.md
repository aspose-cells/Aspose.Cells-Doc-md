---
title: Arbeitsblatt an ein angepasstes Sammlungsobjekt binden, indem GridWeb verwendet wird
type: docs
weight: 130
url: /de/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: Dieser Artikel zeigt, wie man ein Arbeitsblatt an eine Sammlung in GridWeb bindet. 
---

{{% alert color="primary" %}} 

Das Microsoft .NET Framework bietet viele Sammlungsklassen, aber manchmal entsprechen sie nicht den Entwicklungsanforderungen. Entwickler erstellen dann **benutzerdefinierte Sammlungen**, und Sie können ein Arbeitsblatt mit solchen benutzerdefinierten Sammlungen in GridWeb verbinden.

{{% /alert %}} 
## **Ein Arbeitsblatt mit einer benutzerdefinierten Sammlung verbinden**
Um dieses Feature zu illustrieren, geht dieser Artikel Schritt für Schritt durch, wie man eine Beispielanwendung erstellt. Erstens, erstellen Sie eine benutzerdefinierte Sammlung und nutzen Sie dann diese Sammlung, um sie an ein Arbeitsblatt zu binden.
### **Schritt 1: Erstellen eines benutzerdefinierten Datensatzes**
Bevor Sie eine benutzerdefinierte Sammlung erstellen, erstellen Sie eine Klasse, um die benutzerdefinierten Datensätze zu halten, die in der Sammlung gespeichert werden. Das Ziel dieses Artikels ist, eine Vorstellung davon zu vermitteln, wie Sie Ihre eigenen benutzerdefinierten Sammlungen erstellen und sie mit GridWeb verbinden können, daher liegt es bei Ihnen, wie Sie den benutzerdefinierten Datensatz erstellen.

Das folgende Beispiel verwendet die Klasse MyCustomRecord, die fünf private Felder und fünf öffentliche Eigenschaften enthält, die den Zugriff auf die privaten Felder steuern. Hier ist die Struktur der Eigenschaften:

- Die StringField1-Eigenschaft zum Lesen und Schreiben von **stringfield1** (Zeichenfolge).
- Die ReadonlyField2-Eigenschaft zum nur Lesen von **stringfield2** (Zeichenfolge).
- Die DateField1-Eigenschaft zum Lesen und Schreiben von **datefield1** (DateTime).
- Die IntField1-Eigenschaft zum Lesen und Schreiben von **intfield1** (ganze Zahl).
- Die DoubleField1-Eigenschaft zum Lesen und Schreiben von **doublefield1** (Dezimalzahl).

**C#**

{{< highlight csharp >}}

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
Erstellen Sie jetzt eine benutzerdefinierte Sammlung, um Kundendatensätze hinzuzufügen und von ihnen zuzugreifen. Um es einfach zu halten, verwendet dieses Beispiel die Klasse MyCollection, die einen schreibgeschützten Indexer enthält. Mit diesem Indexer können wir jeden benutzerdefinierten Datensatz aus der Sammlung abrufen.

**C#**

{{< highlight csharp >}}

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
### **Schritt 3: Ein Arbeitsblatt mit einer benutzerdefinierten Sammlung verbinden**
Der Vorgang des Erstellens einer benutzerdefinierten Sammlung ist abgeschlossen. Verwenden Sie nun die benutzerdefinierte Sammlung, um sie an ein Arbeitsblatt in Aspose.Cells.GridWeb zu binden. Erstellen Sie zunächst ein Webformular, fügen Sie dem Formular die GridWeb-Steuerelement hinzu und fügen Sie etwas Code hinzu.

Um die benutzerdefinierte Sammlung für die Bindung zu verwenden, erstellen Sie zuerst ein Objekt der Klasse MyCollection (die im obigen Schritt erstellt wurde).
Erstellen und fügen Sie dann MyCustomRecord-Objekte zum MyCollection-Objekt hinzu.

{{% alert color="primary" %}} 

Fragen Sie sich, warum in der Klasse MyCollection keine Methode zum Hinzufügen eines MyCustomRecord-Objekts zur Sammlung vorhanden war? Werfen Sie noch einmal einen Blick auf den obigen Code und Sie werden feststellen, dass die MyCollection-Klasse von der CollectionBase-Klasse abgeleitet ist (die das IList-Interface implementiert hat, das eine Add-Methode zum Hinzufügen eines Objekts zur Sammlung bereitstellt). Verwenden Sie die Add-Methode der IList-Klasse, indem Sie das MyCollection-Objekt zu IList aufwerten.

{{% /alert %}} 

Legen Sie abschließend das MyCollection-Objekt als Datenquelle des Arbeitsblatts fest und binden Sie das Arbeitsblatt an die Sammlung. Zu diesem Zeitpunkt können Sie auch Validierungsregeln für die gebundenen Spalten des Arbeitsblatts erstellen.

**C#**

{{< highlight csharp >}}

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
### **Schritt 4: Behandlung des InitializeNewBindRow-Ereignisses des Arbeitsblatts**
Im obigen Code haben Sie möglicherweise eine zusätzliche Codezeile bemerkt, die verwendet wurde, um den Ereignishandler GridWeb1_InitializeNewBindRow dem InitializeNewBindRow des Arbeitsblatts zuzuweisen. Dieses Ereignis wird ausgelöst, wenn eine neue gebundene Zeile zum Arbeitsblatt hinzugefügt wird. Wir haben einen Ereignishandler für dieses Ereignis erstellt, aufgrund der Eigenschaft DateField1 des MyCustomRecord-Objekts.

Aspose.Cells.GridWeb initialisiert automatisch **int** und **double** Werte mit **Null (0)**, wenn eine neue gebundene Zeile dem GridWeb-Steuerelement hinzugefügt wird. Für Datumswerte möchten wir jedoch, dass das GridWeb-Steuerelement automatisch das aktuelle Datum vom System hinzufügt. Dazu haben wir den Ereignishandler GridWeb1_InitializeNewBindRow für das InitializeNewBindRow-Ereignis erstellt.

Greifen Sie mit dem Argument bindObject auf eine bestimmte Instanz der Klasse MyCustomRecord aus dem GridWeb zu und weisen Sie dann dem DateField1-Eigenschaft das aktuelle Systemdatum zu.

**C#**

{{< highlight csharp >}}

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
Führen Sie die Anwendung aus, indem Sie entweder **Strg+F5** drücken oder auf die **Start**-Schaltfläche in VS.NET klicken. Das Webformular wird in einem neuen Browserfenster geöffnet. 

**Arbeitsblatt an benutzerdefinierte Sammlung gebunden** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



Klicken Sie mit der rechten Maustaste auf das GridWeb-Steuerelement, um einen Datensatz hinzuzufügen oder zu löschen. Fügen Sie beispielsweise ein neues Aufzeichnung zum Arbeitsblatt hinzu, indem Sie die Option **Zeile hinzufügen** auswählen. 

**Auswahl der Option Zeile hinzufügen im Menü** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



Wenn eine neue Zeile zum Arbeitsblatt hinzugefügt wird, enthalten die Zellen Standarddaten, einschließlich des aktuellen Systemdatums. 

**Neue Zeile mit Standarddaten zum Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Nachdem Sie Änderungen an den Daten vorgenommen haben, klicken Sie auf **Speichern** oder **Übermitteln**, um Ihre Änderungen zu speichern. 

**Speichern von Änderungen durch Klicken der Schaltfläche Speichern** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Fazit**
{{% alert color="primary" %}} 

In diesem Artikel wurde gezeigt, wie ein Arbeitsblatt an eine erstellte benutzerdefinierte Sammlung gebunden wird. Mit Aspose.Cells.GridWeb können Entwickler Arbeitsblätter entweder über den Arbeitsblatt-Designer im GUI-Modus oder durch Codierung an eine Datenbank oder benutzerdefinierte Sammlungen binden. Dies bietet Entwicklern eine Vielzahl von Optionen für die Erstellung von Anwendungen.

{{% /alert %}}
