---
title: Filtrera data
type: docs
weight: 80
url: /sv/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tillhandahåller autofilter och anpassade datafilterfunktioner. Dessa funktioner ger dig ett sätt att välja endast de objekt i ett kalkylblad som du vill visa i en lista. Dessutom kan du filtrera objekt i en lista enligt fastställda kriterier. Filtrera text, siffror eller datum med filtreringsfunktionerna.

{{% /alert %}} 
## **Arbeta med filter**
Använd kalkylbladet AddAutoFilter-metoden för att aktivera autofiltrering för ett kalkylblad. Denna metod accepterar rad-, start- och slutkolumnindex.

För att aktivera anpassat filter, använd kalkylbladet AddCustomFilter-metoden som accepterar radindexet som filtret måste tillämpas på och de anpassade filtreringskriterierna.

Exemplet nedan implementerar både automatiska och anpassade datafilter. I exemplet är autofiltreringsfunktionen aktiverad och filtrerade rader söks utifrån vissa kriterier.

**Inmatning: datalistan i det första kalkylbladet** 

![todo:image_alt_text](filter-data_1.jpg)

**Utgång: aktivera autofilterfunktionen** 

![todo:image_alt_text](filter-data_2.jpg)
### **Auto-filter**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Anpassat datafilter**
**Anpassad filtrerad data baserat på kriterierna** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
