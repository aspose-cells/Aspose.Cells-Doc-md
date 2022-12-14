---
title: Aspose.Cells för Java 19.12 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-19-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Java 19.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43047|Lägger till verktygstipstext i cellen för export i HTML|Ny funktion|
|CELLSJAVA-43002|Oväntad CPU-hotspot i ZipOutputStream när XSLB öppnas|Förbättring|
|CELLSJAVA-43008|Möjlighet att inaktivera laddning av OLE-objekt när du öppnar en arbetsbok|Förbättring|
|CELLSJAVA-42793|Fontwork SmartArt-objekt förlorade under ODS till XLSX-konvertering|Insekt|
|CELLSJAVA-43020|Radiell graf förvrängd efter anrop av Chart.Calcluate()|Insekt|
|CELLSJAVA-43022|Form till bild-fel för XLS-filer|Insekt|
|CELLSJAVA-43046|LoadOptions.setParsingFormulaOnOpen(false) orsakar oönskade resultat när getFormula() anropas|Insekt|
|CELLSJAVA-43052|Valideringsproblem för booleska värden|Insekt|
|CELLSJAVA-43054|Problem med CSV Merge i portugisiska inställningar|Insekt|
|CELLSJAVA-43056|Cell.setFormula() uppdateras inte för externa länkar|Insekt|
|CELLSJAVA-42767|Bild missade under konvertering av Excel till PDF|Insekt|
|CELLSJAVA-42913|Inbäddade Visio objekt renderade felaktigt till PDF|Insekt|
|CELLSJAVA-42883|Problem med att extrahera graftext från Aspose.Cells för fil i Java 95-format|Insekt|
|CELLSJAVA-42931|Bilagor/objekt hämtade inte från Excel95|Insekt|
|CELLSJAVA-43051|Bildförhållande bibehålls inte för bilden|Insekt|
|CELLSJAVA-43057|Problem med att lägga till rubrikbild på första sidan i utdata Excel|Insekt|
|CELLSJAVA-43069|MS Excel ger ett reparationsmeddelande när den återsparade filen öppnas med Aspose.Cells|Insekt|
|CELLSJAVA-43060|Undantag "java.lang.NullPointerException" på Workbook.save efter att ha ställt in extern datakälla som tom|Undantag|
|CELLSJAVA-42923|Undantag vid laddning av XLS-dokument|Undantag|

## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
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
Uppsättningar för att rendera EMF-metafil.
### **Lägger till egenskapen PdfSaveOptions.EmfRenderSetting**
Uppsättningar för att rendera EMF-metafil under rendering till PDF-fil.
### **Lägger till metoden ShapeCollection.AddSvg().**
Lägger till svg-bild.
### **Lägger till WorkbookSettings.QuotePrefixToStyle-egenskapen**
Anger om Style.QuotePrefix-egenskapen ställs in när strängvärdet (som börjar med ett citattecken ) anges i cellen
### **Lägger till egenskapen HtmlSaveOptions.AddTooltipText**
Anger om man lägger till verktygstipstext när data inte kan visas helt. Standardvärdet är falskt.
