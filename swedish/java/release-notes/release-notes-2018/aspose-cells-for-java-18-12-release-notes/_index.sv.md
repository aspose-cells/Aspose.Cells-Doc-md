---
title: Aspose.Cells för Java 18.12 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-18-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Java 18.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42745|Får inte anslutningspunkter eftersom dess returnerade typ är 'zo[]'|Ny funktion|
|CELLSJAVA-42662|Ge möjlighet att exportera intervall som HTML|Ny funktion|
|CELLSJAVA-42746|Datafält saknas när XLSX konverteras till HTML|Ny funktion|
|CELLSJAVA-42747|Värdet existerar fortfarande när XLSX konverteras till HTML-filformat|Ny funktion|
|CELLSJAVA-42748|LightCells API kan inte ladda en stor fil|Förbättring|
|CELLSJAVA-42727|Textformatering saknas i HTML-utdata från MS Excel-intervallet|Insekt|
|CELLSJAVA-42744|Ikonuppsättningar blir feljusterade när XLSX konverteras till HTML|Insekt|
|CELLSJAVA-42772|Export av namngivna intervalldata renderas inte korrekt till HTML (Java)|Insekt|
|CELLSJAVA-42753|Ett problem hittades i Named Range|Insekt|
|CELLSJAVA-42764|Validering returnerar alltid sant för 'getInCellDropDown()'-metoden|Insekt|
|CELLSJAVA-42768|Fel kultur anpassat format returneras för olika platser (Tyskland, franska, Italien och Spanien)|Insekt|
|CELLSJAVA-42758|Excel till PDF-konvertering - problem med rendering av mätdiagram|Insekt|
|CELLSJAVA-42761|PDF-återgivning kastar OutOfMemoryError-undantaget|Insekt|
|CELLSJAVA-42759|CellsException vid konvertering av filer|Undantag|
|CELLSJAVA-42755|Undantag "NullPointerException" när XLSX-fil(er) instansieras|Undantag|
|CELLSJAVA-42762|NumberFormatException under bearbetning av filer|Undantag|
|CELLSJAVA-42774|NullPointerException när en CSV laddas|Undantag|
|CELLSJAVA-42765|Undantag "com.aspose.cells.CellsException" när en Excel-fil renderas till PDF-filformat|Undantag|
|CELLSJAVA-42754|"IllegalStateException: Ogiltig kodning: null" när ett XLS-filformat instansieras|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen HtmlSaveOptions.ExportSingleTab**
Anger om den enskilda fliken exporteras när filen bara har ett kalkylblad i sig. Standardvärdet är falskt.
### **Lägger till egenskapen HtmlSaveOptions.ExportPrintAreaOnly**
Anger om utskriftsområdet endast exporteras till html-fil. Standardvärdet är falskt.
### **Tar bort föråldrad Workbook.Initialize()-metod**
Använd Workbook constructor istället.
### **Tar bort föråldrad Workbook.Styles-egenskap**
Använd Workbook.CreateStyle() för att skapa och manipulera stil för arbetsbok istället för StyleCollection.Add(); Använd Workbook.GetNamedStyle(sträng) för att få namngiven stil istället för StyleCollection.
### **Tar bort föråldrad Workbook.CheckWriteProtectedPassword()-metod**
Använd metoden WorkbookSettings.WriteProtection.ValidatePassword istället.
### **Lägger till LoadDataFilterOptions.VBA enum**
Alternativet som används för att ignorera VBA-projekt när mallfilen laddas.
### **Lägger till egenskapen Style.InvariantCustom**
Hämtar den kulturoberoende mönstersträngen för talformat (inklusive mönstersträngen för inbyggt tal).
### **Lägger till egenskapen FindOptions.ValueTypeSensitive**
Anger om den sökta cellvärdetypen ska vara samma som den sökta nyckeln.
### **Föråldrade egenskapen FindOptions.SearchNext**
Använd egenskapen FindOptions.SearchBackward istället, det sanna värdet för denna nya egenskap motsvarar false för SearchNext.
### **Tar bort föråldrade Cells. Metoderna FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains och FindNumber**
Använd metoden Cells.Find (object,Cell,FindOptions) istället. För att få samma resultat med metoderna FindNumber, FindString, ställ in FindOptions.ValueTypeSensitive som sant.
### **Tar bort föråldrad metod Cells.ImportGridView(System.Web.UI.WebControls.GridView,int ,int , bool ,bool ,bool )**
Använd metoden Cells.ImportGridView (System.Web.UI.WebControls.GridView gridView,int firstRow,int firstColumn,ImportTableOptions). istället.
### **Tar bort föråldrad Cells.Starta egendom**
Använd egenskapen Cells.FirstCell istället.
### **Tar bort föråldrad Cells.Slut egendom**
Använd egenskapen Cells.LastCell istället.
### **Tar bort egenskapen Cells[int]**
Använd metoden Cells.GetEnumerator() för att iterera alla celler i detta kalkylblad istället.
### **Tar bort föråldrade metoder Cells.ImportDataColumn()**
Använd metoden Cells.ImportData (DataTable,int,int,ImportTableOptions) istället.
### **Tar bort föråldrade Cells.ImportDataReader()-metoder**
Använd metoden Cells.ImportData (IDataReader, int, int,ImportTableOptions) istället.
### **Tar bort föråldrad Shape.Rotation-egenskap**
Använd egenskapen Shape.RotationAngle istället.
### **Tar bort föråldrad Validation.AreaList-egenskap**
Använd egenskapen Validation.Areas istället.
### **Tar bort föråldrad stilkonstruktor**
Använd metoden CellsFactory.CreateStyle() eller Workbook.CreateStyle() istället.
### **Tar bort föråldrad Shape.IsPrinted-egenskap**
Använd egenskapen Shape.IsPrintable istället.
### **Tar bort föråldrad PivotItem.Move(int)-metod**
Använder metoden PivotItem.Move(int , bool ) istället.
### **Tar bort föråldrad Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,objekt[]), Cells.ExportDataTable int, int, int, int , Cells.ExportDataTable(DataTable, int, int[],int, bool) och Cells.ExportDataTable(DataTable,int, int, int, bool, bool) metoder**
Använd metoden ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions) istället.
### **Lägger till ExtPage.setServlet(HttpServletRequest req,HttpServletResponse resp.)**
 Initierar servletkontext för ExtPage.
### **Lägger till metoden ExtPage.getBean().**
 Hämtar GridWebBean-instans från ExtPage.
### **Tar bort metoden ExtPage.getBean(HttpServletRequest req).**
 Använd ExtPage.getBean() istället.
### **Lägger till egenskapen ExtPage.Maxholders**
 Indikerar maximala GridWeb-instanser för servern som ska behållas (att skapa varje ny sida eller uppdatera betraktas som en ny kontrollinstans), standardvärdet är 1000.
### **Lägger till egenskapen ExtPage.Memoryinstanceexpires**
 Indikerar utgångstiden i sekunder av kontrollinstansen på servern, om tiden går ut kommer den att tas bort från servern, standardvärdet är 3600, cirka en timme.
### **Lägger till egenskapen ExtPage.MemoryCleanRateTime**
 Indikerar varje gång varaktighet i sekunder för att utföra kontrollarbetet, för att kontrollera om kontrollinstansen har löpt ut, om den har löpt ut tar den bort den, standardvärdet är 7200, cirka två timmar.
