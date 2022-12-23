---
title: Adatta righe e colonne
type: docs
weight: 20
url: /it/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di ridimensionare automaticamente la larghezza e l'altezza delle celle in base al contenuto. Questa funzione è disponibile anche tramite Aspose.Cells in modo che gli sviluppatori possano ridimensionare automaticamente le dimensioni di una cella in fase di esecuzione.

{{% /alert %}}

## **Montaggio automatico**

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo esamina l'utilizzo di[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class per adattare automaticamente righe o colonne.

### **Riga AutoFit - Semplice**

 L'approccio più diretto per ridimensionare automaticamente la larghezza e l'altezza di una riga consiste nel chiamare il metodo[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) metodo. Il[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)Il metodo accetta un indice di riga (della riga da ridimensionare) come parametro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **AutoFit Row in un intervallo di Cells**

 Una riga è composta da molte colonne. Aspose.Cells consente agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccaricata di[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)metodo. Richiede i seguenti parametri:

- **Indice di riga**, l'indice della riga che sta per essere adattata automaticamente.
- **Indice della prima colonna**, l'indice della prima colonna della riga.
- **Indice dell'ultima colonna**, l'indice dell'ultima colonna della riga.

 Il[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)Il metodo controlla il contenuto di tutte le colonne nella riga e quindi adatta automaticamente la riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Colonna AutoFit in un intervallo di Cells**

 Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base al contenuto in un intervallo di celle nella colonna chiamando una versione sovraccaricata di[**Adatta colonna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)metodo che accetta i seguenti parametri:

- **Indice di colonna**l'indice della colonna che sta per essere adattata automaticamente.
- **Indice prima riga**, l'indice della prima riga della colonna.
- **Indice dell'ultima riga**, l'indice dell'ultima riga della colonna.

 Il[**Adatta colonna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Il metodo controlla il contenuto di tutte le righe nella colonna e quindi adatta automaticamente la colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Adatta righe per unione Cells**

 Con Aspose.Cells è possibile adattare automaticamente le righe anche per le celle che sono state unite utilizzando il[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)la classe fornisce[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) proprietà che può essere utilizzata per adattare automaticamente le righe per le celle unite.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)accetta[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerabile che ha i seguenti membri.

- Nessuno: ignora le celle unite.
- FirstLine: espande solo l'altezza della prima riga.
- LastLine: espande solo l'altezza dell'ultima riga.
- EachLine: espande solo l'altezza di ogni riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Puoi anche provare a utilizzare le versioni sovraccaricate di[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Adatta automaticamente colonne**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) metodi che accettano un intervallo di righe/colonne e un'istanza di[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) per adattare automaticamente le righe/colonne selezionate con il tuo desiderato[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)di conseguenza.

Le firme dei suddetti metodi sono le seguenti:

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opzioni)
1. AutoFitColumns(int primaColumn, int ultimaColumn,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opzioni)

{{% /alert %}}

## **Importante da sapere**

{{% alert color="primary" %}}

 Se una cella viene unita, i metodi AutoFit non verranno applicati, che è lo stesso comportamento di Microsoft Excel. Puoi aggirare questo problema utilizzando il filtro automatico API. Inoltre, se il testo in una cella è a capo, il[**Adatta colonna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) metodo non sarà applicato neanche. Un'altra cosa che devi sapere è che il*Adatta automaticamente*metodi richiedono tempo. Quindi, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}

## **Argomenti avanzati**
- [Adatta righe per unione Cells](/cells/it/net/autofit-rows-for-merged-cells/)
