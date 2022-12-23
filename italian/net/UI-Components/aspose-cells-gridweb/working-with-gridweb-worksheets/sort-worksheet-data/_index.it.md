---
title: Ordina i dati del foglio di lavoro
type: docs
weight: 80
url: /it/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

L'ordinamento è una caratteristica molto preziosa quando si tratta di elaborazione dei dati. I dati non ordinati sono una seccatura per gli utenti durante la ricerca di informazioni specifiche. Aspose.Cells.GridWeb supporta potenti funzionalità di ordinamento. Questo argomento illustra l'ordinamento dei dati utilizzando Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Ordinamento dei dati**
Aspose.Cells.GridWeb consente agli sviluppatori di ordinare i dati orizzontalmente e verticalmente in modo che gli sviluppatori possano ordinare i dati dall'alto verso il basso o da sinistra a destra.
### **Da cima a fondo**
Per ordinare i dati dall'alto verso il basso:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina l'intervallo di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare l'orientamento dall'alto verso il basso.

L'esempio seguente ordina i dati in quattro colonne di un foglio di lavoro in ordine decrescente. Solo venti righe delle quattro colonne sono ordinate dall'alto verso il basso.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

![cose da fare:immagine_alt_testo](sort-worksheet-data_1.png)

Dopo aver eseguito il codice, i dati vengono ordinati in ordine crescente.

![cose da fare:immagine_alt_testo](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Da sinistra a destra**
Per ordinare i dati da sinistra a destra:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina l'intervallo di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare da sinistra a destra.

L'esempio seguente ordina i dati in quattro righe in ordine crescente. Solo quattro righe di sette colonne sono ordinate da sinistra a destra.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

![cose da fare:immagine_alt_testo](sort-worksheet-data_3.png)

Dopo aver eseguito il codice, i dati vengono ordinati in ordine crescente.

![cose da fare:immagine_alt_testo](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: gli esempi precedenti mostrano l'ordinamento dei dati sulla base di una colonna (dall'alto verso il basso) o di una riga (da sinistra a destra). Aspose.Cells.GridWeb può anche ordinare i dati in base a più di una colonna o riga. Per fare ciò, passare una matrice di indici di colonna o di riga al metodo Sort. È supportato anche l'ordinamento del tipo di dati ibridi.

{{% /alert %}}
