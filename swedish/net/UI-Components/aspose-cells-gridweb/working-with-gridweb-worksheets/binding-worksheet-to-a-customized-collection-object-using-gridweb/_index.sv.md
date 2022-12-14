---
title: Bindande arbetsblad till ett anpassat samlingsobjekt med GridWeb
type: docs
weight: 130
url: /sv/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Microsoft .NET Framework erbjuder många samlingsklasser men ibland uppfyller de inte utvecklingskraven så utvecklare skapar**anpassade samlingar**, och kan behöva binda sådana anpassade samlingar med Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Bindning av ett kalkylblad med en anpassad samling**
För att illustrera denna funktion går den här artikeln igenom hur man skapar en exempelapplikation, steg för steg. Skapa först en anpassad samling och använd sedan samlingen för att binda med ett kalkylblad.
### **Steg 1: Skapa en anpassad post**
Innan du skapar en anpassad samling, skapa en klass för att hålla de anpassade poster som kommer att lagras i samlingen. Syftet med den här artikeln är att ge en uppfattning om hur du skapar dina egna anpassade samlingar och binder dem med Aspose.Cells.GridWeb, så hur du skapar den anpassade posten är upp till dig.

Exemplet nedan använder klassen MyCustomRecord som innehåller fem privata fält och fem publika egenskaper som styr åtkomsten till de privata fälten. Här är strukturen för fastigheter:

-  Egenskapen StringField1 för att läsa och skriva**strängfält1** (sträng).
-  Egenskapen ReadonlyField2 för att endast läsa**stringfield2** (sträng).
-  Egenskapen DateField1 för att läsa och skriva**datumfält1** (Datum Tid).
-  Egenskapen IntField1 för att läsa och skriva**intfield1** (heltal).
-  DoubleField1-egenskapen för att läsa och skriva**dubbelfält1** (dubbel).

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
### **Steg 2: Skapa en anpassad samling**
Skapa nu en anpassad samling att lägga till kundposter till och komma åt dem från. För att göra det enkelt använder detta exempel klassen MyCollection som innehåller en skrivskyddad indexerare. Med denna indexerare kan vi få vilken anpassad post som helst som lagras i samlingen.

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
### **Steg 3: Bind ett kalkylblad med en anpassad samling**
Processen att skapa en anpassad samling är klar. Använd nu den anpassade samlingen för att binda till ett kalkylblad i Aspose.Cells.GridWeb. Skapa först ett webbformulär, lägg till GridWeb-kontrollen till det och lägg till lite kod.

För att använda den anpassade samlingen för bindning, skapa först ett objekt av klassen MyCollection (skapat i steget ovan).
Skapa och lägg sedan till MyCustomRecord-objekt till MyCollection-objektet.

{{% alert color="primary" %}} 

Undrar du varför det inte fanns en metod i MyCollection-klassen för att lägga till ett MyCustomRecord-objekt till samlingen. Ta en titt på koden ovan och du kommer att märka att MyCollection-klassen ärvs från CollectionBase-klassen (som har implementerat IList-gränssnittet som tillhandahåller en Add-metod för att lägga till ett objekt i samlingen). Använd IList-klassens Add-metod genom att skicka upp MyCollection-objektet till IList.

{{% /alert %}} 

Slutligen ställer du in MyCollection-objektet som kalkylbladets datakälla och binder kalkylbladet med samlingen. Vid det här laget kan du också skapa valideringsregler för de bundna kolumnerna i kalkylbladet.

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
### **Steg 4: Hantera kalkylbladets InitializeNewBindRow-händelse**
I koden ovan kanske du har märkt en extra kodrad som används för att tilldela händelsehanteraren GridWeb1_InitializeNewBindRow till kalkylbladets InitializeNewBindRow. Denna händelse utlöses när en ny bunden rad läggs till i kalkylbladet. Vi skapade en händelsehanterare för denna händelse på grund av MyCustomRecord-objektets DateField1-egenskap.

 Aspose.Cells.GridWeb initieras automatiskt**int** och**dubbel** värden med**noll (0)**när en ny bunden rad läggs till i GridWeb-kontrollen. För datum vill vi att GridWeb-kontrollen automatiskt lägger till det aktuella datumet från systemet. För att göra det har vi skapat GridWeb1_InitializeNewBindRow-händelsehanteraren för InitializeNewBindRow-händelsen.

Få åtkomst till en viss instans av klassen MyCustomRecord från GridWeb med hjälp av argumentet bindObject och tilldela sedan det aktuella systemdatumet till dess DateField1-egenskap.

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
### **Steg 5: Kör applikationen**
 Kör programmet genom att antingen trycka på**Ctrl+F5** eller klicka på**Start** knappen i VS.NET. Webbformuläret öppnas i ett nytt webbläsarfönster.

**Arbetsblad inbundet med en anpassad samling** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Högerklicka på GridWeb-kontrollen för att lägga till eller ta bort en post. Lägg till exempel till en ny post i kalkylbladet genom att välja**Lägg till rad** alternativ.

**Välj alternativet Lägg till rad från menyn** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 När en ny rad läggs till i kalkylbladet innehåller cellerna standarddata inklusive aktuellt systemdatum.

**Ny rad har lagts till i kalkylbladet med standarddata** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



När du har gjort ändringar i data klickar du**Spara** eller**Skicka in** för att spara dina ändringar.

**Spara ändringar genom att klicka på knappen Spara** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Slutsats**
{{% alert color="primary" %}} 

Den här artikeln visade hur man binder ett kalkylblad till en anpassad samling skapad. Med hjälp av Aspose.Cells.GridWeb kan utvecklare binda kalkylblad till antingen en databas eller anpassade samlingar via kalkylbladsdesignern i ett GUI-läge eller genom kodning. Detta ger ett brett utbud av alternativ för utvecklare för att skapa applikationer.

{{% /alert %}}
