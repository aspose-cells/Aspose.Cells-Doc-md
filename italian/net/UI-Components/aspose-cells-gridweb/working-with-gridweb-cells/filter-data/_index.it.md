---
title: Filtrare i dati
type: docs
weight: 80
url: /it/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb, filtro, filtrare i dati, filtraggio dei dati
description: Questo articolo presenta come filtrare i dati in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb fornisce funzionalità di filtro automatico e filtro dati personalizzato. Queste funzionalità ti consentono di selezionare solo gli elementi in un foglio di lavoro che desideri visualizzare in un elenco. Inoltre, puoi filtrare gli elementi in un elenco secondo i criteri impostati. Filtra testi, numeri o date con le funzionalità di filtraggio.

{{% /alert %}} 
## **Lavorare con i filtri**
Usa il metodo AddAutoFilter del foglio di lavoro per abilitare il filtro automatico per un foglio di lavoro. Questo metodo accetta gli indici di riga, inizio e fine colonna.

Per abilitare il filtro personalizzato, utilizzare il metodo AddCustomFilter del foglio di lavoro che accetta l'indice di riga a cui applicare il filtro e i criteri di filtraggio personalizzati.

Nell'esempio sottostante vengono implementati sia i filtri dati automatici che personalizzati. Nell'esempio, la funzione di filtro automatico è abilitata e le righe filtrate vengono cercate in base a determinati criteri.

**Input: l'elenco dei dati nel primo foglio di lavoro** 

![todo:image_alt_text](filter-data_1.jpg)

**Output: abilita la funzione di filtro automatico** 

![todo:image_alt_text](filter-data_2.jpg)
### **Filtro automatico**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Filtro Dati Personalizzato**
**Dati filtrati personalizzati in base ai criteri** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
