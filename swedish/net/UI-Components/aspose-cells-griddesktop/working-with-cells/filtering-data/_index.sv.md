---
title: Filtrera data
type: docs
weight: 100
url: /sv/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** tillhandahåller Auto-Filter och Custom Data Filter-funktioner för användarna. Genom att använda dessa funktioner kan du hitta ett sätt att bara välja de objekt från kalkylbladet som du vill visa i en lista. Dessutom har du rätt att filtrera objekt i en lista enligt ett fastställt villkor. Du kan filtrera text, siffror eller datum med Auto-Filter / Custom Data Filter-funktionen.

 Du kan använda**Aktivera AutoFilter** Boolean attribut för**RowFilterSettings** klass för att aktivera Auto-Filter-funktionen för GridDesktop-kontrollen. Det finns några andra egenskaper för klassen som du kan använda, t.ex**HeaderRow** , **StartRow** och**EndRow**för att ange rubrik, start- och slutradindex. De**Kriterier** egenskapen används för att ställa in de anpassade filtreringskriterierna. Klassen har också en metod som heter**Filterrader** för att få de filtrerade raderna baserat på de givna kriterierna.

 Sökattributet "innehåller" (skiftlägeskänsligt) i RowFilter stöds också av GridDesktop. Du kan använda**Ignorera fall** egendom av**GridColumn** klass för att ange attributet skiftlägeskänslighet för ditt behov. Du kan också använda en egendom som heter**IsStartWithCriteria** av**GridColumn** klass för att indikera om RowFilter använder StartWith-kriterierna på en kolumn; standardvärdet för egenskapen är inställt på false.

{{% /alert %}} 
## **Filtrera data**
Vi implementerar både Auto-Filter och Custom Data Filter-funktioner i det här exemplet. Vi fyller i en datalista i GridDesktop, aktiverar Auto-Filter-funktionen och söker sedan efter filtrerade rader baserat på vissa kriterier.
### **Auto-Filter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Anpassat datafilter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
