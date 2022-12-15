---
title: Aspose.Cells for .NET 18.8 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-18-8-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 18.8](https://www.nuget.org/packages/Aspose.Cells/18.8.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42992|Tillämpa textjustering på partiell text inuti TextBox|Ny funktion|
|CELLSNET-44155|Läs/skriv anslutningar av XLSB-fil|Ny funktion|
|CELLSNET-46123|Stöd tolka formler för revisionsloggar till binär array|Ny funktion|
|CELLSNET-46220|Ställ in alternativet ContentCopyForAccessibility när du konverterar kalkylblad till PDF-filformat|Ny funktion|
|CELLSNET-43560|Kryptera en ODS-fil|Ny funktion|
|CELLSNET-43556|Öppna krypterad ODS-fil|Ny funktion|
|CELLSNET-46209|Stöd för att läsa och skriva DConn av XLS-fil|Ny funktion|
|CELLSNET-43326|Lägg till överbelastningar till CopyRows och CopyColumns med alternativ för Klistra in special|Ny funktion|
|CELLSNET-41637|Hämta inställningar för delsummor|Ny funktion|
|CELLSNET-46252|Argument för att hoppa över rad/rader som datarubriker i exportintervall till datatabell|Förbättring|
|CELLSNET-46226|Bläckanteckningar blir vanliga bilder efter konvertering|Förbättring|
|CELLSNET-41693|Förbättring av kolumner för automatisk passning ingår|Förbättring|
|CELLSNET-46263|Applikationen hänger sig medan XLS konverteras till PDF|Prestanda|
|CELLSNET-46262|Cell bakgrunden är fel när celltextorienteringen är lutad i utdata-PDF|Insekt|
|CELLSNET-44761|Text i en form har inte renderats korrekt i PDF|Insekt|
|CELLSNET-43916|Formskugga saknas vid konvertering av kalkylark till HTML|Insekt|
|CELLSNET-46251|Applikationen hänger sig medan XLSX konverteras till HTML|Insekt|
|CELLSNET-46241|Problem med multilines i HTML|Insekt|
|CELLSNET-46219|Bredden från HTML-taggen följs inte vid konvertering av HTML till XLSX|Insekt|
|CELLSNET-46280|Undantag uppstod vid import av data till Excel-fil med SmartMarkers|Insekt|
|CELLSNET-46267|Problem med datafiltrering översta raderna|Insekt|
|CELLSNET-46264|R1C1Formula-egenskapen har ändrat sitt beteende|Insekt|
|CELLSNET-46258|Problem med att beräkna omvänd VLOOKUP-matrisformel|Insekt|
|CELLSNET-46197|Datavalideringsproblem - om du infogar fel värde och klickar på en annan cell inte automatiskt återställer valideringscellen till dess tidigare värde|Insekt|
|CELLSNET-46276|Excel till PDF-konvertering - en tom sida läggs till|Insekt|
|CELLSNET-46275|Stor PDF skapad från XLS|Insekt|
|CELLSNET-46259|Konvertering av Excel till PDF lägger till en rak linje|Insekt|
|CELLSNET-46255|Sidnummerproblem (i sidfoten) i Excel till PDF-rendering|Insekt|
|CELLSNET-46238|Det gick inte att ladda krypterad ODS-fil|Insekt|
|CELLSNET-46231|Text i kolumn A-celler återges inte korrekt i utdata-PDF-filen|Insekt|
|CELLSNET-46165|Aspose.Cells slutar svara när man försöker konvertera en Excel-fil till PDF-filformat|Insekt|
|CELLSNET-46236|Skadad MS Excel-fil efter anonymisering|Insekt|
|CELLSNET-45192|Den sparade XLS-filen visas i skyddsvy|Insekt|
|CELLSNET-46235|Bilden kan inte visas när du sparar i XLS-format|Insekt|
|CELLSNET-46225|Hantering av returfrakt med dubbla citattecken|Insekt|
|CELLSNET-46218|Efter att ha kört AutoFitColumns återges kolumnorden fortfarande inte helt|Insekt|
|CELLSNET-46139|Workbook.DataConnections visar inte anslutningsinformationen för XLS-filen|Insekt|
|CELLSNET-46042|Snedstreck konverteras till bakre snedstreck efter att externa länkar ändrats|Insekt|
|CELLSNET-45377|Dataanslutningar hittades inte i XLS-dokument|Insekt|
|CELLSNET-44487|Dataanslutningen försvinner när XLT konverteras till XLSM|Insekt|
|CELLSNET-44486|Dataanslutningen försvinner när XLS konverteras till XLSM|Insekt|
|CELLSNET-43563|Diagram går förlorade när XLSX konverteras till ODS|Insekt|
|CELLSNET-41002|Ekvationen försvinner under formatkonvertering (XLSX -> XLS)|Insekt|
|CELLSNET-46277|Undantag vid beräkning av formler|Undantag|
|CELLSNET-46249|Undantag görs vid läsning av HTML-fil|Undantag|
|CELLSNET-46246|Undantaget görs när digital signatur läggs till på molnplattformsservern för GroupDocs|Undantag|
|CELLSNET-46232|Ogiltigt cellnamnundantag när XLSX-filen laddas|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen PdfSecurityOptions.AccessibilityExtractContent**
Tillstånd att kopiera eller extrahera innehåll (till stöd för tillgänglighet för funktionshindrade användare eller för andra ändamål).
#### **Lägger till DigitalSignature(System.Byte[],System.String,System.String,System.DateTime) konstruktor**
Konstruktör av DigitalSignature.
#### **Lägger till klassen SubtotalSetting**
Representerar inställningen för delsumman.
#### **Lägger till metoden Cells.RetrieveSubtotalSetting(CellArea)**
Hämtar inställningen för delsumma.
#### **Lägger till överbelastningsmetoden Range.ExportDataTable(Aspose.Cells.ExportTableOptions).**
Stöder alternativ för export av intervall.
#### **Lägger till egenskapen WebQueryConnection.IsSameSetting och tar bort egenskapen WebQueryConnection.IsFirstRow**
Använd egenskapen WebQueryConnection.IsSameSetting istället.
#### **Lägger till egenskapen WebQueryConnection.IsXmlSourceData och tar bort egenskapen WebQueryConnection.IsSourceData**
Använd egenskapen WebQueryConnection.IsXmlSourceData istället.
#### **Lägger till egenskapen Shape.IsEquation**
Anger om formen innehåller ekvation.
#### **Lägger till överbelastning Cells.CopyColumns(Int32,Int32,PasteOptions) och Cels.CopyRows(Int32,Int32,PasteOptions) metod**
Stöder inklistringsalternativ när du kopierar rader och kolumner.
#### **Lägger till egenskapen Axis.IsAutoTickLabelSpacing**
Indikerar om avståndet mellan bocketiketter är automatiskt.
