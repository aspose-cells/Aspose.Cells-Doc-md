---
title: Aspose.Cells för Java 17.9 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-17-9-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 17.9](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.9/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42391|Cell bredd som visas i den resulterande PDF-filen är inte densamma som i Excel-filen när du använder funktionen "Visa formel"|Ny funktion|
|CELLSJAVA-42379|Implementera namngiven destination vid rendering till PDF-utdata (bokmärkesfråga)|Ny funktion|
|CELLSJAVA-42401|Måste räkna upp alla former för att ställa in Z-ordningen för formen korrekt|Förbättring|
|CELLSJAVA-42368|Ange namn på ActiveX-kontrollen (ListBox)|Förbättring|
|CELLSJAVA-42369|HTML-utdata från Excel-dokument innehåller hashvärden istället för faktiska värden|Insekt|
|CELLSJAVA-42366|Att spara "2.2 CompleteEmail.html" till XLSX-format genererar korrupta filer|Insekt|
|CELLSJAVA-42365|När "2.1 CompleteEmail.html" läses in i Workbook-objektet skapas NullPointerException|Insekt|
|CELLSJAVA-42381|Arbetsboksberäkning är fel för Lookup Excel-formel|Insekt|
|CELLSJAVA-42380|Arrayformeln i arket beräknas annorlunda via Aspose.Cells|Insekt|
|CELLSJAVA-42370|Felaktiga hyperlänkar och PDF-innehåll|Insekt|
|CELLSJAVA-42395|Återgivning - Sjökortsbilden är inte korrekt|Insekt|
|CELLSJAVA-42393|Kategoriaxeletiketter saknas vid konvertering av Excel till PDF|Insekt|
|CELLSJAVA-42384|Färgen på negativa staplar är inte korrekt när Excel konverteras till PDF|Insekt|
|CELLSJAVA-42378|Stapelfärgen ändrades vid konvertering av Excel till PDF när setCrossAt() användes|Insekt|
|CELLSJAVA-42377|Värdet på huvudaxelenheterna i diagrammet returneras fel|Insekt|
|CELLSJAVA-42364|Dataetiketter från cellintervall kommer inte när de exporteras till PDF|Insekt|
|CELLSJAVA-42359|Dataetiketter saknas för en serie som har stapelvärden som 100|Insekt|
|CELLSJAVA-42314|Diagrammet är tomt i utdata-PNG|Insekt|
|CELLSJAVA-42313|Diagrammet är tomt i utdata-PDF-filen|Insekt|
|CELLSJAVA-42374|Teckenreferenser tolkade felaktigt av Aspose Cells|Insekt|
|CELLSJAVA-42373|Att kopiera arbetsboken och sedan spara förstör Excel-utdatafilen|Insekt|
|CELLSJAVA-42392|Undantag "com.aspose.cells.CellsException: okänt excel-innehåll!" på att instansiera en krypterad Excel-fil|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen HTMLLoadOptions.LoadStyleStrategy**
Indikerar strategin för att tillämpa stil för analyserade värden vid konvertering av strängvärde till nummer eller DateTime.
### **Lägger till klass AbstractCalculationMonitor**
Tillhandahåller API:er för användare att övervaka framstegen i formelberäkningen.
### **Lägger till egenskapen CalculationOptions.CalculationMonitor**
Tillåter användaren att tillhandahålla anpassad implementering för att övervaka framstegen i formelberäkningen.
### **Lägger till enum GridlineType**
Räknar upp rutnätstyp.
### **Lägger till egenskapen ImageOrPrintOptions.GridlineType**
Hämtar eller ställer in rutnätstyp.
### **Lägger till egenskapen PdfSaveOptions.GridlineType**
Hämtar eller ställer in rutnätstyp.
### **Lägger till metoderna Name.GetRanges(bool) och Name.GetRange(bool)**
För mestadels enkla namnobjekt, såsom namngivna intervall med absoluta referenser, behöver namnets referens inte beräknas upprepade gånger. Så GetRanges(false)/GetRange(false) kommer inte att räkna om Name-objektet när man hämtar motsvarande intervall och därför kan prestandan förbättras avsevärt om dessa metoder anropas upprepade gånger.
### **Lägger till egenskapen PdfBookmarkEntry.DestinationName**
Hämtar eller ställer in namnet på destinationen. Om destinationsnamn är inställt kommer destinationen att definieras som en namngiven destination med detta namn.
### **Lägger till metoden DataSorter.AddKey().**
Lägger till sorterat kolumnindex och sorteringsordning med anpassad sorteringslista.
### **Lägger till metoden Picture.Copy().**
Kopierar inställningar från andra bilder.
### **Lägger till metoden Shape.ToFrontOrBack().**
Tar fram formen eller skickar den till baksidan.
### **Lägger till enum ConnectionDataSourceType.Table**
Representerar tabellen som datakälla för anslutningen.
### **Lägger till metoden PageSetup.SetFitToPages().**
Ställer in antalet sidor som kalkylbladet skalas till när det skrivs ut.
### **Lägger till PdfSaveOptions.StreamProvider-egenskapen och ResourceLoadingType-enum**
Hämtar och ställer in typen av laddning av extern resurs.
### **Lägger till metoderna VbaModuleCollection.AddDesignerStorage() och GetDesignerStorage()**
Får och ställer in designerlagringen för VBA-projektet.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Lägg till PDF-bokmärken med namngivna destinationer](/cells/sv/java/add-pdf-bookmarks-with-named-destinations/)
- [Kontrollera laddningen av externa resurser i MS Excel Workbook medan du renderar till PDF](/cells/sv/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok](/cells/sv/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Skapa Ta bort och få GridCell-kommentarer](/cells/sv/java/create-remove-and-get-gridcell-comments/)
- [Skicka form fram eller bak i arbetsbladet](/cells/sv/java/send-shape-front-or-back-inside-the-worksheet/)
- [Sortera data i kolumn med anpassad sorteringslista](/cells/sv/java/sort-data-in-column-with-custom-sort-list/)
