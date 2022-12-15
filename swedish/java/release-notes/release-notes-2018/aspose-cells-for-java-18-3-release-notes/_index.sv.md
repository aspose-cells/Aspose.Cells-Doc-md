---
title: Aspose.Cells for Java 18.3 Release Notes
type: docs
weight: 100
url: /sv/java/aspose-cells-for-java-18-3-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.3.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42519|Lägg till PdfSaveOptions.DrawObjectEventHandler liknande ImageOrPrintOptions.DrawObjectEventHandler|Ny funktion|
|CELLSJAVA-42543|Extrahera etikettnamn som kan ställas in för paketobjekt inbäddade i MS Excel-fil|Ny funktion|
|CELLSJAVA-42535|Att använda stream för att importera Excel-fil via GridWebBean.importExcelFile() är ogiltigt eller existerar inte|Förbättring|
|CELLSJAVA-42529|Hur man identifierar kalkylbladsformer via DrawObjectEventHandler|Förbättring|
|CELLSJAVA-42558|Det går inte att komma åt etikettobjekt för horisontell kategoriaxel|Förbättring|
|CELLSJAVA-42552|Utdata HTML matchar inte med MS Excel|Insekt|
|CELLSJAVA-42536|Excel-filer skadade efter öppning/spara av Aspose.Cells API:er|Insekt|
|CELLSJAVA-42513|Extra kolumner kommer i slutet av varje rad i utdata-HTML för ett intervall|Insekt|
|CELLSJAVA-42542|Excel-filen är skadad och har några celler ändrade efter att ha sparats|Insekt|
|CELLSJAVA-42524|Beräkningsfel finns i det dolda bladet, nämligen "KD020"|Insekt|
|CELLSJAVA-42514|ImportTableOptions.setInsertRows() fungerar inte när ResultSet importeras till kalkylbladet|Insekt|
|CELLSJAVA-42505|Kommentarer bifogade till cellerna (i mallfilen) visas inte när Excel-filen importeras till GridWeb|Insekt|
|CELLSJAVA-42520|Inkonsekventa cellkoordinater rapporterade av ImageOrPrintOptions.DrawObjectEventHandler|Insekt|
|CELLSJAVA-42518|Radkanter är feljusterade i utdata-PDF-filen|Insekt|
|CELLSJAVA-42561|X-axelskalan är felaktig i PNG-utdata från Excel-diagram|Insekt|
|CELLSJAVA-42556|Återgivningen av diagrammet är inte korrekt i den utgående PDF-filen|Insekt|
|CELLSJAVA-42547|Diagrammet ersätts med rött X vid konvertering av XLSX till ODS|Insekt|
|CELLSJAVA-42546|Bilder förlorade vid konvertering av ODS till XLSX|Insekt|
|CELLSJAVA-42538|Egenskaper extraheras inte från XLS- och XLSX-filer|Insekt|
|CELLSJAVA-42534|Att spara XLS till XLSB tar bort allowEditRanges|Insekt|
|CELLSJAVA-42532|Styr externa resurser med WorkbookSetting.StreamProvider - det fungerar for .NET men fungerar inte for Java|Insekt|
|CELLSJAVA-42525|Ange formelfält när du importerar data till kalkylblad - det fungerar for .NET men fungerar inte for Java|Insekt|
|CELLSJAVA-42521|Kinesiska tecken i det inbäddade filnamnet (titel) visas inte väl i anteckningsblocket|Insekt|
|CELLSJAVA-42533|Undantag "NullPointerException" inträffade vid extrahering av SmartArt-formtext|Undantag|
|CELLSJAVA-42545|Undantag "ReadElementString kan endast anropas när innehållet är enkelt eller tomt" när en ODS-fil laddas|Undantag|
|CELLSJAVA-42526|Fel i cell B4 - Ogiltig formel - undantag inträffar vid inställning av formel|Undantag|
|CELLSJAVA-42522|ArrayIndexOutOfBoundsException vid öppning av fil via Aspose.Cells|Undantag|
|CELLSJAVA-42517|Undantag "com.aspose.cells.CellsException: Ogiltig formel:" när en ODS-fil laddas|Undantag|
# **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen HtmlSaveOptions.ExportSimilarBorderStyle**
Anger om liknande kantstil exporteras när kantstilen inte stöds av webbläsare. Om du vill importera HTML- eller MHT-filen till Excel, behåll standardvärdet. Standardvärdet är falskt.
#### **Lägger till egenskapen Axis.AxisLabels**
Hämtar beteckningarna för axeln efter anrop av metoden Chart.Calculate().
#### **Lägger till ny enumtyp: GridValidationType.CustomServerFunction**
Representerar anpassad funktionsvalidering på serversidan.
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
