---
title: Implementera GridDesktop-databindningsfunktionen i kalkylblad
type: docs
weight: 10
url: /sv/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

Databindning är en spännande funktion som erbjuds av Microsoft .NET Framework. Vi vet att DataGrid-kontrollen som erbjuds av Microsoft stöder databindning, vilket innebär att ett DataGrid kan bindas till vilken datakälla som helst (med hjälp av DataSet-, DataTable- och DataView-objekt). Den här funktionen har gjort utvecklarnas liv mycket enklare. Baserat på samma koncept stöder Aspose.Cells.GridDesktop även databindning, vilket gör att utvecklare kan binda kalkylblad till vilken datakälla som helst. Den här artikeln utforskar funktionen.

{{% /alert %}} 
## **Skapa en exempeldatabas**
1.  Skapa en exempeldatabas att använda med exemplet. Vi använde Microsoft Access för att skapa en exempeldatabas med en produkttabell (schema nedan).

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Tre dummy-poster läggs till i tabellen Produkter.
   **Poster i produkttabellen** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Skapa en exempelapplikation**
Skapa nu ett enkelt skrivbordsprogram i Visual Studio och gör följande.

1. Dra "GridControl"-kontrollen från verktygslådan och släpp den i formuläret.
1. Släpp fyra knappar från verktygslådan längst ner i formuläret och ställ in deras textegenskap som**Bind Woksheet**, **Lägg till rad**, **Ta bort rad** och**Uppdatering till databas** respektive.
## **Lägga till namnutrymme och deklarera globala variabler**
Eftersom det här exemplet använder en Microsoft Access-databas lägger du till namnområdet System.Data.OleDb överst i koden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Du kan nu använda klasserna paketerade under detta namnutrymme.

1. Deklarera globala variabler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Fyller Dataset med data från databasen**
Anslut nu till exempeldatabasen för att hämta och fylla data i ett DataSet-objekt.

1. Använd OleDbDataAdapter-objektet för att ansluta till vår exempeldatabas och fyll en DataSet med data hämtade från produkttabellen i databasen, som visas i koden nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Bindande arbetsblad med DataSet**
Bind samman kalkylbladet med tabellen Produkter i datauppsättningen:

1. Öppna ett önskat arbetsblad.
1. Bind samman kalkylbladet med DataSets produkttabell.

 Lägg till följande kod till**Bind arbetsblad** knappens klickhändelse.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Ställa in kolumnrubriker för kalkylblad**
Det bundna kalkylbladet laddar nu data framgångsrikt men kolumnrubrikerna är märkta A, B och C som standard. Det skulle vara bättre att ställa in kolumnrubrikerna till kolumnnamnen i databastabellen.

Så här ställer du in kalkylbladets kolumnrubriker:

1. Hämta bildtexterna för varje kolumn i datatabellen (produkter) i datauppsättningen.
1. Tilldela bildtexterna till rubrikerna i kalkylbladskolumner.

 Lägg till koden skriven i**Bind arbetsblad** knappens klickhändelse med följande kodavsnitt. Genom att göra detta kommer de gamla kolumnrubrikerna (A, B och C) att ersättas med ProductID, ProductName och ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Anpassa bredd och stilar för kolumner**
För att förbättra utseendet på kalkylbladet ytterligare är det möjligt att ställa in bredden och stilarna för kolumner. Till exempel, ibland består kolumnrubriken eller värdet inuti kolumnen av ett långt antal tecken som inte får plats i cellen. För att lösa sådana problem stöder Aspose.Cells.GridDesktop att ändra bredden på kolumner.

 Lägg till följande kod till**Bind arbetsblad** knapp. Kolumnbredderna kommer att anpassas enligt de nya inställningarna.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop stöder också att tillämpa anpassade stilar på kolumner. Följande kod, bifogad till**Bind arbetsblad** knappen, anpassar kolumnstilarna för att göra dem mer presentabla.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Kör nu programmet och klicka på**Bind arbetsblad** Knapp.
## **Lägga till rader**
För att lägga till nya rader i ett kalkylblad, använd metoden Worksheet class AddRow. Detta läggs till en tom rad längst ner och en ny DataRow läggs till i datakällan (här läggs en ny DataRow till i DataSets DataTable). Utvecklare kan lägga till så många rader de vill genom att anropa AddRow-metoden igen och igen. När en rad har lagts till kan användare ange värden i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Ta bort rader**
Aspose.Cells.GridDesktop stöder också radering av rader genom att anropa Worksheet-klassen RemoveRow-metoden. Ta bort en rad med Aspose.Cells.GridDesktop kräver att radens index tas bort.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Lägga till ovanstående kod till**Ta bort rad** knappen och kör programmet. Några få poster visas innan raden tas bort. Välj en rad och klicka på**Ta bort rad** knappen tar bort den valda raden.
## **Spara ändringar i databasen**
Slutligen, för att spara eventuella ändringar som gjorts av användare i kalkylbladet tillbaka till databasen, använd OleDbDataAdapter-objektets uppdateringsmetod. Uppdateringsmetoden tar datakällan (DataSet, DataTable etc.) i kalkylbladet för att uppdatera databasen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  Lägg till ovanstående kod till**Uppdatering till databas** knapp.
1. Kör programmet.
1. Utför några operationer på kalkylbladets data, kanske lägg till nya rader och redigera eller ta bort befintliga data.
1.  Klicka sedan**Uppdatering till databas** för att spara ändringarna i databasen.
1. Kontrollera databasen för att se att tabellposterna har uppdaterats därefter.
