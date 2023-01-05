---
title: Aspose.Cells for Java 8.3.2 Release Notes
type: docs
weight: 90
url: /sv/java/aspose-cells-for-java-8-3-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.3.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.3.2/)

{{% /alert %}} 

\1) Aspose.Cells 


Huvudfunktioner

Utgivna arkivändringar för JDK som stöds

Från och med nu tillhandahåller vi endast en enda Jar-fil för 1.6 och uppåt i arkivet.

Andra förbättringar och förändringar

Nya egenskaper

(CELLSJAVA-41144) - Möjlighet att ta bort Style från StyleCollection när du sparar HTML
(CELLSJAVA-41127) - Ange anpassade avgränsare för hela arbetsboken
(CELLSJAVA-41143) - Ange jobb-/dokumentnamn vid utskrift med Aspose.Cells

Förbättringar

(CELLSJAVA-41145) - Smart generering av CSS vid export av kalkylark till HTML
(CELLSJAVA-41177) - Cell.setHtmlString fungerar inte när du använder "<s><span style="color:#ff00ff;">S2</span></s>"
(CELLSJAVA-41162) - Lägg till standardteckensnittskataloger för Mac och Linux i söklistan för teckensnitt

Prestanda

(CELLSJAVA-41119) - Chart.toImage hänger på obestämd tid

Buggar

(CELLSJAVA-41165) - PivotChart uppdateras inte efter uppdatering av källdata och rendering av kalkylarket till PDF
(CELLSJAVA-41156) - Chart.refreshPivotData gör att datumen i diagramaxeln konverteras till siffror medan kalkylbladet konverteras till PDF
(CELLSJAVA-41154) - Extra rad visas i HTML-utdata medan intervallet klistras in med PasteType.ALL
(CELLSJAVA-41151) - Konstigt beteende när det gäller formatering i den utgående pivottabellrapporten när du använder och utan att använda kodraden som motsvarar hämtning av radintervall
(CELLSJAVA-41150) - FormatCondition stöds inte för Numbers-format vid rendering till HTML-filformat
(CELLSJAVA-41146) - Felaktig rendering av gränsen vid konvertering av kalkylblad till HTML
(CELLSJAVA-41134) - XLSB2007TestNewS.xlsb laddas inte och fortsätter att öka minnesförbrukningen
(CELLSJAVA-41129) - Extra rader visas när utdata HTML visas i Chrome
(CELLSJAVA-41122) - Öppna och spara Finansiellt_Påstående_Inmatning_Rapportera_Withdata.xlsb gör det korrupt
(CELLSJAVA-41098) - Uppdatera pivottabellen tar bort pivottabellens formatering vid konvertering till PDF
(CELLSJAVA-41157) - MemorySetting.MEMORY_PREFERENCE gör att XLS skadas
(CELLSJAVA-41149) - Felaktig återgivning av tid när kalkylblad konverteras till PDF
(CELLSJAVA-41148) - Excel hittade oläsbart innehåll... fel när arbetsboken öppnades och sparades
(CELLSJAVA-41141) - Cell ställs inte in med metoden ListObject.putCellValue()
(CELLSJAVA-41140) - Utvidgning av tabell kopierar inte formel till nya rader
(CELLSJAVA-41166) - XPS Viewer kan inte öppna Aspose.Cells genererad XPS
(CELLSJAVA-41163) - SVG export skapar ogiltig fil
(CELLSJAVA-41153) - Shape.toImage lagrar bilden i BMP-format istället för SVG för andra former än diagram
(CELLSJAVA-41137) - Problem med att ställa in dataetiketternas cellintervallsvärden
(CELLSJAVA-41128) - Diagram renderas inte bra när du sparar om XLSX-filen
(CELLSJAVA-41125) - Sjökortsbilden har ett brus med när den konverteras med lägre upplösning
(CELLSJAVA-40928) - Kinesisk text i diagramkategorititlar återges inte korrekt
(CELLSJAVA-41158) - Problem med formateringsdata i pivottabellrapporten
(CELLSJAVA-41159) - Problem med att beräkna pivottabelldata
(CELLSJAVA-41175) - Trendline-serier visas inte i förklaringen

Undantag

(CELLSJAVA-41164) - java.lang.NullPointerException på Cells.find
(CELLSJAVA-41131) - Spara till PDF fastnar och minnesproblem med källfilen XLSB

Offentlig API och bakåtinkompatibla ändringar

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

 Lägger till WorkbookSettings.NumberDecimalSeparator, NumberGroupSeparator egenskaper
 Hämtar/ställer in separatorerna som används för att formatera/tolka numeriska värden.

Lägger till metoden WorkbookSettings.CheckWriteProtectedPassword().
 Kontrollerar om lösenordet är korrekt skrivskyddat lösenord.

 Lägger till egenskapen Picture.SignatureLine och klassen SignatureLine.
 Används för att skapa och läsa inställningen för signaturraden.

 Lägger till egenskapen PivotItem.Position.
 Anger positionsindex i alla PivotItems, inte PivotItems under samma överordnade nod.

 Lägger till egenskapen PivotItem.PositionInSameParentNode.
 Anger positionsindex i PivotItems under samma överordnade nod.

 Lägger till metoden PivotItem.Move(int count, bool isSameParent).
Flyttar objektet uppåt eller nedåt.

 Lägger till metoden Worksheet.RefreshPivotTables().
Uppdaterar alla pivottabeller i detta arbetsblad.

 Lägger till metoden Workbook.GetNamedStyle(strängnamn).
Hämtar den namngivna stilen i arbetsbokens stilpool efter namn.

 Lägger till Cells.ImportTwoDimensionArray(object,, object,, int, int, TxtLoadOptions)
Importerar en tvådimensionell datamatris till ett kalkylblad med mer flexibla alternativ definierade i TxtLoadOptions.

 Lägger till egenskapen PageSetup.IsAutomaticPaperSize.
 Indikerar om pappersstorleken är automatisk.

 Lägger till egenskaper för XpsSaveOptions.OnePagePerSheet
Om OnePagePerSheet är sant , kommer allt innehåll på ett ark endast att matas ut till en sida som resultat.

 Lägger till egenskaper för XpsSaveOptions.PageIndex
Hämtar eller ställer in det 0-baserade indexet för den första sidan som ska sparas.

 Lägger till egenskaper för XpsSaveOptions.PageCount
Hämtar eller ställer in antalet sidor som ska sparas.

 Lägger till metoden SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)
Återger arbetsbladet till skrivaren.

 Lägger till metoden WorkbookRender.ToPrinter(sträng PrinterName, int PrintPageIndex, int PrintPageCount)
Återger arbetsboken till skrivaren.

 Lägger till egenskaper för PdfSaveOptions.IsFontSubstitutionCharGranularity
Anger om teckensnittet endast byts ut när cellteckensnittet inte är kompatibelt med det.

 Lägger till egenskapen GridWeb.AutoRefreshChart
Anger om diagrambilden uppdateras under uppdatering av cellvärdet. Standardvärdet är sant.

 Lägger till metoden GridWeb.RefreshChartShape().
Uppdaterar hela diagrambilden för det aktiva kalkylbladet.

 Obsoletes Workbook.SaveOptions-egenskap
Användare bör bygga korrekta SaveOptions och sedan använda Workbook.Save() med det.

 Föråldrad StyleCollection-klass och Workbook.Styles-egenskap
Användare bör använda Workbook.CreateStyle() för att skapa och manipulera stil för arbetsbok istället för StyleCollection.Add() och använda Workbook.GetNamedStyle(string) för att få namngiven stil istället för StyleCollectionstring.

 Föråldrade metoden PivotItem.Move(int count).
Använder metoden PivotItem.Move(int count, bool isSameParent) för istället.

 Tar bort alla föråldrade Open()- och Save()-metoder i Workbook.

 Tar bort föråldrad Workbook.SetOleSize()-metod.

 Tar bort föråldrade IsProtected-, Språk- och Regionegenskaper för Workbook.

 Tar bort föråldrade Workbook.LoadData()-metoder.

 Tar bort föråldrade Open()- och Save()-metoder i WorkbookDesigner.

Tar bort föråldrade egenskaper för ReCalcOnOpen,Language, Encoding och ConvertNumericData för WorkbookSettings.

 Tar bort föråldrade egenskaper HidePivotFieldList, EnableHTTPCompression,IsMinimized,IsHidden,SheetTabBarWidth för WorksheetCollection.

 Tar bort föråldrade egenskaper för WindowLeft,WindowLeftInch,WindowLeftCM,WindowTop,WindowTopInch,WindowTopCM,WindowWidth,WindowWidthInch,WindowWidthCM,WindowHeight,WindowHeightInch,WindowHeightCM,WindowHeightCM.

 Tar bort föråldrad DeleteName()-metod för WorksheetCollection.

 Tar bort föråldrade HPageBreaks och VPageBreaks av arbetsblad.

 Tar bort föråldrade DisplayHTMLCrossString och ExportChartImageFormat av HtmlSaveOptions.

 Tar bort föråldrad ExpCellNameToXLSX-egenskap för SaveOptions.

 Tar bort föråldrade DefaultFont, Compliance, PdfBookmark och PdfImageCompression egenskaper för SaveOptions.

 Tar bort föråldrad TxtSaveOptions.AlwaysQuoted-egenskap.


Notera
Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.3.2 också inkluderade i denna 076157316.
