---
title: Formattare righe e colonne
linktitle: Righe e colonne
type: docs
weight: 100
url: /it/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET può supportare il cambiamento dell altezza della riga o della larghezza della colonna, nonché l applicazione della formattazione alle righe o alle colonne.
keywords: Imposta l altezza della riga e la larghezza della colonna, regola l altezza della riga e la larghezza della colonna, cambia l altezza della riga o la larghezza della colonna, formatta righe e colonne, come impostare l altezza della riga e la larghezza della colonna.
---


{{% alert color="primary" %}}

Quando si lavora con fogli e si aggiungono dati alle righe o alle colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, l'applicazione della formattazione alle righe o alle colonne significa che l'altezza o la larghezza attuale deve cambiare per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Tuttavia, con Aspose.Cells gli sviluppatori possono eseguire queste operazioni a tempo di esecuzione.

{{% /alert %}}

## **Lavorare con le righe**

### **Come regolare l'altezza della riga**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi in seguito in maggior dettaglio.

### **Come impostare l'altezza di una riga**

È possibile impostare l'altezza di una singola riga chiamando il metodo [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Il metodo [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) prende i seguenti parametri come segue:

- **Indice di riga**, l'indice della riga a cui si sta modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Come impostare l'altezza di tutte le righe in un foglio di lavoro**

Se gli sviluppatori hanno bisogno di impostare la stessa altezza della riga per tutte le righe nel foglio di lavoro, possono farlo utilizzando la proprietà [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

**Esempio:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Lavorare con colonne**

### **Come impostare la larghezza di una colonna**

Imposta la larghezza di una colonna chiamando il metodo [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Il metodo [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) prende i seguenti parametri:

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.
- **Larghezza di colonna**, la larghezza desiderata della colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Come impostare la larghezza della colonna in pixel**

Imposta la larghezza di una colonna chiamando il metodo [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Il metodo [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) prende i seguenti parametri:

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.
- **Larghezza della colonna**, la larghezza della colonna desiderata in pixel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Come impostare la larghezza di tutte le colonne in un foglio di lavoro**

Per impostare la stessa larghezza della colonna per tutte le colonne nel foglio di lavoro, utilizzare la proprietà [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Argomenti avanzati**
- [Adatta automaticamente righe e colonne](/cells/it/net/autofit-rows-and-columns/)
- [Converti testo in colonne utilizzando Aspose.Cells](/cells/it/net/convert-text-to-columns-using-aspose-cells/)
- [Copia righe e colonne](/cells/it/net/copying-rows-and-columns/)
- [Elimina righe e colonne vuote in un foglio di lavoro](/cells/it/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Raggruppa e scollega righe e colonne](/cells/it/net/grouping-and-ungrouping-rows-and-columns/)
- [Nascondi e mostra righe e colonne](/cells/it/net/hiding-and-showing-rows-and-columns/)
- [Inserisci o elimina righe in un foglio di lavoro di Excel](/cells/it/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Inserimento ed eliminazione di righe e colonne di un file di Excel](/cells/it/net/inserting-and-deleting-rows-and-columns/)
- [Rimuovere righe duplicate in un foglio di lavoro](/cells/it/net/remove-duplicate-rows-in-a-worksheet/)
- [Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro](/cells/it/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
