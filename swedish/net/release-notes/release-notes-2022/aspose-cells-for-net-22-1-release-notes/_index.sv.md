---
title: Aspose.Cells för .NET 22.1 Release Notes
type: docs
weight: 12
url: /sv/net/aspose-cells-for-net-22-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 22.1](https://www.nuget.org/packages/Aspose.Cells/22.1.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50082|Stöd för att returnera originalindex för sorterade rader/kolumner för sort()-funktionen|Ny funktion|
|CELLSNET-50088|Stöd för att ställa in utskriftsjobbnamn med PrinterSettings under rendering till skrivare|Ny funktion|
|CELLSNET-50060|Upptäck om textfilen är csv eller tsv.|Ny funktion|
|CELLSNET-49939|Innehåll dolda rader och kolumner när du får Cells.MaxDisplayRange|Förbättring|
|CELLSNET-50054|Felaktigt resultat för beräkning av FREQUENCY-funktionen i matrisformel|Förbättring|
|CELLSNET-50072|Funktion som inte stöds: CUBESET|Förbättring|
|CELLSNET-50017|Hur man lägger till en bubbla bredvid diagramtitel & diagramaxeltext|Förbättring|
|CELLSNET-50038| Olika beteenden om att kollapsa och expandera grupper på flera nivåer|Förbättring|
|CELLSNET-50041| BMP-bildfiler visas inte i sidhuvud/sidfot|Förbättring|
|CELLSNET-50108|XLS till PDF: Konverteringen stannar med fullt minne|Prestanda|
|CELLSNET-50128|Radavståndet blir smalare - Excel till PDF-konvertering|Insekt|
|CELLSNET-50086|Cell färger försvinner efter konvertering till PDF|Insekt|
|CELLSNET-49996|Rich text-värden för celler kan gå vilse med MemoryPreference-läget|Insekt|
|CELLSNET-50042| Namnet på cellerna ändras under inspelning|Insekt|
|CELLSNET-50055|Egenskapen för lokalt intervallnamn FullText är inte escaped om det överordnade kalkylbladet har en apostrof|Insekt|
|CELLSNET-50154|GridWeb kan inte ladda /save från cache för .csv-fil|Insekt|
|CELLSNET-50063|Utskrift av Excel-fil återger två sidor istället för en sida|Insekt|
|CELLSNET-50094|Kalkylbladsinnehåll renderas inte korrekt i Excel till PDF-konvertering|Insekt|
|CELLSNET-50129|Utskriftspositionen går upp i takt med att sidan följs - Excel till PDF-konvertering|Insekt|
|CELLSNET-50131|Tecknen saknas - Excel till PDF-konvertering|Insekt|
|CELLSNET-49578| Fel max/min-värde beräknat från diagram av Aspose.Cells|Insekt|
|CELLSNET-50087|Utdatadiagrammet visas inte korrekt efter att serietypen ändrats|Insekt|
|CELLSNET-50197|Förklaringen i vattenfallsdiagrammet kan inte raderas eller döljas|Insekt|
|CELLSNET-50065|Olika beteenden när det gäller att kollapsa och utöka radgrupper på flera nivåer|Insekt|
|CELLSNET-50137|XLSX till HTML odeklarerad variabel "nod" i skript|Insekt|
|CELLSNET-50157|AutoFitMergedCellsType.EachLine fungerar inte för automatisk anpassning av kolumner|Insekt|
|CELLSNET-50165|Fonetisk guidefont ändras efter att filen har sparats|Insekt|
|CELLSNET-50208|En del text går förlorad när du sparar som HTML|Insekt|
|CELLSNET-50095|Undantag för att öppna XSLB-filen|Undantag|
|CELLSNET-50096|StackOverflowException när tomma kolumner tas bort|Undantag|
|CELLSNET-50071|Konvertering till HTML-undantag "Unsupported function: CUBESET"|Undantag|
|CELLSNET-50097|Undantag för att öppna XSLX-filen via Aspose.Cells|Undantag|
|CELLSNET-50133|NullReferenceException vid jämförelse av FillFormat|Undantag|
|CELLSNET-50138|Undantag för att öppna en XLSB-fil|Undantag|
|CELLSNET-50016|Diagram till EMF felaktiga axelvärden|Regression|
|


## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Ändrar beteende för att ta bort externa länkar från arbetsboken.**

I gamla versioner tar vi inte bort den externa länken vars url innehåller "AddIns". Sådant beteende är utformat för vissa användares speciella krav. Defekten med en sådan lösning är uppenbar: användare kan ange vilket giltigt filnamn eller sökväg som helst för de externa referenserna och i själva verket vill de flesta inte att de externa länkarna ska behandlas annorlunda. Från den här versionen filtrerar vi inte längre dessa externa länkar. Om användare har särskilda krav på vissa externa länkar, kan de kontrollera alla objekt i ExternalLinkCollection en efter en och bara ta bort de som de vill ta bort (med ExternalLinkCollection.RemoveAt(int)-metoden).

### **Ändrar beteende för Cell. Typ för ogiltigt datum och tid.**

I gamla versioner, om en cell begärs att formateras som datum och tid, returnerar Cell.Type CellValueType.IsDateTime oavsett om det numeriska värdet för denna cell är giltigt för datum och tid eller inte. Detta kan orsaka undantag om användare är beroende av Cell.Skriv endast och försöker ringa Cell.DateTimeValue. Från den här versionen returnerar vi CellValueType.IsNumeric för sådana typer av celler så att användaren kan vägledas för att få cellvärdet genom korrekt API.

### **Ändrar beteende för Cells.MaxDisplayRange.**

I gamla versioner täcker intervallvärdet för den här egenskapen alla celler som har instansierats i cellsamlingen. Från denna version gör vi att de osynliga raderna/kolumnerna exkluderas från kanterna på visningsområdet om det bara finns instansierade celler i dessa rader/kolumner.

### **Ändrar DataSorter.Sort()-metoder för att returnera de ursprungliga indexen för sorterade rader/kolumner.**

I gamla versioner returnerar DataSorter.Sort() metoder ingenting. Från denna version returnerar vi de ursprungliga indexen för rader/kolumner som motsvarar intervallet som har sorterats. Detta ger användaren möjlighet att utföra avancerad kontroll och operationer för sorteringen.

### **Lägger till egenskapen TxtLoadOptions.ExtendToNextSheet.**

Stöder import av CSV/TSV-data till flera kalkylblad om radantalet eller kolumnantal data överskrider ms excels gräns.

### **Lägger till metoden ExternalLinkCollection.Clear().**

Tar bort alla externa länkar från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.Clear(bool updateReferencesAsLocal).**

När du tar bort alla externa länkar från arbetsboken kan användaren bestämma hur man ska göra med formlerna som har referenser till dessa externa länkar. Om "updateReferencesAsLocal" är sant, kommer alla anpassade definierade funktioner i de externa länkarna att flyttas till den aktuella arbetsboken. Till exempel är en cells formel "='externalsource.xlam'!customfunction()", efter att den externa länken "externalsource.xlam" har tagits bort, kommer denna cells formel att bli "=customfunction()".

### **Lägger till ExternalLinkCollection.RemoveAt(int)-metoden.**

Tar bort en angiven extern länk från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.RemoveAt(int, bool updateReferencesAsLocal).**

I likhet med metoden ExternalLinkCollection.Clear(bool updateReferencesAsLocal) kan användaren bestämma hur formler som refererar till den angivna externa länken ska göras samtidigt som den tas bort från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.GetEnumerator().**

Tillhandahåller en enumerator för att iterera genom alla externa länkar i arbetsboken.

### **Föråldrade Workbook.RemoveExternalLinks()-metoden.**

Använd metoden ExternalLinkCollection.Clear() istället.

### **Obsoletes Workbook.HasExernalLinks()-metoden.**

Använd ExternalLinkCollection.Count för att kontrollera om det finns externa länkar i arbetsboken.

### **Tar bort föråldrad klass StyleCollection.**

Använd Workbook.CreateStyle() och Workbook.GetNamedStyle(sträng) för att manipulera stilar.

### **Lägger till konstruktorn PptxSaveOptions(bool saveAsImage).**

Representerar alternativ för att spara .pptx-fil. Om det är sant kommer arbetsboken att konverteras till några bilder av .pptx-filen. Om False, kommer arbetsboken att konverteras till vissa tabeller av .pptx-fil.

### **Lägger till metoden SheetRender.ToPrinter(PrinterSettings printerSettings, string jobName).**

Återge arbetsbladet till skrivaren med skrivarinställningar och skrivarjobbnamn.

### **Lägger till metoden WorkbookRender.ToPrinter(PrinterSettings printerSettings, string jobName).**

Återge arbetsboken till skrivaren med skrivarinställningar och skrivarjobbnamn.

### **Lägger till klassen ChartGlobalizationSettings.**

 Representerar globaliseringsinställningarna för diagram.

### **Lägger till egenskapen DataLabels.IsNeverOverlap.**

Indikerar om dataetiketterna aldrig överlappar varandra. (För cirkeldiagram)

### **Lägger till TickLabelItem-klassen.**

Inkludera information om ett Ticklabel-objekt.

### **Lägger till egenskapen TickLabelItem.Height.**

Får höjden på Ticklabel-objektet i förhållande till diagramhöjden.

### **Lägger till egenskapen TickLabelItem.Width.**

Får bredden på Ticklabel-objektet i förhållande till diagrambredden.

### **Lägger till egenskapen TickLabelItem.X.**

Får X av Ticklabel-objekt i förhållande till diagrambredd.

### **Lägger till egenskapen TickLabelItem.Y.**

Får Y av Ticklabel-objekt i förhållande till diagramhöjd.

### **Lägger till egenskapen TickLabels.TickLabelItems.**

Får föremålen från TickLabel.

