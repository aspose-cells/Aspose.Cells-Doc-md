---
title: Aspose.Cells för Java 22.11 Release Notes
type: docs
weight: 2
url: /sv/java/aspose-cells-for-java-22-11-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 22.11](https://releases.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.11/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44888|"+" och "-" försvann efter konvertering - Excel till HTML-rendering|
|CELLSJAVA-44775|Diagrametiketter överlappade i diagram till bildrendering|
|CELLSJAVA-44882|Tabell-till-bild-rendering - En av etiketterna finns inuti munkdiagrammet|
|CELLSJAVA-44943|XLSX till PDF: Diagrametiketter renderade inte korrekt|
|CELLSJAVA-44928|XLS till PDF: Otillräcklig data för en bild|
|CELLSJAVA-44910|Konvertera Excel till HTML resulterar i tusentals liknande små bilder|
|CELLSJAVA-44944|Ändra storlek på tabeller ändra formateringen av celler|
|CELLSJAVA-44948| Bilder kan inte visas i arket när HTML konverteras till Excel|
|CELLSJAVA-44908|Undantag "java.lang.OutOfMemoryError: Java heap space" vid laddning av stora XLSB-filer|
|CELLSJAVA-44929|Regression: "java.lang.NullPointerException" på Workbook.calculateFormula()|
|CELLSJAVA-44927|Undantag "java.lang.IndexOutOfBoundsException: Index: 5, Storlek: 5" vid konvertering av Excel-fil till HTML|
|CELLSJAVA-44939|Fel "java.lang.StringIndexOutOfBoundsException: Strängindex utanför intervallet: 0" vid försök att läsa en Excel-fil|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till egenskapen Cell.IsDynamicArrayFormula**

Anger om cellens formel är dynamisk matrisformel (sant) eller äldre matrisformel (falsk).

### **Föråldrade egendomen SparklineGroup.SparklineCollection och lägger till egendomen SparklineGroup.Sparklines**

Använd egenskapen SparklineGroup.Sparklines istället.

### **Föråldrade egendomen Worksheet.SparklineGroupCollection och lägger till egenskapen Worksheet.SparklineGroups**

Använd egenskapen Worksheet.SparklineGroups istället.