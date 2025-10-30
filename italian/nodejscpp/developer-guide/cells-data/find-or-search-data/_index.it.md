---  
title: Trova o Cerca Dati
type: docs  
weight: 50  
url: /it/nodejs-cpp/find-or-search-data/  
description: Impara come trovare o cercare celle in un foglio di lavoro che contengono dati specificati tramite l API Aspose.Cells for Node.js via C++.  
keywords: Trova dati Node.js via C++, cerca dati Node.js via C++, Trova celle contenenti una formula Node.js via C++, cerca celle contenenti una formula Node.js via C++, Trova dati o formule usando FindOptions Node.js via C++, cerca dati o formule usando FindOptions Node.js tramite C++, Trova o Cerca celle contenenti un valore di stringa o numero specificato Node.js via C++, trova o cerca celle che contengono dati specifici  
---  

{{% alert color="primary" %}}  
Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati.  
{{% /alert %}}  

## **Ricerca delle celle contenenti dati specificati**  

### **Utilizzando Microsoft Excel**  

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati. Se selezioni **Modifica** dal menu **Trova** in Microsoft Excel, vedrai una finestra di dialogo in cui puoi specificare il valore di ricerca.  

Qui stiamo cercando il valore "Arance". Aspose.Cells consente anche agli sviluppatori di trovare celle nel foglio di lavoro contenenti valori specificati.  

### **Usando Aspose.Cells for Node.js via C++**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una raccolta [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) che rappresenta tutte le celle del foglio di lavoro. La raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre vari metodi per trovare celle in un foglio di lavoro contenenti dati inseriti dall’utente. Alcuni di questi metodi sono discussi più dettagliatamente di seguito.  

{{% alert color="primary" %}}  
Tutti i metodi di ricerca restituiscono i riferimenti delle celle contenenti i dati specificati da cercare.  
{{% /alert %}}  

## **Ricerca delle celle contenenti una formula**  

Gli sviluppatori possono trovare una formula specifica nel foglio di lavoro chiamando il metodo [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) nella raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). In genere, il metodo [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) accetta tre parametri:  

- **Oggetto:** L'oggetto da cercare. Il tipo dovrebbe essere int, double, DateTime, string, bool.  
- **Cella precedente:** Cella precedente con lo stesso oggetto. Questo parametro può essere impostato su null se si cerca dall'inizio.  
- **OpzioniDiRicerca:** Opzioni per trovare l'oggetto richiesto.  

Gli esempi seguenti utilizzano i dati del foglio di lavoro per praticare i metodi di ricerca:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Ricerca di dati o formule mediante FindOptions**  

È possibile trovare valori specificati utilizzando il metodo [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) con vari [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Tipicamente, il metodo [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) accetta i seguenti parametri:  

- **Valore di ricerca**, i dati o il valore da cercare.  
- **Celle precedenti**, l'ultima cella che conteneva lo stesso valore. Questo parametro può essere impostato su null durante la ricerca dall'inizio.  
- **Opzioni di ricerca**, le opzioni di ricerca.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Ricerca delle celle contenenti un valore di stringa specificato o numero**  

È possibile trovare valori stringa specifici chiamando lo stesso metodo [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) presente nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) con vari [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Specifica le proprietà [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) e [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-). Il seguente esempio di codice illustra come utilizzare queste proprietà per trovare celle con un diverso numero di stringhe all'inizio, al centro o alla fine della stringa della cella.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Argomenti avanzati**  
- [Trova celle con stile specifico](/cells/it/nodejs-cpp/find-cells-with-specific-style/)  
- [Verifica se il valore della cella inizia con un apice singolo](/cells/it/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Cerca dati usando valori originali](/cells/it/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
