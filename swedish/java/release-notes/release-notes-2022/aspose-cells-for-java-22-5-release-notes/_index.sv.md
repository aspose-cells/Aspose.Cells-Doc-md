---
title: Aspose.Cells for Java 22.5 Release Notes
type: docs
weight: 8
url: /sv/java/aspose-cells-for-java-22-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 22.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.5/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44554|Förbättra LightCells-modellen för att ställa in formler|
|CELLSJAVA-44535|implementera fokuscell med vertikal/horisontell rullningslist automatisk rullning till lämplig position|
|CELLSJAVA-44588|Upptäck filformat för stream med lösenord|
|CELLSJAVA-44481|Problem med metoden ThreadedComment.setCreatedTime().|
|CELLSJAVA-44483|Sortering fungerar inte efter gruppering av raderna|
|CELLSJAVA-44522|Dubbelt värde till sträng ger tailing noll vilket är felaktigt när man jämför med ms excels resultat|
|CELLSJAVA-44501| sök nästa nummer efter filen duohangduolie.zip|
|CELLSJAVA-44529|implementera sökning efter freezepan|
|CELLSJAVA-44530|undersöka frågan om setactivecell fungerar inte ibland|
|CELLSJAVA-44534|Grafik i utskriftsområdet exporteras inte i Excel till HTML konvertering|
|CELLSJAVA-44539|Diagrammet flyttas åt höger vid konvertering till html med utskriftsområde|
|CELLSJAVA-44568|Textning med flera rader försvinner förutom den första raden i konverteringen HTML till XLS|
|CELLSJAVA-44512|Diagram saknas vid export av diagram till svg i html|
|CELLSJAVA-44556|Problem med datavisning i datatabellen efter att koordinataxeln är inställd på logaritmisk skala - Excel till HTML/PDF konvertering|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Ändringar för att spara arbetsbok med LightCells**

För att göra formelrelaterade funktioner tillgängliga för LightCells, i gamla versioner behåller vi all formeldata i cellmodell i minnet när vi sparar arbetsbok med LightCells. Detta orsakade missförstånd och missbruk av LightCells för vissa användare. Användaren trodde att cellens formeldata har släppts utanför räckvidden för StartCell(Cell) men faktiskt inte. För de flesta användare som använder LightCells är deras primära oro prestanda (minneskostnad). Få människor kommer att använda formelrelaterade funktioner förutom att ställa in enkel formel till cellen i processen att spara arbetsboken. Så från den här versionen lägger vi till några begränsningar för att ändra cellobjektet inom ramen för metoden StartCell(Cell). Nu är det inte tillåtet att ställa in delade formler, matrisformler för det givna cellobjektet i metoden StartCell(Cell). Om sådan typ av formler behövs, bör användaren ställa in dem innan arbetsboken sparas. Med denna ändring förbättrade vi prestandan för de flesta användare som behöver spara enkla formel för celler till den resulterande kalkylarksfilen med LightCells.

### **Tar bort föråldrad metod Cell.SetAddInFormula()**

Använd WorksheetCollection.RegisterAddInFunction() och Cell.Formula/Cell.SetFormula() istället.

### **Lägger till ExceptionType.FileCorrupted enum**

Representerar typen av undantag där filen är skadad.

### **Lägger till WarningType.Limitation enum**

Representerar varningstypen är begränsningen av Excel.

### **Lägger till metoden ShapeGuideCollection.Add(strängnamn, dubbelvärde).**

Lägger till en formguide.

