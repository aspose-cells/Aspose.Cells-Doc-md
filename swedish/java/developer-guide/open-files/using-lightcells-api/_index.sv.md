---
title: Användning av LightCells API
type: docs
weight: 80
url: /sv/java/using-lightcells-api/
---

{{% alert color="primary" %}}

Ibland måste du läsa och skriva stora Microsoft Excel-filer med en enorm lista över data eller innehåll i arket. LightCells API är användbar för att skapa stora Excelfiler: med det behöver du minne och får bättre prestanda och effektivitet.

{{% /alert %}}

## **Händelsestyrd arkitektur**

Aspose.Cells tillhandahåller LightCells API, främst utformat för att manipulera celldata en i taget utan att bygga en komplett datamodellblock (med hjälp av Cell-samlingen etc.) i minnet. Det fungerar i ett händelsestyrt läge.

För att spara arbetsböcker, ange cellinnehållet cell för cell vid sparande, och komponenten sparar det till utdatafilen direkt.

När du läser mallfiler parsa komponenten varje cell och tillhandahåller deras värde en i taget.

I båda procedurerna bearbetas sedan en Cell-objekt och kastas sedan bort, Workbook-objektet håller inte samlingen. I detta läge sparas därför minnet när Microsoft Excel-fil med en stor datamängd importeras och exporteras, vilket annars skulle använda mycket minne.

Även om LightCells API bearbetar cellerna på samma sätt för XLSX- och XLS-filer (det läser inte faktiskt in alla celler i minnet utan bearbetar en cell och kastar sedan bort den), sparar det minnet effektivare för XLSX-filer än XLS-filer på grund av de olika datamodellerna och strukturerna för de två formaten.

För **XLS-filer** kan utvecklare dock för att spara minne specificera en temporär plats för att spara temporära data som genereras under sparandeprocessen. Vanligtvis kan **användning av LightCells API för att spara XLSX-fil spara 50 % eller mer minne** än att använda det vanliga sättet, **sparande XLS-fil kan spara cirka 20-40 % minne**.

### **Skrivning av stora Excel-filer**

Aspose.Cells tillhandahåller en gränssnitt, LightCellsDataProvider, som måste implementeras i ditt program. Gränssnittet representerar Dataprovider för att spara stora kalkylbladsfiler i lättviktigt läge.

När du sparar en arbetsbok i detta läge kontrolleras startSheet(int) när varje kalkylblad i arbetsboken sparas. För ett ark, om startSheet(int) är sant, då tillhandahålls all data och egenskaper för rader och celler i detta ark som ska sparas av denna implementation. Först kallas nextRow() för att få nästa radindex som ska sparas. Om ett giltigt radindex returneras (radindexet måste vara i stigande ordning för rader som ska sparas), tillhandahålls en Row-objekt som representerar denna rad för implementationen för att ange dess egenskaper med startRow(Row).

För en rad kontrolleras nästaCell() först. Om ett giltigt kolumnindex returneras (kolumnindexet måste vara i stigande ordning för alla celler i en rad som ska sparas), tillhandahålls en Cell-objekt som representerar denna cell för att ange data och egenskaper med startCell(Cell). Efter att data för denna cell har angetts, sparas denna cell direkt till den genererade kalkylbladsfilen och nästa cell kontrolleras och bearbetas.

Följande exempel visar hur LightCells API fungerar.

Programmet skapar en stor fil med 100 000 poster i ett kalkylblad, fyllt med data. Vi har lagt till några hyperlänkar, strängvärden, numeriska värden och också formler till vissa celler i kalkylbladet. Dessutom har vi formaterat en rad celler också.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Läsning av stora Excel-filer**

Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataHandler, som måste implementeras i ditt program. Gränssnittet representerar dataprovider för att läsa stora kalkylbladsfiler i lättviktigt läge.

Vid läsning av en arbetsbok i detta läge kontrolleras startSheet() när varje kalkylblad i arbetsboken läses. För ett ark, om startSheet() returnerar true, då kontrolleras och bearbetas all data och egenskaper för cellerna i arkets rader och kolumner. För varje rad kallas startRow() för att kontrollera om den måste bearbetas. Om en rad måste bearbetas, läses först radens egenskaper och utvecklare kan komma åt dess egenskaper med processRow().

Om radens celler också måste bearbetas, då returnerar processRow() true och startCell() kallas för varje befintlig cell i raden för att kontrollera om den måste bearbetas. Om den måste det, kallas processCell().

Följande exempelkod illustrerar denna process. Programmet läser en stor fil med miljontals poster. Det tar lite tid att läsa varje kalkylblad i arbetsboken. Exempelkoden läser filen och hämtar det totala antalet celler, antal strängar och antal formler för varje kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

En klass som implementerar LightCellsDataHandler-gränssnittet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
