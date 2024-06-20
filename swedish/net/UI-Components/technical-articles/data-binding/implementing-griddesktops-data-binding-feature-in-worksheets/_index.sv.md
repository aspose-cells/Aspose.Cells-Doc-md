---
title: Implementering av GridDesktop Data Binding Feature i Worksheeter
type: docs
weight: 10
url: /sv/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop, databindning, data, bind
description: Den här artikeln introducerar hur man binder data i GridDesktop.
---

{{% alert color="primary" %}} 

Data Binding är en spännande funktion som erbjuds av Microsoft .NET Framework. Vi vet att DataGrid-kontrollen som erbjuds av Microsoft stöder data binding, vilket innebär att en DataGrid kan vara bunden till valfri Data Source (använda DataSet, DataTable och DataView objekt). Denna funktion har gjort utvecklarnas liv mycket enklare. Baserat på samma koncept stöder även Aspose.Cells.GridDesktop data binding, vilket gör att utvecklare kan binda arbetsblad till valfri datakälla. Den här artikeln utforskar funktionen.

{{% /alert %}} 
## **Skapar en provdatabas**
1. Skapa en provdatabas att använda med exemplet. Vi använde Microsoft Access för att skapa en provdatabas med en produktstabell (schema nedan). 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Tre fiktiva poster läggs till i produkttabellen.
   **Poster i produkttabellen** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Skapa en provapplikation**
Skapa nu en enkel skrivbordsapplikation i Visual Studio och gör följande.

1. Dra kontrollen "GridControl" från verktygsfältet och släpp den på formuläret.
1. Släpp fyra knappar från verktygsfältet längst ner på formuläret och ställ in deras textegenskap som **Bind Woksheet**, **Lägg till rad**, **Ta bort rad** och **Uppdatera till databasen** respektive.
## **Lägg till Namnområde och Deklarera Globala Variabler**
Eftersom detta exempel använder en Microsoft Access-databas, lägg till System.Data.OleDb-namnområdet högst upp i koden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Du kan nu använda klasserna förpackade under detta namnområde.

1. Deklarera globala variabler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Fylla Dataset med Data från Databasen**
Anslut nu till den provdatabasen för att hämta och fylla data i ett Dataset-objekt.

1. Använd OleDbDataAdapter-objektet för att ansluta till vår provdatabas och fylla ett Dataset med data som hämtats från produkttabellen i databasen, enligt koden nedan.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Bindning av kalkylark med Dataset**
Binda kalkylarket till Datasetets produkttabell:

1. Öppna önskat kalkylark.
1. Binda kalkylarket till Datasetets produktstabell.

Lägg till följande kod i händelsen för knappen **Bind Kalkylark**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Inställning av kolumnrubriker för kalkylark**
Det bundna kalkylarket laddar nu data framgångsrikt men kolumnrubrikerna är som standard märkta A, B och C. Det skulle vara bättre att ställa in kolumnrubrikerna till kolumnnamnen i databastabellen.

För att ställa in kolumnrubriker för kalkylarket:

1. Hämta bildtexterna för varje kolumn i DataTable (Products) i Datasetet.
1. Tilldela bildtexterna till rubrikerna för kalkylarkskolumnerna.

Lägg till den skrivna koden i händelsen för knappen **Bind Kalkylark** med följande kodsnutt. Genom att göra detta kommer de gamla kolumnrubrikerna (A, B och C) att ersättas med ProductID, ProductName och ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Anpassning av bredd och stil för kolumnerna**
För att förbättra kalkylarkets utseende ytterligare är det möjligt att ställa in bredd och stil för kolumnerna. Till exempel, ibland består kolumnrubriken eller värdet inuti kolumnen av ett långt antal tecken som inte passar inuti cellen. För att lösa sådana problem stöder Aspose.Cells.GridDesktop att ändra kolumnernas bredd.

Lägg till följande kod till knappen **Bind Kalkylark**. Kolumnbredderna kommer att anpassas enligt de nya inställningarna.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop stöder också att tillämpa anpassade stilar på kolumnerna. Följande kod, tillagd i knappen **Bind Kalkylark**, anpassar kolumnstilarna för att göra dem mer presenterbara.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Kör nu programmet och klicka på **Bind Worksheet**-knappen.
## **Lägger till rader**
För att lägga till nya rader i ett kalkylblad, använd Worksheet-klassens AddRow-metod. Det här lägger till en tom rad längst ner och en ny DataRow läggs till i datakällan (här läggs en ny DataRow till i DataSetets DataTable). Utvecklare kan lägga till så många rader de vill genom att fortsätta anropa AddRow-metoden. När en rad har lagts till kan användare ange värden i den.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Ta bort rader**
Aspose.Cells.GridDesktop stödjer också att ta bort rader genom att anropa Worksheet-klassens RemoveRow-metod. Det krävs index för den rad som ska tas bort vid borttagning av en rad med Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Lägg till ovanstående kod i **Delete Row**-knappen och kör programmet. Några poster visas innan raden tas bort. Genom att välja en rad och klicka på **Delete Row**-knappen tas den valda raden bort.
## **Spara ändringar till databasen**
Slutligen, för att spara alla ändringar som användare har gjort i kalkylbladet tillbaka till databasen, använd OleDbDataAdapter-objektets Update-metod. Update-metoden tar datakällan (DataSet, DataTable etc.) för kalkylbladet för att uppdatera databasen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Lägg till ovanstående kod i **Uppdatera till databas**-knappen.
1. Kör programmet.
1. Utför några operationer på kalkylbladsdata, kanske lägga till nya rader och redigera eller ta bort befintliga data.
1. Klicka sedan på **Uppdatera till databas** för att spara ändringarna i databasen.
1. Kontrollera databasen för att se att tabellens poster har uppdaterats därefter.
