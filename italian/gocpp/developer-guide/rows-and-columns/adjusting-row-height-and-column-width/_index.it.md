---
title: Regolazione dell altezza della riga e della larghezza della colonna
type: docs
weight: 10
url: /it/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

Quando si lavora con i fogli di calcolo e si aggiungono dati alle righe o alle colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, applicare formattazioni su righe o colonne significa che l'altezza o la larghezza corrente deve cambiare per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma, con Aspose.Cells gli sviluppatori possono eseguire queste operazioni durante l'esecuzione.

{{% /alert %}}

## **Lavorare con le righe**

### **Regolazione dell'altezza della riga**

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) fornisce una collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/) che rappresenta tutte le celle del foglio. La collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/) fornisce diversi metodi per gestire le righe o le colonne di un foglio di lavoro. Alcuni di questi sono discussi nel dettaglio di seguito.

#### **Impostazione dell'altezza di una riga**

È possibile impostare l'altezza di una singola riga chiamando il metodo [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) prende i seguenti parametri come segue:

- **Indice di riga**, l'indice della riga a cui si sta modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **Impostazione dell'altezza di tutte le righe in un foglio di lavoro**

Se gli sviluppatori hanno bisogno di impostare la stessa altezza di riga per tutte le righe del foglio di lavoro, possono farlo usando il metodo [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **Lavorare con colonne**

### **Impostazione della larghezza di una colonna**

Imposta la larghezza di una colonna chiamando il metodo [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) prende i seguenti parametri:

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.
- **Larghezza di colonna**, la larghezza desiderata della colonna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **Impostazione della larghezza di tutte le colonne in un foglio di lavoro**

Per impostare la stessa larghezza di colonna per tutte le colonne del foglio di lavoro, utilizza il metodo [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
