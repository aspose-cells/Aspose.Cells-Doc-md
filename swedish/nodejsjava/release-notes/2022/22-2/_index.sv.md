---
title: Aspose.Cells för Node.js via Java 22.2 Release Notes
type: docs
weight: 11
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-22-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Node.js via Java 22.2](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.2/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44317|Texten i denna xlsx är förvrängd|
|CELLSJAVA-44271|När du konverterar Excel till PDF skiftar utdatapositionen jämfört med fallet med manuell konvertering|
|CELLSJAVA-44197|När du konverterar XLSX till PDF visas inte pivottabellens tidslinjeform (fönster).|
|CELLSJAVA-44267|Arbetsbok som innehåller en pivottabell blir skadad|
|CELLSJAVA-44114|XLSX till PDF: Data i vetenskapligt nummerformat från XLSX-filen matchar inte data i utdata-PDF-filen|
|CELLSJAVA-44293|Återsparad Excel-fil måste återställas när den öppnas i MS Excel|
|CELLSJAVA-43194|Bilderna visas felaktigt|
|CELLSJAVA-44243|GridWeb spring demo spara fil misslyckades i jdk1.8|
|CELLSJAVA-44276|radhuvudets höjd överensstämmer inte med radinnehållet efter redigeringscellen för filen 249.xls|
|CELLSJAVA-44284|öka minnesundantaget för filen bug.xlsx|
|CELLSJAVA-44229|Formel går förlorad när td-innehåll lindas med div-tagg|
|CELLSJAVA-44247|En rad text lindas under konvertering till pdf|
|CELLSJAVA-44175| problem med överlappande Donut Chart-etiketter|
|CELLSJAVA-44192| Kategoriaxelns objektnamn i grafen är avskuret i Excel till PDF-konvertering|
|CELLSJAVA-44233|Oändlig loop vid konvertering av XLSX-fil|
|CELLSJAVA-44263|Att ställa in riktningen för kartetiketttexten till vertikalt träder inte i kraft|
|CELLSJAVA-44268| Undantag "java.lang.NullPointerException" på Chart.toPdf-metoden|
|CELLSJAVA-44302|Textriktningen för koordinataxeln är fel efter att Excel-filen konverterats till HTML|
|CELLSJAVA-44314|Fel axeletiketter för diagramkategori i diagram till bild-rendering|
|CELLSJAVA-44274|Stöds SVG-format för läsning eller rendering till PDF|
|CELLSJAVA-44311|Undantag "java.lang.OutOfMemoryError: Java heap space" vid rendering till HTML-filformat|
|CELLSJAVA-44285|Undantag "java.lang.ClassCastException: com.aspose.cells.n2f kan inte castas till com.aspose.cells.o90" när Workbook.calculateFormula() anropas|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Föråldrad Cells.AddAddInFunction()-metoden.**

Använd metoderna WorksheetCollection.RegisterAddInFunction() istället.

### **Lägger till metoden NameCollection.Filter() och NameScopeType enum.**

Hämtar de definierade namnen efter omfattning.

### **Lägger till MsoDrawingType.Timeline enum.**

Representerar typ av tidslinjeritningsobjekt.

