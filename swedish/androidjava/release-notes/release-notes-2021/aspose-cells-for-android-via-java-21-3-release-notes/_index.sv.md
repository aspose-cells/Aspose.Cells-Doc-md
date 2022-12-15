---
title: Aspose.Cells for Android via Java 21.3 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-android-via-java-21-3-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 21.3.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43375|Kontrollera Excel VBA-lösenord|
|CELLSJAVA-43400|Stöd UNIQUE() funktion|
|CELLSJAVA-42863|Hämta diagrams undertitel|
|CELLSJAVA-43401|Stöd för enhetligt formateringsresultat för japanska eran för alla JDK:er|
|CELLSJAVA-43398|Villkorlig formatering återges inte korrekt i ODS till HTML-konvertering|
|CELLSJAVA-43371|XLSX till PDF-konvertering hänger sig|
|CELLSJAVA-43353|Olika diagram på excel till pdf|
|CELLSJAVA-43377|Bildplaceringsproblem vid konvertering av Excel till HTML|
|CELLSJAVA-43381|DAYS funktionsberäkningsfel|
|CELLSJAVA-43342|Kombinationsdiagram kan inte visas korrekt i excel till pdf|
|CELLSJAVA-43354|Procentandelar visades inte i de små histogrammen|
|CELLSJAVA-40264|Fel med formulärkontroller eller ActiveX-kontroller när du sparar som EXCEL_97_TO_2003|
|CELLSJAVA-43372|Skadad fil skapades vid konvertering av ODS till XLSX|
|CELLSJAVA-43378|Visa som tomt ändras från sant till falskt efter kloning av arbetsboken|
|CELLSJAVA-43382|Kopiera producerar skadad arbetsbok|
|CELLSJAVA-43364|Problem när du sparar diagram med bild i markören till bild|
|CELLSJAVA-43389|Arbetsbok/arbetsblad Lösenordsskyddsinställningar förlorade när du sparade som XLSB-filformat|
|CELLSJAVA-43392|Kopiering av ark ger en korrupt arbetsbok|
|CELLSJAVA-43388|Utdatafilen är korrupt efter kopiering av arbetsbok|
|CELLSJAVA-43406|Problem vid konvertering av HTML till Excel|
|CELLSJAVA-43399|CalculateFormula() skapar många feltypvärden #VALUE|
|CELLSJAVA-43362|Procentuellt problem för etiketter vid utskrift av diagram|
|CELLSJAVA-43384|Procentuella problem för vissa etiketter vid rendering till PDF och utskrift av diagram|
|CELLSJAVA-43402|Generera exakt diagrambild från Excel-fil|
|CELLSJAVA-43408|Toppen av diagrammet skärs av och den lutande linjen går upp|
|CELLSJAVA-43379|Undantag uppstod när arbetsboken sparades som HTML|
|CELLSJAVA-43376|Undantag "java.lang.ClassCastException: Överflöde i int till byte-konvertering. int värde: 144" vid inläsning av en XLSX-fil|
|CELLSJAVA-43387|Export av ett ark till HTML ger undantag|
|CELLSJAVA-43412|CellsException i xlsx till html-konvertering|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Föråldrad PdfSaveOptions(SaveFormat) konstruktor.**

Använd PdfSaveOptions()-konstruktorn istället.

### **Föråldrad XlsbSaveOptions(SaveFormat) konstruktor.**

Använd XlsbSaveOptions()-konstruktorn istället.

### **Föråldrad XlsSaveOptions(SaveFormat) konstruktor.**

Använd XlsSaveOptions()-konstruktorn istället.

### **Föråldrad SpreadsheetML2003SaveOptions(SaveFormat) konstruktor.**

Använd SpreadsheetML2003SaveOptions()-konstruktorn istället.

### **Lägger till metoden Chart.GetChartDataRange().**

Hämtar dataintervallskällan för diagrammet.

### **Lägger till metoden Chart.SwitchRowColumn().**

Byter rad/kolumn för diagrammets dataintervallskälla.

### **Lägger till metoden OleObject.SetEmbeddedObject().**

Ställer in inbäddat objekt.

### **Lägger till metoden VbaProject.ValidatePassword().**

Validerar lösenordet för VBA-projektet.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerBackgroundColor och Series.MarkerBackgroundColor, lägger till egenskapen Marker.BackgroundColor.**

Använder Marker.BackgroundColor istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerForegroundColor och Series.MarkerForegroundColor , lägger till egenskapen Marker.ForegroundColor.**

Använder Marker.ForegroundColor istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerBackgroundColorSetType och Series.MarkerBackgroundColorSetType , lägger till egenskapen Marker.BackgroundColorSetType.**

Använder Marker.BackgroundColorSetType istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerForegroundColorSetType och Series.MarkerForegroundColorSetType , lägger till egenskapen Marker.ForegroundColorSetType.**

Använder Marker.ForegroundColorSetType istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerSize och Series.MarkerSize.**

Använder Marker.MarkerSize istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerStyle och Series.MarkerStyle.**

Använder Marker.MarkerStyle istället.

### **Ändrar beteendet för Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

gamla versioner tar vi bort alla kolumninställningar samtidigt som vi raderar tomma rader om kalkylbladet är tomt (inga celldata). Detta gör det omöjligt för användaren att bara ta bort tomma rader och behålla alla kolumninställningar. Från 21.2 rensar vi inte längre kolumninställningar. Om användaren behöver ta bort kolumninställningar för tomt kalkylblad, bör han kontrollera att det inte finns några data i arket och sedan rensa kolumnsamlingen manuellt.
I gamla versioner tar vi inte bort tomma rader under form. Detta gör det omöjligt för användaren att ta bort alla tomma rader som de förväntar sig. Från 12.2 tar vi bort de tomma raderna under form tillsammans med andra vanliga tomma rader.

### **Föråldrad Range.CellCount-egenskap.**

Använd Range.RowCount och Range.ColumnCount för att få det totala cellantalet istället.

### **Lägger till egenskapen AutoFilter.ShowFilterButton.**

Indikerar om filterknappen för autofiltret visas.

### **Tar bort egenskapen SeriesCollection.SecondCatergoryData.**

Använd egenskapen SeriesCollection.SecondCategoryData istället.

### **Tar bort StyleModifyFlag.Spacing enum.**

Den är inte använd.

### **Lägger till egenskapen SignatureLine.Id.**

Hämtar eller ställer in identifierare för denna signaturrad.

### **Lägger till egenskapen DigitalSignature.Id.**

Anger ett UUID som kan korsreferens med UUID för signaturraden som lagras i dokumentinnehållet.

### **Lägger till egenskapen DigitalSignature.ProviderId.**

Anger klass-ID för signaturleverantören.

### **Lägger till egenskapen DigitalSignature.Image.**

Anger en bild för den digitala signaturen.

### **Lägger till egenskapen DigitalSignature.Text.**

Anger texten för den faktiska signaturen i den digitala signaturen.

### **Lägger till metoden Cells.ClearMergedCells().**

Tar bort alla sammanslagna celler.

### **Lägger till metoden Workbook.RemovePersonalInformation().**

Tar bort all personlig information.

### **Lägger till egenskapen WorkbookSettings.ForceFullCalculate.**

Egenskapen instruerar ms excel att helt beräkna varje gång en beräkning utlöses.

### **Lägger till DocxSaveOptions(Boolean) konstruktor.**

Representerar alternativ för att spara .docx-filer.

### **Tar bort föråldrad WorkbookSettings.IsWriteProtected-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.IsWriteProtected istället.

### **Tar bort föråldrad WorkbookSettings.RecommendReadOnly-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.RecommendReadOnly istället.

### **Tar bort föråldrad WorkbookSettings.WriteProtectedPassword-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.Password istället.
