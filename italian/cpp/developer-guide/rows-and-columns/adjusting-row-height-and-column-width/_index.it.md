---
title: Regolazione dell'altezza della riga e della larghezza della colonna
type: docs
weight: 10
url: /it/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Quando si lavora con fogli di calcolo e si aggiungono dati a righe o colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, l'applicazione della formattazione su righe o colonne significa che l'altezza o la larghezza correnti devono essere modificate per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma con Aspose.Cells gli sviluppatori possono eseguire queste operazioni in fase di esecuzione.

{{% /alert %}} 
## **Lavorare con le righe**
### **Regolazione dell'altezza della riga**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe fornisce a[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) raccolta che rappresenta tutte le celle del foglio di lavoro. Il[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito in modo più dettagliato.
#### **Impostazione dell'altezza di una riga**
 È possibile impostare l'altezza di una singola riga chiamando il file[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) della collezione[Imposta altezza riga](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) metodo. Il[Imposta altezza riga](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)metodo prende i seguenti parametri come segue:

- **Indice di riga**, l'indice della riga di cui stai modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Impostazione dell'altezza di tutte le righe in un foglio di lavoro**
 Se gli sviluppatori devono impostare la stessa altezza di riga per tutte le righe nel foglio di lavoro, possono farlo utilizzando il file[Imposta altezza standard](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) metodo del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collezione.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Lavorare con le colonne**
### **Impostazione della larghezza di una colonna**
 Imposta la larghezza di una colonna chiamando il metodo[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) della collezione[Imposta larghezza colonna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) metodo. Il[Imposta larghezza colonna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)metodo accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna di cui stai modificando la larghezza.
- **Larghezza della colonna**, la larghezza della colonna desiderata.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Impostazione della larghezza di tutte le colonne in un foglio di lavoro**
 Per impostare la stessa larghezza di colonna per tutte le colonne nel foglio di lavoro, utilizzare il[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) della collezione[Imposta larghezza standard](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
