---
title: Raggruppamento, Sblocco righe e colonne
type: docs
weight: 30
url: /it/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduzione**

In un file Microsoft Excel, è possibile creare un'outline per i dati che consente di mostrare e nascondere livelli di dettaglio con un singolo clic del mouse.

Fare clic sui **Simboli di Outline**, 1,2,3, + e - per visualizzare rapidamente solo le righe o colonne che forniscono sommari o intestazioni per le sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per vedere i dettagli sotto un sommario o un'intestazione individuale.

## **Gestione raggruppata di righe e colonne**

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) fornisce una collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/) che rappresenta tutte le celle del foglio.

La collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi nel dettaglio di seguito.

### **Raggruppamento di righe e colonne**

È possibile raggruppare righe o colonne chiamando i metodi [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) e [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Entrambi i metodi richiedono i seguenti parametri:

- L'indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- L'indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Impostazioni di raggruppamento**

Microsoft Excel consente di configurare le impostazioni di raggruppamento per la visualizzazione:

- Le righe di riassunto sotto il dettaglio.
- Le colonne di riepilogo a destra del dettaglio.

## **Sganciare Righe e Colonne**

Per sgrouppare qualsiasi riga o colonna raggruppata, chiamare i metodi [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) e [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Entrambi i metodi richiedono due parametri:

- L'indice della prima riga o colonna, la prima riga/colonna da disraggruppare.
- L'indice dell'ultima riga o colonna, l'ultima riga/colonna da disraggruppare.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
