---
title: Aspose.Cells for .NET 17.10 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-17-10-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 17.10](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.10/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-45695|Ställ in talformat för celler i diagrammets datatabell|Ny funktion|
|CELLSNET-45666|Få SheetId-fältet i Excel-kalkylbladet|Ny funktion|
|CELLSNET-45664|Läsa och skriva Extern anslutning av XLSB fil|Ny funktion|
|CELLSNET-45660|Återgivning av ark till bild - Justeringsproblem för asiatiska teckensnitt|Förbättring|
|CELLSNET-45408|Värdet försvinner eller ändrar färg när det konverteras till PDF|Insekt|
|CELLSNET-45696|Slicern rör sig inte ner i arket när du lägger in rader|Insekt|
|CELLSNET-45675|Fel vid beräkning av formlerna (som inbegriper "SUMPRODUKT" och "TRANSPOSERA")|Insekt|
|CELLSNET-45651|Textboxens storlek ändras när kinesiskt teckensnitt används i arbetsboken vid rendering till PDF|Insekt|
|CELLSNET-45678|Delvis saknade tecken vid konvertering till bild|Insekt|
|CELLSNET-45667|Trendlinjeetiketter uppdateras inte i MS Excel när vi manuellt ändrar källvärdet i cellerna|Insekt|
|CELLSNET-45620|Färg och intervall mellan skalan är olika för 3D-diagram|Insekt|
|CELLSNET-45397|Aspose.Cells känner igen teckensnitt i diagrammet felaktigt|Insekt|
|CELLSNET-45700|MS Excel 2016-tilläggsrutan togs bort från filen efter öppnande/spara av Aspose.Cells|Insekt|
|CELLSNET-45693|Kalkylblad är inte längre skyddat i utdatafilen i SpreadsheetML till XLSX konvertering|Insekt|
|CELLSNET-45691|Dokumentet är skadat när det sparas på nytt|Insekt|
|CELLSNET-45690|Stilar verkar ha överförts felaktigt för vissa celler - SpreadsheetML till XLSX konvertering|Insekt|
|CELLSNET-45688|Datumkolumnen är inte korrekt sorterad|Insekt|
|CELLSNET-45687|Arbetsbladsskyddsegenskaper transporteras inte från SpreadsheetML|Insekt|
|CELLSNET-45683|SpreadsheetML AllowSort-elementet fungerar inte i utgången XLSX|Insekt|
|CELLSNET-45682|MS Excel visar ett felmeddelande "Excel hittade oläsbart innehåll...."|Insekt|
|CELLSNET-45676|Dokumentet är skadat när det sparas på nytt på grund av att utrymme i kalkylbladsnamnet inte bryts|Insekt|
|CELLSNET-45673|Justeringsstil som gäller för SpredsheetML|Insekt|
|CELLSNET-45670|Cells färg går förlorad vid konvertering till bild|Insekt|
|CELLSNET-45692|GridWeb delar inte upp rader när du klickar på "+"-knappen|Insekt|
|CELLSNET-45654|Kommentar som lagts till i cellen hämtas inte på klientsidan - Aspose.Cells.GridWeb|Insekt|
|CELLSNET-45645|Undantag uppstår vid öppning av BUDGET RH 3_0.xlsm i GridWeb|Insekt|
|CELLSNET-45657|Inmatningssträngen var inte i ett korrekt format - Undantag på metoden Pivot.CalculateData().|Undantag|
|CELLSNET-45703|Undantag vid konvertering av XLSM fil tillbaka till XLS filformat|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till AbstractCalculationMonitor.Interrupt(string)-metoden**
Tillåter användare att avbryta fortskridandet av formelberäkningar.
#### **Lägger till HtmlCrossType.MSExport enum**
Visar strängen som MS Excel som exporterar HTML.
#### **Lägger till egenskapen Worksheet.TabId**
Hämtar den interna identifieraren för arket.
#### **Lägger till enum OLEDBCommandType.None**
Kommandotypen är inte specificerad.
#### **Lägger till enum ConnectionDataSourceType**
Representerar datakällans typ av anslutning.
#### **Föråldrade egenskapen ExternalConnection.Credentials och ExternalConnection.ReConnectionMethod**
Använd egenskapen ExternalConnection.CredentialsMethodType och ExternalConnection.ReconnectionMethodType istället.
#### **Föråldrade egenskapen WebQueryConnection.EditPage**
Använd egenskapen WebQueryConnection.EditWebPage istället.
#### **Lägger till egenskapen Seris.ValuesFormatCode**
Representerar nummerformatets kod för serievärden.
#### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Ställ in värdeformatets kod för diagramserien](/cells/sv/net/set-the-values-format-code-of-chart-series/)
- [Använd egenskapen Sheet.SheetId för OpenXml med Aspose.Cells](/cells/sv/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Läs och skriv extern anslutning av XLSB-fil](/cells/sv/net/read-and-write-external-connection-of-xls-and-xlsb-files/)
- [Avbryt eller avbryt formelberäkningen av arbetsboken](/cells/sv/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Ange hur strängen ska korsas i utdata HTML med HtmlCrossType](/cells/sv/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
