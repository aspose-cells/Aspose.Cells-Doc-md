---
title: Arbeta med Arbetsblad GridWeb
type: docs
weight: 30
url: /sv/java/working-with-worksheets-gridweb/
---

## **Åtkomst till Arbetsblad**

Detta ämne diskuterar åtkomst till arbetsblad i GridWeb-kontrollen. Vi kan även kalla dessa arbetsblad webb-arbetsblad eftersom de tillhör GridWeb och används i webbapplikationer.

Alla arbetsblad som ingår i GridWeb-kontrollen är lagrade i en GridWorksheetCollection av GridWeb-kontrollen. Det är enkelt att komma åt ett specifikt arbetsblad genom dess bladindex.

Utvecklare kan komma åt ett specifikt arbetsblad genom att ange dess bladindex enligt exemplet nedan i kodsnutten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Ta bort ett Arbetsblad**

Detta ämne ger kort information om att ta bort arbetsblad från Microsoft Excel-filer med hjälp av GridWeb API. Ta bort ett arbetsblad genom att ange dess bladindex.

Utvecklare kan ta bort ett specifikt arbetsblad genom att ange dess bladindex med hjälp av metoden removeAt från samlingen GridWorksheetCollection enligt exemplet nedan i kodsnutten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Lägga till Arbetsblad**

Arbetsblad är en viktig del av GridWeb. All data hanteras och lagras i form av arbetsblad. GridWeb tillåter utvecklare att lägga till ett eller flera arbetsblad till Aspose.Cells.GridWeb-kontrollen. Detta ämne visar enkla tillvägagångssätt för att lägga till arbetsblad i GridWeb.

### **Utan att ange bladnamn**

Det enklaste sättet att lägga till ett arbetsblad i Aspose.Cells.GridWeb är att anropa metoden add från klassen GridWorksheetCollection i GridWeb-kontrollen. Detta skapar arbetsblad som använder standardnamn (t.ex. Sheet1, Sheet2, Sheet3 osv.) och lägger till dem i GridWeb-kontrollen.

**Utdata: Ett arbetsblad med standardnamn har lagts till i GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Med angivet bladnamn**

För att lägga till ett arbetsblad med ett specifikt namn till GridWeb-kontrollen istället för att använda det förvalda nämningsmönstret, anropa en överlagrad version av add-metoden som tar den specificerade strängen SheetName. Till exempel lägger exemplet nedan till ett arbetsblad med namnet Faktura.

**Utdata: Ett arbetsblad med ett angivet namn har lagts till i GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add()-metoden returnerar det nya arbetsbladets index som kan användas för att komma åt instansen av arbetsbladet. För mer information om hur man kommer åt arbetsblad, läs [Åtkomst till Arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Byta namn på ett Arbetsblad**

Att byta namn på ett arbetsblad kan vara mycket användbart när man arbetar med många arbetsblad i GridWeb och beslutar att ändra deras namn för att göra dem mer meningsfulla. Till exempel kan ett arbetsblad som innehåller en faktura döpas om till Faktura istället för Sheet1. Detta ämne beskriver denna enkla men användbara funktion.

### **Byta namn på ett Arbetsblad**

Alla arbetsblad innehåller en Name-egenskap som tillåter utvecklare att komma åt eller ändra namn på arbetsbladen. För att byta namn på ett arbetsblad:

1. Kom åt ett arbetsblad från GridWorksheetCollection.
1. Byt namn på det valda arbetsbladet.

{{% alert color="primary" %}}

För mer information om hur man kommer åt arbetsblad i Aspose.Cells.GridWeb, vänligen se [Åtkomst till Arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Innan koden körs har arbetsbladet ett standardnamn, som Sheet1.

**Ingångsfil: ett arbetsblad med ett standardnamn Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Efter att koden har körts, är arbetsbladet omdöpt till Faktura.

**Resultat: arbetsbladet är omdöpt till Faktura** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Kopiera ett kalkylblad**

[Lägga till Arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets) beskriver hur man lägger till nya arbetsblad i GridWeb. Det är också möjligt att lägga till en kopia (eller replika) av ett annat arbetsblad till Aspose.Cells.GridWeb-kontrollen. Denna funktion kan vara användbar när identiska eller liknande data i ett arbetsblad också krävs i ett annat arbetsblad. I sådana fall är det enklare att kopiera ett befintligt arbetsblad och lägga till det i Aspose.Cells.GridWeb som ett nytt arbetsblad istället för att skapa det från grunden.

### **Genom att använda arkindex**

Exemplet nedan visar hur man lägger till en kopia av ett arbetsblad till GridWeb-kontrollen genom att ange arbetsbladets index i metoden addCopy från GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Genom att använda arknamn**
Exemplet nedan visar hur man lägger till en kopia av ett arbetsblad till GridWeb-kontrollen genom att ange arbetsbladets namn i metoden addCopy från GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

addCopy-metoden returnerar det nytt tillagda arbetsbladets index som kan användas för att komma åt arbetsbladsinstansen. För mer information om hur man kommer åt arbetsblad, läs [Åtkomst till Arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Arbeta med Namngivna Områden**

Normalt används kolumn- och radetiketter för att unikt hänvisa till celler. Men du kan skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden.

Ordet **namn** kan hänvisa till en sträng av tecken som representerar en cell, cellintervall, formel eller konstant värde. Använd till exempel lättförståeliga namn, såsom Produkter, för att referera till svårförståeliga intervall, såsom Försäljning!C20:C30.

Etiketter kan användas i formler som hänvisar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn. **Namngivna intervall** är en av de mest kraftfulla funktionerna i Microsoft Excel.

Användare kan tilldela ett namn till ett intervall och använda det namnet i formler. Aspose.Cells.GridWeb stödjer denna funktion.

### **Lägga till/hänvisa namngivna områden i formler**

GridWeb-kontrollen tillhandahåller två klasser (GridName och GridNameCollection) för att arbeta med namngivna intervall.

Följande kodsnutt kommer att hjälpa dig att förstå hur du använder dem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Hantera kommentarer i arbetsbladet**

Detta ämne diskuterar tillägg, åtkomst och borttagning av kommentarer från arbetsblad. Kommentarer är användbara för att lägga till anteckningar eller användbar information för användare som kommer att arbeta med arket. Utvecklare har flexibiliteten att lägga till kommentarer till valfri cell i arbetsbladet.

### **Arbeta med kommentarer**

#### **Lägga till kommentarer**

För att lägga till en kommentar i arbetsbladet, följ stegen nedan:

1. Lägg till kontrollen Aspose.Cells.GridWeb till webbformuläret.
1. Gå till det arbetsblad där du ska lägga till kommentarer.
1. Lägg till en kommentar i en cell.
1. Ange en anteckning för den nya kommentaren.

**En kommentar har lagts till i arbetsbladet** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Åtkomst till kommentarer**

För att komma åt en kommentar:

1. Gå till den cell som innehåller kommentaren.
1. Hämta cellens referens.
1. Skicka referensen till kommentarsamlingen för att komma åt kommentaren.
1. Det är nu möjligt att ändra kommentarens egenskaper.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Ta bort kommentarer**

För att ta bort en kommentar:

1. Gå till cellen som förklarats ovan.
1. Använd Comment-samlingens removeAt-metod för att ta bort kommentaren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Hantera hyperlänkar i arbetsbladet**

Detta ämne diskuterar vilka typer av hyperlänkar som stöds i Aspose.Cells.GridWeb och hur man hanterar dem programmatiskt. Hyperlänkar kan användas antingen för att skapa länkar till webbadresser eller för att utföra återuppringning till en server.

### **Typer av hyperlänkar**

Följande hyperlänkar stöds av Aspose.Cells.GridWeb:

- Text-URL-hyperlänkar, URL-hyperlänkar tillämpade på texten.
- Bild-URL-hyperlänkar, URL-hyperlänkar som tillämpas på bilder.

#### **Text-URL-hyperlänkar**

Exemplet nedan lägger till två hyperlänkar till ett kalkylblad. En har ett _blank mål medan den andra är inställd på _parent.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Utmatning: text hyperlänkar tillagt i kalkylbladet**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Bild-URL-hyperlänkar**

Exemplet nedan lägger till bild-URL-hyperlänk till ett kalkylblad.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Utmatning: bildhyperlänk tillagt i kalkylbladet**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Sortera Data**

Att sortera är en mycket värdefull funktion när det gäller datahantering. Osorterad data är smärtsamt för användare när de söker efter specifik information. Aspose.Cells.GridWeb stödjer kraftfulla sorteringsfunktioner. Det här ämnet diskuterar sortering av data med hjälp av Aspose.Cells.GridWeb API.

Aspose.Cells.GridWeb tillåter utvecklare att sortera data horisontellt och vertikalt så att utvecklare kan sortera data uppifrån och ner eller från vänster till höger.

### **Från Uppifrån och Ner**

För att sortera data från upptill och ner orientering:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Kom åt kalkylbladet som du vill sortera.
1. Sortera dataområdet i valfri ordning (stigande eller fallande). Se till att välja upptill och ner orientering.

Exemplet nedan sorterar data i två kolumner (Elev-ID och Elevnamn) i stigande ordning. Endast tolv rader av två kolumner sorteras i topp till botten-orientering.

Innan du tillämpar koden innehåller kalkylbladet ostrukturerad data.

**Indata: osorterad data** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Efter att koden har körts är datan sorterad i stigande ordning.

**Utmatning: data sorterad från topp till botten i stigande ordning** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Från Vänster till Höger**

För att sortera data från vänster till höger:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Kom åt kalkylbladet som du vill sortera.
1. Sortera dataområdet i valfri ordning (stigande eller fallande). Se till att välja vänster till höger orientering.

Exemplet nedan sorterar data i två rader (Elev-ID och Elevnamn) i stigande ordning. Endast två rader av fyra kolumner sorteras från vänster till höger.

Innan du tillämpar koden innehåller kalkylbladet ostrukturerad data.

**Indata: osorterad data innan körningskoden** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Efter att koden har körts är datan sorterad i stigande ordning.

**Utmatning: data sorterad från vänster till höger i stigande ordning** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Sökning och ersättning**

Ett av de snabbaste sätten att göra upprepande ändringar i en stor kalkylblad är att använda funktionen Hitta och ersätt. Hitta hjälper dig att hitta en textsträng eller data och ersätta det med ett nytt värde. Aspose.Cells.GridWeb ger denna funktion. Den gör det möjligt för dig att söka efter och ersätta med en specifik textsträng eller värde i kalkylarket klient-sida genom en enkel dialogruta. Den låter dig till och med söka efter partiella data.

### **Hitta/Ersätt Dialogrutan**

Det finns två sätt att öppna Hitta/Ersätt dialogrutan på:

1. När kontrollen är aktiv, tryck på **CTRL+F** för att öppna dialogrutan, eller tryck på **CTRL+R** tangenten för att öppna dialogrutan med **Ersätt**-knappen aktiverad.
1. Flytta markören till cellområdet i kalkylbladet, högerklicka sedan. Välj **Hitta** eller **Ersätt** från menyn.

**Välja Hitta**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

En sök- och ersätt-dialog visas.

**Hitta/ersätt dialogrutan**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Använda sök**

För att söka:

1. Öppna Hitta/ersätt dialogrutan.
1. Skriv in strängen du vill söka efter i fältet Hitta vad.
1. Klicka på Hitta nästa för att söka.

Nästa cell som matchar din sökning markeras.

{{% alert color="primary" %}}

Om din sökfråga inte hittas visas en dialogruta för att meddela dig.

{{% /alert %}}

### **Sökalternativ**

Det finns några sökalternativ som du kan anpassa i dialogrutan. Tabellen nedan listar dem.

|**Nr.**|**Alternativnamn**|**Beskrivning**|
| :- | :- | :- |
|1|Matcha skiftläge|Anger om skiftlägeskänslighet ska användas vid sökning.|
|2|Matcha hela ord|Anger om hela ordet ska matchas vid sökning.|
|3|Sök uppåt|Anger om sökningen ska göras nedifrån upp.|
|4|Reguljärt uttryck|När det är markerat kommer kontrollen att behandla strängen i fältet Hitta vad som ett reguljärt uttryck i sökningsprocessen.|
|5|Hitta i formler/värden|När Formler väljs kommer kontrollen att matcha formeln eller den omformaterade värdet för cellerna om formeln eller det omformaterade värdet finns. När Värden väljs kommer kontrollen att endast matcha det visade värdet för cellerna.|

### **Använda Ersätt**

För att ersätta text eller värden:

1. Öppna Hitta/ersätt dialogrutan genom att trycka på **CTRL+F**, eller högerklicka på en cell och välj **Hitta** innan du klickar på **Ersätt**.
1. Skriv in ersättningssträngen i fältet **Ersätt med**.
1. Klicka på **Ersätt**.

För att ersätta text:

1. Öppna dialogrutan.
1. Ange den text du vill hitta i fältet **Hitta vad**, och den text du vill ersätta det med i fältet **Ersätt med**.
1. Ersätt en förekomst åt gången genom att klicka på **Hitta nästa** följt av **Ersätt**.
1. Om du är väldigt säker på vad arbetsbladet innehåller, klicka på **Ersätt alla**.

{{% alert color="primary" %}}

Om arbetsbladet inte är i redigeringsläge visas inte **Ersätt**-knappen.

{{% /alert %}}

## Lägg till/Ta bort hyperlänkar från klientens sida

Aspose.Cells GridWeb stöder nu att lägga till och ta bort hyperlänkar från klientens sida. För detta tillhandahåller API:et funktionerna "addCelllink" och "delCelllink". Följande kodsnuttar demonstrerar hur man lägger till och tar bort hyperlänkar från klientens sida i GridWeb.

### Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Du kan även länka till ark med följande kodsnutt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Uppdatera typsnittsinställningar Från Klientens Sida

Aspose.Cells GridWeb stöder nu att ändra typsnittsinställningar från klientens sida. För detta tillhandahåller API:en följande funktioner

- **updateCellFontStyle**: Parametrar - r/i/b/ib för vanlig/kursiv/fet/kursiv&&fet
- **updateCellFontSize**: Parametrar - fontnamn, etc. 'System'
- **updateCellFontName**: Parametrar - fontstorlek, etc. '12pt'
- **updateCellFontColor**: Parametrar - inget/u/l/ul/ för inget/understrykning/streck över/understrykning&&streck över
- **updateCellFontLine**: Parametrar - html-färg som #aa22ee eller välkänt färgnamn som grönt, rött,...
- **updateCellBackGroundColor**: Parametrar - html-färg som #aa22ee eller välkänt färgnamn som grönt, rött,...

Följande kodsnutt visar hur man ändrar typsnittsinställningar från klientens sida i GridWeb.

### Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Lägg till/Ta bort kommentarer Från Klientens Sida

Aspose.Cells GridWeb stöder nu att lägga till och ta bort kommentarer från klientens sida. För detta tillhandahåller API:en funktionerna "addcomments" och "delcomments". Följande kodsnutt visar hur man lägger till och tar bort kommentarer från klientens sida i GridWeb.

### Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Visa knappar för att lägga till/ta bort arbetsblad

Aspose.Cells GridWeb stöder nu att lägga till och ta bort blad genom att använda knappar i verktygsfältet. För att knapparna ska vara synliga på framsidan måste du ställa in **GridWeb1.ShowAddButton** till **true**. Följande kodsnutt visar hur man lägger till Lägg till/Ta bort-knappar i GridWeb verktygsfältet.

### Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
