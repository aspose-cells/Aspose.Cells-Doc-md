---
title: Formattazione della tabella pivot
type: docs
weight: 10
url: /it/net/formatting-pivot-table/
description: Come formattare la tabella pivot con Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **Aspetto della tabella pivot**

Come creare una tabella pivot spiega come creare una semplice tabella pivot. Questo articolo descrive come personalizzare l'aspetto di una tabella pivot impostando varie proprietà:

- Opzioni del formato della tabella pivot
- Opzioni di formato dei campi pivot
- Opzioni di formato del campo dati

###  **Impostazione delle opzioni di formato della tabella pivot**

 IL[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)La classe controlla la tabella pivot complessiva e può essere formattata in diversi modi.

####  **Impostazione del tipo di formattazione automatica**

Microsoft Excel offre diversi formati di report preimpostati. Aspose.Cells for Python via .NET supportano anche queste opzioni di formattazione. Per accedervi:

1.  Impostato[**Tabella pivot.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)a *vero**.
1.  Assegna un'opzione di formattazione dal file[**Tipo di formattazione automatica tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)enumerazione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Impostazione delle opzioni di formato**

L'esempio di codice riportato di seguito mostra come formattare la tabella pivot per mostrare i totali generali per righe e colonne e come impostare l'ordine dei campi del report. Mostra inoltre come impostare una stringa cliente per valori null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Formattazione manuale di Look and Feel**

Per formattare manualmente l'aspetto del rapporto tabella pivot, invece di utilizzare formati di rapporto preimpostati, utilizza il file[**Tabella pivot.format_all(stile)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) E[**Tabella pivot.format(riga, colonna, stile)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)metodi. Crea un oggetto di stile per la formattazione desiderata, ad esempio:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Impostazione delle opzioni di formato del campo pivot**

 IL[**Campo pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)La classe rappresenta un campo in una tabella pivot e può essere formattata in diversi modi. L'esempio di codice seguente mostra come:

- Accedi ai campi delle righe.
- Impostazione dei totali parziali.
- Impostazione dell'ordinamento automatico.
- Impostazione della visualizzazione automatica.

####  **Impostazione del formato dei campi riga/colonna/pagina**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Impostazione del formato dei campi dati**

L'esempio di codice seguente mostra come impostare i formati di visualizzazione e il formato numerico per i campi dati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Cancellazione dei campi pivot**

 IL[**Collezione PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) ha un metodo denominato[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)che ti consente di cancellare i campi pivot. Usalo quando desideri cancellare tutti i campi pivot nelle aree, ad esempio pagina, colonna, riga o dati.
L'esempio di codice seguente mostra come cancellare tutti i campi pivot in un'area dati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
