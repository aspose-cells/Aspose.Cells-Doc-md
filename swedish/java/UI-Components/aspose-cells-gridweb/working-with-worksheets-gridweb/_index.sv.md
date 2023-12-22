---
title: Arbeta med kalkylblad GridWeb
type: docs
weight: 30
url: /sv/java/working-with-worksheets-gridweb/
---
##  **Åtkomst till arbetsblad**

Det här ämnet diskuterar åtkomst till kalkylblad för GridWeb-kontrollen. Vi kan också kalla dessa arbetsblad för webbkalkylblad eftersom de tillhör GridWeb och används i webbapplikationer.

Alla kalkylblad som finns i GridWeb-kontrollen lagras i en GridWorksheetCollection av GridWeb-kontrollen. Det är enkelt att komma åt ett visst kalkylblad genom dess arkindex.

Utvecklare kan komma åt ett specifikt kalkylblad genom att ange dess arkindex som visas nedan i exempelkodavsnittet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

##  **Ta bort ett arbetsblad**

Det här avsnittet ger kort information om hur du tar bort kalkylblad från Microsoft Excel-filer med hjälp av GridWeb API. Ta bort ett kalkylblad genom att ange dess arkindex.

Utvecklare kan ta bort ett specifikt kalkylblad genom att ange dess arkindex med hjälp av GridWorksheetCollection-samlingens removeAt-metod som visas nedan i exempelkodavsnittet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

##  **Lägga till arbetsblad**

Arbetsblad är en integrerad del av GridWeb. All data hanteras och lagras i form av arbetsblad. GridWeb tillåter utvecklare att lägga till ett eller flera kalkylblad till Aspose.Cells.GridWeb-kontrollen. Det här ämnet visar enkla metoder för att lägga till kalkylblad till GridWeb.

###  **Utan att ange arbetsbladsnamn**

Det enklaste sättet att lägga till ett kalkylblad till Aspose.Cells.GridWeb är att anropa GridWorksheetCollection-klassens add-metod i GridWeb-kontrollen. Detta skapar kalkylblad som använder standardnamn (det vill säga Sheet1, Sheet2, Sheet3 och så vidare) och lägger till dem i GridWeb-kontrollen.

**Utdata: ett kalkylblad med standardnamn har lagts till i GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

###  **Med specificerat bladnamn**

För att lägga till ett kalkylblad med ett specifikt namn till GridWeb-kontrollen istället för att använda standardnamnschemat, anropa en överbelastad version av add-metoden som tar den angivna strängen SheetName. Exempelvis lägger exemplet nedan till ett kalkylblad med namnet Faktura.

**Utdata: ett kalkylblad med ett angivet namn har lagts till i GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 Metoden add() returnerar det nya kalkylbladets index som kan användas för att komma åt instansen av detta kalkylblad. För mer information om hur du kommer åt arbetsblad, läs[Åtkomst till arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **Byta namn på ett arbetsblad**

Att byta namn på ett kalkylblad kan vara mycket användbart när man arbetar med många kalkylblad i GridWeb och bestämmer sig för att ändra deras namn för att göra dem mer meningsfulla. Till exempel kan ett kalkylblad som innehåller en faktura döpas om till Faktura istället för Blad1. Det här avsnittet beskriver denna enkla men användbara funktion.

###  **Byta namn på ett arbetsblad**

Alla kalkylblad innehåller en Name-egenskap som tillåter utvecklare att komma åt eller ändra kalkylbladens namn. Så här byter du namn på ett kalkylblad:

1. Öppna ett kalkylblad från GridWorksheetCollection.
1. Byt namn på det valda kalkylbladet.

{{% alert color="primary" %}}

 För mer information om hur du kommer åt arbetsblad i Aspose.Cells.GridWeb, se[Åtkomst till arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Innan koden körs har kalkylbladet ett standardnamn, till exempel Sheet1.

**Indatafil: ett kalkylblad med standardnamnet Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Efter att ha kört koden byts kalkylbladet om till Faktura.

**Utdata: kalkylbladet döps om till Faktura** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

##  **Kopiera ett arbetsblad**

[Lägga till arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)beskriver hur man lägger till nya kalkylblad till GridWeb. Det är också möjligt att lägga till en kopia (eller replika) av ett annat kalkylblad till Aspose.Cells.GridWeb-kontrollen. Den här funktionen kan vara användbar när identiska eller liknande data i ett kalkylblad också krävs i ett annat kalkylblad. När så är fallet är det lättare att kopiera ett befintligt kalkylblad och lägga till det i Aspose.Cells.GridWeb som ett nytt kalkylblad istället för att skapa det från början.

###  **Använder Sheet index**

Exempelkoden nedan visar hur man lägger till en kopia av ett kalkylblad till GridWeb-kontrollen genom att ange kalkylbladets index i GridWorksheetCollections addCopy-metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
###  **Använder arknamn**
Exempelkoden nedan visar hur man lägger till en kopia av ett kalkylblad till GridWeb-kontrollen genom att ange kalkylbladets namn i GridWorksheetCollections addCopy-metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 Metoden addCopy returnerar det nyligen tillagda kalkylbladets index som kan användas för att komma åt kalkylbladsinstansen. För mer information om hur du kommer åt arbetsblad, läs[Åtkomst till arbetsblad](/cells/sv/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **Arbeta med Named Ranges**

Normalt används kolumn- och radetiketter för att unikt referera till celler. Men du kan skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden.

 Ordet**namn** kan hänvisa till en teckensträng som representerar en cell, cellintervall, formel eller konstant värde. Använd till exempel lättförståeliga namn, som Produkter, för att referera till svårförståeliga intervall, som Sales!C20:C30.

 Etiketter kan användas i formler som refererar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn.**Namngivna intervall** är en av de mest kraftfulla funktionerna i Microsoft Excel.

Användare kan tilldela ett namn till ett intervall och använda det namnet i formler. Aspose.Cells.GridWeb stöder den här funktionen.

###  **Lägga till/refera till namngivna intervall i formler**

GridWeb-kontrollen tillhandahåller två klasser (GridName och GridNameCollection) för att arbeta med namngivna intervall.

Följande kodavsnitt hjälper dig att förstå hur du använder dem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

##  **Hantera kommentarer i arbetsblad**

Det här ämnet diskuterar att lägga till, komma åt och ta bort kommentarer från kalkylblad. Kommentarer är användbara för att lägga till anteckningar eller användbar information för användare som ska arbeta med arket. Utvecklare har flexibiliteten att lägga till kommentarer till valfri cell i kalkylbladet.

###  **Arbeta med kommentarer**

####  **Lägger till kommentarer**

För att lägga till en kommentar till arbetsbladet, följ stegen nedan:

1. Lägg till kontrollen Aspose.Cells.GridWeb i webbformuläret.
1. Öppna kalkylbladet du lägger till kommentarer till.
1. Lägg till en kommentar till en cell.
1. Ange en anteckning för den nya kommentaren.

**En kommentar har lagts till i arbetsbladet** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

####  **Åtkomst till kommentarer**

För att komma åt en kommentar:

1. Öppna cellen som innehåller kommentaren.
1. Få cellens referens.
1. Skicka referensen till kommentarsamlingen för att komma åt kommentaren.
1. Det är nu möjligt att ändra kommentarens egenskaper.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

####  **Ta bort kommentarer**

Så här tar du bort en kommentar:

1. Gå till cellen enligt beskrivningen ovan.
1. Använd kommentarsamlingens removeAt-metod för att ta bort kommentaren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

##  **Hantera hyperlänkar i arbetsblad**

Det här ämnet diskuterar vilka typer av hyperlänkar som stöds i Aspose.Cells.GridWeb och hur man hanterar dem programmatiskt. Hyperlänkar kan användas för att antingen skapa länkar till webbadresser eller för att utföra återsändning till en server.

###  **Typer av hyperlänkar**

Följande hyperlänkar stöds av Aspose.Cells.GridWeb:

- Text URL-hyperlänkar, URL-hyperlänkar som tillämpas på texten.
- Bild-URL-hyperlänkar, URL-hyperlänkar som tillämpas på bilder.

####  **Text URL hyperlänkar**

Exemplet nedan lägger till två hyperlänkar till ett kalkylblad. Den ena har ett _blank mål medan den andra är inställd på _parent.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Utdata: texthyperlänkar läggs till i kalkylbladet**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

####  **Bild URL-hyperlänkar**

Exemplet nedan lägger till hyperlänk för bildadress till ett kalkylblad.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Utdata: bildhyperlänk har lagts till i kalkylbladet**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

##  **Sortering av data**

Sortering är en mycket värdefull funktion när det kommer till databehandling. Osorterade data är jobbigt för användare när de söker efter specifik information. Aspose.Cells.GridWeb stöder kraftfulla sorteringsfunktioner. Det här ämnet diskuterar sortering av data med hjälp av Aspose.Cells.GridWeb API.

Aspose.Cells.GridWeb låter utvecklare sortera data horisontellt och vertikalt så att utvecklare kan sortera data från topp till botten eller vänster till höger.

###  **Från topp till tå**

Så här sorterar du data från topp till botten:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Öppna kalkylbladet som du vill sortera.
1. Sortera dataintervallet i valfri ordning (stigande eller fallande). Var noga med att välja topp till botten orientering.

Exemplet nedan sorterar data i två kolumner (Student ID och Student Name) i ett kalkylblad i stigande ordning. Endast tolv rader med två kolumner är sorterade i topp till botten orientering.

Innan du använder koden innehåller kalkylbladet oordnade data.

**Inmatning: osorterade data** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Efter exekvering av koden sorteras data i stigande ordning.

**Utdata: data sorterad uppifrån och ned i stigande ordning** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

###  **Från vänster till höger**

Så här sorterar du data från vänster till höger:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Öppna kalkylbladet som du vill sortera.
1. Sortera dataintervallet i valfri ordning (stigande eller fallande). Var noga med att välja vänster till höger.

Exemplet nedan sorterar data i två rader (Student ID och Student Name) i stigande ordning. Endast två rader med fyra kolumner sorteras från vänster till höger.

Innan du använder koden innehåller kalkylbladet oordnade data.

**Indata: osorterad data innan kodavsnittet körs** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Efter exekvering av koden sorteras data i stigande ordning.

**Utdata: data sorterad från vänster till höger i stigande ordning** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

##  **Söka och ersätta**

Ett av de snabbaste sätten att göra repetitiva ändringar i ett stort kalkylblad är att använda sök- och ersätt-funktionen. Find hjälper dig att hitta en textsträng eller data och ersätta den med ett nytt värde. Aspose.Cells.GridWeb tillhandahåller denna funktion. Det gör att du kan söka efter och ersätta med en specifik textsträng eller värde i kalkylbladets klientsida genom en enkel dialog. Det låter dig till och med leta efter partiella data.

###  **Dialogrutan Sök/Ersätt**

Det finns två sätt att öppna dialogrutan Sök/Ersätt:

1.  När kontrollen är aktiv, tryck**CTRL+F** för att öppna dialogrutan, eller tryck**CTRL+R** för att öppna dialogrutan med**Byta ut** knappen aktiverad.
1.  Flytta markören till cellområdet i kalkylbladet och högerklicka sedan. Välj**Hitta** eller**Byta ut** från menyn.

**Välj Sök**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

En dialogruta för sök och ersätt visas.

**Dialogrutan Sök/ersätt**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Använder Hitta**

Att söka:

1. Öppna dialogrutan Sök/Ersätt.
1. Skriv strängen du vill söka efter i fältet Hitta vad.
1. Klicka på Hitta nästa för att söka.

Nästa cell som matchar ditt sökvillkor är markerad.

{{% alert color="primary" %}}

Om ditt sökkriterium inte hittas visas en dialogruta som talar om för dig.

{{% /alert %}}

###  **Sökalternativ**

Det finns några sökalternativ som du kan anpassa i dialogrutan. Tabellen nedan listar dem.

|**Nej.**|**Alternativets namn**|**Beskrivning**|
| :- | :- | :- |
|1|Liknande fall|Anger om skiftlägeskänsligt ska användas vid sökning.|
|2|Matcha hela ordet|Anger om hela ordet ska matchas vid sökning.|
|3|Sök upp|Indikerar om sökningen kommer att göras från botten till toppen.|
|4|Vanligt uttryck|När den är markerad kommer kontrollen att behandla strängen i textrutan Hitta vad som ett reguljärt uttryck i sökprocessen.|
|5|Hitta i Formler/Värden|När formlerna är vald kommer kontrollen att matcha formeln eller det oformaterade värdet för cellerna om formeln eller det oformaterade värdet finns. När värden är vald kommer kontrollen endast att matcha det visade värdet för cellerna.|

###  **Använder Ersätt**

Så här ersätter du text eller värden:

1.  Öppna dialogrutan Sök/Ersätt genom att trycka på**CTRL+F**, eller välj högerklicka på en cell och välj **Sök** innan du klickar på *Ersätt**.
1.  Skriv ersättningssträngen i**Ersätta med**fält.
1. Klicka på *Ersätt**.

Så här ersätter du text:

1. Öppna dialogrutan.
1.  Skriv in texten du vill hitta i**Hitta vad** fältet och texten du vill ersätta det inom**Ersätta med** fält.
1.  Ersätt en förekomst i taget genom att klicka**Hitta nästa** följt av *Ersätt**.
1. Om du är mycket säker på vad kalkylbladet innehåller, klicka på *Ersätt alla**.

{{% alert color="primary" %}}

 Om kalkylbladet inte är i redigeringsläge,**Byta ut** knappen visas inte.

{{% /alert %}}

## Lägg till/ta bort hyperlänkar från klientsidan

Aspose.Cells GridWeb stöder nu att lägga till och ta bort hyperlänkar från klientsidan. För detta tillhandahåller API funktionerna "addCelllink" och "delCelllink". Följande kodsnuttar visar hur man lägger till och tar bort hyperlänkar från klientsidan i GridWeb.

###  Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Du kan också länka till arket med hjälp av följande kodavsnitt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

##  Uppdatera teckensnittsinställningar från klientsidan

Aspose.Cells GridWeb stöder nu ändring av teckensnittsinställningar från klientsidan. För detta tillhandahåller API följande funktioner

- *updateCellFontStyle**: Params - r/i/b/ib för vanlig/kursiv/fet/kursiv&&fet
- *updateCellFontSize**: Params - teckensnittsnamn, etc. 'System'
- *updateCellFontName**: Params - fontsize, etc. '12pt'
- *updateCellFontColor**: Params - none/u/l/ul/ för ingen/understrecka/överstruken/understruken&&överstruken
- *updateCellFontLine**: Params - html-färg som #aa22ee eller välkänt färgnamn som grönt, rött,...
- *updateCellBackGroundColor**: Params - html-färg som #aa22ee eller välkänt färgnamn som grönt, rött,...

Följande kodavsnitt visar hur du ändrar teckensnittsinställningar från klientsidan i GridWeb.

###  Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

##  Lägg till/ta bort kommentarer från klientsidan

Aspose.Cells GridWeb stöder nu att lägga till och ta bort kommentarer från klientsidan. För detta tillhandahåller API funktionerna "addcomments" och "decomments". Följande kodavsnitt visar hur man lägger till och tar bort kommentarer från klientsidan i GridWeb.

###  Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

##  Visa knappar för att lägga till/ta bort kalkylblad

 Aspose.Cells GridWeb stöder nu att lägga till och ta bort ark genom att använda knappar i verktygsfältet. För att knapparna ska vara synliga på fronten måste du ställa in**GridWeb1.ShowAddButton** till *sant**. Följande kodavsnitt visar hur man lägger till Lägg till/ta bort-knappar i GridWeb-verktygsfältet.

###  Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
