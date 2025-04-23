---
title: Accesso alla Tabella da una Cella e Aggiunta di Valori al suo Interno utilizzando Offset di Riga e Colonna
type: docs
weight: 110
url: /it/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalmente, si aggiungono valori all'interno della Tabella o dell'oggetto Lista utilizzando il metodo [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-). Ma a volte potresti dover aggiungere valori all'interno della Tabella o dell'oggetto Lista utilizzando gli offset di riga e colonna.

Per accedere alla Tabella o all'oggetto Lista da una cella, utilizzare il metodo [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--). E per aggiungere valori al suo interno utilizzando gli offset di riga e colonna, utilizzare il metodo [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-).

{{% /alert %}}

## Esempio

### Screenshots che confrontano i file di origine e di output

Lo screenshot seguente mostra il file Excel di origine utilizzato all'interno del codice. Contiene la tabella vuota ed evidenzia la cella D5 che si trova all'interno della tabella. Accederemo a questa tabella dalla cella D5 utilizzando il metodo [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) e quindi aggiungeremo i valori al suo interno utilizzando i metodi [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-) e [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-).

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Codice Java per accedere alla tabella da una cella e per aggiungere valori al suo interno utilizzando gli offset di riga e colonna

Il codice di esempio seguente carica il file Excel di origine come mostrato nello screenshot precedente e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
{{< app/cells/assistant language="java" >}}
