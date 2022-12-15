---
title: Aspose.Cells for .NET 19.8 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-19-8-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.8](https://www.nuget.org/packages/Aspose.Cells/19.8.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46823|Stöd för elliptisk kurva digital signaturalgoritm (ECDSA) för P-384 och P-521|Ny funktion|
|CELLSNET-46813|Stöd för att extrahera OLE Embedded .MOL-fil|Ny funktion|
|CELLSNET-46822|Upptäcker skillnaden mellan interna och externa hyperlänkar|Ny funktion|
|CELLSNET-42334|Aspose.Cells.GridWeb-kompatibilitet med MVC|Förbättring|
|CELLSNET-46804|Förbättra prestanda för beräkning av stor matris med dubbla värden|Prestanda|
|CELLSNET-46856|Dokumentet kan inte sparas när det sparas mer än 10 gånger|Prestanda|
|CELLSNET-46827|Innehåll saknas i XLSX till ODS-konvertering|Insekt|
|CELLSNET-46833|Former förvrängs i Excel till PDF-konvertering|Insekt|
|CELLSNET-46835|Ritningsformer renderas inte korrekt i Excel till PDF-rendering|Insekt|
|CELLSNET-46848|Problem med arabisk text i Excel till PDF-rendering|Insekt|
|CELLSNET-44973|Det går inte att ställa in fyllningsfärgen för pivottabellcellerna|Insekt|
|CELLSNET-46818|Alla stilar exporteras inte när du sparar till HTML|Insekt|
|CELLSNET-46824|Pivottabellen skadad efter att pivotkällans data uppdaterades|Insekt|
|CELLSNET-46820|Problem med datagruppering av smart markör|Insekt|
|CELLSNET-46840|Problem med metoden Workbook.RemoveUnusedStyles|Insekt|
|CELLSNET-46853|Vissa kolumner renderas i röd färg i Excel till PDF-rendering|Insekt|
|CELLSNET-46829|DBConnection-objektet tillhandahåller inget värde för DBConnection.ConnectionInfo|Insekt|
|CELLSNET-46830|Läs och skriv till Queries|Insekt|
|CELLSNET-46841|Öppnar specifik XLS-fil med Aspose-fel|Insekt|
|CELLSNET-46845|Problem i beteendet för ImportTableOptions.InsertRows|Insekt|
|CELLSNET-46846|Excel-filen skadad efter att ha sparats på nytt|Insekt|
|CELLSNET-46849|Problem med externa dataanslutningar|Insekt|
|CELLSNET-46850|Datagruppering bevaras inte när du använder Cells.DeleteRange()|Insekt|
|CELLSNET-46855|InsertRows delar felaktigt upp grupperade rader|Insekt|
|CELLSNET-46858|XLSX till ODS-konvertering ändrar texttypsnitt i läroboken|Insekt|
|CELLSNET-46859|Förhandsgranskning visar inte textrutan i ODS-fil konverterad från XLSX|Insekt|
|CELLSNET-46723|Ett undantag görs när du hämtar bild från SheetRender för krypterad ODS-fil|Undantag|
|CELLSNET-46842|Att beräkna diagram på ett excel med ett nummer > int.MaxValue genererar ett fel|Undantag|
|CELLSNET-46828|"IndexOutOfRangeException" när du använder smart markör med en pivottabell och sparar arbetsboken|Undantag|
|CELLSNET-46814|Undantag "Index var utanför gränserna för arrayen" vid konvertering av XLSX till PDF|Undantag|
|CELLSNET-46831|Undantag vid rendering av en Excel-fil till PDF|Undantag|
|CELLSNET-46844|Workbook.CalculateFormula() orsakar NullReferenceException|Undantag|
|CELLSNET-46832|Undantag "Invalid MsoLineDashStyle string val" när ett XLSX-filformat laddas|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till klass SheetPrintingPreview**
Förhandsvisning av arbetsbladsutskrift.
#### **Lägger till klass WorkbookPrintingPreview**
Förhandsvisning av arbetsbokutskrift.
#### **Lägger till egenskapen QueryTable.ExternalConnection.**
Får anslutningen av frågetabellen.
#### **Lägger till Hyperlink.LinkType-egenskapen och enum TargetModeType.**
Representerar länktypen för hyperlänken.
