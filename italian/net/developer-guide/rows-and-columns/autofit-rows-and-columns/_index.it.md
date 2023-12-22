---
title: Adatta righe e colonne automaticamente
type: docs
weight: 20
url: /it/net/autofit-rows-and-columns/
description: Questo articolo mostra come adattare automaticamente righe, colonne, righe di celle unite e righe in un intervallo di celle tramite Aspose.Cells for .NET API.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di ridimensionare automaticamente la larghezza e l'altezza delle celle in base al contenuto. Questa funzionalità è disponibile anche tramite Aspose.Cells in modo che gli sviluppatori possano ridimensionare automaticamente le dimensioni di una cella in fase di esecuzione.

{{% /alert %}}

##  **Adattamento automatico**

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo esamina l'utilizzo di[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class per adattare automaticamente righe o colonne.

###  **Adatta riga: semplice**

 L'approccio più semplice per ridimensionare automaticamente la larghezza e l'altezza di una riga è chiamare il metodo[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) metodo. IL[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)Il metodo accetta come parametro un indice di riga (della riga da ridimensionare).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **Come adattare automaticamente la riga in un intervallo di Cells**

 Una riga è composta da molte colonne. Aspose.Cells consente agli sviluppatori di adattare automaticamente una riga in base al contenuto di un intervallo di celle all'interno della riga chiamando una versione sovraccaricata del[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)metodo. Richiede i seguenti parametri:

- *Indice riga**, l'indice della riga che sta per essere adattata automaticamente.
- *Indice prima colonna**, l'indice della prima colonna della riga.
- *Indice dell'ultima colonna**, l'indice dell'ultima colonna della riga.

 IL[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)Il metodo controlla il contenuto di tutte le colonne della riga e quindi adatta automaticamente la riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **Come adattare automaticamente la colonna in un intervallo di Cells**

 Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base al contenuto di un intervallo di celle nella colonna richiamando una versione sovraccaricata di[**Adatta colonna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)metodo che accetta i seguenti parametri:

- *Indice colonna**, l'indice della colonna che sta per essere adattata automaticamente.
- *Indice della prima riga**, l'indice della prima riga della colonna.
- *Indice dell'ultima riga**, l'indice dell'ultima riga della colonna.

 IL[**Adatta colonna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Il metodo controlla il contenuto di tutte le righe nella colonna e quindi adatta automaticamente la colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **Come adattare automaticamente le righe per l'unione Cells**

 Con Aspose.Cells è possibile adattare automaticamente le righe anche per le celle che sono state unite utilizzando il comando[**Opzioni di montaggio automatico**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**Opzioni di montaggio automatico**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)la classe fornisce[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) proprietà che può essere utilizzata per adattare automaticamente le righe alle celle unite.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)accetta[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerabile che ha i seguenti membri.

- Nessuno: ignora le celle unite.
- FirstLine: espande solo l'altezza della prima riga.
- LastLine: espande solo l'altezza dell'ultima riga.
- EachLine: espande solo l'altezza di ogni riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Puoi anche provare a utilizzare le versioni sovraccaricate di[**Adattamento automatico delle righe**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Adatta colonne**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) metodi che accettano un intervallo di righe/colonne e un'istanza di[**Opzioni di montaggio automatico**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) per adattare automaticamente le righe/colonne selezionate a quelle desiderate[**Opzioni di montaggio automatico**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)di conseguenza.

Le firme dei suddetti metodi sono le seguenti:

1.  AutoFitRows(int startRow, int endRow,[**Opzioni di montaggio automatico**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opzioni)
1.  AutoFitColumns(int primaColonna, int ultimaColonna,[**Opzioni di montaggio automatico**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opzioni)

{{% /alert %}}

##  **Importante da sapere**

{{% alert color="primary" %}}

Se una cella viene unita, i metodi di adattamento automatico non verranno applicati, che è lo stesso comportamento di Microsoft Excel. Puoi aggirare questo problema utilizzando il filtro automatico API. Inoltre, se il testo in una cella va a capo, il[**Adatta colonna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) neanche il metodo verrà applicato. Un'altra cosa che devi sapere è che il*Adattamento automatico*i metodi richiedono molto tempo. Pertanto, dovresti chiamare questi metodi il più raramente possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}

##  **Argomenti avanzati**
- [Adatta automaticamente le righe per l'unione Cells](/cells/it/net/autofit-rows-for-merged-cells/)
