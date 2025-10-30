---
title: Accesso alla Tabella da una Cella e Aggiunta di Valori al suo Interno utilizzando Offset di Riga e Colonna
type: docs
weight: 230
url: /it/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalmente, si aggiungono valori all'interno della Tabella o dell'oggetto Lista utilizzando il metodo [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool). Ma a volte potresti dover aggiungere valori all'interno della Tabella o dell'oggetto Lista utilizzando gli offset di riga e colonna.

Per accedere alla tabella o all'oggetto elenco da una cella, utilizzare il metodo [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#). Per aggiungere valori al suo interno utilizzando gli spostamenti di riga e colonna, utilizzare il metodo [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

{{% /alert %}}

Lo screenshot seguente mostra il file Excel di origine utilizzato all'interno del codice. Contiene la tabella vuota ed evidenzia la cella D5 che si trova all'interno della tabella. Accederemo a questa tabella dalla cella D5 utilizzando il metodo [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) e quindi aggiungeremo i valori al suo interno utilizzando i metodi [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) e [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

## Esempio

### Screenshots che confrontano i file di origine e di output

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Codice Python per accedere alla tabella da una cella e aggiungere valori all’interno usando offset di riga e colonna

Il codice di esempio seguente carica il file Excel di origine come mostrato nello screenshot precedente e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
