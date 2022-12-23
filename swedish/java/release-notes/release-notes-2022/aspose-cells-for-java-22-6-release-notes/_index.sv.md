---
title: Aspose.Cells for Java 22.6 Release Notes
type: docs
weight: 7
url: /sv/java/aspose-cells-for-java-22-6-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 22.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.6/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44632|Stöder formatering av hela dataraden i pivottabellen|
|CELLSJAVA-44611|Förbättring för att läsa tomma celler från xlsx-fil|
|CELLSJAVA-44616|Ursprungliga inställningar för villkorlig formatering i destinationsområdet bör tas bort vid kopiering av intervall|
|CELLSJAVA-44658|Stöd BouncyCastle v1.71|
|CELLSJAVA-44628|Hur man behåller procentformat för vissa pivotrader när man expanderar noddata för en pivotkolumn/-fält|
|CELLSJAVA-44483|Sortering fungerar inte efter gruppering av raderna|
|CELLSJAVA-44609|Långsam kopiering med villkorlig formatering med nyare version|
|CELLSJAVA-44622|När du sorterar stora grupper med flera nycklar, kastar den "java.lang.ArrayIndexOutOfBoundsException"|
|CELLSJAVA-44630|Problem med Smart Markers-funktionen sedan Aspose Cells 22.5|
|CELLSJAVA-44646|Rensa innehåll på kopierade ark kastar NullPointerException|
|CELLSJAVA-44656|Cells.getMaxDataColumn returnerar ett annat (fel) värde i 22.5|
|CELLSJAVA-44650|Excel-dokumentsidan är rörig när den laddas in i Aspose.Cells.GridWeb(Java)|
|CELLSJAVA-44660|Problem med datajustering när du laddar XLS till Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44661|Problem när du laddar et-filen till Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44584|Titeln på axeln i diagrammet roteras i utdatabilden - Konvertering av diagram till bild|
|CELLSJAVA-44615|Grå linje ritad i utdatabilden från filen XLS|
|CELLSJAVA-44665|Laddar ODS filen hänger sig|
|CELLSJAVA-44651|Felet "Inte ett numeriskt värde" vid konvertering av Excel-ark till HTML/PDF|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till klassen CellsDataTableFactory**

Den här klassen tillhandahåller api för att skapa instanser av ICellsDataTable från anpassade objekt för användarens bekvämlighet.

### **Lägger till egenskapen Workbook.CellsDataTableFactory**

Ge användaren CellsDataTableFactory för att skapa en instans av ICellsDataTable från anpassade objekt.

### **Lägger till metoden Cell.GetDependentsInCalculation(bool)**

Enligt nuvarande beräkningskedja, få alla celler vars beräknade resultat beror på denna cell.

### **Lägger till metoden Cell.GetPrecedentsInCalculation()**

Enligt nuvarande beräkningskedja, hämta alla prejudikat (referens till celler i aktuell arbetsbok) som används av denna cells formel när du beräknar den.

### **Föråldrade metoderna Cell.GetLeafs() och Cell.GetLeafs(bool)**

Använd metoden Cell.GetDependentsInCalculation(bool) istället.

### **Lägger till metoden PivotTable.FormatRow(int row, Style style).**

Formatera raddata i det vridbara området.

### **Lägger till egenskapen Shapes.CreateId**

Får skapande id för formen.

### **Lägger till WarningType.InvalidData enum**

Representerar den ogiltiga datatypen.

### **Lägger till överbelastningsmetoden ChartCollection.Add().**

Lägger till ett diagram med datakälla.

### **Lägger till metoden Chart.GetActualSize().**

Hämtar den faktiska storleken på diagrammet i pixelenhet.

### **Föråldrade egenskapen Chart.ActualChartSize**

Använd metoden Chart.GetActualSize() istället.

### **Föråldrade egenskapen PdfSaveOptions.ImageType**

Diagram och Shape renderas alltid som vektorelement (t.ex. punkt, linje) för renderingskvalitet.

### **Föråldrade egenskapen ImageOrPrintOptions.ChartImageType**

Diagram och Shape renderas alltid som vektorelement (t.ex. punkt, linje) för renderingskvalitet.

### **Tar bort föråldrad egenskap ImageOrPrintOptions.ImageFormat-egenskap**

Använd egenskapen ImageOrPrintOptions.ImageType istället.

### **Tar bort föråldrad egenskap ImageOrPrintOptions.IsImageFitToPage-egenskapen**

Fastigheten är värdelös.