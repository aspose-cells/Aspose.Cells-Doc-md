---
title: Aspose.Cells for .NET 21.8 Release Notes
type: docs
weight: 5
url: /sv/net/aspose-cells-for-net-21-8-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.8](https://www.nuget.org/packages/Aspose.Cells/21.8.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-48470|Stöd skalning av kalkylbladssidor vid export av filer till HTML|Ny funktion|
|CELLSNET-41286|Stöd XML-kartor|Ny funktion|
|CELLSNET-45255|Stöd för Apples .nummer? filformat|Ny funktion|
|CELLSNET-47737| Stöd för att läsa senaste Apples .numbers-filformat|Ny funktion|
|CELLSNET-48205|Lägg till Auto-fill (mönster) hantera MS Excel-funktion för siffror, text eller datum, etc.|Ny funktion|
|CELLSNET-48435|Slå samman fler tomma utrymmen i output html.|Förbättring|
|CELLSNET-46412|Licensen fungerar inte i releaseversionen av MVC-applikationen när den distribueras på IIS-servern|Förbättring|
|CELLSNET-47888|Lämpliga SmartMarkers krävs för att uppnå önskad effekt|Förbättring|
|CELLSNET-48452|Stöd läsning av bildformulär nummer 09-filer.|Förbättring|
|CELLSNET-48372|Vänta på spara till html för XLSB-filen|Prestanda|
|CELLSNET-48091|Objekt med rotation är förvrängt.|Insekt|
|CELLSNET-48173|Flytta in texterna i diagramformerna|Insekt|
|CELLSNET-48241|Textpositionen i pentagonformen är fel|Insekt|
|CELLSNET-48247|Böjningspilen försvinner vid konvertering till pdf.|Insekt|
|CELLSNET-48363|Den rika textens position beräknas upprepade gånger, vilket gör att texten flyttas uppåt.|Insekt|
|CELLSNET-47839|Forma till bild Fel när XLSX sparades till PDF|Insekt|
|CELLSNET-48312|Problem med zoomnivån i output html.|Insekt|
|CELLSNET-48329|Bildjusteringsproblem vid export av intervall till HTML|Insekt|
|CELLSNET-48333| Tabellkolumner i intervallet med bottenjustering kombineras i konverterade HTML|Insekt|
|CELLSNET-48365| Slicers skapade från pivottabellens basfält fungerar inte|Insekt|
|CELLSNET-48359|Makron tas bort efter migrering från XLS till XLSM|Insekt|
|CELLSNET-48448|Diagramdatakällan med namngivet intervall har inte analyserats korrekt|Insekt|
|CELLSNET-47369|Kartpunkt saknas och formen kläms in genererad EMF-bild|Insekt|
|CELLSNET-48497|Den genererade xlsx-filen är trasig efter att cellen har länkats till XmlMap|Insekt|
|CELLSNET-48132| Problem när du ändrar dataetikettposition för Donut Chart|Insekt|
|CELLSNET-48385|XLSX till TIFF: Grafstaplar återges inte i utdata|Insekt|
|CELLSNET-48386|Fel teckensnittsnamn för typsnittsnamn på kategoriaxeln|Insekt|
|CELLSNET-48503|Inriktningen av axeltiteln är en förskjutning i utdata-pdf|Insekt|
|CELLSNET-48509|Diagram visas ibland inte baserat på förklaringsposition|Insekt|
|CELLSNET-48374|Bilden som infogas i ett Excel-dokument ändras storlek när standardteckensnittet ändras|Insekt|
|CELLSNET-48384|Ställa in Array till Range.Value : den går utanför eller utanför gränserna för intervallområdet|Insekt|
|CELLSNET-48410|Automatisk centrering när du skickar en lista med strängar med smarta markörer|Insekt|
|CELLSNET-48460|PowerQueries går förlorade efter ersättning|Insekt|
|CELLSNET-48478|XML-filens innehåll laddas inte|Insekt|
|CELLSNET-48492|Problem med 100% Stacked Bar och huvudenheten och mindre enheten|Insekt|
|CELLSNET-48504|Ogiltigt kolumnindex vid konvertering av XLSX|Insekt|
|CELLSNET-48512|Rensa AutoFilter fungerar inte korrekt|Insekt|
|CELLSNET-48477|PivotTable.CalculateData-metoden ger undantag|Undantag|
|CELLSNET-48395|Shape to image raise undantag i docker-miljö för filen Display.xlsx|Undantag|
|CELLSNET-48367|Undantag görs när PlotArea-bredden är 0|Undantag|
|CELLSNET-48172|"Shape to image-fel" vid konvertering av Excel-fil till PDF|Undantag|
|CELLSNET-48490|"Aritmetisk operation resulterade i ett spill." undantag när filen XLS är öppen|Undantag|
|CELLSNET-48545|Undantag uppstod när Shape.UpdateSelectedValue() anropades|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till klassen AbstractInterruptMonitor.**

Tillhandahåller AbstractInterruptMonitor som bas för implementeringar för avbrottsövervakning. Klassen InterruptMonitor blir nu en implementering av den. Typen av InterruptMonitor-egenskaper för LoadOptions och Workbook blir nu också AbstractInterruptMonitor så att användaren kan använda sin egen implementering för att styra de tidskrävande operationerna.

### **Lägger till egenskapen HtmlSaveOptions.WorksheetScalable.**

Indikerar om du zoomar in eller ut html via kalkylbladszoomnivå när du sparar fil till html, standardvärdet är falskt.

### **Lägger till åsidosättande WorksheetCollection.GetRangeByName()-metoden.**

Hämtar Range-objekt efter namn från definierade namn eller tabeller.

### **Lägger till metoden Range.AutoFill().**

Fyller automatiskt data till intervallet.

### **Lägger till WarningType.IO enum.**

Representerar varningen för skadad fil.

