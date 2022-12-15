---
title: Aspose.Cells for Android via Java 21.12 Release Notes
type: docs
weight: 1
url: /sv/java/aspose-cells-for-android-via-java-21-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 21.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43994|Stöd för att avbryta exekveringen av WorkbookDesigner.process i SmarkMarker|
|CELLSJAVA-44039|Ändra PDF Producer-attribut från den genererade PDF-filen|
|CELLSJAVA-43768|Java Heap Space Problem observeras vid konvertering av XLSX-fil till PDF|
|CELLSJAVA-43875|Undantag "Ogiltig FontUnderlineType string val" vid laddning av XLSX-filen|
|CELLSJAVA-43876|Undantag "java.lang.ArrayIndexOutOfBoundsException" vid inläsning av en XLSX-fil|
|CELLSJAVA-43844|En förbättring som behövs för bokföringsnummerformat|
|CELLSJAVA-43953|Återge specifik text/del "Cell" och "Kommentar" för att översättas till japanska i Excel till PDF-konvertering|
|CELLSJAVA-43469|Möjlig regression: Prestandaförsämring av FormatConditionCollection.addArea()|
|CELLSJAVA-43646|Skuggeffekten av texten återges inte korrekt|
|CELLSJAVA-43760|Likbent triangelorientering är felaktig|
|CELLSJAVA-43786|När du konverterar XLS-fil till XLSX, renderas vissa delar angående former inte korrekt|
|CELLSJAVA-43838|Efter exekvering av XlsToXlsx försvinner AutoShape|
|CELLSJAVA-43839|Efter exekvering av XlsToXlsx är den vänstra hakparentesen förlorad|
|CELLSJAVA-43842|Efter att ha kört XlsToXlsx skiljer sig formen på LeftBracket från originalet|
|CELLSJAVA-43848|Excel till PDF-konvertering - vissa WordArt-tecken lindas inte på samma sätt som i Excel-fil|
|CELLSJAVA-43880|Felaktiga rundade hörn i textrutan efter konvertering av xls till xlsx|
|CELLSJAVA-43867|Ikonen för villkorligt format skiljer sig vid export till html|
|CELLSJAVA-43812|excelToHtml: Formpositionsförskjutningen är felaktig|
|CELLSJAVA-43871|Prism 9 OLE-objekt visas inte på utdata-PDF|
|CELLSJAVA-43883|Felaktiga renderade sidstorlekar|
|CELLSJAVA-43881|Sammanfogning av filer gör att bakgrundsfärgsinställningen för arken saknas|
|CELLSJAVA-43892|Kanter för Excel som konverterats till HTML saknas|
|CELLSJAVA-43935|Forma text teckensnittsstorlek när du sparar och laddar XLS-fil|
|CELLSJAVA-43952|Tillfällig licens Utgångsfråga|
|CELLSJAVA-43954|XLSX till PDF: Bilden orsakar ett undantag "java.lang.OutOfMemoryError: Java heap space"|
|CELLSJAVA-43902|Vissa kanter i Excel som konverterats till HTML är överflödiga|
|CELLSJAVA-43933|När du exporterar till HTML med endast en data skiljer sig det villkorliga formatet från Excel|
|CELLSJAVA-43878| Felaktig placering av Excel-klusterstapeldiagramdataetiketter|
|CELLSJAVA-43895|Linjeform och andra diagramformer renderas inte korrekt när XLS konverteras till XLSX|
|CELLSJAVA-43934|Cirkeldiagrametiketterna matchade inte med Excel efter manipulering eller uppdatering av diagram|
|CELLSJAVA-43519|Sammanslagna celler som ingår i dolda rader eller kolumner ger en ojämn HTML-tabell|
|CELLSJAVA-43962|Effekten är inkonsekvent efter att det villkorliga formatet i excel har konverterats till HTML|
|CELLSJAVA-43983|Regression: Oändlig loop vid konvertering av XLSX till PDF|
|CELLSJAVA-44029|XLSX till PDF: Bilden konverteras inte|
|CELLSJAVA-44093| Problem med textavkortning med rektangelformer vid rendering till bild i nyare Aspose.Cells for Java versioner|
|CELLSJAVA-44089|DataLabels.setShadow() är inte tillgänglig och den är inte lika med metoden Series.setShadow()|
|CELLSJAVA-44000|Cells stil är felaktig i HTML när man använder ikonuppsättning och annan villkorlig formatering samtidigt|
|CELLSJAVA-43932|Problem med att ställa in dataetiketternas position för exploderade munkdiagram i utdatabilden|
|CELLSJAVA-44094|Diagramtitel trunkeras vid export till PDF|
|CELLSJAVA-43533|Problem med att skapa XLSX till HTML i Ubuntu|
|CELLSJAVA-43987|Den högra kanten av sammanslagna celler går förlorad i html|
|CELLSJAVA-44016|Problem vid konvertering av Excel-filen som innehåller bildens URL till HTML|
|CELLSJAVA-43787|Undantag "IllegalArgumentException: bindestreck längder alla noll ..." i Excel till HTML-rendering|
|CELLSJAVA-43885|IllegalArgumentException vid konvertering av Excel|
|CELLSJAVA-43874|Workbook.save kastar ett undantag på en specifik fil med Aspose.Cells endast när Aspose-licensen tillämpas|
|CELLSJAVA-43969|Ett namn med COUNTIF-funktionen och extern referens ger ett NullPointerException|
|CELLSJAVA-43903|java.lang.NumberFormatException: För inmatningssträng vid rendering av Excel-fil till HTML|
|CELLSJAVA-44071|com.aspose.cells.CellsException: Du har angett för få parametrar för funktionen IF när du anropar Workbook.calculateFormula()|
|CELLSJAVA-44104|NullPointerException vid import av SpreadSheetML|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Lägger till överbelastad metod Name.GetRefersTo().**

Hämtar formeluttrycket baserat på den angivna cellen.

### **Lägger till överbelastad metod Range.AutoFill().**

Fyll automatiskt målområdet med fyllningstyp.

### **Lägger till egenskapen Comment.IsThreadedComment.**

Anger om denna kommentar är trådad kommentar.

### **Lägger till egenskapen HtmlSaveOptions.IgnoreInvisibleShapes.**

Anger om osynliga former används när du sparar html.

### **Lägger till egenskapen Range.CurrentRegion.**

Returnerar ett intervall avgränsat av valfri kombination av tomma rader och tomma kolumner.

### **Lägger till AxisBins klass.**

 Representerar axelfack för histogramdiagram.

### **Lägger till metod SheetRender.GetPageSizeInch(int pageIndex)**

Få sidstorlek på utdatabilden? i enhet av tum.

### **Lägger till metod WorkbookRender.GetPageSizeInch(int pageIndex)**

Få sidstorlek utdatabild? i enhet av tum.

### **Lägger till enum CellValueFormatStrategy.DisplayString.**

Med denna strategi kommer Cell.GetStringValue(CellValueFormatStrategy) att ta hänsyn till gränsen för kolumnbredden vid formatering av cellvärden med visningsstilen. Om det formaterade resultatet överskrider den tillgängliga bredden, kan en eller flera "#" returneras, precis som vad ms excel visar för sådana typer av celler.

### **Lägger till egenskapen WorksheetCollection.ActiveSheetName.**

Hämtar och ställer in det aktiva arknamnet för arbetsboken.

### **Lägger till klasserna JsonLoadOptions och JsonSaveOptions.**

Representerar alternativen för att ladda eller spara filerna.

### **Lägger till egenskapen ImageSaveOptions.StreamProvider.**

Ange strömmarna om det finns två eller fler sidor.

### **Lägger till LoadFormat.Image och LoadFormat.Json enum.**

Representerar bilden och json-typen.

### **Lägger till SaveFormat.Bmp, SaveFormat.Emf,SaveFormat.Gif,SaveFormat.Jpg,SaveFormat.Json och SaveFormat.Png enum**

Nya sparade format som stöds.

### **Lägger till FileFormatType.Emf,FileFormatType.Gif,FileFormatType.Jpg,FileFormatType.Json,FileFormatType.Png,FileFormatType.Wmf enum**

Nya filformatstyper som stöds.

### **Fler begränsningar för att lägga till områden för validering.**

Vi har ändrat områdesmodellen för validering och villkorlig formatering för prestandaövervägande. Den nya modellen kräver fler begränsningar för sekvensen av tillagda områden. För Validation.AddArea(CellArea cellArea, bool checkIntersection, bool checkEdge) och Validation.AddAreas(CellArea[]areas, bool checkIntersection, bool checkEdge), om de två "check"-parametrarna är falska, måste användaren se till att de tillagda områdena sorteras i stigande ordning efter de övre vänstra hörnen. Annars kan oväntade resultat fås för andra operationer. I den nya versionen, eftersom prestandan för att lägga till stora mängder områden har förbättrats avsevärt, tror vi inte att Validation.AddArea(CellArea cellArea) kommer att vara en flaskhals längre. Så vi tror att användare bara kan ringa AddArea(CellArea cellArea) direkt, utan att behöva använda dessa två speciella metoder.

### **Ändrat beteende för att ändra områden av Validation/ConditionalFormatting.**

För validering och villkorlig formatering, i gamla versioner kan deras områden backas upp av CellArea-objektet som hämtats från eller ställts in på dem. Så om användaren ändrar fältvärdet för CellArea-objektet kan områdena också ändras, och vice versa. I själva verket är detta ett oväntat resultat från synen på API design. Från denna version har denna bieffekt tagits bort och användaren kan inte ändra områdena genom att ändra CellArea-objektet längre.

### **Ändrade beteende för att lägga till formatvillkor i FormatConditionCollection.**

För FormatConditionCollection.AddCondition(...)-metoder, gör gamla versioner prioritet för en nyligen tillagd som den lägsta. Det skiljer sig från ms excels beteende. Från den här versionen, precis som vad du får för operationen i ms excel, gör vi det nyligen tillagda formatvillkorets prioritet som den högsta.

### **Lägger till egenskapen AbstractInterruptMonitor.TerminateWithoutException.**

Den här egenskapen anger när ett avbrott har krävts för en process, om processen ska avslutas med ett undantag eller bara avslutas tyst. Som standard är den här egenskapen falsk, det vill säga att processen avslutas av ett undantag när den avbryts.

### **Lägger till WorkbookSettings.ResourceProvider-egenskapen.**

Omdöpt egenskap för WorkbookSettings.StreamProvider för att göra den mer lämpad för sin funktion och lättare för användare att förstå.

### **Lägger till alternativet LoadDataFilterOptions.Revision.**

Vissa mallfiler kan innehålla stora mängder revisionsloggar och som orsakar dålig prestanda för att ladda arbetsboken. Användaren kan använda detta alternativ för att kontrollera om dessa revisionsloggar ska laddas eller inte.

### **Lägger till egenskapen JsonLoadOptions.MultipleWorksheets.**

Anger om varje attribut för JsonObject-objekt importeras som ett kalkylblad när alla underordnade noder är matrisnoder.

### **Lägger till FileFormatType.SqlScript, SaveFormat.SqlScript och SqlScriptSaveOptions**

Representerar alternativen för att spara sql-skript.

### **Lägger till SaveFormat.Xml, LoadFormat.Xml, XmlSaveOptions och XmlLoadOptions**

Representerar alternativen för R/W xml-filer.

### **Lägger till egenskapen HtmlSaveOptions.SaveAsSingleFile.**

 Anger om excel sparas som en enda fil.

### **Lägger till egenskapen JsonLoadOptions.MultipleWorksheets.**

 Anger om data från Json-filen laddas till flera kalkylblad

### **Lägger till egenskapen PdfSaveOptions.Producer.**

 Hämtar och ställer in producent av genererade pdf-dokument.

### **Lägger till metoderna ListColumn.GetCustomTotalsRowFormula() och ListColumn.SetCustomTotalsRowFormula()**

 Hämtar och ställer in den anpassade formeln för totalraden i tabellen.

### **Föråldrad metod SheetRender.GetPageSize(int pageIndex)**

Använd SheetRender.GetPageSizeInch(int pageIndex) istället.

### **Föråldrad WorkbookSettings.StreamProvider-egenskap.**

Använd egenskapen WorkbookSettings.ResourceProvider istället.

### **Tar bort den föråldrade egenskapen PdfSaveOptions.StreamProvider.**

Använd egenskapen WorkbookSettings.ResourceProvider istället.

