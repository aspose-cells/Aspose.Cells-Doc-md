---
title: Accesso alla Tabella da una Cella e Aggiunta di Valori al suo Interno utilizzando Offset di Riga e Colonna
type: docs
weight: 230
url: /it/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalmente, si aggiungono valori all'interno della Tabella o dell'oggetto Lista utilizzando il metodo [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index). Ma a volte potresti dover aggiungere valori all'interno della Tabella o dell'oggetto Lista utilizzando gli offset di riga e colonna.

Per accedere alla tabella o all'oggetto elenco da una cella, utilizzare il metodo [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable). Per aggiungere valori al suo interno utilizzando gli spostamenti di riga e colonna, utilizzare il metodo [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

{{% /alert %}}

Lo screenshot seguente mostra il file Excel di origine utilizzato all'interno del codice. Contiene la tabella vuota ed evidenzia la cella D5 che si trova all'interno della tabella. Accederemo a questa tabella dalla cella D5 utilizzando il metodo [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) e quindi aggiungeremo i valori al suo interno utilizzando i metodi [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) e [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

## Esempio

### Screenshots che confrontano i file di origine e di output

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Codice C# per accedere alla tabella dalla cella e aggiungere valori al suo interno utilizzando gli spostamenti di riga e colonna

Il codice di esempio seguente carica il file Excel di origine come mostrato nello screenshot precedente e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
