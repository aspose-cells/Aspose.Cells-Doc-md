---
title: Filtrera data
type: docs
weight: 80
url: /sv/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb, filtrera, filtrera data, dataskiktar
description: Den här artikeln introducerar hur man filtrerar data i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb erbjuder automatisk filtrering och anpassade dataskiktsfunktioner. Dessa funktioner ger dig en möjlighet att välja endast de objekt i ett kalkylblad som du vill visa i en lista. Dessutom kan du filtrera objekt i en lista enligt angivna kriterier. Filtrera text, nummer eller datum med filtreringsfunktionerna.

{{% /alert %}} 
## **Arbeta med filtrar**
Använd arbetsbladets AddAutoFilter-metod för att aktivera automatisk filtrering för ett arbetsblad. Denna metod accepterar rad-, start- och slutkolumnindex.

För att aktivera anpassad filtrering, använd arbetsbladets AddCustomFilter-metod som accepterar radindex till vilken filtreringen ska tillämpas och de anpassade filtreringskriterierna.

Exemplet nedan implementerar både automatisk och anpassad dataskiktsfiltrering. I exemplet är den automatiska filtreringsfunktionen aktiverad och de filtrerade raderna söks baserat på vissa kriterier.

**Indata: datalistan i det första arbetsbladet** 

![todo:image_alt_text](filter-data_1.jpg)

**Utdata: aktivera automatisk filtreringsfunktion** 

![todo:image_alt_text](filter-data_2.jpg)
### **Automatisk filtrering**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Anpassad dataskiktsfiltrering**
**Anpassad filtrerad data baserat på kriterierna** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
