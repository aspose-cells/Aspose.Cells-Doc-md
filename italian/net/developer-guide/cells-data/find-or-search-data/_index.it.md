---
title: Trova o cerca dati
type: docs
weight: 50
url: /it/net/find-or-search-data/
description: Scopri come trovare o cercare celle in un foglio di lavoro che contiene dati specificati tramite Aspose.Cells for .NET API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contiene dati specificati.

{{% /alert %}}

##  **Risultato Cells contenente i dati specificati**

###  **Utilizzando Microsoft Excel**

 Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contiene dati specificati. Se selezioni**Modificare** dal**Trovare** in Microsoft Excel, verrà visualizzata una finestra di dialogo in cui è possibile specificare il valore di ricerca.

Qui stiamo cercando il valore "Arance". Aspose.Cells consente inoltre agli sviluppatori di trovare celle nel foglio di lavoro contenenti valori specificati.

###  **Utilizzando Aspose.Cells**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) raccolta che rappresenta tutte le celle del foglio di lavoro. IL[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fornisce diversi metodi per trovare celle in un foglio di lavoro contenente dati specificati dall'utente. Alcuni di questi metodi sono discussi di seguito in modo più dettagliato.

{{% alert color="primary" %}}

Tutti i metodi Find restituiscono i riferimenti delle celle contenenti i dati specificati da cercare.

{{% /alert %}}

##  **Trovare Cells contenente una formula**

 Gli sviluppatori possono trovare una formula specifica nel foglio di lavoro chiamando il file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**Trovare**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metodo. In genere, il[**Trovare**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)il metodo accetta tre parametri:

- **Oggetto:**L'oggetto da cercare. Il tipo deve essere int,double,DateTime,string,bool.
- **Cella precedente:**Cella precedente con lo stesso oggetto. Questo parametro può essere impostato su null se si effettua la ricerca dall'inizio.
- FindOptions: opzioni per trovare l'oggetto richiesto.

Gli esempi seguenti utilizzano i dati del foglio di lavoro per esercitarsi con i metodi di ricerca:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **Ricerca di dati o formule utilizzando FindOptions**

 È possibile trovare valori specificati utilizzando il comando[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**Trovare**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metodo con vari[**TrovaOpzioni**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . In genere, il[**Trovare**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)il metodo accetta i seguenti parametri:

- *Valore di ricerca**, il dato o il valore da cercare.
- *Cella precedente**, l'ultima cella che conteneva lo stesso valore. Questo parametro può essere impostato su null durante la ricerca dall'inizio.
- *Opzioni di ricerca**, le opzioni di ricerca.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **Ricerca Cells contenente il valore stringa o il numero specificato**

 È possibile trovare valori di stringa specificati chiamando lo stesso[**Trovare**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metodo trovato in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) raccolta con vari[**TrovaOpzioni**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Specificare la[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) E[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) proprietà. Il codice di esempio seguente illustra come utilizzare queste proprietà per trovare celle con un numero diverso di stringhe in**inizio** o al**centro** o al**FINE** della stringa della cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **Argomenti avanzati**
- [Trova Cells con stile specifico](/cells/it/net/find-cells-with-specific-style/)
- [Scopri se il valore della cella inizia con virgolette singole](/cells/it/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Cerca dati utilizzando valori originali](/cells/it/net/search-data-using-original-values/)
