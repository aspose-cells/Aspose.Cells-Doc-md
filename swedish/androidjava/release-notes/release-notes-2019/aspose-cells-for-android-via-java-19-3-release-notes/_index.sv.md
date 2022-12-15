---
title: Aspose.Cells for Android via Java 19.3 Release Notes
type: docs
weight: 50
url: /sv/java/aspose-cells-for-android-via-java-19-3-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 19.3.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41026|Stöd för Excel 95/5.0 (XLS-filer)|Ny funktion|
|CELLSJAVA-42827|Infoga rad med InsertOptions liknande MS Excel|Ny funktion|
|CELLSJAVA-42845|Behåll avgränsare för tomma rader när du exporterar en XLS-fil till CSV|Ny funktion|
|CELLSJAVA-42778|Undantag "stil textRotation måste vara mellan 0 och 180" när XLSM laddas|Förbättring|
|CELLSJAVA-42712|Förbättra JavaDocs för Aspose.Cells for Java|Förbättring|
|CELLSJAVA-42823|Användning av FontUnderlineType.WORDS skapar undantag|Förbättring|
|CELLSJAVA-42846|Resultaten för textextraktion skiljer sig åt|Förbättring|
|CELLSANDROID-85|Problem med omvandling av ark till bild med transparenta bilder ovanför andra bilder|Insekt|
|CELLSJAVA-42290|Mdash och ndash infogade i textrutor i diagram renderas inte korrekt i diagrammets PDF|Insekt|
|CELLSJAVA-42750|Det gick inte att hämta sidfältens objekt i pivottabellsrapporten|Insekt|
|CELLSJAVA-42783|Problem med genomstruken text i genererat HTML-filformat|Insekt|
|CELLSJAVA-42784|Data i vissa celler (t.ex. G7, H7, etc.) renderas inte på samma sätt som i originalfilen i Excel till HTML/bildkonvertering|Insekt|
|CELLSJAVA-42797|Vissa stilar återges inte i HTML-inmatning|Insekt|
|CELLSJAVA-42807|Formel/funktion "ISOWEEKNUM"-beräkning är inte detsamma som MS Excel|Insekt|
|CELLSJAVA-42794|ODS till XLSX - Textfärg ändrad|Insekt|
|CELLSJAVA-42795|ODS till XLSX - Teckensnittet genomstrukits inte korrekt bevarat|Insekt|
|CELLSJAVA-42796|ODS till XLSX - Textrutans dimensioner ändrade|Insekt|
|CELLSJAVA-42798|ODS -> XLSX - Hyperlänk är funktionell men visas som vanlig text|Insekt|
|CELLSJAVA-42802|ODS till XLSX, procentandelar går förlorade i stapeldiagrammet|Insekt|
|CELLSJAVA-42803|Outline "SummaryRowBelow" påverkas inte när du sparar som XLSB-filformat|Insekt|
|CELLSJAVA-42826|Data med villkorlig formatering utelämnades vid konvertering av XLSX till HTML|Insekt|
|CELLSJAVA-42815|Att lägga till komplexa referenser till definierade namn resulterar i korrupt MS Excel-arbetsbok|Insekt|
|CELLSJAVA-42822|Cell.getValidationValue returnerar fel värde för det angivna värdet|Insekt|
|CELLSJAVA-42829|Anpassat funktionsnamn inom de delade formlerna ersatt av ett annat namn|Insekt|
|CELLSJAVA-42824|Axeltitlar saknas och annan formatering är fel av diagram i Excel till PDF/A-konvertering|Insekt|
|CELLSJAVA-42814|Pilarna i PNG-utdata matchar inte pilarna i Excel-diagrammet|Insekt|
|CELLSJAVA-42777|Fel radhöjd har ändrats när du använder automatisk anpassning av rader|Insekt|
|CELLSJAVA-42813|Arbetsboksinställningen "ReCalculateOnOpen" kvarstod inte|Insekt|
|CELLSJAVA-42816|Ofullständig visning för AutoFitterOptions.setAutoFitMergedCells(true)|Insekt|
|CELLSJAVA-42817|Textboxens bakgrundsfärg ändrades oväntat|Insekt|
|CELLSJAVA-42821|När den första raden i ett intervall tas bort uppdateras intervallet felaktigt|Insekt|
|CELLSJAVA-42828|När du använder Cell.setHtmlString läggs en ny rad till i slutet av texten|Insekt|
|CELLSJAVA-42844|Texten är inte korrekt justerad i PDF-utdata|Insekt|
|CELLSJAVA-42834|Ändrar svart textfärg till röd|Insekt|
|CELLSJAVA-42839|Spridningsdiagram renderas inte i Excel till PDF-konvertering|Insekt|
|CELLSJAVA-42840|Horisontella axeletiketter renderas inte bra för diagram i Excel till PDF-rendering|Insekt|
|CELLSJAVA-42842|2D Bubble diagram renderas inte i Excel till PDF-konvertering|Insekt|
|CELLSJAVA-42833|Problem när du bäddar in samma PDF-fil i flera ark i en arbetsbok|Insekt|
|CELLSJAVA-42836|Workbook.hasExernalLinks() returnerar inte sant för DDE-länkar|Insekt|
|CELLSJAVA-42848|Teckensnittsinställning och andra objekt som inte kopierats med Range.copy()-funktionen|Insekt|
|CELLSJAVA-42757|CellsException vid konvertering av filer|Undantag|
|CELLSJAVA-42799|Undantag "java.lang.ArrayIndexOutOfBoundsException: -32768" när ett XLSX-filformat laddas|Undantag|
|CELLSJAVA-42800|ArrayIndexOutOfBoundsException när en arbetsbok laddas|Undantag|
|CELLSJAVA-42820|Undantag "Invalid IMEModeType string val" när ett XLSX-filformat laddas|Undantag|
|CELLSJAVA-42849|IndexOutOfBoundsException undantag vid konvertering av XLSX till HTML|Undantag|
|CELLSJAVA-42831|Undantag har tagits upp av Excel efter att ha tillämpat stil på intervallet av rubrikceller|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

**Lägger till metoden PivotTable.ShowReportFilterPageByName(strängfältnamn).**

Visar alla rapportfiltersidor enligt PivotFields namn, PivotField måste finnas i PageFields.
### **Lägger till metoden PivotTable.ShowReportFilterPageByIndex(int posIndex)**
Visar alla rapportfiltersidor enligt positionsindex i sidfälten.
### **Lägger till metoden PivotTable.ShowReportFilterPage(PivotField pageField)**
Visar alla rapportfiltersidor enligt PivotField, PivotField måste finnas i PageFields.
### **Lägger till klasserna DataSorterKey och DataSorterKeyCollection**
Representerar nyckeln för datasorteraren.
### **Lägger till metoden DataSorter.AddKey(Int32,SortOnType,SortOrder,Object)**
Lägger till sorteringsnyckeln som cellens bakgrundsfärg, teckensnittsfärg.
### **Lägger till egenskapen Aspose.Cells.DataSorter.Keys**
Får alla nycklar till datasorteraren.
### **Lägger till SortOnType enum**
Representerar typen av sorterad data.
### **Lägger till klass ODSLoadOptions**
Representerar alternativen för att ladda ODS-fil.
### **Lägger till egenskapen HTMLLoadOptions.ProgId**
Hämtar program-id för att skapa filen. används endast för MHT-filer.
### **Lägger till egenskapen PdfSaveOptions.TextCrossType**
Hämtar eller ställer in visning av texttyp när textbredden är större än cellbredden.
### **Lägger till TextCrossType enum-klass**
Räknar upp visning av texttyp när textbredden är större än cellbredden.
### **Lägger till WorksheetCollection.RegisterAddInFunction() metoder**
Ersättning av Cell.SetAddInFormula(), ett mer bekvämt och effektivt sätt för användare att lägga till och använda tilläggsfunktioner.
### **Föråldrad metod Cell.SetAddInFormula().**
Registrera tilläggsfunktionerna först med WorksheetCollection.RegisterAddInFunction() och ställ sedan in formeln för Cell med Cell.Formula/Cell.SetFormula() istället.
### **Lägger till Cells.CountLarge fastighet**
Funktionellt sett är den samma som Count-egenskapen, förutom att Count-egenskapen kan generera ett spillfel när det finns för många instansierade Cell-objekt.
### **Lägger till metoden Hyperlink.Delete().**
Tar bort denna hyperlänk.
### **Lägger till Range.Hyperlinks-egenskap**
Får alla hyperlänkar i sortimentet.
### **Lägger till enum CopyFormatType**
Representerar typen av kopieringsformat när du infogar rader.
### **Lägger till klassen InsertOptions och metoden Cells.InsertRows(int, int , InsertOptions)**
Infogar rader med vissa alternativ.
### **Lägger till metoderna FileFormatUtil.DetectFileFormat(Stream,String) och FileFormatUtil.DetectFileFormat(String,String)**
Upptäcker filformatet för krypterad OOXML-fil.
### **Lägger till egenskaperna ListObject.AlternativeDescription och ListObject.AlternativeText**
Hämtar och ställer in alternativ text och beskrivning av tabellen.
### **Lägger till Line.ThemeColor-egenskapen**
Hämtar och ställer in linjens temafärg.
### **Lägger till klassen Mode3d och MsoModel3dFormat**
Kapslar in objektet som representerar en enda 3D-modell i ett kalkylblad.
### **Lägger till ImageType.Gltf enum**
Representerar typen av 3D-modell.
### **Ändringar för standardteckensnitt för laddad XLS-mallfil**
äldre versioner stödde vi inte att använda teckensnittet som definierats i temat (avancerad funktion i MS Excel 2007 och senare versioner) enligt regionen när XLS-mallfilerna laddas. På vissa användares krav har vi stött det från v19.3. Om regionen har specificerats i XLS-mallfilen kommer vi att tillämpa teckensnittet som definierats i temat enligt det sparade specificerade regionvärdet. Annars kommer vi att tillämpa typsnittet som definieras i temat enligt applikationsmiljöns regionala inställningar. Detta kommer att göra att standardteckensnittet för arbetsboken (laddat från XLS-mallfil som har specificerat temadata) ändras och sedan påverka andra funktioner, såsom kolumnbredd, formstorlek, renderingseffekt, ... etc.
### **Lägger till metoden Name.GetReferredAreas(bool recalculate).**
Tillhandahåller referenserna som hänvisas till av det definierade namnet som GetRanges(bool recalculate)-metoden. Men de returnerade referenserna representeras av ReferredArea-objekt som ger rikare funktioner inklusive externa länkar.
### **Lägger till egenskapen TxtSaveOptions.KeepSeparatorsForBlankRow**
Anger om separatorer ska matas ut för tom rad. Standardvärdet är falskt vilket betyder att innehållet för den tomma raden kommer att vara tomt.
### **Lägger till enum AutoFitMergedCellsType**
Representerar typen av automatiskt anpassade sammanslagna celler.
### **Föråldrar egenskapen AutoFitterOptions.AutoFitMergedCells och lägger till egenskapen AutoFitterOptions.AutoFitMergedCellsType**
Hämtar och ställer in typen av automatisk passande radhöjd.
### **Lägger till klasser JSONUtility och JsonLayoutOptions**
Den används för att importera json-filer.
### **Lägger till klassen TableToRangeOptions och metoden ListObject.ConvertToRange(TableToRangeOptions options)**
Konverterar tabellen till intervall med alternativ.

{{% alert color="primary" %}} 

Since the code base of Aspose.Cells for Android via Java matches the code of relevant .NET and Java version(s), most of the changes, enhancements and fixes included in the Aspose.Cells for .NET v19.1, Aspose.Cells for .NET v19.2, Aspose.Cells for .NET v19.3, Aspose.Cells for Java v19.1, Aspose.Cells for Java v19.2 och Aspose.Cells for Java v19.3 är också inkluderade i denna 07611073411 0761107311 19.39.

{{% /alert %}}
