---
title: Aspose.Cells för Java 17.5 Release Notes
type: docs
weight: 80
url: /sv/java/aspose-cells-for-java-17-5-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 17.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.5/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41130|Ändra språket för de fördefinierade orden för pivottabellen|Förbättring|
|CELLSJAVA-42272|Alternativ för att bädda in hyperlänken i en Excel-cell|Förbättring|
|CELLSJAVA-42283|NullPointerException uppstår när filtret finns utanför det namngivna intervallet|Insekt|
|CELLSJAVA-42282|Genom att kopiera ett kalkylblad visas filtrerade rader i HTML-utdatafilen|Insekt|
|CELLSJAVA-42276|Innehållet visas annorlunda (viss text saknas) i icke IE-webbläsare (t.ex. Google chrome) - Excel till HTML-rendering|Insekt|
|CELLSJAVA-42247|Villkorlig formatering går förlorad när pivottabellen uppdateras i kalkylarket|Insekt|
|CELLSJAVA-42257|Villkorlig formateringsstil är bruten|Insekt|
|CELLSJAVA-42202|Excel-formeln fungerar inte korrekt - den visas som 6 istället för 0|Insekt|
|CELLSJAVA-42286|Att spara XLS-fil med grafer använder 100 % CPU|Insekt|
|CELLSJAVA-42251|Titeln är skymd av trendetiketterna i den utgående PDF-filen|Insekt|
|CELLSJAVA-42284|Workbook.getFonts() visar ytterligare teckensnitt efter att samma kalkylblad har laddats om|Insekt|
|CELLSJAVA-42281|Sammanfoga/kopiera till Excel-ark - Mellanslag i början av cellerna behålls inte|Insekt|
|CELLSJAVA-42280|Ogiltig sträng i filen - fel uppstår när en Excel-fil öppnas|Insekt|
|CELLSJAVA-42275|Namnen på vissa parametrar för offentliga metoder har ändrats i den nyare versionen|Insekt|
|CELLSJAVA-42271|Worksheet.autoFitColumns() fungerar inte bra med celler som har radbrytningar|Insekt|
|CELLSJAVA-42266|Sortering av Excel-filen som innehåller kommentarer skadar den utgående Excel-filen|Insekt|
|CELLSJAVA-42265|Sortering av kommentarer orsakar felet "Excel hittade oläsbart innehåll...." när utdatafilen öppnas i MS Excel|Insekt|
|CELLSJAVA-42264|Nedsänkta och upphöjda problem i OpenOffice ODS-fil vid konvertering till HTML eller PDF|Insekt|
|CELLSJAVA-42268|Undantag: "java.lang.NullPointerException" vid rendering av ett diagram till bild|Undantag|
|CELLSJAVA-42278|Undantag: "java.lang.IndexOutOfBoundsException: Index: 12, Storlek: 12" när du sparar till HTML-filformat|Undantag|
|CELLSJAVA-42274|Undantag: "java.lang.StringIndexOutOfBoundsException: Strängindex utanför intervallet: 0" när en XLSX-fil laddas|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen ExportTableOptions.ExportAsHtmlString**
Exporterar HTML-strängvärdet för cellerna till datatabellen.
### **Lägger till PageSetup.Copy (PageSetup source, CopyOptions copyOptions) metod**
Kopierar inställningarna för Utskriftsformat.
### **Lägger till egenskapen ImportTableOptions.ShiftFirstRowDown**
Indikerar om den första raden flyttas ner vid infogning av tabell.
### **Lägger till metoden PageSetup.CustomPaperSize()**
Ställer in den anpassade pappersstorleken, i enheten tum.
### **Lägger till egenskapen PageSetup.PrinterSettings**
Hämtar och ställer in inställningarna för standardskrivaren.
### **Lägger till konstanter PaperSizeType.CUSTOM**
Representerar den anpassade pappersstorleken.
### **Lägger till konstanter PdfCompliance.PDF_A_1_A**
Representerar PDF-format som är kompatibelt med PDFA-1a.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Konvertera Excel-fil till PDF-format som är kompatibelt med PDFA-1a](/cells/sv/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Kopiera inställningar för sidinställningar från källarbetsbladet till målarbetsbladet](/cells/sv/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Implementera anpassad pappersstorlek på arbetsbladet för rendering](/cells/sv/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil](/cells/sv/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [Flytta första raden nedåt när du infogar Cells datatabellrader](/cells/sv/java/shift-first-row-down-when-inserting-cells-data-table-rows/)
