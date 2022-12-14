---
title: Bindning av ett kalkylblad med databas med hjälp av kalkylbladsdesigner i VS.Net 2005
type: docs
weight: 40
url: /sv/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 Den här artikeln diskuterar det enklaste sättet att binda kalkylblad med databastabeller i**Visual Studio.Net 2005** med hjälp av ett specialverktyg som medföljer Aspose.Cells.GridWeb som heter som**Arbetsbladsdesigner** . Den här artikeln skulle definitivt få dig att känna hur enklare det är att använda databindningsfunktionen i Aspose.Cells.GridWeb med hjälp av**Arbetsbladsdesigner** .

{{% /alert %}}

## **Bindning av ett kalkylblad med databas med hjälp av kalkylbladsdesigner i VS.Net 2005**

 Syftet med den här artikeln är att låta alla utvecklare lära sig hur du kan skapa en databindande applikation i**VS.Net 2005** och förstå användningen och rollen av**Arbetsbladsdesigner** redaktör. Det bästa sättet att lära sig och förstå allt är genom exempel. Så i den här artikeln skulle det också vara bäst för oss att skapa en exempelapplikation för att demonstrera användningen av**Arbetsbladsdesigner** i bindande arbetsblad med databas. Låt oss skapa en ansökan steg för steg.

### **Steg 1: Skapa en exempeldatabas**

 Först och främst kommer vi att skapa en exempeldatabas som kommer att användas i den här artikeln. Vi har använt MS Access för att skapa en exempeldatabas som innehåller**Produkter** tabell vars schema visas nedan:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**Figur:** Designinformation av**Produkter** tabell

 Få dummy-poster läggs till**Produkter** tabell som visas nedan i figuren:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**Figur:** Rekord i**Produkter** tabell

### **Steg 2: Designa exempelapplikation**

 En**ASP.NET webbapplikation** skapas och designas i Visual Studio.NET 2005 som visas i figurerna nedan. Dessa skärmbilder är användbara för de utvecklare som inte är så bekanta med att använda Aspose.Cells.GridWeb i Visual Studio.Net 2005.

Första start VS.Net 2005.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**Figur:** Startar VS.Net 2005

Skapa en ny webbplats från Arkiv|Ny|Webbplats...-menyn.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**Figur:** Skapa en ny webbplats

 Efter att ha klickat på Arkiv|Ny|Webbplats... menyalternativ,**Ny webbplats** dialogrutan visas. Klicka på**Bläddra** knappen i den.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**Figur:** Ny webbplatsdialog

 Efter att ha klickat på**Bläddra**knappen väljer du platsmappen i den lokala IIS. Du kan skapa en ny mapp och göra den till en virtuell mapp enligt bilden.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**Figur:** Skapa en ny mapp


 Efter att ha klickat på**Öppna** knappen i**Välj Plats** dialog,**Ny webbplats** dialogrutan kommer att se ut.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**Figur:** Ställa in projektplats

Nu är projektet skapat

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**Figur:** Skapade projekt

### **XHTML och HTML-lägen**

**Aspose.Cells.GridWeb** stöder helt XHTML Mode som är implementerat som standard i VS.Net 2005 sedan**Xhtml-läge** egendom av**GridWeb** kontroll är inställd på**Sann** som standard när du placerar kontrollen på webbsidan. Men om du vill implementera HTML-läge för kontrollen i VS.Net 2005, kan du göra det ganska enkelt. Du måste ändra**<!DOCTYPE>** tagga lite i webbsidans källkod och ställ in**Xhtml-läge** egendom av**GridWeb** kontroll till**Falsk** .

#### **I det här ämnet kommer vi att använda HTML-läge för kontrollen. Så följ stegen nedan**

##### **1. Växla till källvyn på webbsidan och hitta följande <!DOCTYPE>-tagg i källkoden.**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

När du har hittat den taggen, välj den fullständiga taggen i källkoden som visas nedan.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**Figur:** Väljer**<!DOCTYPE>-taggen**

 Ersätt**<!DOCTYPE>** tagga från din källkod med följande.

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**Figur:** Modifierar**<!DOCTYPE>-taggen**

##### **2. Efter kommer du att lägga till GridWeb-kontrollen i webbformuläret. Du bör välja kontrollen och välja egenskapen XhtmlMode i fönstret Egenskaper för att ställa in den på False.**

**Lägger till GridWeb till WebForm** 

 Högerklicka på**Verktygslåda** och välj**Välj objekt...** från menyn.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**Figur:** Att välja artiklar

 Välj nu**GridWeb** komponent och klicka**OK**

{{% alert color="primary" %}}

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**Figur:** Väljer**GridWeb** komponent i komponentdialogrutan

 Nu den**GridWeb** läggs till som visas i figuren nedan.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**Figur:** **GridWeb** läggs till i verktygslådan

 Placera**GridWeb** på webbformuläret som visas nedan.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**Figur:** Placering**GridWeb** på webbsidan

{{% /alert %}} {{% alert color="primary" %}}

**Procedur** : Välj kontrollen, välj nu**Xhtml-läge** egendom från**Egenskaper** fönstret och ställ in det på**Falsk** värde.

{{% /alert %}}

##### **Steg 3: Ansluta till databasen med Server Explorer och ställa in anslutningsobjekt**

Först lägger vi till MS Access-databasen till projektet som vi tidigare skapat i**Steg 1** . Du kanske ser det**db.mdb** filen läggs till i projektet.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**Figur:** Lade till databas i projektmappen

 Nu går vi till**Komponentdesigner** fönstret i webbformuläret med hjälp av webbsidans högerklicksmenyalternativ.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**Figur:** Väljer**Visa komponentdesigner** alternativ

Fönstret Component Designer visas enligt nedan.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**Figur:** Komponentdesignerfönster

 Dubbelklicka på**OleDbConnection** komponent från datapanelen för att placera oleDbConnection1-objekt till fönster.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**Figur:** oleDbConnection1-objekt

 Nu är det dags att ansluta till databasen. Vi kan göra det enkelt genom att använda**Server Explorer** i Visual Studio.NET 2005. Välj bara**Uppkoppling** i**Server Explorer** och högerklicka. Du kommer att se en snabbmeny som visas framför dig. Välj**Lägg till anslutning...** alternativ från menyn som visas nedan i figuren:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**Figur:** Väljer**Lägg till anslutning...** alternativ från menyn


 Efter att ha valt**Lägg till anslutning...**alternativ från menyn,**Lägg till anslutning** dialogrutan öppnas och**Bläddra** för att välja databasfil som visas nedan.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**Figur:** Välja databasfil

Du kan testa anslutningen.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**Figur:** Testar anslutningen

Du kan bläddra i anslutningen för att kontrollera tabellen och dess fält.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**Figur:** Kontrollera tabellen och dess fält för anslutningen

 Om du nu väljer**oleDbAnslutning1** objekt i**Komponentdesigner** fönstret, kan du välja anslutningssträngen relaterad till den befintliga anslutningen som just skapades, den finns där i "ConnectionString"-egenskapen för**oleDbAnslutning1** objekt i fönstret Egenskaper.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**Figur:** Väljer anslutningssträngen för objektet

 Slutligen ändras objektets modifierare till**Skyddad** för bättre tillgänglighet.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**Figur:** Ställa in objektets modifierare

##### **Steg 4: Konfigurera dataadapterobjekt**

 Lägg nu till en**OleDbDataAdapter** komponent från panelen Data i verktygslådan för att konfigurera den. Dubbelklicka på**OleDbDataAdapter** verktygslådans datapanel kommer den att starta sin konfigurationsguide och välja den befintliga anslutningen som visas i bilden:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**Figur:** Konfigurationsguide för dataadapter

 Efter att ha klickat**Nästa** knappen klickar du på**Frågebyggare** att lägga till**Produkter** tabell, välj Alla kolumner och klicka**OK** knapp.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**Figur:** Lägger till produkttabell

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**Figur:** Frågebyggare

 Klicka nu**Avsluta** knappen för att avsluta guiden.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**Figur:** Avslutar guiden

 Efter att ha konfigurerat guiden läggs oleDbDataAdapter1 automatiskt till i fönstret som visas nedan. Du kan också ställa in dess modifierare till**Skyddad**.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**Figur:** Hämtar OleDbDataAdapter-objektet i designerfönstret

##### **Steg 5: Generera datauppsättning**

 Eftersom vi har skapat databasanslutning och dataadapterobjekt men ändå behöver vi något där vi kan lagra data efter att ha kopplat till databasen. A**Dataset** objekt kan lagra data exakt och vi kan också generera det enkelt med VS.NET 2005 IDE. För att göra det, välj**oleDbDataAdaper1**och högerklicka. En snabbmeny skulle dyka upp med några alternativ. Välj**Generera** **Datauppsättning...** alternativ från menyn som visas nedan i figuren.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**Figur:** Väljer**Generera** **Datauppsättning...** alternativ från menyn

 Efter att ha valt**Generera** **Datauppsättning...** alternativ från menyn, a**Generera datauppsättning** dialogrutan skulle öppnas. Med den här dialogrutan kan vi välja vad som skulle vara namnet på den nya**Dataset** objekt som ska skapas och vilka tabeller som ska läggas till**Dataset** . Kolla upp**Lägg till denna datauppsättning till designern** alternativet och klicka**OK** knappen som visas nedan i bilden.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**Figur:** Klickar**OK** knappen för att generera**Dataset**

 Nu kan du se en**datamängd 11** objekt lagts till designern som visas nedan i figuren. Ställ in objektmodifieraren till**Skyddad**.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**Figur:** **Dataset** genereras och läggs till i designerfönstret

Viss kod genereras automatiskt i den .cs-filrelaterade anslutningen, dataadaptern, datasetobjektet.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**Figur:** Genererad kod

##### **Steg 6: Använda kalkylbladsdesignern**

Nu är det dags att öppna hemligheten. Välj kontrollen och högerklicka. En snabbmeny skulle öppnas. Välj alternativet Arbetsbladsdesigner... från menyn som visas nedan i figuren.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**Figur:** Väljer**Arbetsbladsdesigner...** alternativ från menyn

 Efter det**Redaktör för kalkylbladssamling** dialog (även kallad**Arbetsbladsdesigner** ) kommer att öppnas kan du se flera egenskaper som kan konfigureras för att binda**Blad 1** med valfri tabell i databasen. Låt oss välja**Datakälla** fast egendom. Skriva**datamängd 11** i den (som vi genererade och lade till i designerfönstret i föregående steg). Klicka sedan på**DataMember** fast egendom. Skriva**Produkter** som ett tabellnamn här som visas nedan i figuren:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**Figur:** Miljö**Datakälla** och**DataMember** egenskaper

 Nu kan du konfigurera**BindColumns** fast egendom. Efter att ha klickat på den kan du nu lägga till bindningskolumnerna och ställa in**Rubrik** , **Data fält** (Det borde vara samma som**Produkter** tabellfält) och andra egenskaper. Du kan ställa in**Är AutoCreated** till**Sann** och ansöka**Godkännande** och ställ in**NumberType**olika fält för dina behov.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**Figur:** Klickar**BindColumns** fast egendom

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**Figur:** **BindColumn Collection Editor** dialog

##### **Steg 7: Lägga till några rader kod för webbsidan**

 Vi har använt**Arbetsbladsdesigner** enkelt och nu måste vi bara lägga till några rader kod

 Först lägger vi till**OnInit** händelserelaterad kod att initiera**InitializeComponent** metod för att initiera och skapa anslutnings-, kommando-, dataadapter- och datasetobjekt. Dessa kodrader läggs inte till med den automatiskt genererade koden, så vi måste lägga till dem manuellt.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**Figur:** Lägger till lite kod1

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**Figur:** Lägger till lite kod2

 Nu lägger vi till lite kod i**Page_Load** händelsehanterare för fyllning**datamängd 11** objekt med data från databasen (med**oleDbDataAdapter1** ) och bindande**GridWeb** styra med**datamängd 11** genom att ringa dess**DataBind** metod.

{{% alert color="primary" %}}   {{% /alert %}}

##### **Exempel:**

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

 Du kan också kontrollera koden som lagts till**Page_Load** händelsehanterare som visas nedan i figuren:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**Figur:** Kod tillagd till**Page_Load** händelsehanterare

Vi har överlägset byggt en mycket användbar databasapplikation. Men den här applikationen låter dig bara se tabellens data. Även om du kan redigera data i**GridWeb** kontroll men när du stänger ditt webbläsarfönster och öppnar din databas. Du skulle upptäcka att ingenting har förändrats. Det betyder att ändringarna du gjorde inte sparas i databasen. Så det är något du måste göra.

 Nu kommer vi att lägga till lite kod till vår applikation så att**GridWeb** kan spara sina ändringar i den faktiska databasen. Låt oss öppna**Egenskaper** ruta och välj**SaveCommand** händelse av**GridWeb** kontroll från listan över dess händelser. Om du dubbelklickar på**SaveCommand** händelse då VS.NET 2005 IDE skapas**GridWeb1_SaveCommand** händelsehanterare för dig. Lägg till lite kod till den här händelsehanteraren för att uppdatera databasen med modifierade data i**Dataset** (bunden med kalkylbladet) med hjälp av**oleDbDataAdapter1**.

##### **Exempel:**

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

 Du kan också kontrollera koden som lagts till**GridWeb1_SaveCommand** händelsehanterare som visas nedan i figuren:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**Figur:** Kod tillagd till**GridWeb1_SaveCommand** händelsehanterare

 Nu, om du kommer att spara dina ändringar i databasen med hjälp av**Spara** knappen på**GridWeb** , de skulle definitivt räddas.

##### **Steg 8: Kör din applikation**

 Slutligen kan vi kompilera och köra vår applikation genom att antingen trycka på**Ctrl+F5** eller klicka**Start** knapp. I felsökningsdialogrutan kan du ange lämpligt felsökningsalternativ och klicka**OK** knappen som visas nedan i bilden.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**Figur:** Kör applikation

 Efter sammanställning,**Default.aspx** sidan i vår webbapplikation kommer att öppnas i ett nytt webbläsarfönster där vi kan se all data som laddas från databasen enligt nedan:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**Figur:** Data laddas in i**GridWeb** kontroll från databasen

 När data laddas in i**GridWeb** kontroll då skulle du känna att Aspose.Cells.GridWeb ger en implicit kontroll av data till sina användare. Låt oss kontrollera vilken typ av datamanipuleringsfunktioner som erbjuds av**GridWeb** till sina användare.

##### **Datavalidering**

Aspose.Cells.GridWeb skapar automatiskt lämpliga valideringsregler för alla bundna kolumner enligt deras datatyper definierade i databasen. Du kan se valideringstypen för en cell genom att föra muspekaren över den som visas nedan i figuren:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**Figur:**Kontrollerar valideringstyp för en cell

 I figuren ovan kan vi se att den valda cellen innehåller**\<INT>** typ av validering, vilket innebär att användare endast kan ange ett heltalsvärde för den, annars uppstår ett valideringsfel. Dessutom,**\<KRÄVS>** visar att värdet av**Serienummer** måste skickas in av användaren.

##### **Ta bort rader**

 För att ta bort en rad bör du först markera en rad (eller valfri cell i raden) och välja**Ta bort rad** alternativ från högerklicksmenyn som visas nedan:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**Figur:** Väljer**Ta bort rad** alternativ från menyn

 Efter att ha valt**Ta bort rad** från menyn raderas raden från**GridWeb** . Klicka nu**spara** knappen på**GridWeb** för att ta bort posten i den ursprungliga databastabellen.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**Figur:** Rutnätsdata (efter att en rad har tagits bort)

##### **Redigera rader**

 Du kan också redigera data i celler eller rader och sedan klicka**Spara** för att spara dina ändringar.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**Figur:** Rutnätsdata (Redigeringspost1)

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**Figur:** Rutnätsdata (Redigeringspost2)

##### **Lägga till rader**

 För att lägga till en rad, välj**Lägg till rad** alternativ från högerklicksmenyn som visas nedan:

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**Figur:** Väljer**Lägg till rad** alternativ från menyn

En ny rad läggs till i arket i slutet av raderna efter val**Lägg till rad** alternativ från menyn. Till vänster om den nyligen tillagda raden skulle du märka en**asterisk** markera, vilket indikerar att raden är en nytillagd.

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**Figur:** Ny rad har lagts till i Grid

 När du har skrivit in värdena i den nya raden klickar du**Spara** för att bekräfta ändringarna i den ursprungliga databastabellen som visas nedan

![todo:image_alt_text](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**Figur:** Spara ändringar i databastabell genom att klicka**Spara** knapp

{{% alert color="primary" %}}   {{% /alert %}}

##### **Slutsats**

{{% alert color="primary" %}}

**Databindning** är en viktig funktion i Aspose.Cells.GridWeb . Det är verkligen enkelt för utvecklare att binda sina kalkylblad med databas med hjälp av**Arbetsbladsdesigner** verktyg som erbjuds av Aspose.Cells.GridWeb . Aspose.Cells.GridWeb är till stor hjälp för utvecklarna att spara tid och ansträngningar för att skapa kraftfulla Grid-lösningar.

{{% /alert %}}
