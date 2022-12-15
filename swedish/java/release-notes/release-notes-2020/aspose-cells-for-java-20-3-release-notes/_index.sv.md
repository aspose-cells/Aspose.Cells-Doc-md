---
title: Aspose.Cells for Java 20.3 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-20-3-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 20.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.3/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43137|Light Cells API: bearbetar ark i en specifik ordning|Ny funktion|
|CELLSJAVA-43135|Ta bort ActiveXControl från bildformen|Ny funktion|
|CELLSJAVA-43141|Lägg till egenskapen ThreadedComment.CreatedTime|Ny funktion|
|CELLSJAVA-42068|GIF i kalkylbladet är fel när arbetsboken konverteras till HTML|Insekt|
|CELLSJAVA-43127|Excel-pivottabellen uppdateras inte automatiskt när filen först öppnas|Insekt|
|CELLSJAVA-43129|Kinesisk text är förvanskad i HTML till XLS-konvertering|Insekt|
|CELLSJAVA-43139|Diagrammen i bladet uppdateras inte när kalkylblad renderas till bild|Insekt|
|CELLSJAVA-43148|Kartetikettens positionsfel|Insekt|
|CELLSJAVA-43124|Vid konvertering till PDF skärs två kolumner bort från tabellen|Insekt|
|CELLSJAVA-43091|Dataetiketter på Donuts-diagrammet överlappas i PDF-filen|Insekt|
|CELLSJAVA-43132|Dataetiketter saknas i vissa diagram vid export av diagram till bild|Insekt|
|CELLSJAVA-43143|Efter WorkbookDesigner.process, diagramutdata null i HTML|Insekt|
|CELLSJAVA-43098|Att ersätta inbäddat objekt med en bild fungerar inte för XLS-filformat|Insekt|
|CELLSJAVA-43122|Ett problem med ordning av trådade kommentarer efter import till Office365 XLSX-filformat|Insekt|
|CELLSJAVA-43134|Strängvärdet för en cell är tomt i Apple Numbers'09|Insekt|
|CELLSJAVA-43144|IsItalic-egenskapen har upptäckts på ett annat sätt än MS Excel (Java)|Insekt|
|CELLSJAVA-43140|IllegalArgumentException vid anrop av calculateFormula()|Undantag|
|CELLSJAVA-43110|Konvertering till PDF - java.lang.NullPointerException|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägg till egenskapen LoadFilter.SheetsInLoadingOrder**
Användare kan åsidosätta den här egenskapen för att ange arken och ordningen som ska laddas när de importerar arbetsböcker från mallfiler.
### **Tar bort föråldrad TickLabels.Background-egenskap**
Använd egenskapen TickLabels.BackgroundMode istället.
### **Föråldrar egenskapen TickLabels.TextDirection och lägger till egenskapen TickLabels.ReadingOrder**
Använd egenskapen TickLabels.ReadingOrder istället.
### **Föråldrade TickLabels.DirectionTypeproperty och lägger till enum ChartTextDirectionType**
Representerar textens riktning.
### **Lägger till metoden Shape.RemoveActiveXControl().**
Tar bort ActiveX-data från formen.
### **Lägger till egenskapen ThreadedComment.CreatedTime.**
Hämtar och ställer in skapad tid för trådade kommentarer.
### **Lägger till egenskapen Worksheet.UniqueId.**
Hämtar och ställer in det unika ID:t för kalkylbladet.
### **Lägger till enum IconSetType.ColorSmilies3 och IconSetType.Smilies3.**
Representerar 3smiles-ikonuppsättningens villkorliga formatering. Endast för .ods file.s
### **Lägger till enum TimePeriodType.LastYear,TimePeriodType.NextYear och ThisYear.**
Representerar det senaste året, nästa år och i år villkorlig formatering. Endast för .ods-filer.
### **Lägger till metoden WorksheetCollection.RefreshPivotTables().**
Uppdaterar alla pivottabeller i filen.
