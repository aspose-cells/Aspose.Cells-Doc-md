---
title: Aspose.Cells for .NET 19.4 Release Notes
type: docs
weight: 90
url: /sv/net/aspose-cells-for-net-19-4-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.4](https://www.nuget.org/packages/Aspose.Cells/19.4.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46619|Stöd för att spara dokument i Markdown-format|Ny funktion|
|CELLSNET-46124|Stöd för att lägga till WebExtension-form|Ny funktion|
|CELLSNET-46553|Stöd för import av JSON-filer|Ny funktion|
|CELLSNET-46653|Stöd för att lägga till WebExtension-uppgiftsrutan|Ny funktion|
|CELLSNET-46656|Stöd trådade kommentarer|Ny funktion|
|CELLSNET-46657|Stöd för att klippa och klistra celler|Ny funktion|
|CELLSNET-46686|Stöd att ta blankt utrymme (teckenkod 20) som nummergruppsavgränsare för det franska språket|Förbättring|
|CELLSNET-46649|Stort PDF genererat jämfört med onlineverktyget iLovePDF|Förbättring|
|CELLSNET-46093|Diagram respekterar inte Page Setup Black and White|Förbättring|
|CELLSNET-46677|Att exportera Excel till PDF återger inte arabiska texter exakt i diagram|Förbättring|
|CELLSNET-46639|Stöd vertikal sidbrytning för filen ODS.|Förbättring|
|CELLSNET-46631|Exception OutOfMemoryException under rendering|Prestanda|
|CELLSNET-46596|Etiketter saknas i form|Insekt|
|CELLSNET-46615|Shape.ToImage() exporterar bilder av olika storlek|Insekt|
|CELLSNET-46637|Formateringsfel i genererad HTML|Insekt|
|CELLSNET-46650|PivotTable.ShowValuesRow är inte inställd på false programmatiskt|Insekt|
|CELLSNET-46652|Pivotbordsskärare tas bort efter laddning och sparas|Insekt|
|CELLSNET-46678|PivotField.IsRepeatItemLabels bibehålls inte i utdata XLSB|Insekt|
|CELLSNET-46671|Range.Copy efter Range.CopyData korrumperar arbetsboken|Insekt|
|CELLSNET-42423|Att spara till PDF trimmar raddata|Insekt|
|CELLSNET-45698|Metoden Worksheet.AutoFitColumns skär av den långa texten medan den renderas till PDF|Insekt|
|CELLSNET-46661|Mindre antal sidor renderade i PDF jämfört med Excel 365|Insekt|
|CELLSNET-46673|Filstorleksproblem vid konvertering av Excel till PDF|Insekt|
|CELLSNET-46632|ChartPoint.Datalabels.ShowValue fungerar inte som förväntat|Insekt|
|CELLSNET-46655|Kategoriaxeletiketter på flera nivåer förlorade när du sparar med RefreshChartCache = true|Insekt|
|CELLSNET-46665|Excel-filen är skadad efter att ha anropat NSeries.Clear() på Surface-diagram|Insekt|
|CELLSNET-46672|Seriedata saknas vid export av diagram till en bild|Insekt|
|CELLSNET-46627|Ett problem med pivotdiagrampekning|Insekt|
|CELLSNET-46640|Horisontell sidbrytning går förlorad om raden är tom när ODS-filen sparas|Insekt|
|CELLSNET-46643|Namngivna intervall kopieras inte när en kolumn kopieras|Insekt|
|CELLSNET-46644|HeadingPairs och TitlesOfParts-taggar går förlorade|Insekt|
|CELLSNET-46651|Excel-filen skadades när den öppnades och sparades|Insekt|
|CELLSNET-46654|Stöd för att lägga till WebExtension|Insekt|
|CELLSNET-46662|Problem med att hämta BuiltInDocumentProperties|Insekt|
|CELLSNET-46663|Bildstorleken ändrades när XLS konverterades till PDF|Insekt|
|CELLSNET-46667|Dolda rader hämtas medan PlotVisibleRows = true|Insekt|
|CELLSNET-46668|Den prickade linjen blir heldragen när XLSX sparas som ODS|Insekt|
|CELLSNET-46669|Form till bild Fel vid rendering av en Excel-fil till PDF|Undantag|
|CELLSNET-46645|Undantag uppstod när PivotTable.GetChildrens() anropades|Undantag|
|CELLSNET-46675|Undantag vid öppning av en XLSX-fil|Undantag|
|CELLSNET-46646|Undantag uppstår genom att öppna Excel-filen efter uppdatering av diagrammet|Undantag|
|CELLSNET-46660|Style.ForegroundColor-egenskapen ger ett undantag för vissa scenarier|Undantag|
|CELLSNET-46688|Undantag togs upp när stilar tillämpades dynamiskt|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till API:er för att spara Markdown-dokument: SaveFormat.Markdown, FileFormatType.Markdown, MarkdownSaveOptions**
Stöder för att spara cellinnehåll som markdown-tabell. Med metoden Workbook.Save() kommer allt cellinnehåll i det aktiva bladet att exporteras som en tabell i nedmärkningsdokumentet.
#### **Tar bort föråldrade egenskaper för TxtLoadOptions**
Använd egenskapen LoadStyleStrategy istället för KeepExactFormat.
#### **Tar bort föråldrad klass LoadDataOption**
Vänligen använd LoadFilter-klassen och LoadOptions.LoadFilter-egenskapen istället.
#### **Tar bort föråldrade egenskaper för LoadOptions**
LoadOptions.ConvertNumericData: använd den här egenskapen med motsvarande underklass av LoadOptions, såsom TxtLoadOptions.
LoadOptions.LoadDataOptions: använd LoadOptions.LoadFilter-egenskapen med anpassad implementering av LoadFilter.
LoadOptions.LoadDataFilterOptions: använd LoadOptions.LoadFilter.LoadDataFilterOptions istället.
LoadOptions.OnlyLoadDocumentProperties: använd LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.DocumentProperties.
LoadOptions.LoadDataAndFormatting/LoadDataOnly: använd LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.CellData | LoadDataFilterOptions.DefinedNames.
#### **Lägger till egenskapen PdfSaveOptions.ExportDocumentStructure**
Hämtar eller ställer in ett värde som avgör om dokumentstrukturen ska exporteras eller inte.
#### **Lägger till klasser av Aspose.Cells.WebExtensions namnutrymme**
Representerar WebExtensions och WebExtension Tasks.
#### **Lägger till egenskaperna WorksheetCollection.WebExtensions och WorksheetCollection.WebExtensionTaskPanes.**
Representerar alla WebExtensions och WebExtensionTasks.
#### **Lägger till klassen WebExtensionShape.**
Representerar formen på WebExtension.
#### **Lägger till metoden Cells.InsertCutCells().**
Infogar skurna celler.
#### **Lägger till metoden Cells.SetViewColumnWidthPixel.**
Ställer in vybredden för kolumnen.
#### **Lägger till klasserna ThreadedCommentCollection och ThreadedComment.**
Representerar den trådade kommentaren.
#### **Lägger till egenskapen WorksheetCollection.ThreadedCommentAuthors.**
Får och ställer in författarna till trådade kommentarer.
#### **Lägger till egenskapen Comment.ThreadedComments.**
Representerar de trådade kommentarerna till kommentaren.
#### **Lägg till metoderna CommentCollection.AddThreadedComment() och CommentCollection.GetThreadedComments().**
Lägger till och får de trådade kommentarerna.
#### **Lägg till egenskapen Chart.SubTitle.**
Hämtar diagrammets underrubrik. Endast för ODS filformat.
