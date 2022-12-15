---
title: Aspose.Cells for .NET 20.7 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-20-7-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.7](https://www.nuget.org/packages/Aspose.Cells/20.7.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47432|Lägg till FilterString()-kriteriestöd|Ny funktion|
|CELLSNET-47410|Felaktig arktyp returnerades för International Macro Sheet|Ny funktion|
|CELLSNET-47463|Stöd loop över alla PivotFields med en vanlig för varje loop|Förbättring|
|CELLSNET-47408|Undersök problem med att ladda två filer synkronisera i aspose.cells.app|Förbättring|
|CELLSNET-47441|Formulärkontrolllänkar borttagna i office 365|Förbättring|
|CELLSNET-47473|Kontrollera om strukturen eller fönstret i arbetsboken är skyddad med ett lösenord.|Förbättring|
|CELLSNET-47433|Arbetsblad.Cells.RemoveDuplicates fungerar inte eller tar för mycket tid.|Prestanda|
|CELLSNET-46753|WorkbookDesigner.Process() hänger sig för stora data|Prestanda|
|CELLSNET-47379|HTML till Excel-konvertering - Kanter saknas när de definieras i CSS|Insekt|
|CELLSNET-47394|Diagramförklaring som innehåller datum har ett annat format i PDF-utdata|Insekt|
|CELLSNET-47400|Villkorsformat skiljer sig från det som är inställt i Excel|Insekt|
|CELLSNET-47402|Pivottabeller har inte uppdaterats|Insekt|
|CELLSNET-47404|Kinesiska tecken är oläsliga när .mht-filen laddas.|Insekt|
|CELLSNET-47411|Det gick inte att skapa en kopia av XLSB|Insekt|
|CELLSNET-47427|Innehållet flyttas vid export till HTML|Insekt|
|CELLSNET-47471|CellAreas of Conditional-format är inte korrekta efter uppdatering och beräkning av pivottabell|Insekt|
|CELLSNET-47426|Felaktigt värde på datavalideringsregeln|Insekt|
|CELLSNET-47456|GetValidation().IgnoreBlank fungerar inte|Insekt|
|CELLSNET-47472|Prestandaproblem med att ställa in delad formelfunktion i nyare versioner|Insekt|
|CELLSNET-47443|Autofilter fungerar inte korrekt i Aspose.Cells.GridDesktop|Insekt|
|CELLSNET-47460|Utskrift av GridWeb på senaste Firefox (versioner: 77 och 78) fungerar inte|Insekt|
|CELLSNET-47461|Att välja flera celler i GridWeb fungerar inte på senaste versionerna av Firefox|Insekt|
|CELLSNET-47417|Cellhöjden är otillräcklig i Excel för PDF-rendering|Insekt|
|CELLSNET-47437|PDF konverterad från XLS ger upphov till ett fel i Acrobat Reader|Insekt|
|CELLSNET-47423|Etiketter för värdeaxel och kategoriaxel i diagram renderas inte i Excel till PDF-konvertering|Insekt|
|CELLSNET-47429|Sunburst-diagram med anpassad fyllningsfärg och inga dataetiketter ger ett fel i ToImage-metoden|Insekt|
|CELLSNET-47438|Scatter diagram färg Excel till PDF konvertering|Insekt|
|CELLSNET-47401|Tabellvärden ändrade efter radering av rader|Insekt|
|CELLSNET-47407|Sammanslagna filer är skadade.|Insekt|
|CELLSNET-47412|Felaktig diagramtyp returnerades för vissa diagram|Insekt|
|CELLSNET-47413|Saknar diagramtitel för vissa diagram|Insekt|
|CELLSNET-47415|CopyRows använder inte destinationsnamngivna intervallvärden i formler|Insekt|
|CELLSNET-47420|Olika resultat av ChartType.Line i XLS och XLSX|Insekt|
|CELLSNET-47425|Prioritet för villkorlig formateringsregel är felaktig för typen DataBar|Insekt|
|CELLSNET-47430|Klistra in formatering av ett intervall resulterade i att ett tomt intervall klistrades in i destinationen|Insekt|
|CELLSNET-47431|Att ändra Cells nummerformatering lägger oväntat till kanter|Insekt|
|CELLSNET-47435|Fel vid uppdatering av parameter i DataMashup > PowerQueryFormula|Insekt|
|CELLSNET-47444|Fel serienamn läst från Waterfall-diagrammet|Insekt|
|CELLSNET-47447|Nummerformat för diagramaxel kan inte hämtas|Insekt|
|CELLSNET-47454|Olika linjehöjder vid samma värde i pixlar|Insekt|
|CELLSNET-47459|Diagrammets storlek ändras efter konvertering tillbaka från .xlsx till .xlsb|Insekt|
|CELLSNET-47462|Fel vid import av JSON till Excel|Insekt|
|CELLSNET-47465|Tabellens stil förlorade när XLS-fil sparades|Insekt|
|CELLSNET-47477|Smarta tillverkare Fältnamn har en prick|Insekt|
|CELLSNET-47439|Nullreferensundantag vid tillämpning av stil|Undantag|
|CELLSNET-47446|Ogiltigt startradindex när kalkylbladet tas bort|Undantag|
|CELLSNET-47466|NullReferenceException vid laddning av XLSX|Undantag|
|CELLSNET-47476|Objektreferens är inte inställd på en instans av ett objektundantag när XLSX laddas|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoden Cells.RemoveDuplicates().**
Överbelastad metod för Cells.RemoveDuplicates(...) för användarens bekvämlighet för att ta bort dubblerade rader i hela arket.
#### **Lägger till egenskapen TickLabels.DisplayNumberFormat.**
Hämtar och ställer in visningsnummerformatet för bocketiketter.
#### **Lägger till metoden Cells.GetViewRowHeight() och Cells.GetViewRowHeightInch().**
Får utsiktsradens höjd.
#### **Lägger till enum SheetType.InternationalMacro.**
Lägger till ny arktyp: internationellt makro.
#### **Lägger till metoden PivotFieldCollection.GetEnumerator().**
Får en uppräkning över elementen i denna samling i rätt ordning.
#### **Lägger till metoden PivotItemCollection.GetEnumerator().**
Får en uppräkning över elementen i denna samling i rätt ordning.
#### **Lägger till egenskapen Workbook.IsWorkbookProtectedWithPassword.**
Indikerar om strukturen och fönstret är skyddade med ett lösenord.
#### **Lägg till klasser PowerQueryFormulaParameters och PowerQueryFormulaParameter**
Representerar parametrarna för powerfrågeformeln.
