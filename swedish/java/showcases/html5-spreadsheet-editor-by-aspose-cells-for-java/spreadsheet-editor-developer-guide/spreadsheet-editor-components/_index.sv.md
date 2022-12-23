---
title: Kalkylarksredigerare - Komponenter
type: docs
weight: 50
url: /sv/java/spreadsheet-editor-components/
---
**Innehållsförteckning**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Arbetsbladsvy](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 Spreadsheet Editor är byggd av ett fåtal komponenter som går samman för att göra hela systemet. Här beskriver vi var och ens syfte och roll.
### **Index.html**
Det är en JSF-sida som beskriver redaktörens användargränssnitt och huvudslutpunkten för vår applikation. All interaktion som utförs mellan webbläsare och server utförs via denna slutpunkt.

Förutom att definiera användargränssnittet, bifogas alla backend-tjänster här med JSF-teknik. När användaren interagerar med UI-händelserna och data skickas fram och tillbaka mellan tjänster och användare för att slutföra våra uppgifter, t.ex. exportera kalkylblad.

Den har två huvudsakliga intresseområden.

**Band**

Området med flikar i verktygsfältet ovanpå kallas band, tekniskt sett. Den innehåller knappar, rullgardinsmenyer, radiomenyer, textrutor och några dolda fält som används för att utföra många operationer på kalkylarket. Dessa knappar när de klickas skicka kommandon till servern och uppdatera arket därefter.

**Ark**

Arket är raderna och kolumnerna. När celler klickas uppdateras menyfliksområdet utan att skicka förfrågningar till servern eftersom all data som behövs av menyfliksområdet är kopplad till varje cell. Menyfliksområdet håller också koll på den valda cellen, raden och kolumnen när användaren navigerar genom arket.

Varje cell har sin egen inline-editor som blir synlig när en cell är i redigeringsläge.
### **Arbetsbladsvy**
Det är en JSF-backend-böna med vyer som ansvarar för att hantera det dynamiska innehållet i användargränssnittet som beskrivs i index.html. Den har händelsehanterare för Ajax-förfrågningar som utlöses när användaren interagerar med användargränssnittet.
### **WorkbookService**
WorkbookService är en JSF-backend-böna med vyer. Den fungerar som en tjänstekomponent och får kalkylarket laddat och urladdat med hjälp av andra tjänster. Den har följande slutpunkter:

**i det**

 De**i det** är**PostConstruct** metod som exekveras direkt efter att objektskapandet har slutförts av Java Application Server. Det kollar efter**url** parameter i begäran parametrar kartlägger och laddar motsvarande kalkylblad från given plats, om möjligt.

**förstöra**

Det är ansvarigt att sanera alla förvärvade resurser när de inte längre behövs.
### **LoaderService**
Det skapar instanser av kalkylblad och sparar dem i minnet så länge de behövs.
### **CellsService**
 De**CellsService** hanterar cache för rader, kolumner, celler, formatering och struktur för kalkylblad.
