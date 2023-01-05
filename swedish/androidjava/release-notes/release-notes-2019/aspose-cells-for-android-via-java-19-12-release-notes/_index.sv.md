---
title: Aspose.Cells for Android via Java 19.12 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-android-via-java-19-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 19.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41814|Stöd anpassad datasortering för det specifika området i pivottabellrapporten|Ny funktion|
|CELLSJAVA-43032|Lägg till Validation.addArea (CellArea cellArea, boolean skipArea) eller Validation.setAreas() metod/överbelastningar till API:erna|Ny funktion|
|CELLSJAVA-42851|Få information om ODATA-anslutningen|Ny funktion|
|CELLSJAVA-43047|Lägger till verktygstipstext i cellen för export i HTML|Ny funktion|
|CELLSJAVA-42988|Prestandaproblem med calculateFormula()|Förbättring|
|CELLSJAVA-43018|Exportera utskriftsområdesintervall till HTML utan att implicit ändra något tillstånd för samma arbetsbok|Förbättring|
|CELLSJAVA-43041|Cells.importCSV ger undantaget "strängvärde får inte överstiga 255 tecken"|Förbättring|
|CELLSJAVA-43043|Cells.removeDuplicates tar mer tid för stora datamängder|Förbättring|
|CELLSJAVA-43002|Oväntad CPU-hotspot i ZipOutputStream när XSLB öppnas|Förbättring|
|CELLSJAVA-43008|Möjlighet att inaktivera laddning av OLE-objekt när du öppnar en arbetsbok|Förbättring|
|CELLSJAVA-43019|Radiellt diagram renderas inte korrekt till HTML|Insekt|
|CELLSJAVA-43027|Efter återgivning till PNG är skalningen av axeln annorlunda.|Insekt|
|CELLSJAVA-42474|Pivottabellen uppdateras inte och är skadad efter uppdatering av källdata|Insekt|
|CELLSJAVA-43033|Konverteringen till PDF slutar inte.|Insekt|
|CELLSJAVA-43034|Ogiltigt ryskt (anpassat) datumformat har hämtats|Insekt|
|CELLSJAVA-43040|LoadFilter tar inte hänsyn till det obligatoriska arket|Insekt|
|CELLSJAVA-43035|Gränser försvinner när Excel-fil konverteras till EMF|Insekt|
|CELLSJAVA-43016|Ogiltigt sidantal från SheetRender|Insekt|
|CELLSJAVA-43026|Efter att ha renderat diagram till bild ändrar dataetiketter stil, och värdena är inte desamma|Insekt|
|CELLSJAVA-43038|Hyperlänkar exporteras inte med Cell.setHtmlString()|Insekt|
|CELLSJAVA-43039|Cell.setHtmlString() renderar inte vissa HTML-taggar/skript till Excel-export|Insekt|
|CELLSJAVA-41103|Pivottabellens datafärgning och formatering återges inte korrekt|Insekt|
|CELLSJAVA-43007|PDF genereras inte som förväntat|Insekt|
|CELLSJAVA-43025|Cell.getStyle.getCustom returnerar fel format för tysk språkversion|Insekt|
|CELLSJAVA-42793|Fontwork SmartArt-objekt förlorades under konverteringen ODS till XLSX|Insekt|
|CELLSJAVA-43020|Radiell graf förvrängd efter anrop av Chart.Calcluate()|Insekt|
|CELLSJAVA-43022|Form till bild-fel för XLS-filer|Insekt|
|CELLSJAVA-43046|LoadOptions.setParsingFormulaOnOpen(false) orsakar oönskade resultat när getFormula() anropas|Insekt|
|CELLSJAVA-43052|Valideringsproblem för booleska värden|Insekt|
|CELLSJAVA-43054|Problem med CSV Sammanfoga i portugisiska inställningar|Insekt|
|CELLSJAVA-43056|Cell.setFormula() uppdateras inte för externa länkar|Insekt|
|CELLSJAVA-42767|Bild missade under konvertering av Excel till PDF|Insekt|
|CELLSJAVA-42913|Inbäddade Visio objekt renderade felaktigt till PDF|Insekt|
|CELLSJAVA-42883|Problem med att extrahera graftext från Aspose.Cells for Java fil i 95-format|Insekt|
|CELLSJAVA-42931|Bilagor/objekt hämtade inte från Excel95|Insekt|
|CELLSJAVA-43051|Bildförhållande bibehålls inte för bilden|Insekt|
|CELLSJAVA-43057|Problem med att lägga till rubrikbild på första sidan i utdata Excel|Insekt|
|CELLSJAVA-43069|MS Excel ger ett reparationsmeddelande när den återsparade filen öppnas med Aspose.Cells|Insekt|
|CELLSJAVA-43013|ArrayIndexOutOfBoundsException när Excel-filen laddas|Undantag|
|CELLSJAVA-43060|Undantag "java.lang.NullPointerException" på Workbook.save efter att ha ställt in extern datakälla som tom|Undantag|
|CELLSJAVA-42923|Undantag vid laddning av XLS Dokument|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.
### **Lägger till metoden Cells.RemoveDuplicates().**
Tar bort dubbletter av data från intervallet.
### **Lägger till egenskapen OleObject.FullObjectBin**
Hämtar den fullständiga inbäddade ole-objektets binära data i mallfilen.
### **Lägger till egenskapen ContentTypeProperty.IsNillable**
Anger om egenskapen kan vara null.
### **Lägg till metoden WorkbookDesigner.SetDataSource(String,ICellsDataTable).**
Ställer in datakällan för smart markördesigner.
### **Lägger till egenskapen ImageOrPrintOptions.PageSavingCallback**
Kontrollera/indikera förloppet för sidsparprocessen..
### **Lägger till egenskapen ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
Anger om teckensnittet endast byts ut när cellteckensnittet inte är kompatibelt med det.
### **Tar bort föråldrad klass HTMLLoadOptions**
Använd klassen HtmlLoadOptions istället.
### **Tar bort föråldrad klass ODSLoadOptions**
Använd klassen OdsLoadOptions istället.
### **Tar bort föråldrad klass JSONUtility**
Använd klassen JsonUtility istället.
### **Lägger till metoder: Validation.AddArea(CellArea,bool,bool),AddAreas(CellArea[], bool, bool),RemoveAreas(CellArea[])**
Lägger till/tar bort valideringsinställningar från givna områden med hänsyn till prestanda.
### **Lägger till metoden Workbook.ImportXml (Stream stream, string sheetName, int row, int col).**
Importerar en XML-filström till arbetsboken.
### **Lägger till metoden Workbook.ExportXml (sträng mapName, Stream stream).**
Exportera XML-data till en ström.
### **Lägger till egenskapen HtmlSaveOptions.ExportArea**
Hämtar eller ställer in den exporterande CellArea för det aktuella aktiva arbetsbladet. Om du ställer in det här attributet kommer utskriftsområdet för det aktuella aktiva arbetsbladet att utelämnas. Endast det angivna området kommer att exporteras när filen sparas till HTML.
### **Lägger till klasser: DataMashup,PowerQueryFormula,PowerQueryFormulaCollection,PowerQueryFormulaItem och PowerQueryFormulaItemCollection**
Får information i DataMashup.
### **Lägger till egenskapen DBConnection.SeverCommand.**
Hämtar och ställer in en andra kommandotextsträng som kvarstår när PivotTable-serverbaserade sidfält används.
### **Lägger till metoden CellsHelper.GetTextWidth().**
Hämtar textens bredd i punktenheten.
### **Tar bort föråldrad DataLabels.BaseField-egenskap**
Använd PivotField.BaseFieldIndex istället.
### **Tar bort föråldrad DataLabels.BaseItem-egenskap**
Använd PivotField.BaseItemIndex istället.
### **Tar bort föråldrad DataLabels.IsValueShown-egenskap**
Använd egenskapen DataLabels.ShowValue istället.
### **Tar bort föråldrad DataLabels.IsPercentageShown-egenskap**
Använd egenskapen DataLabels.ShowPercentage istället.
### **Tar bort föråldrad DataLabels.IsBubbleSizeShown-egenskap**
Använd egenskapen DataLabels.ShowBubbleSize istället.
### **Tar bort föråldrad DataLabels.IsCategoryNameShown-egenskap**
Använd egenskapen DataLabels.ShowCategoryName istället.
### **Tar bort föråldrad DataLabels.IsSeriesNameShown-egenskap**
Använd egenskapen DataLabels.ShowSeriesName istället.
### **Tar bort föråldrad DataLabels.IsLegendKeyShown-egenskap**
Använd egenskapen DataLabels.ShowLegendKey istället.
### **Lägger till alternativet LoadOptions.KeepUnparsedData**
Alternativet anger om den oparsade datan ska behållas i minnet för arbetsboken när den laddas från en mallfil. Om användare inte behöver spara tillbaka arbetsboken helt och hållet, särskilt när de bara behöver läsa något speciellt innehåll i arbetsboken (t.ex. med någon form av LoadFilter), behövs inte den oparsade datan längre och de kan ställa in den här egenskapen som falsk för att få bättre prestanda. För gamla versioner, när arbetsbok laddades från en mallfil med användarspecificerat LoadFilter, behölls inte de oparsade data av prestandaskäl. Nu tillhandahåller vi det här alternativet och gör dess standardvärde sant, det kan påverka prestandan för användarnas fall av att använda LoadFilter. Om så är fallet bör användarna uttryckligen ange den här egenskapen som falsk i sin applikation.
### **Lägger till alternativet LoadDataFilterOptions.Picture**
Alternativet som anger om bilden ska laddas.
### **Lägger till alternativet LoadDataFilterOptions.OleObject**
Alternativet som anger om OleObject ska laddas.
### **Lägger till alternativet LoadDataFilterOptions.Drawing**
Alternativet som anger om ritobjekt (inklusive diagram, bild, OleObject och alla andra ritobjekt) ska laddas.
### **Föråldrade LoadDataFilterOptions.Shape-alternativet**
Använd (LoadDataFilterOptions.Drawing & ~LoadDataFilterOptions.Chart) istället för LoadDataFilterOptions.Shape.
### **Lägger till klassen FormulaParseOptions**
Ger användaralternativ för att ställa in formler.
### **Lägger till metoder: Cell.SetFormula(strängformel,FormulaParseOptions optioner,objektvärde),SetArrayFormula(string arrayFormula,int rowNumber,int columnNumber,FormulaParseOptions options),SetSharedFormula(string sharedFormula,int rowNumber,FormulaParseNumberOption)**
Ställer in formler med alternativ.
### **Föråldrade metoder: Cell.SetFormula(strängformel,bool ärR1C1,bool ärLokal,objektvärde),SetArrayFormula(sträng arrayFormula,int radNumber,int kolumnNumber,bool ärR1C1,bool ärLokal),SetSharedFormula,(intkolonnNumberFormula,,introwdNumber isR1C1,bool isLocal)**
Använd motsvarande metoder med FormulaParseOptions istället.
### **Lägger till FileFormatType.OTP enum**
Stöder detektering av .OTP-filformatet.
### **Lägger till AutoFitterOptions.AutoFitWrappedTextType-egenskapen och AutoFitWrappedTextType-enum.**
Hämtar och ställer in typen av automatisk anpassning av inslagen text.
### **Lägger till klassen EmfRenderSetting**
Uppsättningar för rendering av EMF metafil.
### **Lägger till egenskapen PdfSaveOptions.EmfRenderSetting**
Uppsättningar för att rendera EMF metafil medan rendering till PDF fil.
### **Lägger till metoden ShapeCollection.AddSvg().**
Lägger till svg-bild.
### **Lägger till WorkbookSettings.QuotePrefixToStyle-egenskapen**
Anger om Style.QuotePrefix-egenskapen ställs in när strängvärdet (som börjar med ett citattecken ) anges i cellen
### **Lägger till egenskapen HtmlSaveOptions.AddTooltipText**
Anger om man lägger till verktygstipstext när data inte kan visas helt. Standardvärdet är falskt.
