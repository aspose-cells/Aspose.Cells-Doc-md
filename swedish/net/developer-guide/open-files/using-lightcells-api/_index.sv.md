---
title: Användning av LightCells API
type: docs
weight: 160
url: /sv/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

Ibland behöver du läsa och skriva stora Microsoft Excel-filer med en stor lista över data eller innehåll i kalkylarket. LightCells API är användbart för att skapa stora Exceldokument: med det behöver du mindre minne och får bättre prestanda och effektivitet.

{{% /alert %}} 
# Event Driven Architecture
Aspose.Cells tillhandahåller LightCells API, främst utformat för att manipulera celldata en i taget utan att bygga en komplett datamodellblock (med hjälp av Cell-samlingen etc.) i minnet. Det fungerar i ett händelsestyrt läge.

För att spara arbetsböcker, ange cellinnehållet cell för cell vid sparande, och komponenten sparar det till utdatafilen direkt.

När du läser mallfiler parsa komponenten varje cell och tillhandahåller deras värde en i taget.

I båda procedurerna bearbetas sedan en Cell-objekt och kastas sedan bort, Workbook-objektet håller inte samlingen. I detta läge sparas därför minnet när Microsoft Excel-fil med en stor datamängd importeras och exporteras, vilket annars skulle använda mycket minne.

Även om LightCells API bearbetar cellerna på samma sätt för XLSX- och XLS-filer (det läser inte faktiskt in alla celler i minnet utan bearbetar en cell och kastar sedan bort den), sparar det minnet effektivare för XLSX-filer än XLS-filer på grund av de olika datamodellerna och strukturerna för de två formaten.

För **XLS-filer** kan utvecklare dock för att spara minne specificera en temporär plats för att spara temporära data som genereras under sparandeprocessen. Vanligtvis kan **användning av LightCells API för att spara XLSX-fil spara 50 % eller mer minne** än att använda det vanliga sättet, **sparande XLS-fil kan spara cirka 20-40 % minne**.
## Skriver en stor Excel-fil
Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataProvider, som behöver implementeras i ditt program. Gränssnittet representerar datatillhandahållare för att spara stora kalkylbladsfiler i lättviktsläge.

När en arbetsbok sparas i detta läge, kontrolleras StartSheet(int) vid sparande av varje arbetsblad i arbetsboken. För ett blad, om StartSheet(int) returnerar true, tillhandahålls all data och egenskaper för rader och celler hos detta blad som ska sparas av denna implementation. Först kallas NextRow() för att få nästa radindex som ska sparas. Om en giltig radindex returneras (radindexet måste vara i stigande ordning för att raderna ska sparas), tillhandahålls en Row-objekt som representerar denna rad för implementeringen för att ställa in sina egenskaper genom StartRow(Row).

För en rad kontrolleras NextCell() först. Om en giltig kolumnindex returneras (kolumnindexet måste vara i stigande ordning för att alla celler i en rad ska sparas), tillhandahålls en Cell-objekt som representerar den cellen där implementering att ställa in dess data och egenskaper genom StartCell(Cell). Efter att cellens data har ställts in sparas cellen direkt till den genererade kalkylbladsfilen och nästa cell kontrolleras och bearbetas.
### Skriva en stor Excel-fil: Exempel
Se följande exempelkod för att se arbete med LightCells API. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.

Programmet skapar en stor fil med **10 000 (10000x30 matris) poster** i ett kalkylblad och fyller dem med fiktiva data. Du kan ange din egen matris genom att ändra variablerna rowsCount och colsCount i metoden Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Läs stora Excel-filer
Aspose.Cells tillhandahåller ett gränssnitt, LightCellsDataHandler, som behöver implementeras i ditt program. Gränssnittet representerar datatillhandahållare för att läsa stora kalkylbladsfiler i lättviktigt läge.

När en arbetsbok läses i detta läge kontrolleras StartSheet vid läsning av varje arbetsblad i arbetsboken. För ett blad, om StartSheet returnerar true, kontrolleras och bearbetas all data och egenskaper hos cellerna i rader och kolumner för bladet av denna gränssnittsimplementation. För varje rad kallas StartRow för att kontrollera om den behöver bearbetas. Om en rad behöver bearbetas läses först dess egenskaper och utvecklaren kan få åtkomst till dess egenskaper med ProcessRow. Om radens celler också behöver bearbetas, bör ProcessRow returnera true och sedan kallas StartCell för varje befintlig cell i raden för att kontrollera om en cell behöver bearbetas. Om en cell behöver bearbetas, kallas sedan ProcessCell för att bearbeta cellen av denna gränssnittsimplementation.
### Läs stora Excel-filer: Exempel
Se följande exempelkod för att se arbete med LightCells API. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.

Programmet läser en stor fil med miljontals poster i ett kalkylblad. Det tar lite tid att läsa varje blad i arbetsboken. Exempelkoden läser filen och hämtar det totala antalet celler, antalet strängar och antalet formler i varje kalkylblad.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
