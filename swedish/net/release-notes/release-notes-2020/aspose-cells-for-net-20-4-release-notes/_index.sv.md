---
title: Aspose.Cells for .NET 20.4 Release Notes
type: docs
weight: 40
url: /sv/net/aspose-cells-for-net-20-4-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.4](https://www.nuget.org/packages/Aspose.Cells/20.4.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47276|XLSX till CSV, kommatecken krävs för tomma celler som också liknar MS Excel|Ny funktion|
|CELLSNET-47054|Stöd sammanslutning av flera celler som ett intervall|Ny funktion|
|CELLSNET-47091|Möjlighet att uppdatera källfältet för PowerQueryFormulaItems|Ny funktion|
|CELLSNET-47273|Ställ in latinsk texttypsnitt och asiatisk texttypsnitt för diagramkategoriaxeln|Förbättring|
|CELLSNET-47217|Stöd datafält, färgskala och ikonuppsättning villkorlig formatering av ODS.|Förbättring|
|CELLSNET-47201|Öppna den lösenordsskyddade filen med Aspose.Cells.GridDesktop|Förbättring|
|CELLSNET-47254|Stöd ange ny rad som i MS-EXCEL i formelfältet|Förbättring|
|CELLSNET-47224|Förbättra prestandan för uppfriskande vridbara rullar.|Prestanda|
|CELLSNET-47243|Vänta på GetDisplayStyle för ett kalkylblad med rader 65536|Prestanda|
|CELLSNET-47289|CalculateFormula() returnerar aldrig|Prestanda|
|CELLSNET-47263|Hänger sig medan jag försöker öppna ODP-dokument i Workbook-konstruktorn|Prestanda|
|CELLSNET-42556|Sortering av PivotField verkar inte fungera|Insekt|
|CELLSNET-47046|Oöppnade citatavgränsare i IMG HTML-attribut i genererad HTML-uppmärkning|Insekt|
|CELLSNET-47208|Pivottabellen håller inte formatet med den senaste versionen|Insekt|
|CELLSNET-47219|Fel formel i tabellkolumnen efter infogning av en rad och uppdatering av den|Insekt|
|CELLSNET-47261|Excel till HTML-rendering - fel teckenstorlek i en exporterad tabell|Insekt|
|CELLSNET-47279|Den första kolumntexten i alla rader är inte underordnad när filen exporteras till HTML|Insekt|
|CELLSNET-47163|Problem med att infoga kolumn och uppdateringsreferens|Insekt|
|CELLSNET-47244|Formler (MROUND, MIN) har inte beräknats korrekt|Insekt|
|CELLSNET-47250|Ta bort dubbletter fungerar endast för den första kolumnen när parametern columnOffsets specificeras|Insekt|
|CELLSNET-47267|Formler beräknas inte i mallfilen|Insekt|
|CELLSNET-47268|TrimLeadingBlankRowAndColumn inkonsekvens|Insekt|
|CELLSNET-47269|XLSX till CSV-konvertering - kommatecken saknas i utdata|Insekt|
|CELLSNET-47200|Problem med överlappning av navigeringsknappar när du ställer in dolt ark som aktivt ark|Insekt|
|CELLSNET-47274|Bakgrundsbilden är inte inställd i GridWeb|Insekt|
|CELLSNET-47179|VBA-signatur med Bouncy Castle lib|Insekt|
|CELLSNET-47258|Problem med streckkodsbilder i ark till TIFF-rendering|Insekt|
|CELLSNET-47216|PowerQueries borta efter källbyte|Insekt|
|CELLSNET-47241|ODS-filen går sönder när teckensnittsstilen ställs in och sparas|Insekt|
|CELLSNET-47252|Numerisk Smart Marker infogar cellvärde som text|Insekt|
|CELLSNET-47262|Problem med 100% Stacked Bar och huvudenheten och mindre enheten|Insekt|
|CELLSNET-47271|Att spara XLSX med inbäddad visio förstör filen|Insekt|
|CELLSNET-47282|Aspose.Cells 20.3: XLSB till XLS konverteringsproblem|Insekt|
|CELLSNET-47291|Fel punkttecken läst från Excel-fil|Insekt|
|CELLSNET-47096|Problem med GridDesktop formelfält med SplitterPane|Insekt|
|CELLSNET-47247|Undantag höjs när Cell.R1C1Formula anropas|Undantag|
|CELLSNET-47235|NullPointerException när refreshPivotData|Undantag|
|CELLSNET-47246|Undantag "Kan inte komma åt en stängd ström" när du sparar en Excel-fil till PDF|Undantag|
|CELLSNET-47086|Ett undantag görs när ett diagram renderas|Undantag|
|CELLSNET-47242|FormatException vid filladdning|Undantag|
|CELLSNET-47266|Undantag "Argumentindex är utanför arrayområdet" när alla bifogade filer laddas|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen ChartTextFrame.DirectionType.**
Hämtar och ställer in textens riktning i diagrammet.
#### **Lägger till ChartTextFrame.ReadingOrder och föråldrar egenskapen ChartTextFrame.TextDirection.**
Använd egenskapen ChartTextFrame.ReadingOrder istället.
#### **Lägger till klasser för den förbättrade funktionen i Revisions.**
Får information om revisionen.
#### **Ändrar standardvärdet för egenskapen TxtSaveOptions.TrimLeadingBlankRowAndColumn.**
För att göra standardbeteendet för att spara CSV på samma sätt med ms excel, ändrade vi standardvärdet och beteendet för den här egenskapen. För gamla versioner var dess standardvärde "**falsk**". Från 20.4 blir dess standardvärde "**Sann**".
#### **Ändrar beteendet för att upptäcka tomma rader/kolumner för att spara CSV.**
För gamla versioner tog vi de rader/kolumner som inte har några data men har anpassade inställningar (synlighet, formatering, ... etc.) som tomma. Från 20.4 tar vi dem inte längre som tomma, det nya beteendet är detsamma med ms excel.
#### **Lägger till egenskapen TxtSaveOptions.ExportArea.**
Anger intervallet av celldata som ska exporteras. Användare kan använda detta alternativ för att få samma resultat med gamla versioner för det ändrade beteendet för TxtSaveOptions.TrimLeadingBlankRowAndColumn och tomma rader/kolumner.
#### **Lägger till UnionRange-klass.**
Representerar fackligt utbud.
#### **Tar bort föråldrad DrawObject.Image-egenskap.**
Använd egenskapen DrawObject.ImageBytes istället.
#### **Lägger till egenskapen Bullet.FontName**
Hämtar och ställer in teckensnittsnamnet på kulan.
#### **Lägger till metoden WorksheetCollection.CreateUnionRange().**
Skapar ett fackligt sortiment.
#### **Tar bort föråldrad SaveType-enum.**
Den är oanvänd.
#### **Tar bort föråldrade egenskaper för OleObject.ImageFormat och Picture.ImageFormat.**
Använd egenskaperna OleObject.ImageType och Picture.ImageType istället.
