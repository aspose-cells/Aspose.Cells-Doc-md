---
title: Manipola tabella pivot
type: docs
weight: 20
url: /it/cpp/manipulate-pivot-table/
---
## **Possibili scenari di utilizzo**
Oltre a creare nuove tabelle pivot, puoi manipolare le tabelle pivot nuove ed esistenti. È possibile modificare i dati nell'intervallo di origine della tabella pivot, quindi aggiornarli e calcolarli e ottenere i nuovi valori delle celle della tabella pivot. Si prega di utilizzare[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6) e[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)metodi dopo aver modificato i valori nell'intervallo di origine della tabella pivot per aggiornare la tabella pivot.
## **Manipola tabella pivot**
 Il codice di esempio seguente carica il file[file excel di esempio](23167013.xlsx) e accede alla tabella pivot esistente all'interno del suo primo foglio di lavoro. Cambia il valore della cella B3 che si trova all'interno dell'intervallo di origine della tabella pivot e quindi aggiorna la tabella pivot. Prima di aggiornare la tabella pivot, accede al valore della cella della tabella pivot H8 che è 15 e dopo aver aggiornato la tabella pivot, il suo valore cambia in 6. Si prega di vedere il[file excel di output](23167014.xlsx)generato con questo codice e lo screenshot che mostra l'effetto del codice di esempio sul file excel di esempio. Si prega di vedere anche l'output della console di seguito che mostra il valore della cella della tabella pivot H8 prima e dopo l'aggiornamento della tabella pivot.

![cose da fare:immagine_alt_testo](manipulate-pivot-table_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **Uscita console**
 Di seguito è riportato l'output della console del codice di esempio precedente quando eseguito con il file fornito[file excel di esempio](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
