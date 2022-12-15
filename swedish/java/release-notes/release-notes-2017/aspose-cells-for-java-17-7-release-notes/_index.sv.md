---
title: Aspose.Cells for Java 17.7 Release Notes
type: docs
weight: 60
url: /sv/java/aspose-cells-for-java-17-7-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 17.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.7/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42322|Stöd för avancerad filterfunktion (MS Excel) för att visa poster som uppfyller komplexa kriterier|Ny funktion|
|CELLSJAVA-42336|ResultSet importerar noll istället för null-värde i XLSX-fil|Förbättring|
|CELLSJAVA-42329|Förbättringar som behövs för datafilter och personsökningsfunktioner - Aspose.Cells.GridWeb (Java)|Förbättring|
|CELLSJAVA-41616|SaveCustomStyleFile finns inte i GridWeb (Java)|Förbättring|
|CELLSJAVA-42321|CellsHelper.setSignificantDigits() ska inte vara (global) statisk funktion|Förbättring|
|CELLSJAVA-42327|Vissa former förvrängs och ändras i Excel till PDF-rendering|Insekt|
|CELLSJAVA-42290|Mdash och ndash infogade i textrutor i diagram renderas inte korrekt i diagrammets PDF|Insekt|
|CELLSJAVA-42338|Fel resultat när du använder SUMIFS-formler|Insekt|
|CELLSJAVA-42337|Aspose.Cells kan inte beräkna värdet på cell B4 i kalkylbladet|Insekt|
|CELLSJAVA-42330|Konstigt resultat när du konverterar från Excel till PDF eller PDF/A med trådar|Insekt|
|CELLSJAVA-42331|Ändringar i kommentarsförfattarfältet bevaras inte|Insekt|
|CELLSJAVA-42328|Fel IconSet returnerade|Insekt|
|CELLSJAVA-42324|Kartans bakgrund saknas efter att ha ställt in en bilds data|Insekt|
|CELLSJAVA-42340|Undantag i tråden "Thread-2" java.lang.OutOfMemoryError: GC-overheadgränsen har överskridits|Undantag|
|CELLSJAVA-42334|Undantaget "Error for ZipFile" visas när du använder OutputFileStream|Undantag|
|CELLSJAVA-42326|com.aspose.cells.CellsException: Ogiltigt lösenord när Excel-filen öppnas|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till metoderna GlobalizationSettings.GetBooleanValueString()/GetErrorValueString()**
Hämtar anpassat visningssträngvärde för cellens booleska värde och felvärde vid formatering/rendering.
### **Tar bort föråldrad ValidationCollection.Add() metod**
Använd metoden ValidationCollection.Add(CellArea) istället.
### **Lägger till egenskapen PdfSaveOptions.CheckWorkbookDefaultFont**
Indikerar om man ska försöka använda arbetsbokens standardteckensnitt först för att visa tecknen vilket teckensnitt som inte är korrekt inställt.
### **Lägger till egenskapen ImageOrPrintOptions.CheckWorkbookDefaultFont**
Indikerar om man ska försöka använda arbetsbokens standardteckensnitt först för att visa tecknen vilket teckensnitt som inte är korrekt inställt.
### **Lägger till FileFormatType.Numbers, LoadFormat.Numbers och SaveFormat.Numbers enum**
Representerar Numbers-kalkylarksfilformatet av Apple Inc/.
### **Lägger till metoden Worksheet.AdvancedFilter().**
Filtrerar data med hjälp av komplexa kriterier.
### **Lägger till egenskapen WorkbookSettings.SignificantDigits**
Hämtar och ställer in antalet signifikanta siffror.
### **Föråldrar egenskapen Validation.AreaList och lägger till egenskapen Validation.Areas**
Hämtar allt område som innehåller datavalideringsinställningarna.
### **Lägger till egenskapen PageSetup.IsAutomaticPaperSize**
Indikerar om pappersstorleken är automatisk.
### **Lägger till metoden FontSettingCollection.Replace().**
Ersätter formens text.
### **Lägger till Cells.importResultSet(ResultSet rs, int rowIndex, int columnIndex, ImportTableOptions options)/Cells.importResultSet(ResultSet rs, String startCell, ImportTableOptions options)**
Stöder import av ResultSet med fler alternativ.
### **Lägger till egenskapen GridWorksheet.CustomColumnCaption**
Hämtar eller ställer in den anpassade kolumntexten för kalkylbladet - Aspose.Cells.GridDesktop.
### **Lägger till egenskapen GridWorksheet.CustomRowCaption**
Hämtar eller ställer in den anpassade radtexten för kalkylbladet - Aspose.Cells.GridDesktop.
### **Lägger till metoden GridDesktop.GetVersion().**
Hämta releaseversionen.
### **Lägger till funktionen GridWebInstance.resize() i GridWeb-klienten js, (GridWebInstance är kontrollobjektet GridWeb)**
Gör att GridWeb-kontrollen är kompatibel med aktuell webbläsarfönsterstorlek.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Läs Numbers-kalkylblad Utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions att ha prioritet](/cells/sv/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Importera data från Microsoft Access Database ResultSet Object till arbetsbladet](/cells/sv/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Använd avancerat filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier](/cells/sv/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Implementera fel och booleskt värde på ryska eller något annat språk](/cells/sv/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/)
- [Bestäm om arbetsbladets pappersstorlek är Automatisk](/cells/sv/java/determine-if-paper-size-of-worksheet-is-automatic/)


