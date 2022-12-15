---
title: Aspose.Cells for Java 18.4 Release Notes
type: docs
weight: 90
url: /sv/java/aspose-cells-for-java-18-4-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.4.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42523|Använd FIPS-kompatibel version av Bouncy Castle i Aspose.Cells API:er|Ny funktion|
|CELLSJAVA-42572|Formel bör inte innehålla mer än 8192 tecken|Förbättring|
|CELLSJAVA-42569|Det går inte att komma åt objekt för horisontella kategoriaxeletiketter i diagram i XLS|Förbättring|
|CELLSJAVA-42580|Hämta/ställ in språkdokumentegenskap|Förbättring|
|CELLSJAVA-42565|Förgrundsfärg vs bakgrundsfärg vs fyllningsfärg - Använd en enda metod som tar två argument|Förbättring|
|CELLSJAVA-42528|"<Font>" är inte en giltig HTML5 och självstängande tagg och webbläsare ger en felaktig bild av dess innehåll|Förbättring|
|CELLSJAVA-42413|Infoga SVG-bildtyp i kalkylbladsceller med Aspose.Cells|Förbättring|
|CELLSJAVA-42551|Vissa former är inte korrekta i den utgående PDF-filen|Insekt|
|CELLSJAVA-42578|Villkorlig formatering går förlorad när Excel sparas till HTML|Insekt|
|CELLSJAVA-42571|Utdata HTML matchar inte med MS-Excel|Insekt|
|CELLSJAVA-42553|Länkar till namngivet område är fel efter export till HTML|Insekt|
|CELLSJAVA-42530|Pivottabeller och motsvarande diagram har inte korrekt datumformat|Insekt|
|CELLSJAVA-42527|Diagram har många värden i x-axeln och värden överlappar varandra|Insekt|
|CELLSJAVA-42581|Aspose.Cells returnerar fel värde för cell A2|Insekt|
|CELLSJAVA-42583|XML-karta skapar inte tabell korrekt|Insekt|
|CELLSJAVA-42577|Hämta/extrahera värden (0 för 0 och blank för blank) med metoden DataPoint.getYValue() för ett givet diagram|Insekt|
|CELLSJAVA-42566|Inversion av undertexter (legendposter) i MS Excel-diagram|Insekt|
|CELLSJAVA-42560|Pilar saknas i PNG-utdata från Excel-diagram|Insekt|
|CELLSJAVA-42508|Java-metoden 'Shape.toImage' fungerar annorlunda med samma metod i .NET|Insekt|
|CELLSJAVA-42573|Aspose.Cells 18.3 rotation för en TextBox fungerar inte för EXCEL_97_TO_2003 spara format|Insekt|
|CELLSJAVA-42570|En tom ny rad visas inuti textrutan efter att du har bearbetat och sparat Excel-filen|Insekt|
|CELLSJAVA-42563|Undantag "java.lang.NullPointerException" vid digital signering av en XLSX-fil|Undantag|
# **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till nytt objekt "CrossHideRight" för HtmlCrossType enum**
Visar HTML-korssträng och döljer den högra strängen när texten överlappas.
#### **Lägger till nytt objekt "TSV" för LoadFormat, SaveFormat och FileFormatType enums**
Representerar en TSV-fil (Tab-separated values), samma som "TabDelimited".
#### **Lägger till enum ImageType**
Representerar typen av bild.
#### **Lägger till egenskaperna MsoTextFrame.RotateTextWithShape och ShapeTextAlignment.RotateTextWithShape**
Anger om texten roterar med formen.
#### **Lägger till egenskaperna OleObject.ImageType och Picture.ImageType**
Hämtar bildens bildformat.
#### **Föråldrade egenskaperna OleObject.ImageFormat och Picture.ImageFormat**
Använd egenskaperna OleObject.ImageType och Picture.ImageType istället.
#### **Lägger till en överbelastningsmetod för AutoFilter.Refresh (System.Boolean).**
Hämtar alla dolda raders index och uppdaterar autofiltret.
#### **Lägger till överbelastning Cell.GetHtmlString(System.Boolean) metod**
Hämtar HTML-strängen som innehåller data och vissa format i den här cellen.
#### **Lägger till egenskapen BuiltInDocumentPropertyCollection.Language**
Hämtar och ställer in språket för filen.
#### **Lägger till Style.SetPatternColor(Aspose.Cells.BackgroundType,System.Drawing.Color,System.Drawing.Color)**
Ställer in mönstret och färgen på cellen
#### **Lägger till egenskapen ChartPoint.XValueType**
Hämtar X-värdestyp av diagrampunkten.
#### **Lägger till egenskapen ChartPoint.YValueType**
Hämtar Y-värdestyp för diagrampunkten.
#### **Lägger till enum PageLayoutAlignmentType**
Representerar sidlayoutjusteringstyper.
#### **Lägger till metoden Chart.ToPdf(System.IO.Stream,System.Single,System.Single,Aspose.Cells.PageLayoutAlignmentType,Aspose.Cells.PageLayoutAlignmentType)**
Skapar diagrammets PDF med önskad sidstorlek och sparar den i en ström.
#### **Lägger till metoden Chart.ToPdf(System.String,System.Single,System.Single,Aspose.Cells.PageLayoutAlignmentType,Aspose.Cells.PageLayoutAlignmentType)**
Skapar diagrammets PDF med önskad sidstorlek och sparar den i en fil.
#### **Lägger till egenskapen PdfSaveOptions.OutputBlankPageWhenNothingToPrint**
Indikerar om en tom sida ska matas ut när det inte finns något att skriva ut.
