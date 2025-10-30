---
title: Trova o Cerca Dati
type: docs
weight: 50
url: /it/python-net/find-or-search-data/
description: Impara come trovare o cercare celle in un foglio di lavoro che contengono dati specificati tramite l API Aspose.Cells for Python via .NET.
keywords: Libreria Excel Python, Trova dati Python, Cerca dati Python, Trova celle contenenti una formula Python, Cercare celle contenenti una formula Python, Trova dati o formule usando FindOptions Python, Cerca dati o formule usando FindOptions Python, Trova o cerca celle contenenti valori o numeri specificati in Python, Trova o cerca celle contenenti dati specificati
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati.

{{% /alert %}}

## **Ricerca delle celle contenenti dati specificati**

### **Utilizzando Microsoft Excel**

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati. Se si seleziona **Modifica** dal menu **Trova** in Microsoft Excel, verrà visualizzata una finestra di dialogo in cui è possibile specificare il valore di ricerca.

Qui stiamo cercando il valore "Arance". Aspose.Cells consente anche agli sviluppatori di trovare celle nel foglio di lavoro contenenti valori specificati.

### **Usare Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta di [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta di [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) che rappresenta tutte le celle nel foglio di lavoro. La raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fornisce diversi metodi per trovare celle in un foglio di lavoro contenenti dati specificati. Alcuni di questi metodi sono discussi di seguito in modo più dettagliato.

{{% alert color="primary" %}}

Tutti i metodi di ricerca restituiscono i riferimenti delle celle contenenti i dati specificati da cercare.

{{% /alert %}}

## **Ricerca delle celle contenenti una formula**

Gli sviluppatori possono trovare una formula specificata nel foglio di lavoro chiamando il metodo [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Tipicamente, il metodo [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) accetta tre parametri:

- **cosa:** L'oggetto da cercare. Il tipo dovrebbe essere int,double,DateTime,string,bool.
- **cella_precedente:** Cella precedente con lo stesso oggetto. Questo parametro può essere impostato su null se si cerca dall'inizio.
- **opzioni_ricerca:** Opzioni per trovare l'oggetto richiesto.

Gli esempi seguenti utilizzano i dati del foglio di lavoro per praticare i metodi di ricerca:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Ricerca di dati o formule mediante FindOptions**

È possibile trovare valori specificati utilizzando il metodo [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) con varie [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions). Tipicamente, il metodo [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) accetta i seguenti parametri:

- **cosa:**, i dati o il valore da cercare.
- **cella_precedente**, l'ultima cella che conteneva lo stesso valore. Questo parametro può essere impostato su null quando si cerca dall'inizio.
- **opzioni_ricerca**, le opzioni di ricerca.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Ricerca delle celle contenenti un valore di stringa specificato o numero**

È possibile trovare valori di stringa specificati chiamando lo stesso metodo [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) trovato nella collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) con varie [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

Specificare le proprietà [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) e [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/). Il codice di esempio seguente illustra come utilizzare queste proprietà per trovare celle con un numero variabile di stringhe all'**inizio** o al **centro** o alla **fine** della stringa della cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Argomenti avanzati**
- [Trova celle con stile specifico](/cells/it/python-net/find-cells-with-specific-style/)
- [Verifica se il valore della cella inizia con un apice singolo](/cells/it/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Cerca dati usando valori originali](/cells/it/python-net/search-data-using-original-values/)
{{< app/cells/assistant language="python-net" >}}
