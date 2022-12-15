---
title: Aspose.Cells for Android via Java 18.3 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-android-via-java-18-3-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 18.3.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42493|Ange ett alternativ för att bestämma om arbetsboksegenskaper ska exporteras|Ny funktion|
|CELLSJAVA-42491|Ge ett alternativ för att bestämma om dokumentegenskaper ska exporteras|Ny funktion|
|CELLSJAVA-42498|Skapa en PdfBookmarkEntry för ett diagramblad|Ny funktion|
|CELLSJAVA-42509|Lägg till konstanten LoadDataFilterOptions.NAMES för att filtrera definierade namn när arbetsboken laddas|Ny funktion|
|CELLSJAVA-42519|PdfSaveOptions.DrawObjectEventHandler behövs precis som ImageOrPrintOptions.DrawObjectEventHandler|Ny funktion|
|CELLSJAVA-42543|Extrahera etikettnamn som kan ställas in för paketobjekt inbäddade i Excel-fil|Ny funktion|
|CELLSJAVA-42510|Observera mycket långsam filtrering i Microsoft Excel 2013 och 2016 när filtret används|Förbättring|
|CELLSJAVA-42464|Fix som behövs för alla ActiveX-kontroller|Förbättring|
|CELLSJAVA-42490|Uteslut oanvända stilar när du exporterar Excel-fil till HTML (överordnat problem-id: CELLSJAVA-42471)|Förbättring|
|CELLSJAVA-42529|Hur man identifierar kalkylbladsformer via DrawObjectEventHandler|Förbättring|
|CELLSJAVA-42558|Det går inte att komma åt objekt med horisontella kategoriaxeletiketter|Förbättring|
|CELLSJAVA-42473|Delar av bilderna är trunkerade eller saknas och de matchar inte originalbilderna|Insekt|
|CELLSJAVA-42469|Bilden sticker ut från formen i den utgående PDF-filen|Insekt|
|CELLSJAVA-42461|Elementformen är felaktig i utdata-HTML|Insekt|
|CELLSJAVA-42495|Excel till HTML - Radbrytning av text ignoreras|Insekt|
|CELLSJAVA-42489|XLSB-filen blir korrupt efter att ha öppnats och sparats|Insekt|
|CELLSJAVA-42487|HTML-utdataavvikelse - Problem med mellanslag|Insekt|
|CELLSJAVA-42471|Irrelevant data ingår när du sparar till HTML|Insekt|
|CELLSJAVA-42467|XLSB skadad efter att ha sparats på nytt|Insekt|
|CELLSJAVA-42488|15-siffriga nummer stämmer inte överens med vad som finns i MS Excel|Insekt|
|CELLSJAVA-42499|Marginaler och layoutskillnader vid jämförelse av utdata-PDF (av Aspose.Cells) med MS Excel-genererad PDF|Insekt|
|CELLSJAVA-42486|Funktionen fungerar inte i Java - ResultSet|Insekt|
|CELLSJAVA-42497|Ark1-former försvinner och stjärnor i Ark2 är rundade|Insekt|
|CELLSJAVA-42512|Ogiltig kodning - Undantag inträffar när Excel-filen laddas|Insekt|
|CELLSJAVA-42507|Makro- och dialogblad upptäcks som vanliga kalkylblad|Insekt|
|CELLSJAVA-42503|MS Excel tillåter inte att spara XLS-fil igen|Insekt|
|CELLSJAVA-42502|Aspose.Cells filtrerar inte data korrekt istället döljer det alla rader|Insekt|
|CELLSJAVA-42552|Utdata HTML matchar inte med Excel|Insekt|
|CELLSJAVA-42536|Excel-filer skadade efter öppning/spara av Aspose.Cells API:er|Insekt|
|CELLSJAVA-42513|Extra kolumner kommer i slutet av varje rad i utdata-HTML för ett intervall|Insekt|
|CELLSJAVA-42542|Excel-filen är skadad och har några celler ändrade efter att ha sparats|Insekt|
|CELLSJAVA-42524|Beräkningsfel finns i det dolda arket, nämligen KD020|Insekt|
|CELLSJAVA-42514|ImportTableOptions.setInsertRows() fungerar inte när ResultSet importeras till kalkylbladet|Insekt|
|CELLSJAVA-42505|Kommentarer som är kopplade till cellerna (i mallfilen) visas inte när Excel-filen importeras till GridWeb|Insekt|
|CELLSJAVA-42520|Inkonsekventa cellkoordinater rapporterade av ImageOrPrintOptions.DrawObjectEventHandler|Insekt|
|CELLSJAVA-42518|Radkanter är feljusterade i utdata-PDF-filen|Insekt|
|CELLSJAVA-42561|X-axelskalan är felaktig i PNG-utdata från Excel-diagram|Insekt|
|CELLSJAVA-42556|Återgivningen av diagrammet är inte korrekt i den utgående PDF-filen|Insekt|
|CELLSJAVA-42547|Diagrammet ersätts med rött X vid konvertering av XLSX till ODS|Insekt|
|CELLSJAVA-42546|Bilder förlorade vid konvertering av ODS till XLSX|Insekt|
|CELLSJAVA-42538|Egenskaper extraheras inte från XLS- och XLSX-filer|Insekt|
|CELLSJAVA-42534|Att spara XLS till XLSB tar bort allowEditRanges|Insekt|
|CELLSJAVA-42533|Undantag "NullPointerException" inträffade vid extrahering av SmartArt-formtext|Insekt|
|CELLSJAVA-42532|Artikelkod - Styr externa resurser med WorkbookSetting.StreamProvider - fungerar inte for Java|Insekt|
|CELLSJAVA-42525|Artikelkod - Ange formelfält när du importerar data till kalkylblad - fungerar inte for Java|Insekt|
|CELLSJAVA-42521|Kinesiska tecken i det inbäddade filnamnet (titel) visas inte väl i anteckningsblocket|Insekt|
|CELLSJAVA-42545|Undantag "ReadElementString kan endast anropas när innehållet är enkelt eller tomt" när en ODS-fil laddas|Undantag|
|CELLSJAVA-42500|NullPointerException inträffar när MS Excel-filen laddas|Undantag|
|CELLSJAVA-42526|Fel i Cell B4-Ogiltig formel - undantag inträffar vid inställningsformel|Undantag|
|CELLSJAVA-42522|ArrayIndexOutOfBoundsException vid öppning av fil via Aspose.Cells|Undantag|
|CELLSJAVA-42517|Undantag "com.aspose.cells.CellsException: Ogiltig formel:" när en ODS-fil laddas|Undantag|
# **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.
#### **Lägger till egenskapen LoadOptions.ParsingPivotCachedRecords**
Anger om tolkning av pivotcachade poster när filen laddas. Standardvärdet är falskt. Gäller endast för filformaten Excel Xlsx, Xltx, Xltm, Xlsm och Xlsb.
#### **Lägger till egenskapen HtmlSaveOptions.ExcludeUnusedStyles**
Anger om oanvända stilar exkluderas. Standardvärdet är falskt. Om du vill importera HTML- eller Mht-filen till Excel, behåll standardvärdet.
#### **Lägger till egenskapen HtmlSaveOptions.ExportDocumentProperties**
Anger om dokumentegenskaper exporteras. Standardvärdet är sant. Om du vill importera HTML- eller Mht-filen till Excel, behåll standardvärdet.
#### **Lägger till egenskapen HtmlSaveOptions.ExportWorksheetProperties**
Anger om kalkylbladsegenskaper exporteras. Standardvärdet är sant. Om du vill importera HTML- eller Mht-filen till Excel, behåll standardvärdet.
#### **Lägger till egenskapen HtmlSaveOptions.ExportWorkbookProperties**
Anger om arbetsboksegenskaper exporteras. Standardvärdet är sant. Om du vill importera HTML- eller Mht-filen till Excel, behåll standardvärdet.
#### **Lägger till metoden PivotTable.GetChildren().**
Får barnens pivottabeller som använder denna pivottabelldata som datakälla.
#### **Lägger till LoadDataFilterOptions.DefinedNames enum**
Anger om definierade namnobjekt laddas när mallfilen laddas.
#### **Ändrar beteendet för LoadDataFilterOptions.Formula enum**
I äldre versioner laddar vi alltid definierade namnobjekt när vi laddar formler. Nu tillhandahåller vi separat enum för definierade Name-objekt explicit, så Formel Enum kommer bara att beteckna att formler ska laddas nu, oavsett vilka definierade Name-objekt kommer att laddas eller inte. En sak bör dock noteras, vanligen definierade namnobjekt används av formler, om användaren bara laddar formler och inte laddar de definierade namnobjekten, kommer cellformeln som refererar till dessa namn att bli skadad och kan orsaka undantag. Så, i allmänhet, om användaren vill ladda formler, bör de definierade namnobjekten också laddas. Men användaren kan bara ladda definierade namnobjekt utan att ladda formler.
#### **Lägg till SheetType.Dialog enum**
Representerar dialogblad.
#### **Lägger till egenskapen WorkbookSettings.MaxRowsOfSharedFormula**
Hämtar och ställer in det maximala radnumret för delad formel. Den delade formeln delas upp i flera delade formler om det totala antalet rader av delade formeln är större än det.
#### **Lägger till WorkbookSettings.StreamProvider-egenskapen**
Hämtar och ställer in strömleverantören för extern resurs.
#### **Lägger till egenskapen ShapeTextAlignment.IsAutoMargin**
Indikerar om marginalen på textramen är atuomatisk.
#### **Lägger till egenskapen ImportTableOptions.IsFormulas**
Representerar vilken kolumn i datatabellen som ska importeras som formler.
#### **Lägger till egenskapen HtmlSaveOptions.ExportSimilarBorderStyle**
Anger om liknande kantstil exporteras när kantstilen inte stöds av webbläsare. Om du vill importera HTML- eller MHT-filen till Excel, behåll standardvärdet. Standardvärdet är falskt.
#### **Lägger till egenskapen Axis.AxisLabels**
Hämtar beteckningarna för axeln efter anrop av metoden Chart.Calculate().
#### **Lägger till ChartType.Map enum**
Representerar kartdiagrammet.
#### **Lägger till egenskapen OleObject.Label**
Hämtar och ställer in visningsetiketten för det länkade Ole-objektet.
#### **Lägger till egenskapen BuiltInDocumentPropertyCollection.DocumentVersion**
Representerar versionen av filen.
#### **Lägger till StyleFlag.QuotePrefix enum**
Anger om stilens QuotePrefix-egenskap tillämpas.
#### **Lägger till DialogBox-klass**
Representerar dialogrutan.
#### **Lägger till egenskapen PdfSaveOptions.DrawObjectEventHandler**
Hämtar och ställer in DrawObjectEventHandler för att hämta DrawObject och Bound under rendering.
#### **Lägger till egenskapen DrawObject.Shape**
Får den relaterade formen under rendering.

{{% alert color="primary" %}} 

Since the code base of Aspose.Cells for Android via Java matches the code of relevant .NET and Java version(s), most of the changes, enhancements and fixes included in the Aspose.Cells for .NET v18.1, Aspose.Cells for .NET v18.2, Aspose.Cells for .NET v18.3, Aspose.Cells for Java v18.1, Aspose.Cells for Java v18.2 och Aspose.Cells for Java v18.3 ingår också i denna 07611073411 08.11073411

{{% /alert %}}
