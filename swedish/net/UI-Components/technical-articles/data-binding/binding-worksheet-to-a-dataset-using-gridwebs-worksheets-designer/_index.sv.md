---
title: Bindning av kalkylblad till en datauppsättning med GridWebs kalkylbladsdesigner
type: docs
weight: 20
url: /sv/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 Den här artikeln diskuterar ett enkelt sätt att binda kalkylblad till databastabeller i GUI-läge med ett specialverktyg som medföljer Aspose.Cells.GridWeb, kalkylbladsdesignern.

{{% /alert %}} 
## **Bindning av ett kalkylblad med databas med hjälp av kalkylbladsdesigner**
	**Steg 1: Skapa en exempeldatabas**
1. Först skapar vi exempeldatabasen som kommer att användas i den här artikeln. Vi använder Microsoft Access för att skapa en databas som innehåller en tabell som heter Produkter. Dess schema visas nedan.
   **Designinformation för produkttabellen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Några få dummyposter läggs till i produkttabellen.
   **Poster i tabellen Produkter** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Steg 2: Designa exempelapplikation**
 En ASP.NET webbapplikation skapas och designas i Visual Studio.NET som visas nedan.
**Designad exempelapplikation** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Steg 3: Anslut till databasen med Server Explorer**
 Det är dags att ansluta till databasen. Vi kan göra det enkelt med hjälp av Server Explorer i Visual Studio.NET.

1.  Välj**Uppkoppling** i**Server Explorer** och högerklicka.
1.  Välj**Lägg till anslutning** från menyn.
   **Välj alternativet Lägg till anslutning** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 Dialogrutan Data Link Properties visas.
**Dialogrutan Data Link Properties** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 Med den här dialogrutan kan du ansluta till vilken databas som helst. Som standard låter den dig ansluta till en SQL Server-databas. För det här exemplet måste vi ansluta till en Microsoft Access-databas.

1.  Klicka på**Leverantör** flik.
1.  Välj**Microsoft Jet 4.0 OLE DB-leverantör** från**OLE DB-leverantör(er)** lista.
1.  Klick**Nästa**.
   **Klicka på Nästa efter att ha valt en OLE DB-leverantör** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 De**Förbindelse** fliksidan öppnas.

1.  Välj Microsoft Access-databasfilen (i vårt fall db.mdb) och klicka på**OK**.
   **Klicka på OK-knappen efter att ha valt databasfil** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 Efter att ha klickat**OK** , kommer en databasanslutning till Microsoft Access-databasen att skapas i**Server Explorer**Dubbelklicka på anslutningen för att se alla tabeller, vyer och lagrade procedurer i databasen.

{{% /alert %}} 
### **Steg 4: Skapa databasanslutningsobjekt grafiskt**
1.  Bläddra i tabellerna i databasen med hjälp av**Server Explorer**.
 Det finns bara ett bord, produkter.
1.  Dra och släpp tabellen Produkter från**Server Explorer** till**Webbformulär**.
   **Dra produkttabellen från Server Explorer och släpp till webbformuläret** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



En dialogruta kan visas.
**Dialog för att bekräfta att databaslösenordet ingår i anslutningssträngen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Bestäm om du vill inkludera ett databaslösenord i anslutningssträngen eller inte. För det här exemplet valde vi**Inkludera inte lösenord**. 
Två databasanslutningsobjekt (oleDbConnection1 och oleDbDataAdapter1) har skapats och lagts till.
**Databasanslutningsobjekt (oleDbConnection1 & oleDbDataAdapter1) skapade och visade** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Steg 5: Generera datauppsättning**
Hittills har vi skapat databasanslutningsobjekt men behöver fortfarande någonstans att lagra data efter att ha anslutit till databasen. Ett DataSet-objekt kan lagra data exakt och vi kan också generera det enkelt med VS.NET IDE.

1.  Välj**oleDbDataAdaper1** och högerklicka.
1.  Välj**Generera datauppsättning** alternativ från menyn.
   **Välj alternativet Generera datauppsättning** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 Dialogrutan Generera datauppsättning visas.
 Här är det möjligt att välja ett namn för det nya DataSet-objektet som ska skapas, och vilka tabeller som ska läggas till det.

1.  Välj**Lägg till denna datauppsättning till designern** alternativ.
1.  Klick**OK**.
   **Klicka på OK-knappen för att generera Dataset** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Ett dataSet11-objekt läggs till i designern.
**Dataset genereras och läggs till designern** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Steg 6: Använda Worksheets Designer**
 Nu är det dags att öppna hemligheten.

1. Välj GridWeb-kontrollen och högerklicka.
1.  Välj**Arbetsbladsdesigner** alternativ från menyn.

   **Välja alternativet Arbetsbladsdesigner** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 Redigeraren för kalkylbladsinsamling (även kallad kalkylbladsdesignern) visas.
**Dialogrutan för redigering av kalkylbladssamling** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



Dialogrutan innehåller flera egenskaper som kan konfigureras för att binda Sheet1 till valfri tabell i databasen.

1.  Välj**Datakälla** fast egendom.
 DataSet11-objektet som genererades i föregående steg listas på menyn.
1. Välj datamängd 11.
1.  Klicka på**DataMember** fast egendom.
 Kalkylbladsdesignern visar automatiskt en lista med tabeller i datamängd 11. Det finns bara ett bord, produkter.
1. Välj tabellen Produkter.
   **Ställa in egenskaperna DataSource och DataMember** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  Kolla**BindColumns** fast egendom.
   **Klicka på BindColumns-egenskapen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 Genom att klicka på**BindColumns** egenskapen öppnar BindColumn Collection Editor.
**BindColumn Collection Editor** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 I BindColumn Collection Editor, alla kolumner i**Produkter** tabellen läggs automatiskt till i BindColumns-samlingen.

1. Välj valfri kolumn och anpassa dess egenskaper.
 Du kan till exempel ändra varje kolumntext.
   **Ändra kolumnen Caption of ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  När du har gjort ändringar klickar du**OK**.
1.  Stäng alla dialogrutor genom att klicka**OK**.
 Slutligen kommer du tillbaka till sidan WebForm1.aspx.
   **Återgår till sidan WebForm1.aspx efter att ha använt kalkylbladsdesignern** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 Ovan visas produkttabellens kolumnnamn. Kolumnernas bredd är liten så de fullständiga namnen på vissa kolumner är inte helt synliga.
### **Steg 7: Lägga till kod till Page_Load Event Handler**
 Vi har använt kalkylbladsdesignern och måste nu bara lägga till kod till händelsehanteraren Page_Load för att fylla dataSet11-objektet med data från databasen (med oleDbDataAdapter1) och binda GridWeb-kontrollen till dataSet11 genom att anropa dess DataBind-metod.

1.  Lägg till koden:

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

1. Kontrollera koden som lagts till i Page_Load-händelsehanteraren.
   **Koden har lagts till i händelsehanteraren Page_Load** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Steg 8: Kör applikationen**
 Kompilera och kör programmet: antingen tryck på**Ctrl+F5** eller klicka**Start**. 
**Kör applikationen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Efter kompileringen öppnas sidan WebForm1.aspx i ett webbläsarfönster med all data laddad från databasen.
**Data laddas in i GridWeb-kontrollen från databasen** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Arbeta med GridWeb Control**
 När data läses in i GridWeb-kontrollen ger det användarna kontroll över datan. Ett antal olika typer av datamanipuleringsfunktioner erbjuds av GridWeb.
### **Datavalidering**
Aspose.Cells.GridWeb skapar automatiskt lämpliga valideringsregler för alla bundna kolumner enligt de datatyper som definieras i databasen. Se valideringstypen för en cell genom att föra markören över den.
**Kontrollerar valideringstyp för en cell** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Här innehåller den markerade cellen**<INT>** validering, vilket innebär att användare endast kan ange heltalsvärden i den. Om de anger ett annat värde uppstår ett valideringsfel. Dessutom,**<KRÄVS>** visar att värdet Produkt-ID måste skickas.
### **Ta bort rader**
 För att ta bort en rad, välj en rad (eller valfri cell i raden), högerklicka och välj**Ta bort rad**.
**Välj alternativet Ta bort rad från menyn** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Raden skulle raderas omedelbart.
**Rutnätsdata (efter att en rad har tagits bort)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Redigera rader**
Redigera data i celler eller rader och klicka sedan**Spara** eller**Skicka in** för att spara ändringarna.
### **Lägga till rader**
1.  För att lägga till en rad, högerklicka på en cell och välj**Lägg till rad**.
   **Välj alternativet Lägg till rad från menyn** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



En ny rad läggs till i arket i slutet av andra rader.
**Ny rad har lagts till i Grid** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 Till vänster om den nya raden finns en asterisk{{< emoticons/cross >}} , vilket indikerar att raden är ny.

1. Lägg till värden på den nya raden.
1.  Klick**Spara** eller**Skicka in** för att bekräfta ändringen.
   **Spara ändringar av data genom att klicka på *Spara** knapp*

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Ställa in nummerformat**
 För tillfället är priserna i**Produktpris** kolumnen visas som numeriska värden. Det är möjligt att få dem att se ut som valuta.

1. Återgå till Visual Studio.NET.
1. Öppna BindColumn Collection Editor.
 De**NumberType** egendom av**Produktpris** kolumnen är inställd på**Allmän**.
   **NumberType-egenskapen inställd på General** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Klick**DropDown List** och välj**Valuta4** från listan.
   **NumberType-egenskapen ändrades till Currency4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Kör programmet igen.
 Värdena i**Produktpris** kolumnen är nu valuta.
   **Produktpriser i valuta Nummerformat** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Redigera data**
 Applikationen låter än så länge endast dess användare se tabelldata. Användare kan redigera data i GridWeb-kontrollen, men när man stänger webbläsaren och öppnar databasen har ingenting förändrats. Ändringarna som görs sparas inte i databasen.

 Följande exempel lägger till kod till applikationen så att GridWeb kan spara ändringar i databasen.

1. Öppna**Egenskaper** och välj GridWeb-kontrollens SaveCommand-händelse från listan.
   **Att välja SaveCommand-händelse för GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  Dubbelklicka på**SaveCommand** händelse och VS.NET skapar händelsehanteraren GridWeb1_SaveCommand.
1.  Lägg till kod till denna händelsehanterare som kommer att uppdatera databasen med eventuella modifierade data i datauppsättningen som är bunden till kalkylbladet med oleDbDataAdapter1.

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

Du kan också kontrollera koden som lagts till i GridWeb1_SaveCommand-händelsehanteraren
**Kod tillagd till händelsehanteraren GridWeb1_SaveCommand** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 Spara ändringar i databasen med hjälp av**Spara** knappen sparar dem nu definitivt.
## **Slutsats**
{{% alert color="primary" %}} 

Databindning är en viktig egenskap hos Aspose.Cells.GridWeb. Det är lätt att binda kalkylblad till en databas med hjälp av verktyget Worksheets Designer som erbjuds av Aspose.Cells.GridWeb. Aspose.Cells.GridWeb sparar tid och ansträngning när du skapar kraftfulla Grid-lösningar.

{{% /alert %}}
