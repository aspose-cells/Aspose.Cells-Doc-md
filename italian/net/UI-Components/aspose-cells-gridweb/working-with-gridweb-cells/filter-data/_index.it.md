---
title: Filtra dati
type: docs
weight: 80
url: /it/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb fornisce funzionalità di filtro automatico e filtro dati personalizzato. Queste funzionalità ti danno un modo per selezionare solo gli elementi in un foglio di lavoro che desideri visualizzare in un elenco. Inoltre, puoi filtrare gli elementi in un elenco in base a criteri impostati. Filtra testo, numeri o date con le funzioni di filtro.

{{% /alert %}} 
## **Lavorare con i filtri**
Usare il metodo AddAutoFilter del foglio di lavoro per abilitare il filtro automatico per un foglio di lavoro. Questo metodo accetta gli indici di riga, inizio e fine colonna.

Per abilitare il filtro personalizzato, utilizzare il metodo AddCustomFilter del foglio di lavoro che accetta l'indice di riga a cui deve essere applicato il filtro ei criteri di filtro personalizzati.

L'esempio seguente implementa filtri di dati sia automatici che personalizzati. Nell'esempio, la funzione di filtro automatico è abilitata e le righe filtrate vengono cercate in base ad alcuni criteri.

**Input: l'elenco dei dati nel primo foglio di lavoro** 

![cose da fare:immagine_alt_testo](filter-data_1.jpg)

**Output: abilita la funzione di filtro automatico** 

![cose da fare:immagine_alt_testo](filter-data_2.jpg)
### **Filtro automatico**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Filtro dati personalizzato**
**Dati filtrati personalizzati in base ai criteri** 

![cose da fare:immagine_alt_testo](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
