---
title: Aspose.Cells för .NET 18.12 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-18-12-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 18.12](https://www.nuget.org/packages/Aspose.Cells/18.12.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46479|Flikens namn är inte tillgängligt när en arbetsbok för ett ark konverteras till HTML|Ny funktion|
|CELLSNET-46503|Styr laddning av VBA-data med LoadDataFilterOptions|Ny funktion|
|CELLSNET-42414|Spårade ändringar förlorade under konvertering från XLSB till XLSM och XLS till XLSM|Förbättring|
|CELLSNET-46090|Texten flyttades lite efter att ha delat upp formen när du sparade en XLS till XLSX|Förbättring|
|CELLSNET-46439|Optimering för minnesprestanda: släpp originalströmmen efter att arbetsboken har laddats|Prestanda|
|CELLSNET-46371|Rutnätslinjer visas inte i vissa ark vid konvertering av XLSX->HTML->XLSX|Insekt|
|CELLSNET-46447|Formatteringar förlorade i HTML till XLS-rendering|Insekt|
|CELLSNET-46494|MHT till XLSX-konvertering - problem med cellinnehåll|Insekt|
|CELLSNET-46468|MS Excel ger ett felmeddelande när utdatafilen öppnas|Insekt|
|CELLSNET-46487|Icke-engelsk språkformel fungerar inte|Insekt|
|CELLSNET-46489|Att radera en rad med ett index och läsa raden med samma index returnerar Cell.ValuType: IsNull|Insekt|
|CELLSNET-46406|Det gick inte att öppna lösenordsskyddat ODS-dokument|Insekt|
|CELLSNET-46466|Nedre text under streckkoden saknas i MS Excel till PDF-rendering|Insekt|
|CELLSNET-46470|Bilden saknas efter återgivning till TIFF-utdata|Insekt|
|CELLSNET-46499|Bilder renderas inte korrekt när de konverteras från Excel till PDF|Insekt|
|CELLSNET-46443|Extra text dök upp i bilden från MS Excel-diagrammet|Insekt|
|CELLSNET-46450|Den renderade bilden från MS Excel-diagrammet har fler axelenheter än originaldiagrammet|Insekt|
|CELLSNET-46451|Problem vid rendering av mallfilen (som innehåller diagrammet) till PDF-filformat|Insekt|
|CELLSNET-46454|Förklaringsordning renderad annorlunda än Excel-diagram i session 0 jämfört med session 1|Insekt|
|CELLSNET-46471|Det går inte att ställa in färgmarkör LineWithDataMarkers i XLS-filformat|Insekt|
|CELLSNET-42729|Text förskjuts när SmartArt-diagram renderas som HTML-filformat|Insekt|
|CELLSNET-46462|Text upprepas medan taggen ersätts med text|Insekt|
|CELLSNET-46483|Fel efter konvertering av dokument med Custom UI xml från XLSB till XLSM|Insekt|
|CELLSNET-46495|Problem upptäckta vid konvertering av diagram till bild|Insekt|
|CELLSNET-46486|Undantag uppstod vid konvertering av XLS till PDF|Undantag|
|CELLSNET-46472|PivotTable.GetChildren() tar upp undantaget "Invalid Cell Name"|Undantag|
|CELLSNET-46452|Undantag "NullReferenceException" när du laddar ett XLSB-filformat|Undantag|
|CELLSNET-46456|ArgumentUndantag vid inläsning av arbetsbok|Undantag|
|CELLSNET-46460|Undantag vid åtkomst till TextBox.HtmlText från XLS|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till egenskapen HtmlSaveOptions.ExportSingleTab**
Anger om den enskilda fliken exporteras när filen bara har ett kalkylblad i sig. Standardvärdet är falskt.
#### **Lägger till egenskapen HtmlSaveOptions.ExportPrintAreaOnly**
Anger om utskriftsområdet endast exporteras till html-fil. Standardvärdet är falskt.
#### **Tar bort föråldrad Workbook.Initialize()-metod**
Använd Workbook constructor istället.
#### **Tar bort föråldrad Workbook.Styles-egenskap**
Använd Workbook.CreateStyle() för att skapa och manipulera stil för arbetsbok istället för StyleCollection.Add(); Använd Workbook.GetNamedStyle(sträng) för att få namngiven stil istället för StyleCollection.
#### **Tar bort föråldrad Workbook.CheckWriteProtectedPassword()-metod**
Använd metoden WorkbookSettings.WriteProtection.ValidatePassword istället.
#### **Lägger till LoadDataFilterOptions.VBA enum**
Alternativet som används för att ignorera VBA-projekt när mallfilen laddas.
#### **Lägger till egenskapen Style.InvariantCustom**
Hämtar den kulturoberoende mönstersträngen för talformat (inklusive mönstersträngen för inbyggt tal).
#### **Lägger till egenskapen FindOptions.ValueTypeSensitive**
Anger om den sökta cellvärdetypen ska vara samma som den sökta nyckeln.
#### **Föråldrade egenskapen FindOptions.SearchNext**
Använd egenskapen FindOptions.SearchBackward istället, det sanna värdet för denna nya egenskap motsvarar false för SearchNext.
#### **Tar bort föråldrade Cells. Metoderna FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains och FindNumber**
Använd metoden Cells.Find (object,Cell,FindOptions) istället. För att få samma resultat med metoderna FindNumber, FindString, ställ in FindOptions.ValueTypeSensitive som sant.
#### **Tar bort föråldrad metod Cells.ImportGridView(System.Web.UI.WebControls.GridView,int ,int , bool ,bool ,bool )**
Använd metoden Cells.ImportGridView (System.Web.UI.WebControls.GridView gridView,int firstRow,int firstColumn,ImportTableOptions). istället.
#### **Tar bort föråldrad Cells.Starta egendom**
Använd egenskapen Cells.FirstCell istället.
#### **Tar bort föråldrad Cells.Slut egendom**
Använd egenskapen Cells.LastCell istället.
#### **Tar bort egenskapen Cells[int]**
Använd metoden Cells.GetEnumerator() för att iterera alla celler i detta kalkylblad istället.
#### **Tar bort föråldrade metoder Cells.ImportDataColumn()**
Använd metoden Cells.ImportData (DataTable,int,int,ImportTableOptions) istället.
#### **Tar bort föråldrade Cells.ImportDataReader()-metoder**
Använd metoden Cells.ImportData (IDataReader, int, int,ImportTableOptions) istället.
#### **Tar bort föråldrad Shape.Rotation-egenskap**
Använd egenskapen Shape.RotationAngle istället.
#### **Tar bort föråldrad Validation.AreaList-egenskap**
Använd egenskapen Validation.Areas istället.
#### **Tar bort föråldrad stilkonstruktor**
Använd metoden CellsFactory.CreateStyle() eller Workbook.CreateStyle() istället.
#### **Tar bort föråldrad Shape.IsPrinted-egenskap**
Använd egenskapen Shape.IsPrintable istället.
#### **Tar bort föråldrad PivotItem.Move(int)-metod**
Använder metoden PivotItem.Move(int , bool ) istället.
#### **Tar bort föråldrad Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,objekt[]), Cells.ExportDataTable int, int, int, int , Cells.ExportDataTable(DataTable, int, int[],int, bool) och Cells.ExportDataTable(DataTable,int, int, int, bool, bool) metoder**
Använd metoden ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions) istället.
