---
title: Aspose.Grid for .NET V2.0.1 Releaseinformation för nya utgåvor
type: docs
weight: 30
url: /sv/net/aspose-grid-for-net-v2-0-1-new-release-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Grid for .NET V2.0.1 Ny version](https://downloads.aspose.com/cells/net/new-releases/aspose.grid-for-.net-v2.0.1-new-release/)

{{% /alert %}} 

Vi har precis släppt Aspose.Grid v.

 Vad har ändrats:

 Aspose.Grid.Skrivbord



 l Stöder import/export till filformatet Excel2007xlsx.

 l Stöder läsning av sammanslagna cellers stil från Excel-fil.

 l Stöder Auto RowFilter och Custom RowFilter; lägga till egenskaperna IgnoreCase och IsStartWithCriteria till GridColumn för att anpassa beteendet för auto radfilter.

 l Lägger till CustomMsgTitle-egenskapen till Validation för att anpassa titeln på MessageBox.

 l Lägger till egenskapen RecalculateFormulas vars standardvärde är sant; när den är inställd på false, kommer inte formeln att räknas om om du tilldelar ett värde till en cell.

 l Lägger till egenskaper för bredd och höjd i kommentaren.

 l Lägger till egenskapen CommentFont till GridDesktop för att ställa in teckensnitt för kommentarer.

 l Tillhandahåller nya versioner för den överbelastade listan av Add-metoden för klassen CommentCollection för att specificera bredd och höjd på kommentarer.

 l Lägger till egenskapen IsVisible i arbetsbladet.

 Stöder läsning/skrivning av CustomProperties av Worksheet i excel-filer och att lägga till skrivskyddad CustomProperties-egenskap till Worksheet.

 l Stöder vlookup funktion/formel.

 l Stöder Ångra/Gör om funktioner när du ändrar värden på celler.

 l Lägger till ContextMenuManager-egenskapen till GridDesktop för att hantera snabbmenyn.

 l Lägger till händelsen RowColumnHiddenChanged.

 l Stöder flerval av rader/kolumner/regioner.

 l Stöder import/exportering av frysta paneler från/till excel-filer.

 l 36 korrigeringar och förbättringar.

 Aspose.Grid.Webb



 l 1 förbättring.



 Problem lösta i Aspose.Grid 2.0.1

|**Utfärdande ID** |**Komponent** |**Sammanfattning** |
|:- |:- |:- |
|7942 | Grid.Desktop| Ställer in värde för enstaka eller flytande typer till cellvisningar tomma.|
|7970 | Grid.Desktop| Kanterna längst ner till höger som inte visades normalt.|
|7971 | Grid.Desktop| Den svarta kanten på den fokuserade cellen som inte visades normalt.|
|7972 | Grid.Desktop| Demofunktioner ger undantag för filsökvägar som demonstrerar Pictures-funktionen.|
|7973 | Grid.Desktop| Lägger till SetSelectedIndex-metoden i ComboBox för att undvika omräkning av alla formler.|
|7974 | Grid.Desktop|Om du trycker på en tangent på ComboBox i en cell skulle det anropa redigering.|
|7975 | Grid.Desktop| Teckenstorleksfel i Format Cell Dialog.|
|7976 | Grid.Desktop| Den fokuserade cellen hade ändrats när valideringen misslyckades.|
|7977 | Grid.Desktop| Klistrar in celler flera gånger, vissa cellers bakgrundsfärg är inställd på blå.|
|7982 | Grid.Desktop| Problem med datasorteringsprestanda|
|7983 | Grid.Desktop| Klickar på rubrikraderna ändras radhöjden/kolumnbredden.|
|7984 | Grid.Desktop| Kan inte kopiera innehåll i inmatningsrutan i en cell via ctrl+c.|
|7985 | Grid.Desktop| Kastar undantag när ett värde över de frysta raderna ändras.|
|7986 | Grid.Desktop| Uppdaterar alla referenser till formlerna när du infogar eller tar bort rader eller kolumner.|
|7987 | Grid.Desktop| Ändrar en cells värde, bara de relativa formlerna kommer att räknas om och inte alla.|
|7988 | Grid.Desktop| Prestandaproblem för att kopiera/klistra in/ta bort ett antal celler|
|7989 | Grid.Desktop| Prestanda för beräkning av matrisformler|
|7990 | Grid.Desktop| Beräknar RowsCount / ColumnsCount-egenskapersfel vid åtkomst till Cells / Rows / Columns-egenskaper i kalkylbladet.|
|7991 | Grid.Desktop| Prestanda för ImportDataTable|
|7992 | Grid.Desktop|Ändrar höjden på hscrollbar och bredden på vscrollbar från 20 pixlar till 16.|
|7993 | Grid.Desktop| Lägger till SetSelectedIndex-metoden i ComboBox för att undvika omräkning av alla formler.|
|7994 | Grid.Desktop| Ändrar färgerna på rutnätslinjer, rubriklinjer och val.|
|7995 | Grid.Desktop| Beräknar synlig bredd på ritningstextfelet när en cell utökade sin text till rätt celler.|
|7996 | Grid.Desktop| Prestanda för rendering av kalkylblad|
|7997 | Grid.Desktop| SetFont & SetFontColor metoderna för GridRow fungerar inte.|
|7998 | Grid.Desktop| Ett ogiltigt cellnamn i formeln kan orsaka en ogiltig cellreferens|
|7999 | Grid.Desktop| Beteendet när du navigerar celler via rullningslister och piltangenter.|
|8000 | Grid.Desktop| Prestanda för att kopiera / klistra in ett stort antal celler inklusive massor av formler|
|8001 | Grid.Desktop| IComparer-undantag uppstår när ett kolumnvärde innehöll int- och strängtyper för automatisk filtrering av data|
|8003 | Grid.Desktop| Använder FormulaError-objekt som nu returnerar värde istället för att kasta undantag|
|8004 | Grid.Desktop| Booleskt värde i en cell återges inte till strängvärde.|
|8006 | Grid.Desktop| Placering av fokuserad cell i valläge för rader/kolumner|
|8007 | Grid.Desktop| Redigera problem med osynligt fokuserad cell|
|8020 | Grid.Desktop|Formelmotorn beräknar nollvärdet till resultatet av en tom sträng.|
|8085 | Grid.Desktop| Uppdaterar formlerfel vid radering av rader.|
|8289 | Grid.Desktop| Förbättrar formelfelmeddelanden.|
|8290 | Grid.Web| Prestandaproblem för många felformler.|

