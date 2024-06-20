---
title: Bindning av arbetsblad till en anpassad samling med objekt med hjälp av GridWeb
type: docs
weight: 130
url: /sv/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: Den här artikeln introducerar hur du binder arbetsblad till samling i GridWeb. 
---

{{% alert color="primary" %}} 

Microsoft .NET Framework erbjuder många samlingar, men ibland uppfyller de inte utvecklingsbehovet, så utvecklare skapar **anpassade samlingar** och du kan binda ett arbetsblad med sådana anpassade samlingar i GridWeb.

{{% /alert %}} 
## **Bindning av ett arbetsblad med en anpassad samling**
För att illustrera den här funktionen går den här artikeln igenom hur man skapar en exempelapplikation steg för steg. Först skapar du en anpassad samling och sedan använder du den samlingen för att binda med ett arbetsblad.
### **Steg 1: Skapa en anpassad post**
Innan du skapar en anpassad samling, skapa en klass för att hålla de anpassade posterna som kommer att lagras i samlingen. Syftet med den här artikeln är att ge en idé om hur du skapar dina egna anpassade samlingar och binder dem med GridWeb, så hur du skapar den anpassade posten är upp till dig.

Nedan används klassen MyCustomRecord som innehåller fem privata fält och fem publika egenskaper som kontrollerar åtkomst till de privata fälten. Här är strukturen för egenskaperna:

- Egenskapen StringField1 för att läsa och skriva till **stringfield1** (sträng).
- Egenskapen ReadonlyField2 för att endast läsa från **stringfield2** (sträng).
- Egenskapen DateField1 för att läsa och skriva **datefield1** (DateTime).
- Egenskapen IntField1 för att läsa och skriva **intfield1** (integer).
- Egenskapen DoubleField1 för att läsa och skriva **doublefield1** (double).

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
### **Steg 2: Skapa en anpassad samling**
Skapa nu en anpassad samling att lägga till kundposter och få åtkomst till dem. För att göra det enkelt används i detta exempel klassen MyCollection, som innehåller en skrivskyddad indexering. Med hjälp av denna indexer kan vi hämta vilken anpassad post som helst som lagras i samlingen.

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
### **Steg 3: Bind en arbetsbok med en anpassad samling**
Processen för att skapa en anpassad samling är klar. Använd nu den anpassade samlingen för att binda till en arbetsbok i Aspose.Cells.GridWeb. Först skapa ett webbformulär, lägg till GridWeb-kontrollen och lägg till lite kod.

För att använda den anpassade samlingen för bindning, skapa först ett objekt av klassen MyCollection (skapad i ovanstående steg).
Skapa sedan och lägg till objekt av typen MyCustomRecord till objektet MyCollection.

{{% alert color="primary" %}} 

Undrar du varför det inte fanns en metod i klassen MyCollection för att lägga till ett objekt av typen MyCustomRecord i samlingen. Titta igen på koden ovan och du kommer att märka att klassen MyCollection ärver från CollectionBase-klassen (som har implementerat IList-gränssnittet som tillhandahåller en Add-metod för att lägga till ett objekt i samlingen). Använd IList-klassens Add-metod genom att uppvakta MyCollection-objektet till IList.

{{% /alert %}} 

Slutligen, ange MyCollection-objektet som arbetsbokens datakälla och bind arbetsboken med samlingen. Vid det här laget kan du också skapa valideringsregler för de bundna kolumnerna i arbetsboken.

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
### **Steg 4: Hantera händelsen InitializeNewBindRow för arbetsboken**
I koden ovan kan du ha lagt märke till en extra rad kod som används för att tilldela händelsehanteraren GridWeb1_InitializeNewBindRow till arbetsbokens InitializeNewBindRow-händelse. Denna händelse utlöses varje gång en ny bunden rad läggs till arbetsboken. Vi skapade en händelsehanterare för denna händelse på grund av egenskapen DateField1 för objektet MyCustomRecord.

Aspose.Cells.GridWeb initialiserar automatiskt **int** och **double** värden till **noll (0)** när en ny bunden rad läggs till GridWeb-kontrollen. För datum vill vi att GridWeb-kontrollen automatiskt lägger till det aktuella datumet från systemet. För att göra detta har vi skapat händelsehanteraren GridWeb1_InitializeNewBindRow för händelsen InitializeNewBindRow.

Få åtkomst till en särskild instans av klassen MyCustomRecord från GridWeb genom att använda bindObject-argumentet och tilldela sedan det aktuella systemdatumet till dess egenskap DateField1.

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
### **Steg 5: Kör applikationen**
Kör applikationen genom att antingen trycka på **Ctrl+F5** eller klicka på **Start**-knappen i VS.NET. Webbformuläret öppnas i ett nytt webbläsarfönster. 

**Arbetsbok bunden med en anpassad samling** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



Högerklicka på GridWeb-kontrollen för att lägga till eller ta bort en post. Till exempel, lägga till en ny post till arbetsboken genom att välja **Lägg till rad** alternativet. 

**Väljer Lägg till rad-alternativet från menyn** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



När en ny rad läggs till arbetsboken innehåller cellerna standarddata inklusive det aktuella systemdatumet. 

**Ny rad tillagd i arbetsbok med standarddata** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Efter att ha gjort ändringar i datan, klicka på **Spara** eller **Skicka** för att spara dina ändringar. 

**Sparar ändringar genom att klicka på Spara-knappen** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Slutsats**
{{% alert color="primary" %}} 

Den här artikeln visade hur man binder en arbetsbok till en anpassad samling. Med hjälp av Aspose.Cells.GridWeb kan utvecklare binda arbetsböcker antingen till en databas eller anpassade samlingar via Worksheets Designer i GUI-läge eller genom kodning. Detta ger utvecklare ett brett utbud av alternativ för att skapa applikationer.

{{% /alert %}}
