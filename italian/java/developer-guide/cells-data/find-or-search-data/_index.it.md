---
title: Trova o Cerca Dati
type: docs
weight: 120
url: /it/java/find-or-search-data/
---

{{% alert color="primary" %}} 

In Microsoft Excel, gli utenti possono cercare celle che contengono dati specifici. Ad esempio, facendo clic su **Modifica** e quindi su **Trova** si apre la finestra di ricerca. Gli utenti inseriscono un valore e fanno clic su **OK** per cercarlo. Excel evidenzia i campi corrispondenti.

**Utilizzo della finestra Trova per trovare celle contenenti un valore specifico** 

![todo:image_alt_text](find-or-search-data_1.png)

In questo esempio, il valore di ricerca è "Arance".

Aspose.Cells consente ai programmatori di cercare tra le celle di un foglio di lavoro per trovarne una che contiene un valore specifico.

{{% /alert %}} 
## **Trova celle che contengono dati specifici**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file di Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), una collezione che consente l'accesso a ciascun foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), una raccolta che rappresenta tutte le celle nel foglio di lavoro. La raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fornisce diversi metodi per trovare celle in un foglio di lavoro che contengono dati specificati dall'utente. Alcuni di questi metodi sono discussi di seguito in modo più dettagliato.

Tutti i metodi di ricerca restituiscono i riferimenti delle celle che contengono il valore di ricerca specificato.
## **Ricerca che Contengono una Formula**
I programmatori possono trovare una formula specifica nel foglio di lavoro chiamando il metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), impostando [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) su [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) e passandolo come parametro al metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

Tipicamente, il metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) accetta due o più parametri:

- Oggetto da cercare: rappresenta un oggetto da trovare nel foglio di lavoro.
- Cella precedente: rappresenta la cella precedente con la stessa formula. Questo parametro può essere impostato su null durante la ricerca dall'inizio.
- Opzioni di ricerca: rappresenta i criteri di ricerca. Negli esempi seguenti vengono utilizzati i dati del foglio di lavoro seguenti per praticare i metodi di ricerca:

**Dati di esempio del foglio di lavoro** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Ricerca di Stringhe**
La ricerca di celle che contengono un valore di stringa è semplice e flessibile. Ci sono diversi modi per cercare, ad esempio cercare celle che contengono stringhe che iniziano con un carattere particolare, o un insieme di caratteri.
### **Ricerca di Stringhe che Iniziano con Caratteri Specifici**
Per cercare il primo carattere in una stringa, chiamare il metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), impostare [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) su [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH) e passarlo come parametro al metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Ricerca di Stringhe che Terminano con Caratteri Specifici**
Aspose.Cells può trovare anche stringhe che terminano con caratteri specifici. Per cercare gli ultimi caratteri in una stringa, chiamare il metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), impostare [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) su [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH) e passarlo come parametro al metodo [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Ricerca con Espressioni Regolari: la Funzionalità RegEx**
Un'espressione regolare fornisce un modo conciso e flessibile per corrispondere (specificare e riconoscere) stringhe di testo, come caratteri, parole o modelli particolari.

Ad esempio, il modello di espressione regolare abc-*~~xyz~~ corrisponde alle stringhe "abc-123-xyz", "abc-985-xyz" e "abc-pony-xyz". * è un carattere jolly quindi il modello corrisponde a qualsiasi stringa che inizia con "abc" e termina con "-xyz", indipendentemente dai caratteri presenti nel mezzo.

Aspose.Cells ti consente di cercare con espressioni regolari.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Argomenti avanzati**
- [Trova celle con stile specifico](/cells/it/java/find-cells-with-specific-style/)
- [Cerca dati usando valori originali](/cells/it/java/search-data-using-original-values/)
