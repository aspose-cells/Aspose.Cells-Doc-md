---
title: Adatta automaticamente righe e colonne
type: docs
weight: 20
url: /it/net/autofit-rows-and-columns/
description: Questo articolo mostra come regolare automaticamente le righe, le colonne, le righe di celle unite e le righe in un intervallo di celle tramite l API Aspose.Cells for .NET.
keywords: Autoadatta righe, autoadatta colonne, autoadatta righe in un intervallo di celle, autoadatta righe di celle unite
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di adattare automaticamente la larghezza e l'altezza delle celle in base al loro contenuto. Questa funzione è disponibile anche tramite Aspose.Cells in modo che gli sviluppatori possano adattare automaticamente le dimensioni di una cella durante l'esecuzione.

{{% /alert %}}

## **Adattamento automatico**

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro in un file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo esamina l'utilizzo della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) per adattare automaticamente le righe o le colonne.

### **Adatta automaticamente la riga - Semplice**

L'approccio più diretto per ridimensionare automaticamente larghezza e altezza di una riga è chiamare il metodo [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Il metodo [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) richiede un indice di riga (della riga da ridimensionare) come parametro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Come adattare automaticamente la riga in un intervallo di celle**

Una riga è composta da molte colonne. Aspose.Cells consente agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccaricata del metodo [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1). Richiede i seguenti parametri:

- **Indice riga**, l'indice della riga da adattare automaticamente.
- **Primo indice colonna**, l'indice della prima colonna della riga.
- **Ultimo indice colonna**, l'indice dell'ultima colonna della riga.

Il metodo [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) controlla i contenuti di tutte le colonne nella riga e quindi adatta automaticamente la riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Come adattare automaticamente la colonna in un intervallo di celle**

Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base al contenuto in un intervallo di celle nella colonna chiamando una versione sovraccarica del metodo [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) che richiede i seguenti parametri:

- **Indice colonna**, l'indice della colonna da adattare automaticamente.
- **Primo indice riga**, l'indice della prima riga della colonna.
- **Ultimo indice di riga**, l'indice dell'ultima riga della colonna.

Il metodo [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) controlla il contenuto di tutte le righe nella colonna e quindi adatta automaticamente la larghezza della colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Come adattare automaticamente le righe per le celle unite**

Con Aspose.Cells è possibile adattare automaticamente le righe anche per le celle che sono state unite utilizzando l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) fornisce la proprietà [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) che può essere utilizzata per adattare automaticamente le righe per le celle unite. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) accetta l'enumerazione [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) che ha i seguenti membri:

- Nessuno: Ignora celle unite.
- PrimaRiga: Espande solo l'altezza della prima riga.
- UltimaRiga: Espande solo l'altezza dell'ultima riga.
- OgniRiga: Espande solo l'altezza di ogni riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

È inoltre possibile provare a utilizzare le versioni sovraccaricate dei metodi [**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) e [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) che accettano un intervallo di righe/colonne e un'istanza di [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) per adattare automaticamente le righe/colonne selezionate con il tuo [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) desiderato.

Le firme dei suddetti metodi sono le seguenti:

1. AutoAdattaRighe(int rigaIniziale, int rigaFinale, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) opzioni)
1. AutoAdattaColonne(int primaColonna, int ultimaColonna, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) opzioni)

{{% /alert %}}

## **Importante sapere**

{{% alert color="primary" %}}

Se una cella è unita, i metodi AutoFit non verranno applicati, che è lo stesso comportamento di Microsoft Excel. È possibile aggirare questa limitazione utilizzando l'API di filtro automatico. Inoltre, se il testo in una cella è a capo, il metodo [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) non verrà applicato. Un'altra cosa da sapere è che i metodi di *AutoFit* richiedono tempo. Quindi, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}

## **Argomenti avanzati**
- [Adattare automaticamente le righe per le celle unite](/cells/it/net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="csharp" >}}
