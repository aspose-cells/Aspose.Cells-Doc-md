---
title: Aspose.Cells for Android via Java 21.6 Release Notes
type: docs
weight: 7
url: /sv/java/aspose-cells-for-android-via-java-21-6-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 21.6.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43396|Konvertering av Excel-ark till textfil tar bort enstaka citat från början|
|CELLSJAVA-43386|Sortering fungerar inte när data innehåller icke-alfanumeriska tecken|
|CELLSJAVA-43452|Japansk kalender som använder en Excel-funktion läses inte korrekt|
|CELLSJAVA-43466|CellsException: Fel för ZipFile vid import av ods|
|CELLSJAVA-43403|Textplacering flyttades till vänster när du sparade som HTML|
|CELLSJAVA-43421|Escape- och radbrytningstecken renderade inte korrekt vid konvertering av HTML till Excel|
|CELLSJAVA-43427|Villkorsformat med datafält Visa värden i HTML-export|
|CELLSJAVA-43428| Bokföringsformat kombinerat med 6-punktsfont förvränger siffror i HTML|
|CELLSJAVA-43429|Text med vertikal textjustering försvinner i HTML|
|CELLSJAVA-43407|Excel-formler hoppas över/ändras efter att filen har sparats|
|CELLSJAVA-43419| Anpassat nummerformat visas inte korrekt i PDF|
|CELLSJAVA-43374|Diagrametiketter upprepas när de bifogade Excel-filerna konverterades till PDF|
|CELLSJAVA-43409| Oväntade dataetiketter dök upp i utdatabilden för diagram|
|CELLSJAVA-43411|Teckensnittsersättningsvarningar fungerar inte i diagram till bildkonvertering|
|CELLSJAVA-43414|Xls till pdf-konverteringsproblem|
|CELLSJAVA-43425|Sidhuvud-sidfot är inte tillgänglig på första sidan när den exporteras till Excel|
|CELLSJAVA-43433|Den refererade bilden renderas inte i PDF|
|CELLSJAVA-43434|SmartMarkers dynamiska formel har fel expanderande cellstil|
|CELLSJAVA-43435| Smart Markers dynamisk formel infogar celler enligt vänster expanderad kolumn men inte enligt kolumnerna i formeln|
|CELLSJAVA-43450|Problem med uppdatering av pivottabell|
|CELLSJAVA-43444|Regression: getLastSavedUniversalTime returnerar felaktigt datum|
|CELLSJAVA-43446|Cells Undantag för spårändringar|
|CELLSJAVA-43448|Regression: Ogiltig referens för lista|
|CELLSJAVA-43457|Oändlig slinga när kopierad arbetsbok sparas|
|CELLSJAVA-43442|Problem med datasortering när du klickar på rubriklänkar i GridWebs vårdemon|
|CELLSJAVA-43443|Problem med redigeringsläge i GridWeb Java|
|CELLSJAVA-43455|Teckensnitt är inte inbäddade i PDF för icke ASCII-tecken när EmbedStandardWindowsFonts ställs in på false|
|CELLSJAVA-43449|Det går inte att ändra teckensnittsfamiljen av diagramelement från "Calibri" till "Aktiv Grotesk"|
|CELLSJAVA-43454|X-axeletiketter är avskurna|
|CELLSJAVA-43445|Regression: saknade raddata för .numbers-filer|
|CELLSJAVA-43463|Tidslinjen är bruten efter att filen har sparats|
|CELLSJAVA-43464|PivotField.hideItem() träder inte i kraft i utdatafilen|
|CELLSJAVA-43470|Text efter en "br"-tagg inom en "th"-tagg trunkeras vid import av ett HTML-dokument|
|CELLSJAVA-43481|Får fel formel från en cell|
|CELLSJAVA-43490|Dokumentegenskaper kan inte extraheras|
|CELLSJAVA-43491|Värdet på formeln som använder datatabellen kan inte extraheras korrekt|
|CELLSJAVA-43498|Formaterat resultat av numeriskt värde är felaktigt för zh_CN-språk|
|CELLSJAVA-43451|Innehållet i Excel-filen visas felaktigt och ChangeStyle (vår) demo fungerar inte korrekt|
|CELLSJAVA-43484|Innehållslayouten är inkonsekvent i Excel till PDF-rendering|
|CELLSJAVA-43465|Saknar några serier av grafer vid konvertering av Excel till PDF|
|CELLSJAVA-43468|Problem med ekvationen av rak linje i Excel till PDF-rendering|
|CELLSJAVA-43432|Diagraminnehåll matchade inte när ett XLS-filformat sparades på nytt|
|CELLSJAVA-43475|Regression: Linjelindade celler skärs av|
|CELLSJAVA-43478|Regression: NUMBERS till PDF, mycket data saknas|
|CELLSJAVA-43485|Regression: Extra innehåll vid rendering av PDF från ODS|
|CELLSJAVA-43492| Konvertering av en XML-fil (SpreadsheetML) tar bort Hidden-inställningen i "Namndefinition" i utdata XLS och XLSX|
|CELLSJAVA-43417|Undantag höjdes när XLSX öppnades från stor fil|
|CELLSJAVA-43431|java.lang.NullPointerException höjdes när Cells.deleteColumn() anropades med den senaste versionen 21.3 medan den fungerar med 21.2|
|CELLSJAVA-43437|IndexOutOfBoundsUndantag för att klicka på andra arksidor i utvärderingsläge|
|CELLSJAVA-43459|NullPointerException i getFormulaLocal() med anpassade GlobalizationSettings|
|CELLSJAVA-43447| Undantag "java.lang.NullPointerException" inträffade vid användning av anpassad stilfil i GridWeb|
|CELLSJAVA-43439|NegativeArraySizeException inträffar vid inläsning av arbetsbok|
|CELLSJAVA-43453|NullPointerException på Workbook.save-metoden|
|CELLSJAVA-43486|NullPointerException vid konvertering av ett HTML-dokument till en arbetsbok|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Lägger till StartAccessCache()/CloseAccessCache()-metoder för arbetsbok och arbetsblad.**

Ge användarna möjlighet att komma åt data i batch-läge med bättre prestanda.

### **Lägger till egenskaperna TxtSaveOptions.ExportQuotePrefix och TxtLoadOptions.TreatQuotePrefixAsValue.**

Ge användarna möjligheten att bestämma hur de ska göra med det ledande citatet av cellens värde vid export/import av CSV/TSV-filer.

### **Lägger till metoderna GlobalizationSettings.GetCollationKey(string,bool) och Compare(string,string,bool).**

Ge användarna möjlighet att åsidosätta standardreglerna för strängjämförelse. För vissa lokaler eller strängvärden kan standardregeln för strängjämförelse inte vara den förväntade (resultatet av vissa funktioner, såsom formelberäkning, sortering, etc., skiljer sig från vad som borde finnas i ms excel). Om så är fallet kan användaren åsidosätta dessa metoder med den förväntade regeln (till exempel kan användaren använda implementeringen av icu-biblioteket).

### **Lägger till enum ImageType.WebP.**

Representerar Weppy-bilden.

### **Lägger till metoden OleObject.SetEmbeddedObject().**

För att kontrollera om ikonen uppdateras automatiskt.

### **Lägger till egenskapen WorkbookDesigner.LineByLine.**

Indikerar om bearbetning av smarta markörer rad för rad.

### **Lägger till egenskapen HtmlSaveOptions.ExportCellCoordinate.**

Anger om excel-koordinater för icke-tomma celler exporteras när filen sparas till html. Standardvärdet är false.Om du vill importera utdata-html till Excel, behåll standardvärdet.

### **Lägger till egenskapen AutoFitterOptions.DefaultEditLanguage.**

Hämtar eller ställer in standardspråk för redigering.

### **Lägger till Slicer.AddPivotConnection(PivotTable pivot) metod.**

Lägger till PivotTable-anslutning för slicer.

### **Lägger till Slicer.RemovePivotConnection(PivotTable pivot) metod.**

Tar bort PivotTable-anslutning av slicer.

### **Lägger till egenskapen TxtSaveOptions.ExportAllSheets.**

Anger om alla kalkylblad exporteras till filen. Dafaut-värdet är falskt som MS Excel.

### **Lägger till FileFormatType.Numbers09 enum.**

Representerar filformatet .numbers 09. Och FileFormatType.Number kommer att representera den senaste.numbers filformattypen senare.

### **Lägger till metoden WorkbookSettings.SetPageOrientationType().**

Ställer in utskriftssidans orienteringstyp för hela filen.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisAutomatic enum.**

Använd DataBarAxisPosition.Automatic enum istället.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisMidpointe num.**

Använd DataBarAxisPosition.Midpoint enum istället.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisNone enum.**

Använd DataBarAxisPosition.None enum istället.

### **Tar bort föråldrade DataBarBorderType.DataBarBorderNone enum.**

Använd DataBarBorderType.None enum istället.

### **Tar bort föråldrade DataBarBorderType.DataBarBorderSolid enum.**

Använd DataBarBorderType.Solid enum istället.

### **Tar bort föråldrad DataBarFillType.DataBarFillGradient enum.**

Använd DataBarFillType.Gradient enum istället.

### **Tar bort föråldrade DataBarFillType.DataBarFillSolid enum.**

Använd DataBarFillType.Solid enum istället.

### **Tar bort föråldrad DataBarNegativeColorType.DataBarColor enum.**

Använd DataBarNegativeColorTypeColor enum istället.

### **Tar bort föråldrad DataBarNegativeColorType.DataBarSameAsPositive enum.**

Använd DataBarNegativeColorType.SameAsPositive enum istället.

### **Tar bort föråldrad OleObject.FileFormatType enum.**

Använd OleObject.FileFormatType enum istället.

### **Tar bort föråldrad DynamicFilterType.Februray enum.**

Använd DynamicFilterType.February enum istället.

### **Lägger till metoden GridCells.MoveRange().**

Flyttar intervallet.

### **Lägger till metoden GridCells.InsertRange().**

Infogar ett område med växlingsalternativ.

### **Lägger till metoden GridCells.DeleteRange().**

Tar bort ett område med skiftalternativ.

### **Ändrar beteendet för egenskapen Cell.IsErrorValue.**

I gamla versioner gäller den här egenskapen endast formelceller. För att det ska överensstämma med andra egenskaper kontrollerar vi från 21.6 även icke-formelceller och om dess värde är felvärde returnerar vi också sant. Användaren kan kontrollera Cell.IsFormula-egenskapen först om han bara behöver kontrollera felvärdet för formelceller.

### **Ändrar beteendet för Cell.Value-egenskapen.**

I gamla versioner returnerar den här egenskapen alltid DateTime-objekt om cellen är formaterad som datumtid och dess värde är numeriskt. Från 21.6 returnerar den här egenskapen själva det numeriska värdet om det överskrider det maximala giltiga DateTime-värdet. Med denna ändring överensstämmer det returnerade objektet med det som visas i formelfältet i ms excel.

### **Lägger till egenskapen Cell.IsNumericValue.**

Ger ett bekvämt och effektivt sätt för användaren att kontrollera om en cells värde är numeriskt värde (int, double, datetime).

### **Lägger till överbelastade metoder för Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula().**

Stöd för att ställa in matrisformler och delade formler med fördefinierade värden.

### **Lägger till enum PdfFontEncoding.**

Representerar pdf-inbäddad teckensnittskodning.

### **Lägger till egenskapen PdfSaveOptions.FontEncoding.**

Hämtar eller ställer in inbäddad teckensnittskodning i pdf.

### **Lägger till egenskapen SlicerCacheItem.Value.**

Returnerar etiketttexten för utsnittsobjektet. Skrivskyddad.

### **Lägger till metoden GlobalizationSettings.GetProtectionNameOfPivotTable().**

Hämtar skyddsnamnet i pivottabellen.

### **Lägger till metoden FileFormatUtil.FileFormatToSaveFormat.**

Konverterar filformat till sparformat.
