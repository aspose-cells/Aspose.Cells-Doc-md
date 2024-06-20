---
title: Adatta automaticamente righe e colonne
type: docs
weight: 20
url: /it/python-net/autofit-rows-and-columns/
description: Questo articolo mostra come adattare automaticamente righe, colonne, righe di celle unite e righe in un intervallo di celle tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Adatta automaticamente righe Python, Adatta automaticamente colonne Python, Adatta automaticamente riga in un intervallo di celle Python, Adatta automaticamente righe di celle unite Python.
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di dimensionare automaticamente la larghezza e l'altezza delle celle in base al loro contenuto. Questa funzione è disponibile anche tramite Aspose.Cells per Python via .NET in modo che gli sviluppatori possano dimensionare automaticamente le dimensioni di una cella durante l'esecuzione.

{{% /alert %}}

## **Adattamento automatico**

Aspose.Cells per Python via .NET fornisce una classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo esamina l'utilizzo della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) per adattare automaticamente righe o colonne.

### **Adatta automaticamente la riga - Semplice**

L'approccio più diretto per ridimensionare automaticamente larghezza e altezza di una riga è chiamare il metodo [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Il metodo [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) richiede un indice di riga (della riga da ridimensionare) come parametro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Come adattare automaticamente la riga in un intervallo di celle**

Una riga è composta da molte colonne. Aspose.Cells per Python via .NET consente agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccarica del metodo [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int). Richiede i seguenti parametri:

- **Indice riga**, l'indice della riga da adattare automaticamente.
- **Primo indice colonna**, l'indice della prima colonna della riga.
- **Ultimo indice colonna**, l'indice dell'ultima colonna della riga.

Il metodo [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) controlla i contenuti di tutte le colonne nella riga e quindi adatta automaticamente la riga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Come adattare automaticamente la colonna in un intervallo di celle**

Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base al contenuto in un intervallo di celle nella colonna chiamando una versione sovraccarica del metodo [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) che richiede i seguenti parametri:

- **Indice colonna**, l'indice della colonna da adattare automaticamente.
- **Primo indice riga**, l'indice della prima riga della colonna.
- **Ultimo indice di riga**, l'indice dell'ultima riga della colonna.

Il metodo [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) controlla il contenuto di tutte le righe nella colonna e quindi adatta automaticamente la larghezza della colonna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Come adattare automaticamente le righe per le celle unite**

Con Aspose.Cells for Python via .NET è possibile adattare automaticamente le righe anche per le celle unite utilizzando l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) fornisce la proprietà [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) che può essere utilizzata per adattare automaticamente le righe per le celle unite. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) accetta l'enumerazione [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) che ha i seguenti membri.

- NONE: Ignora le celle unite.
- FIRST_LINE: Espande solo l'altezza della prima riga.
- LAST_LINE: Espande solo l'altezza dell'ultima riga.
- EACH_LINE: Espande solo l'altezza di ogni riga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

È inoltre possibile provare a utilizzare le versioni sovraccaricate dei metodi [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) e [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) che accettano un intervallo di righe/colonne e un'istanza di [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) per adattare automaticamente le righe/colonne selezionate con il tuo [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) desiderato.

Le firme dei suddetti metodi sono le seguenti:

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) options)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Importante sapere**

{{% alert color="primary" %}}

Se una cella è unita, i metodi AutoFit non verranno applicati, che è lo stesso comportamento di Microsoft Excel. È possibile aggirare questa limitazione utilizzando l'API di filtro automatico. Inoltre, se il testo in una cella è a capo, il metodo [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) non verrà applicato. Un'altra cosa da sapere è che i metodi di *AutoFit* richiedono tempo. Quindi, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}

## **Argomenti avanzati**
- [Adattare automaticamente le righe per le celle unite](/cells/it/python-net/autofit-rows-for-merged-cells/)
