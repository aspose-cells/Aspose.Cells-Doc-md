---
title: Använder LightCells API
type: docs
weight: 160
url: /sv/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

Ibland behöver du läsa och skriva stora Microsoft Excel-filer med en enorm lista med data eller innehåll i kalkylbladet. LightCells API är användbar för att skapa enorma Excel-kalkylblad: med den behöver du mindre minne och få bättre prestanda och effektivitet.

{{% /alert %}} 
# Händelsedriven arkitektur
Aspose.Cells tillhandahåller LightCells API, huvudsakligen utformade för att manipulera celldata en efter en utan att bygga ett komplett datamodellblock (med Cell-samlingen etc.) i minnet. Det fungerar i ett händelsestyrt läge.

För att spara arbetsböcker, ange cellinnehållet cell för cell när du sparar, och komponenten sparar det direkt i utdatafilen.

När du läser mallfiler analyserar komponenten varje cell och ger deras värde en efter en.

I båda procedurerna bearbetas ett Cell-objekt och kasseras sedan, Workbook-objektet innehåller inte samlingen. I detta läge sparas därför minne vid import och export av Microsoft Excel-fil som har en stor datamängd som annars skulle använda mycket minne.

Även om LightCells API bearbetar cellerna på samma sätt för XLSX- och XLS-filer (den laddar faktiskt inte alla celler i minnet utan bearbetar en cell och kasserar den), sparar den minne mer effektivt för XLSX-filer än XLS-filer på grund av de olika datamodellerna och strukturerna för de två formaten.

 I alla fall,**för XLS-filer** , för att spara mer minne kan utvecklare ange en tillfällig plats för att spara temporär data som genereras under Spara-processen. Vanligen,**att använda LightCells API för att spara XLSX-fil kan spara 50 % eller mer minne** än att använda det vanliga sättet,**Att spara XLS kan spara cirka 20-40 % minne**.
## Skriva en stor Excel-fil
Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataProvider, som måste implementeras i ditt program. Gränssnittet representerar dataleverantören för att spara stora kalkylbladsfiler i lättviktsläge.

När du sparar en arbetsbok med det här läget, kontrolleras StartSheet(int) när du sparar alla kalkylblad i arbetsboken. För ett ark, om StartSheet(int) är sant, tillhandahålls alla data och egenskaper för rader och celler i detta ark som ska sparas av denna implementering. I första hand anropas NextRow() för att få nästa radindex som ska sparas. Om ett giltigt radindex returneras (radindexet måste vara i stigande ordning för att raderna ska sparas), tillhandahålls ett Row-objekt som representerar denna rad för implementering för att ställa in dess egenskaper med StartRow(Row).

För en rad kontrolleras NextCell() först. Om ett giltigt kolumnindex returneras (kolumnindexet måste vara i stigande ordning för att alla celler i en rad ska sparas), så tillhandahålls ett Cell-objekt som representerar den cellen för implementering för att ställa in dess data och egenskaper av StartCell(Cell). Efter att cellens data har ställts in, sparas cellen direkt i den genererade kalkylbladsfilen och nästa cell kontrolleras och bearbetas.
### Skriva en stor Excel-fil:Exempel
Se följande exempelkod för att se hur LightCells API fungerar. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.

 Programmet skapar en enorm fil med**10 000 (10 000 x 30 matris) poster** i ett kalkylblad och fyller dem med dummydata. Du kan ange din egen matris genom att ändra variablerna rowsCount och colsCount i metoden Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Läsa stora Excel-filer
Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataHandler, som måste implementeras i ditt program. Gränssnittet representerar dataleverantör för att läsa stora kalkylbladsfiler i lättviktsläge.

När du läser en arbetsbok i det här läget, kontrolleras StartSheet när du läser alla kalkylblad i arbetsboken. För ett ark, om StartSheet returnerar sant, kontrolleras och bearbetas alla data och egenskaper för cellerna i rader och kolumner i arket av implementeringen av detta gränssnitt. För varje rad anropas StartRow för att kontrollera om den behöver bearbetas. Om en rad behöver bearbetas läses dess egenskaper först och utvecklaren kan komma åt dess egenskaper med ProcessRow. Om radens celler också behöver bearbetas, bör ProcessRow returnera true och sedan anropas StartCell för varje befintlig cell i raden för att kontrollera om en cell behöver bearbetas. Om en cell behöver bearbetas, anropas ProcessCell för att bearbeta cellen genom implementeringen av detta gränssnitt.
### Läsa stora Excel-filer: Exempel
Se följande exempelkod för att se hur LightCells API fungerar. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.

Programmet läser en enorm fil med miljontals poster i ett kalkylblad. Det tar lite tid att läsa varje blad i arbetsboken. Exempelkoden läser filen och hämtar det totala antalet celler, antalet strängar och formelantalet i varje kalkylblad.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
