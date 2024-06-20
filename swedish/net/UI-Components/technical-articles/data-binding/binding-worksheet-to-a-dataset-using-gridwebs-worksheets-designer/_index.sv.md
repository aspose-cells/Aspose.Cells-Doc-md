---
title: Bindning av arbetsblad till en DataSet med hjälp av GridWebs arbetsbladsdesigner
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: Den här artikeln introducerar hur man använder arbetsbladsdesignern för att binda arbetsblad till en DataSet i GridWeb.
---

{{% alert color="primary" %}} 

Den här artikeln diskuterar en enkel metod för att binda arbetsblad till databastabeller i GUI-läge med hjälp av ett särskilt verktyg som medföljer Aspose.Cells.GridWeb, arbetsbladsdesignern. 

{{% /alert %}} 
## **Binda ett arbetsblad med databas med hjälp av arbetsbladsdesignern**
	**Steg 1: Skapa en provdatabas**
1. Först skapar vi den provdatabas som kommer att användas i den här artikeln. Vi använder Microsoft Access för att skapa en databas som innehåller en tabell som kallas Produkter. Dess schema visas nedan.
   **Designinformation för Produkter-tabellen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Några dummyposter läggs till i Produkter-tabellen.
   **Poster i Produkter-tabellen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Steg 2: Design av provapplikation**
En ASP.NET-webbapplikation skapas och designas i Visual Studio.NET enligt nedan. 
**Designad provapplikation** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Steg 3: Anslutning till databas med Server Explorer**
Det är dags att ansluta till databasen. Vi kan enkelt göra det med hjälp av Server Explorer i Visual Studio.NET. 

1. Välj **Dataanslutning** i **Server Explorer** och högerklicka.
1. Välj **Lägg till anslutning** från menyn.
   **Att välja alternativet Lägg till anslutning** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



Dialogrutan Egenskaper för dataanslutning visas. 
**Dialogrutan Egenskaper för dataanslutning** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



Med hjälp av denna dialogruta kan du ansluta till valfri databas. Som standard kan du ansluta till en SQL Server-databas. För det här exemplet behöver vi ansluta till en Microsoft Access-databas. 

1. Klicka på fliken **Leverantör**.
1. Välj **Microsoft Jet 4.0 OLE DB Provider** från listan över **OLE DB-leverantör(er)**.
1. Klicka på **Nästa**.
   **Klicka på Nästa efter att ha valt en OLE DB-leverantör** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


Fliken **Anslutning** öppnas. 

1. Välj filen för Microsoft Access-databasen (i vårt fall db.mdb) och klicka på **OK**.
   **Klicka på OK-knappen efter att ha valt databasfil** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

Efter att ha klickat på **OK** skapas en databasanslutning till Microsoft Access-databasen i **Server Explorer**. Dubbelklicka på anslutningen för att se alla tabeller, vyer och lagrade procedurer i databasen.

{{% /alert %}} 
### **Steg 4: Skapande av databasanslutningsobjekt grafiskt**
1. Bläddra i tabellerna i databasen med hjälp av **Server Explorer**.
   Det finns endast en tabell, Produkter. 
1. Dra och släpp tabellen Produkter från **Server Explorer** till **Webbformuläret**.
   **Dra tabellen Produkter från Server Explorer och släpp till webbformuläret** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



En dialogruta kan visas.
**Dialogruta för att bekräfta inkludering av databaslösenord i anslutningssträng** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Decidera om du vill inkludera ett databaslösenord i anslutningssträngen eller inte. För det här exemplet valde vi **Inkludera inte lösenord**. 
Två databasanslutningsobjekt (oleDbConnection1 och oleDbDataAdapter1) har skapats och lagts till.
**Databasanslutningsobjekt (oleDbConnection1 och oleDbDataAdapter1) skapade och visas** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Steg 5: Generering av DataSet**
Hittills har vi skapat anslutningsobjekt till databasen men behöver fortfarande någonstans att lagra data efter anslutning till databasen. En DataSet-objekt kan lagra data exakt och vi kan också generera det lätt med hjälp av VS.NET IDE. 

1. Välj **oleDbDataAdaper1** och högerklicka.
1. Välj **Skapa DataSet** alternativet från menyn.
   **Val av Skapa DataSet-alternativ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



Skapa DataSet-dialogen visas. 
Här är det möjligt att välja ett namn för det nya DataSet-objekt som ska skapas, och vilka tabeller som ska läggas till det. 

1. Välj **Lägg till detta dataset till formgivaren** alternativet.
1. Klicka på **OK**.
   **Klicka på OK-knappen för att generera DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



En dataSet11-objekt läggs till formgivaren.
**DataSet genererat och tillagt till formgivaren** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Steg 6: Användning av Worksheet-formgivaren**
Nu är det dags att öppna den hemliga. 

1. Välj GridWeb-kontrollen och högerklicka.
1. Välj **Worksheet-formgivaren** alternativet från menyn. 

   **Val av Worksheet-formgivaralternativ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



Arbetsbokssamlingsredigeraren (även kallad Worksheets Designer) visas. 
**Worksheet Collection Editor-dialog** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



Dialogen innehåller flera egenskaper som kan konfigureras för att binda Sheet1 till valfri tabell i databasen.

1. Välj **DataSource**-egenskapen.
   dataSet11-objektet som genererades i det föregående steget listas på menyn. 
1. Välj dataSet11.
1. Klicka på **DataMember**-egenskapen.
   Worksheet-formgivaren visar automatiskt en lista över tabeller i dataSet11. Det finns bara en tabell, Products.
1. Välj tabellen Products.
   **Inställning av DataSource- och DataMember-egenskaper** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. Kryssa i **BindColumns**-egenskapen.
   **Klicka på BindColumns-egenskapen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



Klicka på **BindColumns**-egenskapen öppnar BindColumn Collection Editor.
**BindColumn Collection Editor** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



I BindColumn Collection Editor, läggs alla kolumner i tabellen Products automatiskt till BindColumns-samlingen. 

1. Välj en kolumn och anpassa dess egenskaper.
   Till exempel kan du ändra varje kolumnrubrik.
   Ändra kolumnrubriken för ProductID-kolumnen 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. Klicka på OK efter att ha gjort ändringarna.
1. Stäng alla dialogrutor genom att klicka på OK.
   Till sist återvänder du till sidan WebForm1.aspx. 
   Tillbaka till sidan WebForm1.aspx efter att ha använt Worksheets Designer 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Ovan visas namnet på Products tabellkolumn. Kolumnernas bredd är liten så hela namnen på vissa kolumner syns inte helt. 
### **Steg 7: Lägga till kod till Page_Load Event Handler**
Vi har använt Worksheets Designer och behöver nu bara lägga till kod till Page_Load-händelsen för att fylla dataSet11-objektet med data från databasen (använda oleDbDataAdapter1) och binda GridWeb-kontrollen till dataSet11 genom att anropa dess DataBind-metod. 

1. Lägg till koden: 

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

1. Kontrollera koden som har lagts till Page_Load-eventet.
   Kod som har lagts till Page_Load-händelsen 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Steg 8: Köra applikationen**
Kompilera och kör applikationen: tryck på Ctrl+F5 eller klicka på Start. 
Köra applikationen 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Efter kompilering öppnas sidan WebForm1.aspx i en webbläsarflik med alla data hämtade från databasen.
Data laddat i GridWeb-kontrollen från databasen 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Arbeta med GridWeb Control**
När data laddas in i GridWeb-kontrollen ger den användarna kontroll över datan. GridWeb erbjuder ett antal olika typer av datamanipuleringsfunktioner. 
### **Data validering**
Aspose.Cells.GridWeb skapar automatiskt lämpliga valideringsregler för alla bundna kolumner enligt de datatyper som är definierade i databasen. Se valideringstypen för en cell genom att hålla muspekaren över den.
Kontrollera valideringstypen för en cell 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Ta bort rader**
För att ta bort en rad, välj en rad (eller cell i raden), högerklicka och välj Radera rad.
Välj alternativet Radera rad från menyn 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Raden kommer att tas bort omedelbart.
Grid-data (efter att en rad är raderad) 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Redigera rader**
Redigera data i celler eller rader och klicka sedan på Spara eller Skicka in för att spara ändringarna. 
### **Lägger till rader**
1. För att lägga till en rad, högerklicka på en cell och välj **Lägg till rad**.
   **Välja alternativet Lägg till rad från menyn** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



En ny rad läggs till i kalkylarket i slutet av de andra raderna.
**Ny rad tillagd i rutnätet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Lägg till värden i den nya raden.
1. Klicka på **Spara** eller **Skicka** för att bekräfta ändringen.
   **Spara ändringar i data genom att klicka på *Spara**-knappen* 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Anga nummerformat**
För närvarande visas priserna i kolumnen **Produktpris** som numeriska värden. Det är möjligt att låta dem se ut som valuta.

1. Återgå till Visual Studio.NET.
1. Öppna BindColumn Collection Editor.
   Egenskapen **NumberType** för kolumnen **Produktpris** är inställd på **Allmän**.
   **Egenskapen NumberType inställd på Allmän** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. Klicka på **DropDownList** och välj **Valuta4** från listan.
   **Egenskapen NumberType ändrad till Valuta4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Kör applikationen igen.
   Värdena i kolumnen **Produktpris** är nu valuta.
   **Produktpriser i valutnummer format** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Redigerar data**
Hittills tillåter applikationen endast sina användare att visa tabelldata. Användare kan redigera data i GridWeb-reglaget men när de stänger webbläsaren och öppnar databasen har ingenting ändrats. De gjorda ändringarna sparas inte i databasen. 

Det följande exemplet lägger till kod i applikationen så att GridWeb kan spara ändringar i databasen. 

1. Öppna **Egenskaper**-fönstret och välj SaveCommand-händelsen för GridWeb-reglaget från listan.
   **Välj SaveCommand-händelsen för GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. Dubbelklicka på **SaveCommand**-händelsen och VS.NET skapar händelseshanteraren GridWeb1_SaveCommand.
1. Lägg till kod i denna händelseshanterare som kommer att uppdatera databasen med eventuellt modifierade data i DataSet bunden till kalkylarket med hjälp av oleDbDataAdapter1. 

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

Du kan också kontrollera koden som har lagts till i händelseshanteraren GridWeb1_SaveCommand
**Kod tillagd i händelseshanteraren GridWeb1_SaveCommand** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Spara ändringar i databasen med **Spara**-knappen sparar dem definitivt nu.
## **Slutsats**
{{% alert color="primary" %}} 

Data binding är en viktig funktion i Aspose.Cells.GridWeb. Det är enkelt att binda kalkylblad till en databas med hjälp av Worksheets Designer-verktyget som erbjuds av Aspose.Cells.GridWeb. Aspose.Cells.GridWeb sparar tid och ansträngning vid skapande av kraftfulla grid-lösningar. 

{{% /alert %}}
