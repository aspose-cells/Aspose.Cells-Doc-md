---
title: Aspose.Cells för Android via Java 18.12 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-android-via-java-18-12-release-notes/
---
{{% alert color="primary" %}}

Den här sidan innehåller utgåvor för Aspose.Cells för Android via Java 18.12.

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42745|Ändra returnerat värde för att få anslutningspunkter|Ny funktion|
|CELLSJAVA-42662|Ge möjlighet att exportera intervall som HTML|Ny funktion|
|CELLSJAVA-42746|Datafält saknas när XLSX konverteras till HTML|Ny funktion|
|CELLSJAVA-42747|Värdet finns fortfarande när XLSX konverteras till HTML|Ny funktion|
|CELLSJAVA-42634|Konvertera vänster höger bandform till bild|Förbättring|
|CELLSJAVA-42713|Aspose.Cells för Java JavaDocs - paketlistfil saknas|Förbättring|
|CELLSJAVA-42528|Teckensnitt är inte en giltig HTML5 och självstängande tagg och webbläsare ger en felaktig bild av dess innehåll|Förbättring|
|CELLSJAVA-42738|Fel räkning av valideringsvärden läses från XLSX|Förbättring|
|CELLSJAVA-42734|Problem samtidigt som på varandra följande avgränsare behandlas som distinkta|Förbättring|
|CELLSJAVA-42731|Datumformatet är felaktigt för japansk språk|Förbättring|
|CELLSJAVA-42748|LightCells API kan inte ladda en stor fil|Förbättring|
|CELLSJAVA-42728|Ett undantag (StackOverFlow) uppstår när du sparar till PDF-utdata|Insekt|
|CELLSJAVA-42729|Fel värde beräknat av ROUNDUP()|Insekt|
|CELLSJAVA-42724|Kopiera ett intervall med PasteType.ALL (Klistra in alternativ) som inte kopierar radhöjder korrekt|Insekt|
|CELLSJAVA-42722|Hyperlänktextformatering förloras när ny text ställs in|Insekt|
|CELLSJAVA-42688|Ogiltigt ryskt datumformat|Insekt|
|CELLSJAVA-42721|Problem med SheetRender-teckensnitt|Insekt|
|CELLSJAVA-42723|Undantag "java.lang.OutOfMemoryError: Java heap space" vid rendering av MS Excel-fil till PDF|Insekt|
|CELLSJAVA-42725|Citat visas i formeln när cellformeln hämtas via Aspose.Cells|Insekt|
|CELLSJAVA-42720|Prestandaförsämring vid användning av villkorlig formatering|Insekt|
|CELLSJAVA-42737|Diagramlinje saknas i XLSX->PNG-konvertering|Insekt|
|CELLSJAVA-42735|Problem med metoden getActualChartSize|Insekt|
|CELLSJAVA-40861|SmartArt kopierar inte när arbetsboken kopieras|Insekt|
|CELLSJAVA-42727|Textformatering saknas i HTML-utdata i Excel-intervallet|Insekt|
|CELLSJAVA-42744|Ikonuppsättningar blir feljusterade när XLSX konverteras till HTML|Insekt|
|CELLSJAVA-42772|Export av namngivna intervalldata renderas inte korrekt till HTML (Java)|Insekt|
|CELLSJAVA-42753|Namngiven Range Issue|Insekt|
|CELLSJAVA-42764|Validering returnerar alltid sant för 'getInCellDropDown()'-metoden|Insekt|
|CELLSJAVA-42768|Fel kultur anpassat format returneras för olika platser (Tyskland, franska, Italien och Spanien)|Insekt|
|CELLSJAVA-42758|Excel till PDF-konvertering - problem med rendering av mätdiagram|Insekt|
|CELLSJAVA-42761|PDF-återgivning kastar OutOfMemoryError-undantaget|Insekt|
|CELLSJAVA-42759|CellsException vid konvertering av filer|Undantag|
|CELLSJAVA-42755|Undantag "NullPointerException" när XLSX-fil(er) instansieras|Undantag|
|CELLSJAVA-42762|NumberFormatException under bearbetning av filer|Undantag|
|CELLSJAVA-42774|NullPointerException när en CSV laddas|Undantag|
|CELLSJAVA-42765|Undantag "com.aspose.cells.CellsException" när en Excel-fil renderas till PDF-filformat|Undantag|
|CELLSJAVA-42754|Undantag "IllegalStateException: Ogiltig kodning: null" vid instansiering av ett XLS-filformat|Undantag|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för Android via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

**Lägger till egenskapen HtmlSaveOptions.WidthScalable**

Anger om skalbar enhet används för att beskriva kolumnbredden vid export av fil till HTML. Standardvärdet är falskt.

**Lägger till egenskapen WorkbookDesigner.UpdateEmptyStringAsNull**

Anger om det tomma strängvärdet bearbetas som null.

**Uppdaterar det returnerade värdet för metoden DocumentProperty.ToDateTime(), egenskaperna BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted och BuiltInDocumentPropertyCollection.LastSavedTime**

Returnerar tiden i lokal tidszon.

**Kräver starkare begränsningar för användarens input för FormatCondition.Formula1/Formula2**

Den vanliga inmatningssträngen kan inte bestämmas om den ska referera till en namnreferens eller om det bara är ett konstant strängvärde. Så nu kräver vi att formeln måste börja med '='-tecken. För vanligt strängvärde "sss", använd format som "=\"sss\"".

**Lägger till egenskapen PivotTable.RefreshedByWho**

Hämtar namnet på användaren som uppdaterade pivottabellen förra gången.

**Lägger till egenskapen PivotTable.RefreshDate**

Hämtar datumet då pivottabellen uppdaterades förra gången.

**Lägger till egenskaper för CalculationData.CellRow/CellColumn**

Ger ett effektivt sätt för användaren att hämta cellens rad- och kolumnindex istället för att hämta objektet Cell.

**Lägger till CalculationCell-klass**

Representerar beräkningsdata för en cell som beräknas.

**Lägger till metoden AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**

Ger en metod för användare att samla in och bearbeta cirkulära referenser.

**Lägger till egenskapen TxtLoadOptions.TreatConsecutiveDelimitersAsOne**

Tillåter användaren att välja om konsekutiva avgränsare ska tas som en när CSV-fil importeras.

**Lägger till metoden FormatCondition.SetFormulas(strängformel1, strängformel2, bool ärR1C1, bool ärLokal)**

Ger ett effektivt och bekvämt sätt för användaren att ställa in formler för FormatCondition.

**Lägger till metoden Validation.GetListValue(int row, int column).**

Tillåter användaren att få värdet för att skapa listan för validering av specifik cell.

**Föråldrad ValidationCollection.Add(Validation validation) metod**

Använd metoden ValidationCollection.Add(CellArea) istället.

**Lägger till metoden Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions)**

Kopior validering.

**Lägger till egenskaperna CreatedUniversalTime,LastPrintedUniversalTime och LastSavedUniversalTime för BuiltInDocumentPropertyCollection**

Returnerar UTC-tid om de inbyggda egenskaperna.

**Lägger till egenskapen OoxmlSaveOptions.UpdateSmartArt**

Indikerar om den smarta konsten uppdateras.

**Lägger till SmartArtShape-klass** 

Representerar den smarta konstformen.

**Lägger till egenskapen HtmlSaveOptions.ExportSingleTab**

Anger om den enskilda fliken exporteras när filen bara har ett kalkylblad. Standardvärdet är falskt.

**Lägger till egenskapen HtmlSaveOptions.ExportPrintAreaOnly**

Anger om utskriftsområdet endast exporteras till html-fil. Standardvärdet är falskt.

**Tar bort föråldrad Workbook.Initialize()-metod**

Använd Workbook constructor istället.

**Tar bort föråldrad Workbook.Styles-egenskap**

Använd Workbook.CreateStyle() för att skapa och manipulera stil för arbetsbok istället för StyleCollection.Add();
Använd Workbook.GetNamedStyle(sträng) för att få namngiven stil istället för StyleCollection

**Tar bort föråldrad Workbook.CheckWriteProtectedPassword()-metod**

Använd metoden WorkbookSettings.WriteProtection.ValidatePassword istället.

**Lägger till LoadDataFilterOptions.VBA enum**

Alternativet att ignorera VBA-projekt när mallfilen laddas.

**Lägger till egenskapen Style.InvariantCustom**

Hämtar den kulturoberoende mönstersträngen för talformat (inklusive mönstersträngen för inbyggt tal).

**Lägger till egenskapen FindOptions.ValueTypeSensitive**

Anger om den sökta cellvärdetypen ska vara samma som den sökta nyckeln.

**Föråldrade egenskapen FindOptions.SearchNext**

Använd egenskapen FindOptions.SearchBackward istället, det sanna värdet för denna nya egenskap motsvarar false för SearchNext.

**Tar bort föråldrade Cells. Metoderna FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains och FindNumber**

Använd metoden Cells.Find(object,Cell,FindOptions) istället. För att få samma resultat med metoderna FindNumber, FindString, ställ in FindOptions.ValueTypeSensitive som sant.

Tar bort föråldrad Cells.Starta egendom

Använd egenskapen Cells.FirstCell istället.

**Tar bort föråldrad Cells.Slut egendom**

Använd egenskapen Cells.LastCell istället.

**Tar bort egenskapen Cells[int]**

Använd metoden Cells.GetEnumerator() för att iterera alla celler i detta kalkylblad istället.

**Tar bort föråldrad Shape.Rotation-egenskap**

Använd egenskapen Shape.RotationAngle istället.

**Tar bort föråldrad Validation.AreaList-egenskap**

Använd egenskapen Validation.Areas istället.

**Tar bort föråldrad stilkonstruktor**

Använd metoden CellsFactory.CreateStyle() eller Workbook.CreateStyle() istället.

**Tar bort föråldrad Shape.IsPrinted-egenskap**

Använd egenskapen Shape.IsPrintable istället.

**Tar bort föråldrad PivotItem.Move(int)-metod**

Använd metoden PivotItem.Move(int , bool ) istället.

**Tar bort föråldrad Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,objekt[]), Cells.ExportDataTable int, int, int, int , Cells.ExportDataTable(DataTable, int, int[],int, bool) och Cells.ExportDataTable(DataTable,int, int, int, bool, bool)metoder**

Använd metoden ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions) istället.

{{% alert color="primary" %}}

Eftersom kodbasen för Aspose.Cells för Android via Java matchar koden för relevanta .NET- och Java-versioner, ingår de flesta ändringar, förbättringar och korrigeringar i Aspose.Cells för .NET v18.10, Aspose.Cells för .NET v18.11 , Aspose.Cells för .NET v18.12, Aspose.Cells för Java v18.10, Aspose.Cells för Java v18.11 och Aspose.Cells för Java v18.12 ingår också i denna Aspose.Cells för Android via Java.

{{% /alert %}}
