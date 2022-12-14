---
title: Aspose.Cells för .NET 17.5 Release Notes
type: docs
weight: 80
url: /sv/net/aspose-cells-for-net-17-5-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 17.5](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.5/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-41365|Stöd PDF/A-1a-kompatibilitet i PdfSaveOptions|Ny funktion|
|CELLSNET-45347|Ta bort befintliga skrivarinställningar i Excel-fil|Ny funktion|
|CELLSNET-45340|Implementera alternativ för anpassad sidstorlek för kalkylbladet|Ny funktion|
|CELLSNET-45327|Stöd export av HTML-cellers data till DataTable|Ny funktion|
|CELLSNET-45316|Stöd driften av GridWeb när ASP.NET Session-läge är SQL Server|Ny funktion|
|CELLSNET-45350|OutOfMemory-fel under bildrendering|Prestanda|
|CELLSNET-45341|Konvertering av XLS till SpreadsheetML med filter förstör utdatafilen|Prestanda|
|CELLSNET-45217|Om du sparar Excel till PDF roteras bilden|Insekt|
|CELLSNET-45306|Fel stilar när du sparar till HTML med css-prefix|Insekt|
|CELLSNET-45304|Textjusteringen av den vertikalt roterade texten är fel i utdata-HTML|Insekt|
|CELLSNET-45299|Text passar inte in i cellen när du sparar som HTML|Insekt|
|CELLSNET-45288|Undantag inträffade vid inläsning av en HTML-fil|Insekt|
|CELLSNET-45274|Pivottabellsdata har inte uppdaterats korrekt|Insekt|
|CELLSNET-45336|Arbetsbokens beräkningsmetod kan inte beräkna XIRR-formel - II|Insekt|
|CELLSNET-45333|Värden i cell M114 och N114 är inte korrekta efter beräkning av arbetsboksformel|Insekt|
|CELLSNET-45318|Arbetsbokens beräkningsmetod kan inte beräkna XIRR-formeln|Insekt|
|CELLSNET-45310|Flera användare möter problem i GridWeb när sessionstillståndet är ur process|Insekt|
|CELLSNET-45324|Teckens position är inte mittjusterad när en Excel-fil renderas till PDF|Insekt|
|CELLSNET-45339|Konverterad från ODS till XML (SpreadsheetML) fil öppnas inte av MS Excel|Insekt|
|CELLSNET-45326|Cell.HtmlString markerar inte den kapslade teckensnittsfärgen korrekt|Insekt|
|CELLSNET-45325|Datavalidering slutar konstigt efter att ha infogat nya rader|Insekt|
|CELLSNET-45322|Cells.ImportDataTable-metoden har ändrats|Insekt|
|CELLSNET-45314|Egenskapen CopyOptions.ExtendToAdjacentRange fungerar inte|Insekt|
|CELLSNET-45312|Den slutliga Excel-filen skiljer sig från den ursprungliga Excel-filen|Insekt|
|CELLSNET-45303|Former (rektanglar, linjer, etc.) binds inte längre när du sparar om från XLSX till XLS filformat|Insekt|
|CELLSNET-45301|Att öppna och spara Excel-filen gör justeringen fel|Insekt|
|CELLSNET-45297|Att öppna och spara XLSM-filen med en nyare version skadar den|Insekt|
|CELLSNET-45296|Att ta bort alla kommentarer från en arbetsbok orsakar fel vid öppning i Excel|Insekt|
|CELLSNET-45308|Översätt "Övrigt" av cirkeldiagram|Insekt|
|CELLSNET-45298|Förklaringsposter döljs inte korrekt i det kombinerade diagrammet|Insekt|
|CELLSNET-45313|Undantag vid tillägg av beräknat fält till pivottabell|Undantag|
|CELLSNET-45307|Form till bild-fel vid rendering av arbetsblad till bild|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till egenskapen ExportTableOptions.ExportAsHtmlString**
Exporterar HTML-strängvärdet för cellerna till datatabellen.
#### **Lägger till PageSetup.Copy (PageSetup source, CopyOptions copyOptions) metod**
Kopierar inställningarna för Utskriftsformat.
#### **Lägger till egenskapen ImportTableOptions.ShiftFirstRowDown**
Indikerar om den första raden flyttas ner vid infogning av tabell.
#### **Lägger till metoden PageSetup.CustomPaperSize()**
Ställer in den anpassade pappersstorleken, i enheten tum.
#### **Lägger till egenskapen PageSetup.PrinterSettings**
Hämtar och ställer in inställningarna för standardskrivaren.
#### **Lägger till enum PaperSizeType.Custom**
Representerar den anpassade pappersstorleken.
#### **Lägger till enum PdfCompliance.PdfA1a**
Representerar PDF-format som är kompatibelt med PDFA-1a.


#### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Konvertera Excel-fil till PDF-format som är kompatibelt med PDFA-1a](/cells/sv/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Kopiera inställningar för sidinställningar från källarbetsbladet till målarbetsbladet](/cells/sv/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Implementera anpassad pappersstorlek på arbetsbladet för rendering](/cells/sv/net/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil](/cells/sv/net/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [Flytta första raden nedåt när du infogar Cells datatabellrader](/cells/sv/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
- [Exportera HTML-strängvärde för Cells till datatabellen](/cells/sv/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Fungerar med GridWeb när ASP.NET Session tillståndsläge är SQL Server](/cells/sv/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)
- [Aktivera olika GridWeb-lägen](/cells/sv/net/enable-different-gridweb-modes/)


