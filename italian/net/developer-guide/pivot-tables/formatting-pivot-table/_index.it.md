---
title: Formattazione della tabella pivot
type: docs
weight: 10
url: /it/net/formatting-pivot-table/
---
## **Aspetto della tabella pivot**

Come creare una tabella pivot spiega come creare una semplice tabella pivot. Questo articolo descrive come personalizzare l'aspetto di una tabella pivot impostando varie proprietà:

- Opzioni formato tabella pivot
- Opzioni di formato dei campi pivot
- Opzioni del formato del campo dati

### **Impostazione delle opzioni di formato della tabella pivot**

 Il[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)class controlla la tabella pivot complessiva e può essere formattata in diversi modi.

#### **Impostazione del tipo di formattazione automatica**

Microsoft Excel offre diversi formati di report preimpostati. Aspose.Cells supporta anche queste opzioni di formattazione. Per accedervi:

1.  Impostare[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) a**VERO**.
1.  Assegna un'opzione di formattazione dal file[**Tipo di formattazione automatica della tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)enumerazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Impostazione delle opzioni di formato**

L'esempio di codice seguente mostra come formattare la tabella pivot per mostrare i totali complessivi per righe e colonne e come impostare l'ordine dei campi del rapporto. Mostra anche come impostare una stringa cliente per valori nulli.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Formattazione manuale dell'aspetto grafico**

 Per formattare manualmente l'aspetto del report della tabella pivot, invece di utilizzare formati di report preimpostati, utilizzare il file[**Tabella pivot.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) e[**Tabella pivot.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)metodi. Crea un oggetto di stile per la formattazione desiderata, ad esempio:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Impostazione delle opzioni di formato del campo pivot**

 Il[**Campo pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)class rappresenta un campo in una tabella pivot e può essere formattato in diversi modi. L'esempio di codice seguente mostra come:

- Accedere ai campi riga.
- Impostazione subtotali.
- Impostazione dell'ordinamento automatico.
- Impostazione della presentazione automatica.

#### **Impostazione del formato dei campi riga/colonna/pagina**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Impostazione del formato dei campi dati**

L'esempio di codice seguente mostra come impostare i formati di visualizzazione e il formato numerico per i campi dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Cancellazione dei campi pivot**

 Il[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) ha un metodo chiamato[**Chiaro()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)che consente di cancellare i campi pivot. Usalo quando vuoi cancellare tutti i campi pivot nelle aree, ad esempio pagina, colonna, riga o dati.
L'esempio di codice seguente mostra come cancellare tutti i campi pivot in un'area dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
