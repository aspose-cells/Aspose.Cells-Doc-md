---
title: Aspose.Cells för Java 21.8 Release Notes
type: docs
weight: 5
url: /sv/java/aspose-cells-for-java-21-8-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 21.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.8/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42494|En stor mängd oanvända stilar genereras i CSS-sektionen|
|CELLSJAVA-43576|Grafiska textvärden visas inte vid konvertering av XLSX till PDF|
|CELLSJAVA-43483|Text efter en "br"-tagg i en "em"-tagg framhävs inte när ett HTML-dokument konverteras till en arbetsbok|
|CELLSJAVA-43526|IllegalArgumentException: Ogiltigt kolumnindex|
|CELLSJAVA-43557|Felaktig färg när du sparar som html|
|CELLSJAVA-43567|Regression: MDURATION-formeln har inte beräknats korrekt|
|CELLSJAVA-43583|Power operator "^" fungerar inte för formelberäkningar|
|CELLSJAVA-43549|Bild saknas i utdata-PDF|
|CELLSJAVA-43566|Standardteckensnitt på MacOS Big Sur|
|CELLSJAVA-42579|Axeletiketter visas inte korrekt - Högerjustering saknas när Excel sparas till Pdf|
|CELLSJAVA-43554|Text i diagramdatatabellen visas inte i utdatabilden|
|CELLSJAVA-43556|XLSX till PDF: Ofullständig diagramtitel|
|CELLSJAVA-40051|Apple iWork-support|
|CELLSJAVA-43119|Konvertering till PDF - Filformat nummer 3.5 stöds inte sedan 2014|
|CELLSJAVA-43538|Diagram utan data gör att XLSX blir korrupt efter att ha sparats med Aspose Cells|
|CELLSJAVA-43547|AutoFitRow ändrar kalkylbladets standardhöjd|
|CELLSJAVA-43591|Fel när filen öppnas i MS Excel sparad av Aspose.Cells|
|CELLSJAVA-43523|CellsException för att läsa formens makronamn: Ogiltig formel|
|CELLSJAVA-43565|"java.lang.ClassCastException" vid läsning av XLSB-fil med LightCells|
|CELLSJAVA-43546|NullPointerException vid extrahering av serienamn på diagram|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till klassen AbstractInterruptMonitor.**

Tillhandahåller AbstractInterruptMonitor som bas för implementeringar för avbrottsövervakning. Klassen InterruptMonitor blir nu en implementering av den. Typen av InterruptMonitor-egenskaper för LoadOptions och Workbook blir nu också AbstractInterruptMonitor så att användaren kan använda sin egen implementering för att styra de tidskrävande operationerna.

### **Lägger till egenskapen HtmlSaveOptions.WorksheetScalable.**

Indikerar om zooma in eller ut html via kalkylblads zoomnivå när du sparar fil till html, standardvärdet är falskt.

### **Lägger till åsidosättande WorksheetCollection.GetRangeByName()-metoden.**

Hämtar Range-objekt efter namn från definierade namn eller tabeller.

### **Lägger till metoden Range.AutoFill().**

Fyller automatiskt data till intervallet.

### **Lägger till WarningType.IO enum.**

Representerar varningen för skadad fil.
