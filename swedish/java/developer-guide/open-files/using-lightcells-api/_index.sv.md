---
title: Använder LightCells API
type: docs
weight: 80
url: /sv/java/using-lightcells-api/
---
{{% alert color="primary" %}}

Ibland behöver du läsa och skriva stora Microsoft Excel-filer med en enorm lista med data eller innehåll i kalkylbladet. LightCells API är användbar för att skapa enorma Excel-kalkylblad: med den behöver du minne och få bättre prestanda och effektivitet.

{{% /alert %}}

## **Händelsedriven arkitektur**

Aspose.Cells tillhandahåller LightCells API, huvudsakligen utformade för att manipulera celldata en efter en utan att bygga ett komplett datamodellblock (med Cell-samlingen etc.) i minnet. Det fungerar i ett händelsestyrt läge.

För att spara arbetsböcker, ange cellinnehållet cell för cell när du sparar, och komponenten sparar det direkt i utdatafilen.

När du läser mallfiler analyserar komponenten varje cell och ger deras värde en efter en.

I båda procedurerna bearbetas ett Cell-objekt och kasseras sedan, Workbook-objektet innehåller inte samlingen. I detta läge sparas därför minne vid import och export av Microsoft Excel-fil som har en stor datamängd som annars skulle använda mycket minne.

Även om LightCells API bearbetar cellerna på samma sätt för XLSX- och XLS-filer (den laddar faktiskt inte alla celler i minnet utan bearbetar en cell och kasserar den), sparar den minnet mer effektivt för XLSX filer på grund av 4 än 4811 filer de olika datamodellerna och strukturerna för de två formaten.

 I alla fall,**för XLS filer** , för att spara mer minne kan utvecklare ange en tillfällig plats för att spara temporär data som genereras under Spara-processen. Vanligen,**att använda LightCells API för att spara XLSX fil kan spara 50 % eller mer minne** än att använda det vanliga sättet,**Att spara XLS kan spara cirka 20-40 % minne**.

### **Skriva stora Excel-filer**

Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataProvider, som måste implementeras i ditt program. Gränssnittet representerar dataleverantör för att spara stora kalkylbladsfiler i lättviktsläge.

När du sparar en arbetsbok i det här läget, markeras startSheet(int) när du sparar alla kalkylblad i arbetsboken. För ett ark, om startSheet(int) är sant, tillhandahålls alla data och egenskaper för rader och celler i detta ark som ska sparas av denna implementering. I första hand anropas nextRow() för att få nästa radindex som ska sparas. Om ett giltigt radindex returneras (radindexet måste vara i stigande ordning för att raderna ska sparas), tillhandahålls ett Row-objekt som representerar denna rad för implementering för att ställa in dess egenskaper med startRow(Row).

För en rad, checkas nextCell() först. Om ett giltigt kolumnindex returneras (kolumnindexet måste vara i stigande ordning för att alla celler i en rad ska sparas), så tillhandahålls ett Cell-objekt som representerar denna cell för att ställa in data och egenskaper av startCell(Cell). Efter att data för denna cell har ställts in, sparas denna cell direkt i den genererade kalkylarksfilen och nästa cell kommer att kontrolleras och bearbetas.

Följande exempel visar hur LightCells API fungerar.

Följande program skapar en enorm fil med 100 000 poster i ett kalkylblad, fylld med data. Vi har lagt till några hyperlänkar, strängvärden, numeriska värden och även formler till vissa celler i kalkylbladet. Dessutom har vi formaterat ett antal celler också.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Läsa stora Excel-filer**

Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataHandler, som måste implementeras i ditt program. Gränssnittet representerar dataleverantören för att läsa stora kalkylbladsfiler i ett lättviktsläge.

När du läser en arbetsbok i det här läget, kontrolleras startSheet() när du läser alla kalkylblad i arbetsboken. För ett ark, om startSheet() returnerar sant, kontrolleras och bearbetas alla data och egenskaper för cellerna i arkets rader och kolumner. För varje rad anropas startRow() för att kontrollera om den behöver bearbetas. Om en rad behöver bearbetas läses radens egenskaper först och utvecklare kan komma åt dess egenskaper med processRow().

Om radens celler också behöver bearbetas, returnerar processRow() true och startCell() anropas för varje befintlig cell i raden för att kontrollera om den behöver bearbetas. Om den gör det anropas processCell().

Följande exempelkod illustrerar denna process. Programmet läser en stor fil med miljontals poster. Det tar lite tid att läsa varje blad i arbetsboken. Exempelkoden läser filen och hämtar det totala antalet celler, antal strängar och formler för varje kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

En klass som implementerar LightCellsDataHandler-gränssnittet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
