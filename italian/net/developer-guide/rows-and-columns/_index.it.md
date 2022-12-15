---
title: Formatta righe e colonne
linktitle: Righe e colonne
type: docs
weight: 100
url: /it/net/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}}

Quando si lavora con fogli di calcolo e si aggiungono dati a righe o colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, l'applicazione della formattazione su righe o colonne significa che l'altezza o la larghezza correnti devono essere modificate per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma con Aspose.Cells gli sviluppatori possono eseguire queste operazioni in fase di esecuzione.

{{% /alert %}}

## **Lavorare con le righe**

### **Regolazione dell'altezza della riga**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito in modo più dettagliato.

### **Impostazione dell'altezza di una riga**

 È possibile impostare l'altezza di una singola riga chiamando il file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) della collezione[**Imposta altezza riga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) metodo. Il[**Imposta altezza riga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)metodo prende i seguenti parametri come segue:

- **Indice di riga**, l'indice della riga di cui stai modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Impostazione dell'altezza di tutte le righe in un foglio di lavoro**

 Se gli sviluppatori devono impostare la stessa altezza di riga per tutte le righe nel foglio di lavoro, possono farlo utilizzando il file[**Altezza standard**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) proprietà del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collezione.

**Esempio:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Lavorare con le colonne**

### **Impostazione della larghezza di una colonna**

 Imposta la larghezza di una colonna chiamando il metodo[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) della collezione[**Imposta larghezza colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) metodo. Il[**Imposta larghezza colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)metodo accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna di cui stai modificando la larghezza.
- **Larghezza della colonna**, la larghezza della colonna desiderata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Impostazione della larghezza della colonna in pixel**

Imposta la larghezza di una colonna chiamando il metodo[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)della collezione[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)metodo. Il[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)metodo accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna di cui stai modificando la larghezza.
- **Larghezza della colonna**la larghezza della colonna desiderata in pixel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Impostazione della larghezza di tutte le colonne in un foglio di lavoro**

 Per impostare la stessa larghezza di colonna per tutte le colonne nel foglio di lavoro, utilizzare il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) della collezione[**Larghezza standard**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Argomenti avanzati**
- [Adatta righe e colonne](/cells/it/net/autofit-rows-and-columns/)
- [Converti testo in colonne usando Aspose.Cells](/cells/it/net/convert-text-to-columns-using-aspose-cells/)
- [Copia di righe e colonne](/cells/it/net/copying-rows-and-columns/)
- [Elimina righe e colonne vuote in un foglio di lavoro](/cells/it/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Raggruppamento e separazione di righe e colonne](/cells/it/net/grouping-and-ungrouping-rows-and-columns/)
- [Nascondere e mostrare righe e colonne](/cells/it/net/hiding-and-showing-rows-and-columns/)
- [Inserisci o elimina righe in un foglio di lavoro Excel](/cells/it/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Inserimento ed eliminazione di righe e colonne di file Excel](/cells/it/net/inserting-and-deleting-rows-and-columns/)
- [Rimuovi le righe duplicate in un foglio di lavoro](/cells/it/net/remove-duplicate-rows-in-a-worksheet/)
- [Aggiorna i riferimenti in altri fogli di lavoro eliminando colonne e righe vuote in un foglio di lavoro](/cells/it/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
