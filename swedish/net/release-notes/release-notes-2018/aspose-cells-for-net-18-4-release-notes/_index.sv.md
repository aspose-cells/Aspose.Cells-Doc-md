---
title: Aspose.Cells for .NET 18.4 Release Notes
type: docs
weight: 90
url: /sv/net/aspose-cells-for-net-18-4-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 18.4](https://www.nuget.org/packages/Aspose.Cells/18.4.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46045|Ställ in Pdf-sidans storlek när du använder metoden Chart.ToPdf|Ny funktion|
|CELLSNET-45590|Stöd för rendering av Histogram MS Excel 2016-diagram|Ny funktion|
|CELLSNET-46007|Lägg till en motsvarande egenskap till egenskapen "FilterMode" för MS Excel Worksheet-objekt (VBA)|Ny funktion|
|CELLSNET-46026|Stöd modifiering av ytterligare celler i cellModifiedOnAjax - Aspose.Cells.GridWeb|Ny funktion|
|CELLSNET-46013|Ny korstyp med att dölja överlagrat innehåll när du sparar som HTML|Förbättring|
|CELLSNET-45965|Möjlighet att bearbeta standard LINK-element under bakåtkonvertering|Förbättring|
|CELLSNET-46032|Generera inte ensidig tom PDF när Excel-filen är tom|Förbättring|
|CELLSNET-46027|Excel till PDF-rendering - Problem med sidhuvud/sidfot|Förbättring|
|CELLSNET-45970|När en kolumn anpassas automatiskt tar Aspose.Cells inte hänsyn till radhöjden när cellen är textraderad|Förbättring|
|CELLSNET-44985|Problem med automatisk anpassning av kolumner med radbrytning av text|Förbättring|
|CELLSNET-42701|AutoFitColumns problem med radbrytningstext|Förbättring|
|CELLSNET-46005|Skrifter omvända för olika ark i utdata-PDF-filformatet|Insekt|
|CELLSNET-45958|Felaktig formatering när XLSX sparas som HTML|Insekt|
|CELLSNET-45907|Saknade värden i renderingen av diagram|Insekt|
|CELLSNET-46034|Det går inte att ta bort pivottabeller (vars datakälla är extern) från XLS-filformat|Insekt|
|CELLSNET-46016|Excel-filen blir korrupt efter uppdatering av pivottabellen|Insekt|
|CELLSNET-45988|Uppdatering av pivottabellen i "Sample2.xlsx" genererar en korrupt Excel-fil|Insekt|
|CELLSNET-46011|Workbook.Calculation ger fel värde för cell F155|Insekt|
|CELLSNET-46001|Fel utvärdering av DateTime-värden vid beräkning av DateTime-funktioner|Insekt|
|CELLSNET-46000|Krympa för att passa på celler gjorde att texten blev något mindre än normalt i den renderade bilden|Insekt|
|CELLSNET-45998|Marginalerna finns kvar när alla marginaler är inställda på noll och OnePagePerSheet är satt till sant.|Insekt|
|CELLSNET-45990|PDF-utdata varierar beroende på optimeringstypen|Insekt|
|CELLSNET-46053|"Inmatningssträngen var inte i korrekt format" vid beräkning av diagram i mallfilen|Insekt|
|CELLSNET-46029|Problem med anpassad datafiltrering|Insekt|
|CELLSNET-46024|Under spara OriginalDataSource med snedstreck ändrats till omvänt snedstreck|Insekt|
|CELLSNET-46018|Bilder och diagram saknas när du sparar OTS-fil|Insekt|
|CELLSNET-46003|ListFillRange i ActiveX ComboBox uppdateras inte|Insekt|
|CELLSNET-46002|Sidhuvudrader visas endast på den första sidan i utdata-PDF|Insekt|
|CELLSNET-45996|Bugg vid A30 - Nylinjer tas bort|Insekt|
|CELLSNET-45995|Bugg vid C32 - Vitt utrymme är borttaget|Insekt|
|CELLSNET-45968|Workbook.CalculateFormula ändrade "#REF!" namnge?"|Insekt|
|CELLSNET-46031|Kolumnen saknas i GridWeb-utdata efter bindning av en anpassad klass|Insekt|
|CELLSNET-46025|Datavalidering misslyckades alltid i Aspose.Cells.GridWeb|Insekt|
|CELLSNET-46020|Cell-värdet är inte korrekt vid import av en Excel-fil till Aspose.Cells.GridWeb|Insekt|
|CELLSNET-46019|Shapes position är inte korrekt i Aspose.Cells.GridWeb|Insekt|
|CELLSNET-46017|Efter att ha infogat rad eller kolumn blir kalkylbladet tomt med en rad/kolumn i antal|Insekt|
|CELLSNET-46009|Värden och kontroller går förlorade när celler redigeras t.ex. I13, I14, I15 etc.|Insekt|
|CELLSNET-45994|Visa valideringsinmatningsmeddelandet i GridWeb|Insekt|
|CELLSNET-45991|Att rulla till den nedre raden och klicka på gruppknappen komprimerar inte raderna|Insekt|
|CELLSNET-45919|Kontroller (alternativknappar och rullningslister) återges inte vid import av en Excel-fil|Insekt|
|CELLSNET-45975|Cells i intervallet L10:L12 kan inte slås samman|Undantag|
|CELLSNET-46008|Ogiltig sträng i filen - undantag inträffar när XLS-filen öppnas|Undantag|
|CELLSNET-46004|Undantag "Inmatningssträngen var inte i korrekt format" när du öppnade en XLSX-fil|Undantag|
|CELLSNET-45992|Aspose.Cells 18.2: Att öppna en viss XLS-fil orsakar ArgumentOutOfRangeException|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
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
