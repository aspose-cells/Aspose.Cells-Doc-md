---
title: Trova o cerca dati
type: docs
weight: 120
url: /it/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 In Microsoft Excel, gli utenti possono cercare celle che contengono dati specifici. Ad esempio, facendo clic**Modificare** e poi**Trova** apre la finestra di dialogo Cerca. Gli utenti immettono un valore e fanno clic**OK** per cercarlo. Excel evidenzia i campi corrispondenti.

**Utilizzo della finestra di dialogo Trova per trovare celle contenenti un valore specifico** 

![cose da fare:immagine_alt_testo](find-or-search-data_1.png)

In questo esempio, il valore di ricerca è "Arance".

Aspose.Cells consente agli sviluppatori di cercare tra le celle in un foglio di lavoro per trovare quelle che contengono un determinato valore.

{{% /alert %}} 
## **Trovare Cells che contengono dati specifici**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , che rappresenta un file Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) classe contiene[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , una raccolta che consente l'accesso a ciascuno dei fogli di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe.

 Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , una raccolta che rappresenta tutte le celle del foglio di lavoro[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fornisce diversi metodi per trovare celle in un foglio di lavoro che contengono dati specificati dall'utente. Alcuni di questi metodi sono discussi di seguito in modo più dettagliato.

Tutti i metodi find restituiscono i riferimenti di cella per tutte le celle che contengono il valore di ricerca specificato.
## **Trovare contenente una formula**
 Gli sviluppatori possono trovare una formula specificata nel foglio di lavoro chiamando il metodo[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ) metodo, impostando il[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) a[LookInType.FORMULE](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) passandolo come parametro al file[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metodo.

 Tipicamente, il[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) accetta due o più parametri:

- Oggetto da cercare: rappresenta un oggetto che è necessario trovare nel foglio di lavoro.
- Il precedente Cell: rappresenta la cella precedente con la stessa formula. Questo parametro può essere impostato su null durante la ricerca dall'inizio.
- Opzioni di ricerca: rappresenta i criteri di ricerca. Negli esempi seguenti, i seguenti dati del foglio di lavoro vengono utilizzati per esercitarsi con i metodi di ricerca:

**Esempio di dati del foglio di lavoro** 

![cose da fare:immagine_alt_testo](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Alla ricerca di stringhe**
La ricerca di celle che contengono un valore stringa è semplice e flessibile. Esistono diversi modi di ricerca, ad esempio cercare celle che contengono stringhe che iniziano con un determinato carattere o insieme di caratteri.
### **Ricerca di stringhe che iniziano con caratteri specifici**
 Per cercare il primo carattere in una stringa, chiama il metodo[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), impostare il metodo[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) a[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)passarlo come parametro al file[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Ricerca di stringhe che terminano con caratteri specifici**
 Aspose.Cells può anche trovare stringhe che terminano con caratteri specifici. Per cercare gli ultimi caratteri in una stringa, chiama il metodo[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), impostare il metodo[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) a[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)passarlo come parametro al file[Trovare](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Ricerca con espressioni regolari: la funzione RegEx**
Un'espressione regolare fornisce un mezzo conciso e flessibile per confrontare (specificare e riconoscere) stringhe di testo, come particolari caratteri, parole o modelli.

Ad esempio, il modello di espressione regolare abc-* ~~xyz~~ corrisponde alle stringhe "abc-123-xyz", "abc-985-xyz" e "abc-pony-xyz".* è un carattere jolly, quindi il modello corrisponde a tutte le stringhe che iniziano con "abc" e terminano con "-xyz", indipendentemente dai caratteri al centro.

Aspose.Cells consente di effettuare ricerche con espressioni regolari.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Argomenti avanzati**
- [Trova le celle con uno stile specifico](/cells/it/java/find-cells-with-specific-style/)
- [Cerca i dati utilizzando i valori originali](/cells/it/java/search-data-using-original-values/)
