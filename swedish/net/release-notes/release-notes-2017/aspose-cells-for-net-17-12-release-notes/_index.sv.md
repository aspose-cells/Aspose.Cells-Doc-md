---
title: Aspose.Cells for .NET 17.12 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-17-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for .NET 17.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-45358|Skaffa CSS separat från HTML uppmärkning när du exporterar till HTML med strömmar|Ny funktion|
|CELLSNET-45697|Implementera Cell.FormulaLocal liknande Microsoft Interop FormulaLocal|Ny funktion|
|CELLSNET-45801|Stöd för Office-tillägg i Excel till PDF-rendering|Ny funktion|
|CELLSNET-45796|Smarta markörer - hur man automatiskt fyller i data till andra kalkylblad om data är för stor och inte kan infogas i ett enda ark|Ny funktion|
|CELLSNET-45791|Uppdatera "Behåll ändringshistorik" när du delar arbetsbok|Ny funktion|
|CELLSNET-45746|Text i cellerna överlappar andra celler på Aspose.Cells.GridDesktop|Ny funktion|
|CELLSNET-45774|Bilder förväxlas i en bildform med texturfyllning|Förbättring|
|CELLSNET-45731|Uppdatering av pivottabellen skadar MS Excel-filen|Insekt|
|CELLSNET-45794|Matrisformel som involverar "MEDIAN" beräknas som tom|Insekt|
|CELLSNET-45779|Cell textjustering ändras i den konverterade bilden|Insekt|
|CELLSNET-45772|En sida gick förlorad när kalkylbladet konverterades till bild|Insekt|
|CELLSNET-45764|Status för DataBars är felaktig i utgången PDF|Insekt|
|CELLSNET-45785|Serien "Nominale i Essere (mln)" Dataetiketter är felaktiga|Insekt|
|CELLSNET-45775|Andra vertikala axeletiketten saknas vid konvertering av diagram till bild|Insekt|
|CELLSNET-45762|Chart.Calculate tar mer tid och fungerar inte|Insekt|
|CELLSNET-45799|Absolut sökväg ändras till relativ sökväg när en XLSX-fil sparas på nytt|Insekt|
|CELLSNET-45797|SetArrayFormula – Behandlas inte som matrisformel|Insekt|
|CELLSNET-45792|Sammanslagna celler förlorade vid kopiering, klistra in kolumnen till nästa kolumn|Insekt|
|CELLSNET-45784|Om du infogar en kolumn får MS Excel ett felmeddelande|Insekt|
|CELLSNET-45778|Kommentarsinställningar ändrades när MS Excel-filen öppnades och sparades|Insekt|
|CELLSNET-45773|Fyllningsformatet ändras för alla textformer i arbetsboken istället för den valda|Insekt|
|CELLSNET-45770|Xlsx-filen är skadad efter att ha laddats och sparats|Insekt|
|CELLSNET-45769|Standardvärdet för egenskapen OoxmlSaveOptions.ExportCellName är true istället för false|Insekt|
|CELLSNET-45768|Workbook.Save(Stream stream, SaveFormat saveFormat) misslyckas om strömmen inte stöder Seek|Insekt|
|CELLSNET-45780|Problem med att visa kalkylbladsdata från höger till vänster|Insekt|
|CELLSNET-45745|Fel vid klickning av rullningslisten på Aspose.Cells.GridDesktop|Insekt|
|CELLSNET-45777|Form till bild-fel uppstår vid konvertering av Excel-fil till PDF|Undantag|
|CELLSNET-45804|Undantag för att öppna en Excel-fil (Strict Open XML Spreadsheet).|Undantag|
|CELLSNET-45798|Index var utanför gränserna för arrayen - Undantag vid rendering av Excel-fil|Undantag|
|CELLSNET-45795|Du måste ange data för valideringskriterier - undantag inträffar när arbetsboken sparas|Undantag|
|CELLSNET-45781|ArgumentOutOfRangeException uppstår när kalkylblad kopieras till en annan arbetsbok|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen HtmlSaveOptions.TableCssId**
Hämtar och ställer in prefixet för typen css-namn som tr,col,td och så vidare, de finns i tabellelementet som har det specifika TableCssId-attributet. Standardvärdet är "".
#### **Lägger till Cell.FormulaLocal egendom**
Får den lokalt formaterade formeln som kan variera beroende på olika språkinställningar för separatorer, inbyggda namn, funktionsnamn, ... etc. Dessa platser är beroende.
#### **Lägger till metoden GlobalizationSettings.GetLocalFunctionName(sträng standardnamn).**
Hämtar det språkberoende funktionsnamnet enligt givet standardfunktionsnamn.
#### **Lägger till metoden GlobalizationSettings.GetLocalBuiltInName(string standardName).**
Hämtar den språkberoende texten för inbyggt Namn enligt given standardtext.
#### **Lägger till egenskapen GlobalizationSettings.ListSeparator**
Hämtar separatorn för lista, funktionsparametrar, ... etc.
#### **Lägger till egenskapen GlobalizationSettings.RowSeparatorOfFormulaArray**
Hämtar avgränsaren för rader i matrisdata i formel.
#### **Lägger till egenskapen GlobalizationSettings.ColumnSeparatorOfFormulaArray**
Hämtar avgränsaren för objekten i arrayens raddata i formel.
#### **Lägger till egenskapen HtmlSaveOptions.ExportWorksheetCSSSeparately**
Anger om kalkylbladets css exporteras separat. Standardvärdet är falskt.
#### **Lägger till LoadDataFilterOptions.Structure för att ersätta LoadDataFilterOptions.None**
LoadDataFilterOptions.None gav tvetydiga anvisningar och orsakade förvirring. Den var utformad för att ange att ingenting laddas för kalkylbladsdata. Nu tillhandahåller vi en ny (medlem), dvs. Struktur för att ersätta den.
#### **Lägger till DataLabelShapeType enum**
Anger den förinställda formgeometrin som ska användas för ett diagram.
#### **Lägger till egenskapen DataLabels.ShapeType**
Hämtar eller ställer in formtyp för dataetikett.
#### **Tar bort vissa föråldrade FileFormatType**
Tar bort föråldrade filformattyper.
#### **Lade till egenskapen WorksheetCollection.RevisionLogs, klassen RevisionLogCollection och klassen Revisions.RevisionLog**
Får inställning av revisionslogg.
#### **Lägger till enum MsoDrawingType.WebExtension**
Representerar webbförlängningsformen.


#### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Fyll i smartmarkördata automatiskt till andra kalkylblad om data är för stor](/cells/sv/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Exportera arbetsblad CSS separat i utdata HTML](/cells/sv/net/export-worksheet-css-separately-in-output/)
- [Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal](/cells/sv/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [Prefix tabellelementstilar med egenskapen HtmlSaveOptions.TableCssId](/cells/sv/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Återge Office-tillägg medan du konverterar Excel till Pdf](/cells/sv/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Ställ in formtypen för dataetiketter för diagram](/cells/sv/net/set-the-shape-type-of-data-labels-of-chart/)
- [Text flödar över från GridDesktop-cellen om den är för lång](/cells/sv/net/text-overflows-from-griddesktop-cell-if-it-is-too-long/)
- [Uppdatera dagar som bevarar historik över revisionsloggar i delad arbetsbok](/cells/sv/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
