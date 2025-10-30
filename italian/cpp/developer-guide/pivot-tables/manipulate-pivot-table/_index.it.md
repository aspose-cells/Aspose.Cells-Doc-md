---
title: Manipolare tabella pivot
type: docs
weight: 20
url: /it/cpp/manipulate-pivot-table/
---

## **Possibili Scenari di Utilizzo**
Oltre a creare nuove tabelle pivot, è possibile manipolare le nuove e esistenti tabelle pivot. È possibile modificare i dati nell'intervallo di origine della tabella pivot e quindi aggiornarli e calcolarli per ottenere i nuovi valori delle celle della tabella pivot. Si prega di utilizzare i metodi [PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) e [PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) dopo aver modificato i valori nell'intervallo di origine della tabella pivot per aggiornare la tabella pivot.
## **Manipolare tabella pivot**
Il seguente codice di esempio carica il [file Excel di esempio](23167013.xlsx) ed accede alla tabella pivot esistente nel suo primo foglio di lavoro. Modifica il valore della cella B3 che si trova all'interno dell'intervallo di origine della tabella pivot e quindi aggiorna la tabella pivot. Prima di aggiornare la tabella pivot, accede al valore della cella H8 della tabella pivot che è 15 e dopo l'aggiornamento della tabella pivot, il suo valore cambia in 6. Si prega di vedere il [file Excel generato](23167014.xlsx) con questo codice e la schermata che mostra l'effetto del codice di esempio sul file Excel di esempio. Si prega inoltre di vedere l'output della console qui sotto che mostra il valore della cella della tabella pivot H8 prima e dopo l'aggiornamento della tabella pivot.

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **Output della console**
Di seguito è riportato l'output della console del codice di esempio sopra quando eseguito con il [file Excel di esempio](23167013.xlsx) fornito.

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
