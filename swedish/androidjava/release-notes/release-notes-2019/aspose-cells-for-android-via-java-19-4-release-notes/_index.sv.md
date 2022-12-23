---
title: Aspose.Cells for Android via Java 19.4 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-android-via-java-19-4-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 19.4.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42838|Inaktiverar egenskapen för automatisk visa aktivitetsfönstret.|Ny funktion|
|CELLSJAVA-42853|Prestandaproblem vid konvertering av XLSX till HTML|Förbättring|
|CELLSANDROID-88|Bild förlorades under konvertering av arbetsbok till PDF|Insekt|
|CELLSJAVA-42852|Etiketten på båda axlarna visas inte|Insekt|
|CELLSJAVA-42856|Excel till HTML problem|Insekt|
|CELLSJAVA-42872|Bild på arket, den högra och nedersta raden saknas|Insekt|
|CELLSJAVA-42873|Det förkonditionerade arket har flera cellbakgrunder och text saknas och är dold.|Insekt|
|CELLSJAVA-42874|Kolumnförlust vid export av en fil till HTML|Insekt|
|CELLSJAVA-42875|Bredden är fel och displayen är ur form|Insekt|
|CELLSJAVA-42878|Resultatet av att beräkna formler är inte korrekt|Insekt|
|CELLSJAVA-40419|Det går inte att skapa taggat PDF vid export från Excel till PDF|Insekt|
|CELLSJAVA-40570|Fel konvertering till PDF och JPG för sidor i olika storlekar|Insekt|
|CELLSJAVA-42833|Problem när du bäddar in samma PDF-fil i flera ark i en arbetsbok|Insekt|
|CELLSJAVA-42858|Problem när du lägger till en bild i sammanslagna celler med smarta markörer med alternativet Picture:FitToCell|Insekt|
|CELLSJAVA-42862|Arknamnet byts om i formler efter importen CSV|Insekt|
|CELLSJAVA-42865|Fel tid läst från en cell i ODS-filen|Insekt|
|CELLSJAVA-42879|Excel-filen blir skadad efter att ha sparats med Aspose.Cells|Insekt|
|CELLSJAVA-42860|java.lang.NullPointerException när du laddar ett ODS filformat|Undantag|
|CELLSJAVA-42871|java.lang.Undantag: Ostödd klon för säkerhetskopierad ström vid konvertering av XLSX till PDF|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.
### **Lägger till API:er för att spara Markdown-dokument: SaveFormat.Markdown, FileFormatType.Markdown, MarkdownSaveOptions**
Stöder för att spara cellinnehåll som markdown-tabell. Med metoden Workbook.Save() kommer allt cellinnehåll i det aktiva bladet att exporteras som en tabell i markdown-dokument.
### **Tar bort föråldrade egenskaper för TxtLoadOptions**
Använd egenskapen LoadStyleStrategy istället för KeepExactFormat.
### **Tar bort föråldrad klass LoadDataOption**
Vänligen använd LoadFilter-klassen och LoadOptions.LoadFilter-egenskapen istället.
### **Tar bort föråldrade egenskaper för LoadOptions**
LoadOptions.ConvertNumericData: använd den här egenskapen med motsvarande underklass av LoadOptions, såsom TxtLoadOptions.
LoadOptions.LoadDataOptions: använd LoadOptions.LoadFilter-egenskapen med anpassad implementering av LoadFilter.
LoadOptions.LoadDataFilterOptions: använd LoadOptions.LoadFilter.LoadDataFilterOptions istället.
LoadOptions.OnlyLoadDocumentProperties: använd LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.DocumentProperties.
LoadOptions.LoadDataAndFormatting/LoadDataOnly: använd LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.CellData | LoadDataFilterOptions.DefinedNames.
### **Lägger till egenskapen PdfSaveOptions.ExportDocumentStructure**
Hämtar eller ställer in ett värde som avgör om dokumentstrukturen ska exporteras eller inte.
### **Lägger till klasser av Aspose.Cells.WebExtensions namnutrymme**
Representerar WebExtensions och WebExtension Tasks
### **Lägger till egenskaperna WorksheetCollection.WebExtensions och WorksheetCollection.WebExtensionTaskPanes.**
Representerar alla WebExtensions och WebExtensionTasks.
### **Lägger till klassen WebExtensionShape**
Representerar formen på WebExtension.
### **Lägger till metoden Cells.InsertCutCells().**
Infogar skurna celler.
### **Lägger till metoden Cells.SetViewColumnWidthPixel.**
Ställer in vybredden för kolumnen.
### **Lägger till klasserna ThreadedCommentCollection och ThreadedComment.**
Representerar den trådade kommentaren.
### **Lägger till egenskapen WorksheetCollection.ThreadedCommentAuthors.**
Får och ställer in författarna till trådade kommentarer.
### **Lägger till egenskapen Comment.ThreadedComments.**
Representerar de trådade kommentarerna till kommentaren.
### **Lägg till metoderna CommentCollection.AddThreadedComment() och CommentCollection.GetThreadedComments().**
Lägger till och får de trådade kommentarerna.
### **Lägg till egenskapen Chart.SubTitle.**
Hämtar diagrammets underrubrik. Endast för ODS filformat.
