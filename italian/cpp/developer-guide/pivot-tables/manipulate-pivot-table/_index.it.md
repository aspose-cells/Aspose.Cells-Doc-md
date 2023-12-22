---
title: Manipolare la tabella pivot
type: docs
weight: 20
url: /it/cpp/manipulate-pivot-table/
---
##  **Possibili scenari di utilizzo**
Oltre a creare nuove tabelle pivot, puoi manipolare le tabelle pivot nuove ed esistenti. È possibile modificare i dati nell'intervallo di origine della tabella pivot, quindi aggiornarli, calcolarli e ottenere i nuovi valori delle celle della tabella pivot. Si prega di utilizzare[Tabella pivot.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) E[Tabella pivot.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)metodi dopo aver modificato i valori nell'intervallo di origine della tabella pivot per aggiornare la tabella pivot.
##  **Manipolare la tabella pivot**
 Il codice di esempio seguente carica il file[file Excel di esempio](23167013.xlsx) e accede alla tabella pivot esistente all'interno del suo primo foglio di lavoro. Modifica il valore della cella B3 che si trova all'interno dell'intervallo di origine della tabella pivot e quindi aggiorna la tabella pivot. Prima di aggiornare la tabella pivot, accede al valore della cella H8 della tabella pivot che è 15 e dopo aver aggiornato la tabella pivot, il suo valore cambia in 6. Consulta la sezione[file Excel di output](23167014.xlsx)generato con questo codice e lo screenshot che mostra l'effetto del codice di esempio sul file Excel di esempio. Consulta anche l'output della console di seguito che mostra il valore della cella H8 della tabella pivot prima e dopo l'aggiornamento della tabella pivot.

![cose da fare:immagine_alt_testo](manipulate-pivot-table_1.png)
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **Uscita della console**
 Di seguito è riportato l'output della console del codice di esempio riportato sopra quando eseguito con il file fornito[file Excel di esempio](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
