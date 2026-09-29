---
title: Formattazione della tabella pivot
type: docs
weight: 10
url: /it/python-net/formatting-pivot-table/
description: Come formattare la tabella pivot con Aspose.Cells per Python via .NET.
keywords: Formattazione tabella pivot.
---

## **Aspetto della tabella pivot**

Come creare una tabella pivot spiega come creare una semplice tabella pivot. Questo articolo descrive come personalizzare l'aspetto di una tabella pivot impostando diverse proprietà:

- Opzioni di formato tabella pivot
- Opzioni di formato dei campi pivot
- Opzioni di formato del campo dati

### **Come impostare le opzioni di formato tabella pivot**

La classe [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) controlla complessivamente la tabella pivot e può essere formattata in vari modi.

#### **Come impostare il tipo di autoformato**

Microsoft Excel offre diverse impostazioni predefinite per i report. Anche Aspose.Cells per Python via .NET supporta queste opzioni di formattazione. Per accedervi:

1. Imposta [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) su **vero**.
1. Assegna un'opzione di formattazione dall'enumerazione [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **Come impostare le opzioni di formattazione**

Il codice di esempio qui sotto mostra come formattare la tabella pivot per mostrare i totali generali per righe e colonne, e come impostare l'ordine dei campi del report. Mostra inoltre come impostare una stringa personalizzata per i valori nulli.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **Formattazione Aspetto e Sensazione Manualmente**

Per formattare manualmente l'aspetto del report della tabella pivot, anziché utilizzare formati di report predefiniti, utilizzare i metodi [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) e [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/). Creare un oggetto stile per la formattazione desiderata, ad esempio:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **Come impostare le opzioni di formato campo pivot**

La classe [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) rappresenta un campo in una tabella pivot e può essere formattata in vari modi. Il codice di esempio qui sotto mostra come:

- Accedere ai campi di riga.
- Impostare i subtotali.
- Impostazione dell'ordinamento automatico.
- Impostazione dell'autovisualizzazione.

#### **Come impostare il formato dei campi riga/colonna/pagina**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **Come impostare il formato dei campi dati**

Il campione di codice sottostante mostra come impostare i formati di visualizzazione e il formato numerico per i campi dati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **Come eliminare i campi di un Pivot**

Il [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) ha un metodo chiamato [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) che ti consente di eliminare i campi di un Pivot. Usalo quando vuoi eliminare tutti i campi di un Pivot nelle aree, ad esempio, pagina, colonna, riga o dati.
Il campione di codice sottostante mostra come eliminare tutti i campi di un Pivot in un'area dati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
