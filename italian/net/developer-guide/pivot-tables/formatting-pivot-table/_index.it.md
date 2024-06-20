---
title: Formattazione della tabella pivot
type: docs
weight: 10
url: /it/net/formatting-pivot-table/
---

## **Aspetto della tabella pivot**

Come creare una tabella pivot spiega come creare una semplice tabella pivot. Questo articolo descrive come personalizzare l'aspetto di una tabella pivot impostando diverse proprietà:

- Opzioni di formato tabella pivot
- Opzioni di formato dei campi pivot
- Opzioni di formato del campo dati

### **Impostazione delle opzioni di formato della tabella pivot**

La classe [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) controlla complessivamente la tabella pivot e può essere formattata in vari modi.

#### **Impostazione del tipo di formato automatico**

Microsoft Excel offre diversi formati preimpostati per i report. Anche Aspose.Cells supporta queste opzioni di formattazione. Per accedervi:

1. Imposta [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) su **vero**.
1. Assegna un'opzione di formattazione dall'enumerazione [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Impostazione delle Opzioni di Formato**

Il codice di esempio qui sotto mostra come formattare la tabella pivot per mostrare i totali generali per righe e colonne, e come impostare l'ordine dei campi del report. Mostra inoltre come impostare una stringa personalizzata per i valori nulli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Formattazione Aspetto e Sensazione Manualmente**

Per formattare manualmente l'aspetto del report della tabella pivot, anziché utilizzare formati di report predefiniti, utilizzare i metodi [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) e [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall). Creare un oggetto stile per la formattazione desiderata, ad esempio:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Impostazione delle opzioni di formato campo pivot**

La classe [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) rappresenta un campo in una tabella pivot e può essere formattata in vari modi. Il codice di esempio qui sotto mostra come:

- Accedere ai campi di riga.
- Impostare i subtotali.
- Impostazione dell'ordinamento automatico.
- Impostazione dell'autovisualizzazione.

#### **Impostazione delle opzioni di formato campi riga/colonna/pagina**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Impostazione del formato dei campi dati**

Il campione di codice sottostante mostra come impostare i formati di visualizzazione e il formato numerico per i campi dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Cancellazione dei Campi di Tabella Pivot**

Il [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) ha un metodo chiamato [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) che ti consente di eliminare i campi di un Pivot. Usalo quando vuoi eliminare tutti i campi di un Pivot nelle aree, ad esempio, pagina, colonna, riga o dati.
Il campione di codice sottostante mostra come eliminare tutti i campi di un Pivot in un'area dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
