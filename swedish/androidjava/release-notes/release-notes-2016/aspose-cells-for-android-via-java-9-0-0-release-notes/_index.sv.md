---
title: Aspose.Cells för Android via Java 9.0.0 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-android-via-java-9-0-0-release-notes/
---
|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41925|Beräkningstiden har ökat med de senaste API-revisionerna|Ny funktion|
|CELLSJAVA-40958|Användarkonfigurerbar teckensnittsersättningsmekanism krävs|Ny funktion|
|CELLSJAVA-41925|Beräkningstiden har ökat med de senaste API-revisionerna|Ny funktion|
|CELLSJAVA-41947|Möjlighet att upptäcka om en DataPoint är i Pie eller Bar|Ny funktion|
|CELLSJAVA-41936|Workbook.calculateFormula()-metoden avslutas aldrig för Excel-källfilen|Förbättring|
|CELLSJAVA-41827|Kalkylark tar mer än 3 minuter att beräkna formler med Workbook.calculateFormula()-metoden|Förbättring|
|CELLSJAVA-41928|Det gick inte att fånga bildresursen när kalkylbladet renderades till HTML med IStreamProvider|Insekt|
|CELLSJAVA-41841|Problem med att rendera kryssrutor till HTML|Insekt|
|CELLSJAVA-41932|Problem med getDisplayStringValue() för datumformaterade värden|Insekt|
|CELLSJAVA-41930|Genom att använda Light Cells API:er för att bearbeta en XLS-fil, bearbetas alltid den första cellen i det första arket|Insekt|
|CELLSJAVA-41931|Teckenavstånd och brytning är inte korrekta för vertikal text vid rendering av kalkylark till PDF|Insekt|
|CELLSJAVA-41709|Kolumnbredden är annorlunda på CentOS än på Windows|Insekt|
|CELLSJAVA-41933|Diagramskalan har ändrats vid rendering av kalkylark till PDF|Insekt|
|CELLSJAVA-41934|Justeringsproblem vid rendering av en Excel-fil till PDF|Insekt|
|CELLSJAVA-41935|Formatering av förklaringsposter störs när kalkylbladet renderas till PDF|Insekt|
|CELLSJAVA-41943|Horisontella axeletiketter har inte renderats helt, det vill säga; alla etiketter saknar visst innehåll i den renderade bilden.|Insekt|
|CELLSJAVA-41940|Filen är skadad efter formelberäkning och spara|Insekt|
|CELLSJAVA-41952|Beräkningsresultatet är inte korrekt|Insekt|
|CELLSJAVA-41941|Matrisformeln beräknas inte korrekt|Insekt|
|CELLSJAVA-41937|Vissa värden från Excel-filen saknas i utgången HTML - XLS till HTML-konvertering|Insekt|
|CELLSJAVA-41969|Cell skuggning saknas vid konvertering av HTML till XLSX|Insekt|
|CELLSJAVA-41955|Arbetsbok till HTML visar '#' i celler|Insekt|
|CELLSJAVA-41942|Kanter saknas, cellskuggning och bilder - HTML till Excel-rendering|Insekt|
|CELLSJAVA-41967|Cells saknas i PDF när flera utskriftsområden definieras i ett enda ark|Insekt|
|CELLSJAVA-41958|Förklaringen på höger sida avkortas i diagrambilden|Insekt|
|CELLSJAVA-41953|Text felplacerad i diagrammet efter konvertering till HTML-format|Insekt|
|CELLSJAVA-41948|Diagrammet ändras vid konvertering av kalkylblad till HTML|Insekt|
|CELLSJAVA-41981|Felaktig position av vertikal linje i diagrammets PDF|Insekt|
|CELLSJAVA-41964|Autofit tar inte hänsyn till indragsnivå|Insekt|
|CELLSJAVA-40260|Ändra texten i en befintlig WordArt i en Excel-fil|Insekt|
|CELLSJAVA-41927|Undantag: "java.lang.OutOfMemoryError" när du sparar i HTML-filformat|Undantag|
|CELLSJAVA-41945|CellsException: Fel vid beräkning av Cell[0Sheet1!E5]at Workbook.calculateFormula vid beräkning av TREND-funktionen|Undantag|
|CELLSJAVA-41946|Att öppna Excel-fil orsakar java.lang.NumberFormatException: För inmatningssträng: "80000020"|Undantag|
|CELLSJAVA-41922|IndexOutOfBoundsException vid kopiering av celler|Undantag|
|CELLSJAVA-41971|Cell.getValidationValue() kastar NullPointerException för anpassad valideringstyp|Undantag|
|CELLSJAVA-41963|Undantag för olaglig nyckelstorlek inträffar när källan a5.xlsx öppnas|Undantag|
|CELLSJAVA-41962|ArrayIndexOutOfBoundsException undantag inträffar när källan a4.xls öppnas|Undantag|
|CELLSJAVA-41961|Ogiltig sträng i filen undantag inträffar när källan a3.xls öppnas|Undantag|
|CELLSJAVA-41960|NegativeArraySizeException-undantaget inträffar när källan a2.xls öppnas|Undantag|
|CELLSJAVA-41959|NullPointerException-undantag uppstår när källan a1.xlsx öppnas|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som har gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Android. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen CopyOptions.ReferToDestinationSheet och metoden Cells.CopyRows(Cells sourceCells, int sourceRowIndex, int destinationRowIndex, int rowNumber, CopyOptions copyOptions)**
När du kopierar intervallet och diagrammet hänvisar till källarket betyder False att det kopierade diagrammets datakälla inte kommer att ändras. Sant betyder att det kopierade diagrammets datakälla refererar till målarket.
### **Lägger till egenskapen HtmlSaveOptions.FilePathProvider**
Hämtar eller ställer in IFlePathProvider för export av arbetsblad till HTML separat.
### **Lägger till IFilePathProvider-gränssnitt**
Representerar den exporterade filsökvägen.
### **Lägger till FontConfigs-klassen**
Anger teckensnittsinställningar.
### **Lägger till FontSourceBase-klassen**
Detta är en abstrakt basklass för klasserna som låter användaren specificera olika teckensnittskällor.
### **Lägger till klassen FileFontSource**
Representerar den enda TrueType-teckensnittsfilen som är lagrad i filsystemet.
### **Lägger till klassen FolderFontSource**
Representerar mappen som innehåller TrueType-teckensnittsfiler.
### **Lägger till klassen MemoryFontSource**
Representerar den enda TrueType-teckensnittsfilen som är lagrad i minnet.
### **Lägger till FontSourceType enum**
Anger typen av en teckensnittskälla.
### **Lägger till CalculationOptions.Rekursiv egenskap**
Anger om de beroende cellerna ska beräknas rekursivt vid beräkning av en cell och det beror på andra celler.
### **Föråldrade CellsHelper.FontDir-egenskapen**
Använd metoden FontConfigs.SetFontFolder(sträng, bool) med mapp rekursiv till false istället.
### **Föråldrad CellsHelper.FontDirs egendom**
Använd metoden FontConfigs.SetFontFolders(string[], bool) med mapp rekursiv till false istället.
### **Obsoletes CellsHelper.FontFiles-egenskapen**
Använd FontConfigs.SetFontSources(FontSourceBase[]) istället.
### **Föråldrar egenskapen Shape.LineFormat och lägger till egenskapen Shape.Line**
Använd egenskapen Shape.Line istället.
### **Föråldrar egenskapen Shape.FillFormat och lägger till egenskapen Shape.Fill**
Använd Shape.Fill-egenskapen istället.
### **Föråldrade ShapeFormat-klassen och Shape.Format-egenskapen**
Använd egenskaperna Shape.Fill och Shape.Line direkt.
### **Föråldrar ShapeFont-klassen och lägger till klassen TextOptions**
Använd TextOptions-klassen istället.
### **Lägger till egenskapen TextOptions.Fill, TextOptions.Outline och TextOptions.Shadow**
Representerar textens fyllning, kontur och skugga.
### **Föråldrar FontSetting.ShapeFont-egenskapen och lägger till FontSetting.TextOptions-egenskapen**
Använd egenskapen FontSetting.TextOptions istället.
### **Lägger till egenskapen Shape.TextOptions.**
Representerar formens textalternativ.
### **Obsoletes Worksheet.SetBackground-metod.**
Använd egenskapen Worksheet.BackgroundImage istället.
### **Föråldrade LineShape.BeginArrowheadStyle och ArcShape.BeginArrowheadStyle**
Använd egenskapen Shape.Line.BeginArrowheadStyle istället.
### **Föråldrade LineShape.BeginArrowheadWidth och ArcShape.BeginArrowheadWidth**
Använd egenskapen Shape.Line.BeginArrowheadWidth istället.
### **Föråldrade LineShape.BeginArrowheadLength och ArcShape.BeginArrowheadLength**
Använd egenskapen Shape.Line.BeginArrowheadLength istället.
### **Föråldrade LineShape.EndArrowheadStyle och ArcShape.EndArrowheadStyle**
Använd egenskapen Shape.Line.EndArrowheadStyle istället.
### **Föråldrade LineShape.EndArrowheadWidth och ArcShape.EndArrowheadWidth**
Använd egenskapen Shape.Line.EndArrowheadWidth istället.
### **Föråldrade LineShape.EndArrowheadLength och ArcShape.EndArrowheadLength**
Använd egenskapen Shape.Line.EndArrowheadLength istället.
### **Tar bort föråldrad Worksheet.CopyConditionalFormatting()-metod.**
### **Tar bort föråldrad Workbook.CheckWriteProtectedPassword()-metod.**
Använd metoden WorkbookSettings.WriteProtection.ValidatePassword istället.
### **Byter namn på Workbook.RemoveDigitalSign som Workbook.RemoveDigitalSignature-metoden.**
### **Obsoletes WorksheetCollection.ClearPivots-metoden lägger till WorksheetCollection.ClearPivottables-metoden.**
Använd metoden WorksheetCollection.ClearPivottables.
### **Lägger till egenskapen ChartSplitType.Auto.**
Representerar att datapunkterna ska delas med standardmekanismen för denna diagramtyp.
### **Lägger till egenskapen ChartPoint.IsInSecondaryPlot.**
Hämtar eller ställer in ett värde indikerar om dessa datapunkter finns i den andra cirkeln eller stapeln på en cirkel- eller stapeldiagram.
### **Lägger till egenskapen OleObject.ClassIdentifier.**
Hämtar eller ställer in klassidentifieraren för det inbäddade objektet.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Android matchar koden för relevant .NET- och Java-version, ingår de flesta ändringar, förbättringar och korrigeringar i Aspose.Cells för .NET v8.9.1, Aspose.Cells för .NET v8.9.2, Aspose.Cells för .NET v9.0.0, Aspose.Cells för Java v8.9.1, Aspose.Cells för Java v8.9.2 och Aspose.Cells för Java v9.0.0 ingår också i denna Aspose.Cells för Android v9.0.0.

{{% /alert %}}
