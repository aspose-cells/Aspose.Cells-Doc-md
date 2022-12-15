---
title: Trova o cerca dati
type: docs
weight: 50
url: /it/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contiene dati specifici.

{{% /alert %}}

## **Trovare Cells contenente dati specificati**

### **Utilizzo di Microsoft Excel**

 Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contiene dati specifici. Se selezioni**Modificare** dal**Trova** menu in Microsoft Excel, verrà visualizzata una finestra di dialogo in cui è possibile specificare il valore di ricerca.

Qui stiamo cercando il valore "Arance". Aspose.Cells consente inoltre agli sviluppatori di trovare celle nel foglio di lavoro contenenti valori specificati.

### **Utilizzando Aspose.Cells**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)raccolta che rappresenta tutte le celle del foglio di lavoro. Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fornisce diversi metodi per trovare celle in un foglio di lavoro contenente dati specificati dall'utente. Alcuni di questi metodi sono discussi di seguito in modo più dettagliato.

{{% alert color="primary" %}}

Tutti i metodi Find restituiscono i riferimenti delle celle contenenti i dati specificati da cercare.

{{% /alert %}}

## **Trovare Cells contenente una formula**

 Gli sviluppatori possono trovare una formula specificata nel foglio di lavoro chiamando il metodo[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) della collezione[**Trova**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metodo. Tipicamente, il[**Trova**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)metodo accetta tre parametri:

- **Oggetto:**L'oggetto da cercare. Il tipo deve essere int,double,DateTime,string,bool.
- **Cella precedente:**Cella precedente con lo stesso oggetto. Questo parametro può essere impostato su null se si esegue la ricerca dall'inizio.
- FindOptions: Opzioni per trovare l'oggetto richiesto.

Gli esempi seguenti utilizzano i dati del foglio di lavoro per esercitarsi con i metodi di ricerca:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Trovare dati o formule utilizzando FindOptions**

 È possibile trovare i valori specificati utilizzando il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) della collezione[**Trova**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metodo con vari[**TrovaOpzioni**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Tipicamente, il[**Trova**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)metodo accetta i seguenti parametri:

- **Valore di ricerca**i dati o il valore da ricercare.
- **Cella precedente**, l'ultima cella che conteneva lo stesso valore. Questo parametro può essere impostato su null durante la ricerca dall'inizio.
- **Trova le opzioni**, le opzioni di ricerca.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Ricerca di Cells contenente il valore o il numero di stringa specificato**

 È possibile trovare i valori di stringa specificati chiamando lo stesso[**Trova**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metodo trovato nel[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione con vari[**TrovaOpzioni**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Specificare la[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) e[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) proprietà. Il codice di esempio seguente illustra come utilizzare queste proprietà per trovare celle con un numero diverso di stringhe in corrispondenza di**inizio** o al**centro** o al**fine** della stringa della cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Argomenti avanzati**
- [Trova Cells con stile specifico](/cells/it/net/find-cells-with-specific-style/)
- [Trova se il valore della cella inizia con virgolette singole](/cells/it/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Cerca i dati utilizzando i valori originali](/cells/it/net/search-data-using-original-values/)
