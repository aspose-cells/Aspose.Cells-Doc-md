---
title: Aspose.Cells for Java 18.2 Release Notes
type: docs
weight: 110
url: /sv/java/aspose-cells-for-java-18-2-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.2.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42509|Lägg till konstanten LoadDataFilterOptions.NAMES för att filtrera definierade namn när arbetsboken laddas|Ny funktion|
|CELLSJAVA-42510|Observera mycket långsam filtrering i Microsoft Excel 2013 och 2016 när filtret används|Förbättring|
|CELLSJAVA-42497|Ark1-former försvinner och stjärnor i Ark2 är rundade|Insekt|
|CELLSJAVA-42512|Ogiltig kodning - Undantag inträffar när Excel-filen laddas|Insekt|
|CELLSJAVA-42507|Makro- och dialogblad upptäcks som vanliga kalkylblad|Insekt|
|CELLSJAVA-42503|MS Excel tillåter inte att XLS-filen sparas igen|Insekt|
|CELLSJAVA-42502|Aspose.Cells filtrerar inte data korrekt istället döljer det alla rader|Insekt|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till LoadDataFilterOptions.DefinedNames enum**
Anger om definierade namnobjekt laddas när mallfilen laddas.
### **Ändrar beteendet för LoadDataFilterOptions.Formula enum**
äldre versioner laddar vi alltid definierade namnobjekt när vi laddar formler. Nu tillhandahåller vi separat enum för definierade Name-objekt explicit, så Formel Enum kommer bara att beteckna att formler ska laddas nu, oavsett vilka definierade Name-objekt kommer att laddas eller inte. En sak bör dock noteras, vanligen definierade namnobjekt används av formler, om användaren bara laddar formler och inte laddar de definierade namnobjekten, kommer cellformeln som refererar till dessa namn att bli skadad och kan orsaka undantag. Så, i allmänhet, om användaren vill ladda formler, bör de definierade namnobjekten också laddas. Men användaren kan bara ladda definierade namnobjekt utan att ladda formler.
### **Lägg till SheetType.Dialog enum**
Representerar dialogblad.
### **Lägger till egenskapen WorkbookSettings.MaxRowsOfSharedFormula**
Hämtar och ställer in det maximala radnumret för delad formel. Den delade formeln delas upp i flera delade formler om det totala antalet rader av delade formeln är större än det.
### **Lägger till WorkbookSettings.StreamProvider-egenskapen**
Hämtar och ställer in strömleverantören för extern resurs.
### **Lägger till egenskapen ShapeTextAlignment.IsAutoMargin**
Indikerar om marginalen på textramen är atuomatisk.
### **Lägger till egenskapen ImportTableOptions.IsFormulas**
Representerar vilken kolumn i datatabellen som ska importeras som formler.
