---
title: Ordina i dati del foglio di lavoro
type: docs
weight: 80
url: /it/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb, sort
description: Questo articolo illustra come ordinare i dati in GridWeb.
---

{{% alert color="primary" %}} 

L'ordinamento è una funzionalità molto preziosa quando si tratta di elaborazione dati. I dati non ordinati sono un problema per gli utenti quando cercano informazioni specifiche. Aspose.Cells.GridWeb supporta potenti funzionalità di ordinamento. Questo argomento discute l'ordinamento dei dati utilizzando l'API Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Ordinamento dati**
Aspose.Cells.GridWeb consente ai programmatori di ordinare i dati in orizzontale e verticale in modo che sia possibile ordinare i dati dall'alto verso il basso o da sinistra a destra.
### **Dall'alto al basso**
Per ordinare i dati in orientamento dall'alto al basso:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina il range di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare l'orientamento dall'alto verso il basso.

Nell'esempio seguente vengono ordinati i dati di quattro colonne di un foglio di lavoro in ordine decrescente. Solo venti righe delle quattro colonne sono ordinate dall'alto verso il basso.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

![todo:image_alt_text](sort-worksheet-data_1.png)

Dopo l'esecuzione del codice, i dati sono ordinati in ordine crescente.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Da sinistra a destra**
Per ordinare i dati da sinistra a destra:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina il range di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare da sinistra a destra.

Nell'esempio seguente vengono ordinati i dati di quattro righe in ordine crescente. Solo quattro righe di sette colonne sono ordinate da sinistra a destra.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

![todo:image_alt_text](sort-worksheet-data_3.png)

Dopo l'esecuzione del codice, i dati sono ordinati in ordine crescente.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Gli esempi sopra mostrano come ordinare i dati in base a una colonna (dall'alto verso il basso) o riga (da sinistra a destra). Aspose.Cells.GridWeb può anche ordinare i dati in base a più di una colonna o riga. Per farlo, passa un array di indici di colonna o riga al metodo Sort. È supportato anche l'ordinamento di dati di tipo ibrido.

{{% /alert %}}
