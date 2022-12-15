---
title: Aspose.Cells for Java 17.8 Release Notes
type: docs
weight: 50
url: /sv/java/aspose-cells-for-java-17-8-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 17.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.8/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42356|Lägg till en egenskap för att indikera om en tom sida ska matas ut eller inte när det inte finns något att skriva ut|Ny funktion|
|CELLSJAVA-42322|Stöd för avancerad filterfunktion (MS Excel) för att visa poster som uppfyller komplexa kriterier|Ny funktion|
|CELLSJAVA-42341|InterruptMonitor tar längre tid att avbryta arbetsboksparandet för en stor fil med pivottabell|Förbättring|
|CELLSJAVA-42358|Formel visas inte i den resulterande PDF-filen|Förbättring|
|CELLSJAVA-42351|WEEKDAY-formeln returnerar fel värde vid beräkning av arbetsboksformel|Förbättring|
|CELLSJAVA-42332|Aspose.Cells kan inte konvertera HTML-filen korrekt medan MS-Excel kan konvertera den korrekt|Insekt|
|CELLSJAVA-42355|För nummer 39 formaterar MS Excel negativt värde med '-' istället för '()' för Italien|Insekt|
|CELLSJAVA-42350|Etiketttexten förskjuts för cirkeldiagrammet|Insekt|
|CELLSJAVA-42343|Olika stilar i vattenfallsdiagrammet återges inte korrekt.|Insekt|
|CELLSJAVA-42342|Vattenfallsdiagrammet visar alltid anslutningslinjer|Insekt|
|CELLSJAVA-42352|Shape uppdateras inte med korrekt värde|Insekt|
|CELLSJAVA-42349|Excel till PDF-konvertering hängde för en XLSX-fil|Insekt|
|CELLSJAVA-42348|Det går inte att importera XLSB-fil (med Aspose.Cells API:er) till MS-Access-databasen|Insekt|
|CELLSJAVA-42357|Undantag uppstår när en Excel-fil sparas i HTML-format|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskapen HtmlSaveOptions.IsExportComments**
Anger om du exporterar kommentarer när filen sparas till HTML, standardvärdet är falskt.
### **Lägger till egenskapen HtmlSaveOptions.DisableDownlevelRevealedComments**
Indikerar om inaktivera Downlevel-avslöjade villkorliga kommentarer vid export av fil till HTML, standardvärdet är false.
### **Lägger till klassen CustomImplementationFactory**
Ger API för användaren att utöka/förbättra komponentens förmåga med några speciella implementeringar för vissa speciella situationer. För närvarande finns det ingen anpassad implementering som stöds for Java version.
### **Lägger till egenskapen CellsHelper.CustomImplementationFactory**
Hämtar/ställer in CustomImplementationFactory-instansen som används av cells-komponenten.
### **Lägger till metoden Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**
Lägger till digital signatur till en redan signerad OOXML-kalkylbladsfil (Excel2007 och senare).
### **Lägger till egenskapen ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**
Indikerar om en tom sida ska matas ut när det inte finns något att skriva ut.
### **Lägger till metoden GridCell.CreateComment**
Skapar ett kommentarsobjekt för en cell.
### **Lägger till metoden GridCell.RemoveComment**
Tar bort kommentarobjektet från cellen.
### **Lägger till GridCell.GetComment-metoden**
Hämtar kommentarobjekt på den här cellen.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Lägg till digital signatur i en redan signerad Excel-fil](/cells/sv/java/add-digital-signature-to-an-already-signed-excel-file/)
- [Inaktivera Downlevel Revealed Comments medan du sparar till HTML](/cells/sv/java/disable-downlevel-revealed-comments-while-saving-to-html/)
- [Exportera kommentarer medan du sparar Excel-fil till HTML](/cells/sv/java/export-comments-while-saving-excel-file-to-html/)
- [Skriv ut tom sida när det inte finns något att skriva ut](/cells/sv/java/output-blank-page-when-there-is-nothing-to-print/)
- [Skapa Ta bort och få GridCell-kommentarer](/cells/sv/java/create-remove-and-get-gridcell-comments/)
