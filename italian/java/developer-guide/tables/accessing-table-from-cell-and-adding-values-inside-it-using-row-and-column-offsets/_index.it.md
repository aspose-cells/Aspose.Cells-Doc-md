---
title: Accesso alla tabella da Cell e aggiunta di valori al suo interno utilizzando gli offset di righe e colonne
type: docs
weight: 110
url: /it/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalmente, aggiungi valori all'interno della tabella o dell'oggetto elenco utilizzando[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) metodo. Ma a volte, potrebbe essere necessario aggiungere valori all'interno della tabella o dell'oggetto elenco utilizzando gli offset di riga e colonna.

Per accedere alla tabella o all'oggetto elenco da una cella, utilizzare il[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) metodo. E per aggiungere valori al suo interno usando gli offset di riga e colonna, usa il file[**ListObject.putCellValue(rigaOffset,colonnaOffset,valore)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) metodo.

{{% /alert %}}

## Esempio

### Screenshot che confrontano i file di origine e di output

 Lo screenshot seguente mostra il file Excel di origine utilizzato all'interno del codice. Contiene la tabella vuota ed evidenzia la cella D5 che si trova all'interno della tabella. Accederemo a questa tabella dalla cella D5 usando[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) metodo e quindi aggiungere i valori al suo interno utilizzando entrambi[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) e[**ListObject.putCellValue(rigaOffset,colonnaOffset,valore)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) metodi.

![cose da fare:immagine_alt_testo](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.

![cose da fare:immagine_alt_testo](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Codice Java per accedere alla tabella dalla cella e aggiungere valori al suo interno utilizzando gli offset di riga e colonna

Il seguente codice di esempio carica il file Excel di origine come mostrato nello screenshot sopra e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
