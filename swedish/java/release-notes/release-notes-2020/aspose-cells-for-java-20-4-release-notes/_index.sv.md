---
title: Aspose.Cells for Java 20.4 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-20-4-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 20.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.4/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43153|Visa vattenfallsdiagramförklaring på turkiska liknande MS Excel|Förbättring|
|CELLSJAVA-43142|Excel till HTML-rendering - vissa celler är inte justerade efter konvertering|Insekt|
|CELLSJAVA-43155|Roterad text sätts ut från cellen när den renderas som HTML|Insekt|
|CELLSJAVA-43161|Felaktig återgivning av ekvationen|Insekt|
|CELLSJAVA-43130|Problem med transparens för vattenfallsdiagram|Insekt|
|CELLSJAVA-43131|Excel till PDF - Former med text som inte konverterats korrekt|Insekt|
|CELLSJAVA-43133|Chart.toImage inkluderar inte dataetiketter i utdatabilden|Insekt|
|CELLSJAVA-43138|Bild genererad med renderingsproblem.|Insekt|
|CELLSJAVA-43151|Stiländringar efter konvertering av XLS-filen|Insekt|
|CELLSJAVA-43158|IllegalArgumentException: Kartstorlek(0) måste vara >= 1|Undantag|
|CELLSJAVA-43149|Undantag uppstod när du sparade XLSM efter att kalkylbladet tagits bort|Undantag|
|CELLSJAVA-43150|Undantag "java.lang.NumberFormatException" vid filladdning|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskapen ChartTextFrame.DirectionType.**
Hämtar och ställer in textens riktning i diagrammet.
### **Lägger till ChartTextFrame.ReadingOrder och föråldrar egenskapen ChartTextFrame.TextDirection.**
Använd egenskapen ChartTextFrame.ReadingOrder istället.
### **Lägger till klasser för den förbättrade funktionen i Revisions.**
Får information om revisionen.
### **Ändrar standardvärdet för egenskapen TxtSaveOptions.TrimLeadingBlankRowAndColumn.**
För att göra standardbeteendet för att spara CSV lika med ms excel, ändrade vi standardvärdet och beteendet för den här egenskapen. För gamla versioner var dess standardvärde "false". Från 20.4 blir dess standardvärde "sant".
### **Ändrar beteendet för att upptäcka tomma rader/kolumner för att spara CSV.**
För gamla versioner tog vi de rader/kolumner som inte har några data men har anpassade inställningar (synlighet, formatering, ... etc.) som tomma. Från 20.4 tar vi dem inte längre som tomma, det nya beteendet är detsamma med ms excel.
### **Lägger till egenskapen TxtSaveOptions.ExportArea.**
Anger intervallet av celldata som ska exporteras. Användare kan använda detta alternativ för att få samma resultat med gamla versioner för det ändrade beteendet för TxtSaveOptions.TrimLeadingBlankRowAndColumn och tomma rader/kolumner.
### **Lägger till UnionRange-klass.**
Representerar fackligt utbud.
### **Tar bort föråldrad DrawObject.Image-egenskap.**
Använd egenskapen DrawObject.ImageBytes istället.
### **Lägger till egenskapen Bullet.FontName**
Hämtar och ställer in teckensnittsnamnet på kulan.
### **Lägger till metoden WorksheetCollection.CreateUnionRange().**
Det skapar ett fackligt utbud.
### **Tar bort föråldrad SaveType-enum.**
Den är oanvänd.
### **Tar bort föråldrade egenskaper för OleObject.ImageFormat och Picture.ImageFormat.**
Använd egenskaperna OleObject.ImageType och Picture.ImageType istället.
