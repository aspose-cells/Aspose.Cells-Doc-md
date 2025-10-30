---
title: Formattare la tabella pivot con Golang tramite C++
linktitle: Formattazione della tabella pivot
type: docs
weight: 10
url: /it/go-cpp/formatting-pivot-table/
description: Impara come personalizzare l aspetto delle pivot table usando Aspose.Cells for C++.
---

## **Aspetto della tabella pivot**

Come creare una tabella pivot spiega come creare una semplice tabella pivot. Questo articolo descrive come personalizzare l'aspetto di una tabella pivot impostando diverse proprietà:

- Opzioni di formato tabella pivot
- Opzioni di formato dei campi pivot
- Opzioni di formato del campo dati

### **Impostazione delle opzioni di formato della tabella pivot**

La classe [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) controlla complessivamente la tabella pivot e può essere formattata in vari modi.

#### **Impostazione del tipo di formato automatico**

Microsoft Excel offre una serie di formati di rapporto preimpostati. Anche Aspose.Cells supporta queste opzioni di formattazione. Per accedervi:

1. Imposta [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) su **vero**.
1. Assegna un'opzione di formattazione dall'enumerazione [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Impostazione delle Opzioni di Formato**

Il frammento di codice di seguito mostra come formattare la pivot table per mostrare i totali generali per righe e colonne, e come impostare l'ordine dei campi del rapporto. Mostra anche come impostare una stringa personalizzata per valori nulli.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Formattazione Aspetto e Sensazione Manualmente**

Per formattare manualmente l'aspetto del rapporto pivot senza usare formati predefiniti, usa i metodi [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) e [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Crea un oggetto stile per il formato desiderato, ad esempio:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Impostazione delle opzioni di formato campo pivot**

La classe [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) rappresenta un campo in una tabella pivot e può essere formattata in vari modi. Il codice di esempio qui sotto mostra come:

- Accedere ai campi di riga.
- Impostare i subtotali.
- Impostazione dell'ordinamento automatico.
- Impostazione dell'autovisualizzazione.

#### **Impostazione delle opzioni di formato campi riga/colonna/pagina**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Impostazione delle Opzioni di Formato dei Campi Dati**

Il campione di codice sottostante mostra come impostare i formati di visualizzazione e il formato numerico per i campi dati.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Cancellazione dei Campi di Tabella Pivot**

Il [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) ha un metodo chiamato [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) che ti consente di eliminare i campi di un Pivot. Usalo quando vuoi eliminare tutti i campi di un Pivot nelle aree, ad esempio, pagina, colonna, riga o dati.
Il campione di codice sottostante mostra come eliminare tutti i campi di un Pivot in un'area dati.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
