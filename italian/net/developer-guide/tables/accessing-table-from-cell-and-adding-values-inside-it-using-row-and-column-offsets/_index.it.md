---
title: Accesso alla tabella da Cell e aggiunta di valori al suo interno utilizzando gli offset di righe e colonne
type: docs
weight: 230
url: /it/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalmente, aggiungi valori all'interno della tabella o dell'oggetto elenco utilizzando[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metodo. Ma a volte, potrebbe essere necessario aggiungere valori all'interno della tabella o dell'oggetto elenco utilizzando gli offset di riga e colonna.

Per accedere alla tabella o all'oggetto elenco da una cella, utilizzare il[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) metodo. Per aggiungere valori al suo interno utilizzando gli offset di riga e colonna, utilizzare il[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) metodo.

{{% /alert %}}

 Lo screenshot seguente mostra il file Excel di origine utilizzato all'interno del codice. Contiene la tabella vuota ed evidenzia la cella D5 che si trova all'interno della tabella. Accederemo a questa tabella dalla cella D5 usando[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) metodo e quindi aggiungere i valori al suo interno utilizzando entrambi[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) e[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)metodi.

## Esempio

### Screenshot che confrontano i file di origine e di output

|![cose da fare:immagine_alt_testo](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.

|![cose da fare:immagine_alt_testo](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### Codice C# per accedere alla tabella dalla cella e aggiungere valori al suo interno utilizzando gli offset di riga e colonna

Il seguente codice di esempio carica il file Excel di origine come mostrato nello screenshot sopra e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
