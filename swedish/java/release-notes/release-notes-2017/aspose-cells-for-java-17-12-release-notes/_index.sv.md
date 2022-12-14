---
title: Aspose.Cells för Java 17.12 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-17-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Java 17.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42479|Förbättrad LoadDataFilterOptions-uppräkning och oklarhet har tagits bort|Förbättring|
|CELLSJAVA-42460|CSV-format - D2 och D6 är IsString men Aspose.Cells behandlar dem som IsNumeric|Förbättring|
|CELLSJAVA-42457|När XLSX konverteras till PDF är vissa linjer i diagram annorlunda|Insekt|
|CELLSJAVA-42465|Vissa CSS-klassdeklarationer har inte prefix i HTML-utdata|Insekt|
|CELLSJAVA-42456|HTML-utdata inkonsekvent med källan - Excel till HTML-konvertering|Insekt|
|CELLSJAVA-42478|Import av långa värden från HSQL DB ger ett undantag|Insekt|
|CELLSJAVA-42466|Ekvationen återges inte bra i den utgående PDF-filen|Insekt|
|CELLSJAVA-42475|Diagram saknas i utdata-PDF-filen|Insekt|
|CELLSJAVA-42459|Dataetiketter för diagrammet saknas i utdata PDF/bild|Insekt|
|CELLSJAVA-42453|Diagrambilden är inte lik Microsoft Excel|Insekt|
|CELLSJAVA-42447|Dataetiketter visas felaktigt i HTML-utdatafilformatet|Insekt|
|CELLSJAVA-42481|Ange kombinationsrutanamn fungerar inte för Excel-källfilen men om den sparas på nytt av Microsoft Excel fungerar det ok|Insekt|
|CELLSJAVA-42476|Microsoft Excel Macro-Enabled Worksheet (.xlsm) blir skadad efter att ha öppnats och sparats via Aspose.Cells API:er|Insekt|
|CELLSJAVA-42470|Om du ställer in en kryssruta länkad cell får MS Excel att få ett felmeddelande när utdatafilen öppnas i den|Insekt|
|CELLSJAVA-42462|Att läsa XLSB-filen kastar NullPointerException|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen HtmlSaveOptions.TableCssId**
Hämtar och ställer in prefixet för typen css-namn som tr,col,td och så vidare, de finns i tabellelementet som har det specifika TableCssId-attributet. Standardvärdet är "".
### **Lägger till Cell.FormulaLocal egendom**
Får den lokalt formaterade formeln som kan variera beroende på olika språkinställningar för separatorer, inbyggda namn, funktionsnamn, ... etc. Dessa platser är beroende.
### **Lägger till metoden GlobalizationSettings.GetLocalFunctionName(sträng standardnamn).**
Hämtar det språkberoende funktionsnamnet enligt givet standardfunktionsnamn.
### **Lägger till metoden GlobalizationSettings.GetLocalBuiltInName(string standardName).**
Hämtar den språkberoende texten för inbyggt Namn enligt given standardtext.
### **Lägger till egenskapen GlobalizationSettings.ListSeparator**
Hämtar separatorn för lista, funktionsparametrar, ... etc.
### **Lägger till egenskapen GlobalizationSettings.RowSeparatorOfFormulaArray**
Hämtar avgränsaren för rader i matrisdata i formel.
### **Lägger till egenskapen GlobalizationSettings.ColumnSeparatorOfFormulaArray**
Hämtar avgränsaren för objekten i arrayens raddata i formel.
### **Lägger till egenskapen HtmlSaveOptions.ExportWorksheetCSSSeparately**
Anger om kalkylbladets css exporteras separat. Standardvärdet är falskt.
### **Lägger till LoadDataFilterOptions.Structure för att ersätta LoadDataFilterOptions.None**
LoadDataFilterOptions.None gav tvetydiga anvisningar och orsakade förvirring. Den var utformad för att ange att ingenting laddas för kalkylbladsdata. Nu tillhandahåller vi en ny (medlem), dvs. Struktur för att ersätta den.
### **Lägger till DataLabelShapeType enum**
Anger den förinställda formgeometrin som ska användas för ett diagram.
### **Lägger till egenskapen DataLabels.ShapeType**
Hämtar eller ställer in formtyp för dataetikett.
### **Tar bort vissa föråldrade FileFormatType**
Tar bort föråldrade filformattyper.
### **Lade till egenskapen WorksheetCollection.RevisionLogs, klassen RevisionLogCollection och klassen Revisions.RevisionLog**
Får inställning av revisionslogg.
### **Lägger till enum MsoDrawingType.WebExtension**
Representerar webbförlängningsformen.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Fyll i smartmarkördata automatiskt till andra kalkylblad om data är för stor](/cells/sv/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Exportera arbetsblad CSS separat i utdata HTML](/cells/sv/java/export-worksheet-css-separately-in-output-html/)
- [Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal](/cells/sv/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [Prefix tabellelementstilar med egenskapen HtmlSaveOptions.TableCssId](/cells/sv/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Återge Office-tillägg medan du konverterar Excel till Pdf](/cells/sv/java/render-office-add-ins-while-converting-excel-to-pdf/)
- [Ställ in formtyp för dataetiketter för diagram](/cells/sv/java/set-the-shape-type-of-data-labels-of-chart/)
- [Uppdatera dagar som bevarar historik över revisionsloggar i delad arbetsbok](/cells/sv/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
