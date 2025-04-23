---
title: Trova o Cerca Dati
type: docs
weight: 50
url: /it/net/find-or-search-data/
description: Scopri come trovare o cercare celle in un foglio di lavoro che contengono dati specificati tramite l API Aspose.Cells for .NET.
keywords: Trova dati, Cerca dati, Trova celle contenenti una formula, Cerca celle contenenti una formula, Trova dati o formule usando FindOptions, Cerca dati o formule usando FindOptions, Trova o cerca celle contenenti un valore o numero specificato, Trova o cerca celle che contengono dati specificati
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati.

{{% /alert %}}

## **Ricerca delle celle contenenti dati specificati**

### **Utilizzando Microsoft Excel**

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati. Se si seleziona **Modifica** dal menu **Trova** in Microsoft Excel, verrà visualizzata una finestra di dialogo in cui è possibile specificare il valore di ricerca.

Qui stiamo cercando il valore "Arance". Aspose.Cells consente anche agli sviluppatori di trovare celle nel foglio di lavoro contenenti valori specificati.

### **Usare Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta di [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta di [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) che rappresenta tutte le celle nel foglio di lavoro. La raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fornisce diversi metodi per trovare celle in un foglio di lavoro contenenti dati specificati. Alcuni di questi metodi sono discussi di seguito in modo più dettagliato.

{{% alert color="primary" %}}

Tutti i metodi di ricerca restituiscono i riferimenti delle celle contenenti i dati specificati da cercare.

{{% /alert %}}

## **Ricerca delle celle contenenti una formula**

Gli sviluppatori possono trovare una formula specificata nel foglio di lavoro chiamando il metodo [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Tipicamente, il metodo [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) accetta tre parametri:

- **Oggetto:** L'oggetto da cercare. Il tipo dovrebbe essere int, double, DateTime, string, bool.
- **Celle precedenti:** Cella precedente con lo stesso oggetto. Questo parametro può essere impostato su null se la ricerca parte dall'inizio.
- FindOptions: Opzioni per trovare l'oggetto richiesto.

Gli esempi seguenti utilizzano i dati del foglio di lavoro per praticare i metodi di ricerca:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Ricerca di dati o formule mediante FindOptions**

È possibile trovare valori specificati utilizzando il metodo [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) con varie [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions). Tipicamente, il metodo [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) accetta i seguenti parametri:

- **Valore di ricerca**, i dati o il valore da cercare.
- **Celle precedenti**, l'ultima cella che conteneva lo stesso valore. Questo parametro può essere impostato su null durante la ricerca dall'inizio.
- **Opzioni di ricerca**, le opzioni di ricerca.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Ricerca delle celle contenenti un valore di stringa specificato o numero**

È possibile trovare valori di stringa specificati chiamando lo stesso metodo [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) trovato nella collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) con varie [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

Specificare le proprietà [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) e [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype). Il codice di esempio seguente illustra come utilizzare queste proprietà per trovare celle con un numero variabile di stringhe all'**inizio** o al **centro** o alla **fine** della stringa della cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Argomenti avanzati**
- [Trova celle con stile specifico](/cells/it/net/find-cells-with-specific-style/)
- [Verifica se il valore della cella inizia con un apice singolo](/cells/it/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Cerca dati usando valori originali](/cells/it/net/search-data-using-original-values/)
{{< app/cells/assistant language="csharp" >}}
