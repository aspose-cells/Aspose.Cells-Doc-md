---
title: Aspose.Cells for Node.js via Java 21.10 Release Notes
type: docs
weight: 3
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-21-10-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 21.10](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.10/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43768|Java Heap Space-problem observeras vid konvertering av XLSX-fil till PDF|
|CELLSJAVA-43875|Undantag "Ogiltig FontUnderlineType string val" vid laddning av XLSX-filen|
|CELLSJAVA-43876|Undantag "java.lang.ArrayIndexOutOfBoundsException" vid inläsning av en XLSX-fil|
|CELLSJAVA-43646|Skuggeffekten av texten återges inte korrekt|
|CELLSJAVA-43760|Likbent triangelorientering är felaktig|
|CELLSJAVA-43786|När du konverterar XLS-filen till XLSX, renderas vissa delar angående former inte korrekt|
|CELLSJAVA-43838|Efter exekvering av XlsToXlsx försvinner AutoShape|
|CELLSJAVA-43839|Efter exekvering av XlsToXlsx är den vänstra hakparentesen förlorad|
|CELLSJAVA-43842|Efter att ha kört XlsToXlsx skiljer sig formen på LeftBracket från originalet|
|CELLSJAVA-43848|Omvandling av Excel till PDF - vissa WordArt-tecken lindas inte på samma sätt som i Excel-fil|
|CELLSJAVA-43880|Felaktiga rundade hörn i textrutan efter konvertering av xls till xlsx|
|CELLSJAVA-43867|Ikonen för villkorligt format skiljer sig vid export till html|
|CELLSJAVA-43812|excelToHtml: Formpositionsförskjutningen är felaktig|
|CELLSJAVA-43871|Prism 9 OLE-objekt visas inte på utgång PDF|
|CELLSJAVA-43883|Felaktiga renderade sidstorlekar|
|CELLSJAVA-43881|Sammanfogning av filer gör att bakgrundsfärgsinställningen för arken saknas|
|CELLSJAVA-43892|Kanter för Excel som konverterats till HTML saknas|
|CELLSJAVA-43787|Undantag "IllegalArgumentException: bindestreck längder alla noll ..." i Excel till HTML-rendering|
|CELLSJAVA-43885|IllegalArgumentException vid konvertering av Excel|
|CELLSJAVA-43874|Workbook.save kastar ett undantag på en specifik fil med Aspose.Cells endast när Aspose-licensen tillämpas|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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

### **Föråldrad metod SheetRender.GetPageSize(int pageIndex)**

Använd SheetRender.GetPageSizeInch(int pageIndex) istället.

### **Lägger till metod SheetRender.GetPageSizeInch(int pageIndex)**

Få sidstorlek på utdatabilden? i enhet av tum.

### **Lägger till metod WorkbookRender.GetPageSizeInch(int pageIndex)**

Få sidstorlek utdatabild? i enhet av tum.

