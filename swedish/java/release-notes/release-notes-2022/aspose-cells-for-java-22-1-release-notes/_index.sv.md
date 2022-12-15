---
title: Aspose.Cells for Java 22.1 Release Notes
type: docs
weight: 12
url: /sv/java/aspose-cells-for-java-22-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 22.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.1/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44162|Stöd för att ta bort extern länk utan att ta bort formlerna|
|CELLSJAVA-44214|Stöd för att autopassa rader för GridWeb|
|CELLSJAVA-44205|Stöd platsberoende enhetstext för koordinataxlar i diagrammet|
|CELLSJAVA-44238|Stöd för att behålla sessionen efter omstart av servern för GridWeb|
|CELLSJAVA-44126|Cell.getDependents() kastar undantag om cellens formel inte har analyserats|
|CELLSJAVA-44161|Fel i extern formel när du importerar en arbetsbok till en annan arbetsbok|
|CELLSJAVA-44130|Texten på dataetiketterna lindas in i utdatadiagrambilden|
|CELLSJAVA-44204|pagineringsproblem för csv|
|CELLSJAVA-43934|Cirkeldiagrametiketterna matchas inte med Excel efter manipulering eller uppdatering av diagram|
|CELLSJAVA-44122|Vid export av HTML skiljer sig dataetiketterna från Excel|
|CELLSJAVA-41949| Innehållet återges annorlunda när du sparar arbetsbok i XLSX- och HTML-format|
|CELLSJAVA-44207|Vid export till HTML blir radhöjden högre|
|CELLSJAVA-44233|Oändlig loop vid konvertering av XLSX-fil|
|CELLSJAVA-44234|Fel på minnet för filen data.xls|
|CELLSJAVA-44246|Undantag "Invalid endrow index" för tom fil|
|CELLSJAVA-44258| Null pekare undantag för fil|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Ändrar beteende för att ta bort externa länkar från arbetsboken.**

I gamla versioner tar vi inte bort den externa länken vars url innehåller "AddIns". Sådant beteende är utformat för vissa användares speciella krav. Defekten med en sådan lösning är uppenbar: användare kan ange vilket giltigt filnamn eller sökväg som helst för de externa referenserna och i själva verket vill de flesta inte att de externa länkarna ska behandlas annorlunda. Från den här versionen filtrerar vi inte längre dessa externa länkar. Om användare har särskilda krav på vissa externa länkar, kan de kontrollera alla objekt i ExternalLinkCollection en efter en och bara ta bort de som de vill ta bort (med ExternalLinkCollection.RemoveAt(int)-metoden).

### **Ändrar beteende för Cell. Typ för ogiltigt datum och tid.**

I gamla versioner, om en cell begärs att formateras som datum och tid, returnerar Cell.Type CellValueType.IsDateTime oavsett om det numeriska värdet för denna cell är giltigt för datum och tid eller inte. Detta kan orsaka undantag om användare är beroende av Cell.Skriv endast och försöker ringa Cell.DateTimeValue. Från den här versionen returnerar vi CellValueType.IsNumeric för sådana typer av celler så att användaren kan vägledas att få cellvärdet med korrekt API.

### **Ändrar beteende för Cells.MaxDisplayRange.**

I gamla versioner täcker intervallvärdet för den här egenskapen alla celler som har instansierats i cellsamlingen. Från denna version gör vi att de osynliga raderna/kolumnerna exkluderas från kanterna på visningsområdet om det bara finns instansierade celler i dessa rader/kolumner.

### **Ändrar DataSorter.Sort()-metoder för att returnera de ursprungliga indexen för sorterade rader/kolumner.**

gamla versioner? DataSorter.Sort() metoder returnerar ingenting. Från denna version returnerar vi de ursprungliga indexen för rader/kolumner som motsvarar intervallet som har sorterats. Detta ger användaren möjlighet att utföra avancerad kontroll och operationer för sorteringen.

### **Lägger till egenskapen TxtLoadOptions.ExtendToNextSheet.**

Stöder import av CSV/TSV-data till flera kalkylblad om radantalet eller kolumnantal data överskrider ms excels gräns.

### **Lägger till metoden ExternalLinkCollection.Clear().**

Tar bort alla externa länkar från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.Clear(bool updateReferencesAsLocal).**

När du tar bort alla externa länkar från arbetsboken kan användaren bestämma hur man ska göra med formlerna som har referenser till dessa externa länkar. Om "updateReferencesAsLocal" är sant, kommer alla anpassade definierade funktioner i de externa länkarna att flyttas till den aktuella arbetsboken. Till exempel är en cells formel "='externalsource.xlam'!customfunction()", efter att den externa länken "externalsource.xlam" har tagits bort, kommer denna cells formel att bli "=customfunction()".

### **Lägger till ExternalLinkCollection.RemoveAt(int)-metoden.**

Tar bort en angiven extern länk från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.RemoveAt(int, bool updateReferencesAsLocal).**

I likhet med metoden ExternalLinkCollection.Clear(bool updateReferencesAsLocal) kan användaren bestämma hur formler som refererar till den angivna externa länken ska göras samtidigt som den tas bort från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.GetEnumerator().**

Tillhandahåller en enumerator för att iterera genom alla externa länkar i arbetsboken.

### **Föråldrade Workbook.RemoveExternalLinks()-metoden.**

Använd metoden ExternalLinkCollection.Clear() istället.

### **Obsoletes Workbook.HasExernalLinks()-metoden.**

Använd ExternalLinkCollection.Count för att kontrollera om det finns externa länkar i arbetsboken.

### **Tar bort föråldrad klass StyleCollection.**

Använd Workbook.CreateStyle() och Workbook.GetNamedStyle(sträng) för att manipulera stilar.

### **Lägger till konstruktorn PptxSaveOptions(bool saveAsImage).**

Representerar alternativ för att spara .pptx-fil. Om det är sant kommer arbetsboken att konverteras till några bilder av .pptx-filen. Om False, kommer arbetsboken att konverteras till vissa tabeller av .pptx-fil.

### **Lägger till klassen ChartGlobalizationSettings.**

 Representerar globaliseringsinställningarna för diagram.

### **Lägger till egenskapen DataLabels.IsNeverOverlap.**

Indikerar om dataetiketterna aldrig överlappar varandra. (För cirkeldiagram)

### **Lägger till TickLabelItem-klassen.**

Inkludera information om ett Ticklabel-objekt.

### **Lägger till egenskapen TickLabelItem.Height.**

Får höjden på Ticklabel-objektet i förhållande till diagramhöjden.

### **Lägger till egenskapen TickLabelItem.Width.**

Får bredden på Ticklabel-objektet i förhållande till diagrambredden.

### **Lägger till egenskapen TickLabelItem.X.**

Får X av Ticklabel-objekt i förhållande till diagrambredd.

### **Lägger till egenskapen TickLabelItem.Y.**

Får Y av Ticklabel-objekt i förhållande till diagramhöjd.

### **Lägger till egenskapen TickLabels.TickLabelItems.**

Får föremålen från TickLabel.

