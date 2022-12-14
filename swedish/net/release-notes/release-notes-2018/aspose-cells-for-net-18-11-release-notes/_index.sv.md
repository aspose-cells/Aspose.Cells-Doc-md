---
title: Aspose.Cells för .NET 18.11 Release Notes
type: docs
weight: 20
url: /sv/net/aspose-cells-for-net-18-11-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 18.11](https://www.nuget.org/packages/Aspose.Cells/18.11.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46377|Kontrollera om en cell har cirkulär formel|Ny funktion|
|CELLSNET-46399|Undantag inträffade vid anrop av PivotTable.RefreshData()|Ny funktion|
|CELLSNET-46394|Hämta pivottabellens uppdateringsdatum som liknar Interop.Excel|Ny funktion|
|CELLSNET-46261|Ersättning av texterna i SmartArt fungerar inte|Ny funktion|
|CELLSNET-46435|GetValidationValue returnerar fel värde för stora tal|Förbättring|
|CELLSNET-46117|Textpositionen ändras lite när formen delas upp|Förbättring|
|CELLSNET-46400|Den hänger sig medan PivotTable.RefreshData anropas|Prestanda|
|CELLSNET-46441|Cell.GetDisplayStyle() hänger för en cell|Prestanda|
|CELLSNET-46423|Formateringsproblem vid konvertering av XLSX till PDF|Insekt|
|CELLSNET-46410|Pivottabellformatet blir trassligt efter uppdatering|Insekt|
|CELLSNET-46404|Bearbetar diagram på samma sätt som bilder när du sparar HTML|Insekt|
|CELLSNET-46388|Filen är korrupt efter att ha laddat och sparat ett XLSX-filformat|Insekt|
|CELLSNET-46387|Problem med att sortera pivottabellen|Insekt|
|CELLSNET-46366|Kanter och bakgrundsfärger saknas vid konvertering av HTML till XLSX|Insekt|
|CELLSNET-46365|Refererade CSS-formatmallar ignorerades när HTML öppnades|Insekt|
|CELLSNET-46431|Resultatet av VLookup-formeln skiljer sig från MS Excel-resultatet|Insekt|
|CELLSNET-46430|Arrayformel fungerar inte efter Workbook.Combine i XLSX till XLSB-konvertering|Insekt|
|CELLSNET-46428|Name.RefersTo hämtar inte rätt värde|Insekt|
|CELLSNET-46413|Att skapa XLSX med villkorlig formatering ger en skadad fil|Insekt|
|CELLSNET-46403|Arrayformel fungerar inte efter Workbook.Combine för att spara till XLSB-filformat|Insekt|
|CELLSNET-46396|Arbetsbok som sparats som SVG är skadad eftersom den faktiskt är en TIFF-fil|Insekt|
|CELLSNET-46420|Graf i PDF får spikproblem|Insekt|
|CELLSNET-46411|Det hänger sig medan XLSX konverteras till PDF|Insekt|
|CELLSNET-46408|Datamarkörer saknas i utdatadiagrambilden från MS Excel-filen|Insekt|
|CELLSNET-46393|Axeletiketter feljusterade efter konvertering av MS Excel-diagram till PNG-bildformat|Insekt|
|CELLSNET-46359|Variation i teckensnittsstorleken för etiketter i diagrammet i SVG-utdatafilen|Insekt|
|CELLSNET-46433|Villkorlig formatering tas bort när namngivna intervall tas bort|Insekt|
|CELLSNET-46427|MS Excel rapporterar ett problem efter att ha öppnat/sparat med Aspose.Cells|Insekt|
|CELLSNET-46421|Document CreatedTime-egenskapen ändras efter att ha sparats i flödet|Insekt|
|CELLSNET-46417|Radbryt text fungerar inte tillsammans med en tom rad ovanför texten|Insekt|
|CELLSNET-46416|Kartlägger data som förlorats när XLSX-filen laddas och sparas|Insekt|
|CELLSNET-46409|Problem med rullgardinslistan efter konvertering från XML|Insekt|
|CELLSNET-46407|Initieringen av arbetsboken tar för lång tid när ett XLSM-filformat laddas|Insekt|
|CELLSNET-46397|Graftiteln går förlorad när XLS konverteras till XLSM|Insekt|
|CELLSNET-46401|ArgumentException när du arbetar med genererad HTML-fil|Undantag|
|CELLSNET-46426|Undantag vid anrop av AutoFitColumns()|Undantag|
|CELLSNET-46415|CellsException undantag under spara när ParsingFormulaOnOpen är falskt|Undantag|
|CELLSNET-46422|Undantag vid bearbetning av smarta taggar|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till egenskapen PivotTable.RefreshedByWho**
Hämtar namnet på användaren som uppdaterade pivottabellen förra gången.
#### **Lägger till egenskapen PivotTable.RefreshDate**
Hämtar datumet då pivottabellen uppdaterades förra gången.
#### **Lägger till egenskaper för CalculationData.CellRow/CellColumn**
Ger ett effektivt sätt för användaren att hämta cellens rad- och kolumnindex istället för att hämta objektet Cell.
#### **Lägger till CalculationCell-klass**
Representerar beräkningsdata för en cell som beräknas.
#### **Lägger till metoden AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**
Ger en metod för användare att samla in och bearbeta cirkulära referenser.
#### **Lägger till egenskapen TxtLoadOptions.TreatConsecutiveDelimitersAsOne**
Tillåter användaren att välja om konsekutiva avgränsare ska tas som en när CSV-fil importeras.
#### **Lägger till metoden FormatCondition.SetFormulas(strängformel1, strängformel2, bool ärR1C1, bool ärLokal)**
Ger ett effektivt och bekvämt sätt för användaren att ställa in formler för FormatCondition.
#### **Lägger till metoden Validation.GetListValue(int row, int column).**
Tillåter användaren att få värdet för att skapa listan för validering av specifik cell.
#### **Föråldrad ValidationCollection.Add(Validation validation) metod**
Använd metoden ValidationCollection.Add(CellArea) istället.
#### **Lägger till metoden Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions)**
Kopior validering.
#### **Lägger till egenskaperna CreatedUniversalTime,LastPrintedUniversalTime och LastSavedUniversalTime för BuiltInDocumentPropertyCollection**
Returnerar UTC-tid om de inbyggda egenskaperna.
#### **Lägger till egenskapen OoxmlSaveOptions.UpdateSmartArt**
Indikerar om den smarta konsten uppdateras.
#### **Lägger till SmartArtShape-klass**
Representerar den smarta konstformen.
