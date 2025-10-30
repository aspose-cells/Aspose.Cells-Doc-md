---
title: Regolazione dell altezza della riga e della larghezza della colonna
type: docs
weight: 10
url: /it/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Quando si lavora con i fogli di calcolo e si aggiungono dati alle righe o alle colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, applicare formattazioni su righe o colonne significa che l'altezza o la larghezza corrente deve cambiare per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma, con Aspose.Cells gli sviluppatori possono eseguire queste operazioni durante l'esecuzione.

{{% /alert %}} 
## **Lavorare con le righe**
### **Regolazione dell'altezza della riga**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) che rappresenta tutte le celle nel foglio di lavoro. La raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi vengono discussi di seguito in maggior dettaglio.
#### **Impostazione dell'altezza di una riga**
E' possibile impostare l'altezza di una singola riga chiamando il metodo [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) della raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) prende i seguenti parametri come segue:

- **Indice di riga**, l'indice della riga a cui si sta modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Impostazione dell'altezza di tutte le righe in un foglio di lavoro**
Se gli sviluppatori hanno bisogno di impostare la stessa altezza di riga per tutte le righe nel foglio di lavoro, possono farlo utilizzando il metodo [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) della raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Lavorare con colonne**
### **Impostazione della larghezza di una colonna**
Imposta la larghezza di una colonna chiamando il metodo [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) della raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.
- **Larghezza di colonna**, la larghezza desiderata della colonna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Impostazione della larghezza di tutte le colonne in un foglio di lavoro**
Per impostare la stessa larghezza di colonna per tutte le colonne nel foglio di lavoro, utilizzare il metodo [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) della raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
