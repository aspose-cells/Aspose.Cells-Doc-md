---
title: Filtrering av data
type: docs
weight: 100
url: /sv/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop, filtrera, filtrera data, AutoFilter, RowFilterr
description: Den här artikeln introducerar hur du filtrerar data i arbetsbladet i GridDesktop.
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** erbjuder funktioner för Auto-Filter och Anpassad Datafiltrering för användarna. Med dessa funktioner kan du välja endast de objekt från arbetsbladet som du vill visa i en lista. Dessutom kan du filtrera objekt i en lista enligt en uppsatt kriterier. Du kan filtrera text, nummer eller datum med funktionen Auto-Filter / Anpassad Datafiltrering.

Du kan använda det booleska attributet **EnableAutoFilter** i klassen **RowFilterSettings** för att aktivera funktionen Auto-Filter för GridDesktop-kontrollen. Det finns några andra egenskaper hos klassen som du kan använda, t.ex **HeaderRow**, **StartRow** och **EndRow** för att ange rubrik, start- och slutradindex. Egenskapen **Criteria** används för att ange anpassade filtreringskriterier. Klassen har också en metod med namnet **FilterRows** för att få de filtrerade raderna baserat på de angivna kriterierna.

Attributet "contains" -typ sökattribut (skiftlägesoberoende) i RowFilter stöds också av GridDesktop. Du kan använda egenskapen **IgnoreCase** i klassen **GridColumn** för att ange skiftlägeskänslighetsattributet enligt ditt behov. Du kan också använda en egenskap med namnet **IsStartWithCriteria** i klassen **GridColumn** för att ange om RowFilter använder StartWith-kriteriet för en kolumn; standardvärdet för egenskapen är satt till false.

{{% /alert %}} 
## **Filtrering av data**
Vi implementerar både Auto-Filter och Anpassad Datafiltreringsfunktioner i det här exemplet. Vi fyller några datalistor i GridDesktop, aktiverar Auto-Filter-funktionen och söker sedan filtrerade rader baserat på vissa kriterier.
### **Auto-Filter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Anpassad dataskiktsfiltrering**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
