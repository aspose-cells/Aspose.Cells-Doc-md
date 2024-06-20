---
title: Formattazione dei dati
type: docs
weight: 80
url: /it/java/data-formatting/
---

## **Approcci per Formattare i Dati nelle Celle**
È un fatto comune che se le celle del foglio di lavoro sono formattate correttamente, diventa più facile per gli utenti leggere i contenuti (dati) della cella. Ci sono molti modi per formattare le celle e i loro contenuti. Il modo più semplice è quello di formattare le celle utilizzando Microsoft Excel in un ambiente WYSIWYG durante la creazione di un Foglio di Calcolo del Designer. Dopo aver creato il foglio di calcolo del designer, è possibile aprire il foglio di calcolo utilizzando Aspose.Cells mantenendo tutte le impostazioni di formato salvate con il foglio di calcolo. Un altro modo per formattare le celle e i loro contenuti è utilizzare l'API Aspose.Cells. In questo argomento, descriveremo due approcci per formattare le celle e i loro contenuti con l'uso dell'API Aspose.Cells.
### **Formattazione celle**
I programmatori possono formattare le celle e i loro contenuti utilizzando l'API flessibile di Aspose.Cells. Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una raccolta di celle. Ciascun elemento nella raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) rappresenta un oggetto della classe **Cell**.

Aspose.Cells fornisce la proprietà [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nella classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), utilizzata per impostare lo stile di formattazione di una cella. Inoltre, Aspose.Cells fornisce anche una classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) che viene utilizzata per lo stesso scopo. Applicare diversi tipi di stili di formattazione alle celle per impostare i loro colori di sfondo o primo piano, i bordi, i caratteri, l'allineamento orizzontale e verticale, il livello di rientro, la direzione del testo, l'angolo di rotazione e molto altro.
#### **Utilizzo del metodo setStyle**
Quando si applicano stili di formattazione diversi a celle diverse, è meglio utilizzare il metodo setStyle della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Di seguito è riportato un esempio per dimostrare l'uso del metodo setStyle per applicare varie impostazioni di formattazione su una cella.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Utilizzo dell'oggetto Style**
Quando si applica lo stesso stile di formattazione a celle diverse, utilizzare l'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

1. Aggiungere un oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) alla raccolta Styles della classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) chiamando il metodo createStyle della classe Workbook.
1. Accedi al nuovo oggetto Style aggiunto dalla collezione Styles.
1. Imposta le proprietà desiderate dell'oggetto Style per applicare le impostazioni di formattazione desiderate.
1. Assegna l'oggetto Style configurato alla proprietà Style di qualsiasi cella desiderata.

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare memoria anche.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Applicazione degli effetti di riempimento a sfumatura**
Per applicare i tuoi desiderati effetti di riempimento gradiente alla cella, utilizza il metodo setTwoColorGradient dell'oggetto Style di conseguenza.
#### **Esempio di codice**
L'output seguente è ottenuto eseguendo il codice sottostante. 

**Applicazione degli effetti di riempimento gradiente** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Configurazione delle impostazioni di allineamento**
Chiunque abbia usato Microsoft Excel per formattare le celle sarà familiare con le impostazioni di allineamento in Microsoft Excel.

**Impostazioni di allineamento in Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Come si può vedere dalla figura sopra, ci sono diversi tipi di opzioni di allineamento:

- [Allineamento del testo](/cells/it/java/data-formatting/) (orizzontale e verticale)
- [Rientro](/cells/it/java/data-formatting/).
- [Orientamento](/cells/it/java/data-formatting/).
- [Controllo testo](/cells/it/java/data-formatting/).
- [Direzione del testo](/cells/it/java/data-formatting/).

Tutte queste impostazioni di allineamento sono completamente supportate da Aspose.Cells e sono discusse in modo più dettagliato di seguito.
### **Configurazione delle impostazioni di allineamento**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Excel. La classe Workbook contiene una WorksheetCollection che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fornisce una raccolta di celle. Ogni elemento nella raccolta di celle rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells fornisce il metodo setStyle nella classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) che viene utilizzato per formattare la cella. La classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) fornisce utili proprietà per configurare le impostazioni del font.

Seleziona qualsiasi tipo di allineamento del testo utilizzando l'enumerazione TextAlignmentType. I tipi di allineamento del testo predefiniti nell'enumerazione TextAlignmentType sono:

|**Tipi di Allineamento del Testo**|**Descrizione**|
| :- | :- |
|Bottom|Rappresenta l'allineamento del testo in basso|
|Center|Rappresenta l'allineamento del testo al centro|
|CenterAcross|Rappresenta l'allineamento del testo al centro tra le celle|
|Distributed|Rappresenta l'allineamento distribuito del testo|
|Fill|Rappresenta l'allineamento di riempimento del testo|
|General|Rappresenta l'allineamento del testo generale|
|Justify|Rappresenta l'allineamento del testo giustificato|
|Left|Rappresenta l'allineamento del testo a sinistra|
|Right|Rappresenta l'allineamento del testo a destra|
|Top|Rappresenta l'allineamento del testo in alto|
{{% alert color="primary" %}} 

È anche possibile applicare l'impostazione giustifica distribuita utilizzando il metodo Style.setJustifyDistributed().

{{% /alert %}} 
#### **Allineamento Orizzontale**
Utilizza il metodo setHorizontalAlignment dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) per allineare il testo orizzontalmente.

Il seguente output è ottenuto eseguendo il codice di esempio qui sotto:

**Allineamento del testo orizzontalmente** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Allineamento Verticale**
Utilizza il metodo setVerticalAlignment dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) per allineare il testo verticalmente.

Il risultato seguente viene ottenuto quando VerticalAlignment è impostato su centro.

**Allineamento del testo verticalmente** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Rientro**
È possibile impostare il livello di rientro del testo in una cella utilizzando il metodo setIndentLevel dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Il risultato seguente viene ottenuto quando IndentLevel è impostato su 2.

**Livello di rientro regolato su 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientamento**
Imposta l'orientamento (rotazione) del testo in una cella con il metodo setRotationAngle dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Il risultato seguente viene ottenuto quando l'angolo di rotazione è impostato su 25.

**Angolo di rotazione impostato su 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Controllo del Testo**
La seguente sezione discute come controllare il testo impostando il rientro del testo, adattamento alla cella e altre opzioni di formattazione.
#### **Testo a Capo**
Il word wrap del testo in una cella rende più facile la lettura: l'altezza della cella si adatta a tutto il testo, anziché tagliarlo o farlo traboccare nelle celle adiacenti.

Attiva o disattiva il word wrap con il metodo setTextWrapped dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Il risultato seguente viene ottenuto quando il word wrap è abilitato.

**Testo avvolto all'interno della cella** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Ridimensionamento per adattarsi**
Un'opzione per il word wrap in un campo è ridurre la dimensione del testo per adattarlo alle dimensioni di una cella. Questo avviene impostando la proprietà IsTextWrapped dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) su **true**.

Il seguente output è ottenuto quando il testo viene ridotto per adattarsi alla cella.

**Testo ridotto per adattarsi all'interno dei limiti della cella** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Unione di celle**
Come Microsoft Excel, Aspose.Cells supporta l'unione di più celle in una sola.

Il seguente output è ottenuto se le tre celle nella prima riga vengono unite per creare una grande cella singola.

**Tre celle unite per creare una grande cella** 

![todo:image_alt_text](data-formatting_9.png)

Usa il metodo di unione della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) per unire le celle. Il metodo di unione prende i seguenti parametri:

- Prima riga, la prima riga da cui iniziare a unire.
- Prima colonna, la prima colonna da cui iniziare a unire.
- Numero di righe, il numero di righe da unire.
- Numero di colonne, il numero di colonne da unire.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Direzione del testo**
È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui caratteri, parole, ecc. vengono visualizzati. Ad esempio, l'inglese è una lingua da sinistra a destra, mentre l'arabo è una lingua da destra a sinistra.

L'ordine di lettura viene impostato con la proprietà TextDirection dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style). Aspose.Cells fornisce tipi di direzione del testo predefiniti nell'enumerazione TextDirectionType.

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|Context| L'ordine di lettura coerente con la lingua del primo carattere inserito|
|LeftToRight| Ordine di lettura da sinistra a destra|
|RightToLeft| Ordine di lettura da destra a sinistra|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Il seguente output è ottenuto se l'ordine di lettura del testo è impostato da destra a sinistra.

**Impostazione dell'ordine di lettura del testo da destra a sinistra** 

![todo:image_alt_text](data-formatting_10.png)
## **Formattazione dei caratteri selezionati in una cella**
[Gestione delle impostazioni del carattere](/cells/it/java/dealing-with-font-settings/) spiega come formattare le celle ma solo come formattare il contenuto delle intere celle. E se si vuole formattare solo alcuni caratteri selezionati?

Aspose.Cells supporta questa funzione. Questo argomento spiega come utilizzare questa funzione.
### **Formattazione dei caratteri selezionati**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene una raccolta di Fogli di lavoro che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe Worksheet fornisce una raccolta di celle. Ogni elemento nella raccolta di celle rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La classe Cell fornisce un metodo caratteri che accetta i seguenti parametri per selezionare un intervallo di caratteri in una cella:

- **Indice di inizio**, l'indice del carattere da cui iniziare la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Nel file di output, nella cella A1, la parola 'Visita' è formattata con il carattere predefinito ma 'Aspose!' è in grassetto e blu.

**Formattazione dei caratteri selezionati** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Se sei interessato a [formattare una parte del testo formattato in una [cella](/cells/it/java/access-and-update-the-portions-of-rich-text-of-cell/), considera di utilizzare i metodi Cell.getCharacters & Cell.setCharacters. Il metodo Cell.getCharacters è utilizzato per accedere alle parti del testo e poi è possibile apportare modifiche utilizzando il metodo Cell.setCharacters, mentre il metodo **get** restituisce un array di oggetti FontSetting che possono essere manipolati per impostare varie proprietà quali nome del font, colore del font, grassetto ecc e il metodo **set** può essere utilizzato per applicare le modifiche.

{{% /alert %}} 
## **Attivazione dei Fogli e Creazione di una Cella Attiva o Selezione di un Intervallo di Celle nel Foglio di lavoro**
A volte potresti aver bisogno di attivare un foglio di lavoro specifico in modo che sia il primo visualizzato quando qualcuno apre il file in Microsoft Excel. Potresti anche aver bisogno di attivare una cella specifica in modo che le barre di scorrimento si spostino sulla cella attiva in modo che sia chiaramente visibile. Aspose.Cells è in grado di fare tutti i compiti sopra menzionati.

Un foglio attivo è il foglio su cui stai lavorando in un workbook. Il nome sulla scheda del foglio attivo è in grassetto per impostazione predefinita. Una cella attiva, invece, è la cella selezionata e in cui vengono inseriti i dati quando si inizia a digitare. Solo una cella è attiva alla volta. La cella attiva è circondata da un bordo spesso per renderla visibile rispetto alle altre celle. Aspose.Cells ti consente anche di selezionare un intervallo di celle nel foglio di lavoro.
### **Attivare un Foglio e Rendere una Cella Attiva**
Aspose.Cells fornisce un'API specifica per queste attività. Ad esempio, il metodo WorksheetCollection.setActiveSheetIndex è utile per impostare un foglio attivo. Allo stesso modo, il metodo Worksheet.setActiveCell viene utilizzato per impostare e recuperare una cella attiva in un foglio di lavoro.

Se desideri che le barre di scorrimento orizzontale e verticale si spostino sulla posizione dell'indice di riga e colonna per dare una buona visualizzazione dei dati selezionati quando il file viene aperto in Microsoft Excel, utilizza le proprietà Worksheet.setFirstVisibleRow e Worksheet.setFirstVisibleColumn.

Nell'esempio seguente è mostrato come attivare un foglio di lavoro e fare in modo che una cella in esso sia attiva. Le barre di scorrimento sono spostate per fare in modo che la 2a riga e la 2a colonna siano la loro prima riga e colonna visibile.

**Impostare la cella B2 come una cella attiva** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Selezione di un Intervallo di Celle nel Foglio di lavoro**
Aspose.Cells fornisce il metodo Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Utilizzando l'ultimo parametro - removeOthers - su true, vengono rimossi altri selezioni di celle o intervalli di celle nel foglio.

L'esempio seguente mostra come selezionare un intervallo di celle nella scheda attiva.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Tutte le classi e i metodi sopra citati sono disponibili nella versione con licenza di Aspose.Cells.

{{% /alert %}} 
## **Formattazione righe e colonne**
La formattazione delle righe e delle colonne in un foglio di calcolo per dare un aspetto al report è probabilmente la funzionalità più utilizzata dell'applicazione Excel. Le API di Aspose.Cells forniscono anche questa funzionalità attraverso il suo modello di dati esponendo la classe Style che gestisce principalmente tutte le funzionalità relative allo stile come il font e i suoi attributi, l'allineamento del testo, i colori di sfondo/primo piano, i bordi, il formato di visualizzazione per numeri e letterali delle date e così via. Un'altra utile classe fornita dalle API di Aspose.Cells è StyleFlag che consente il riuso dell'oggetto Style. 

In questo articolo cercheremo di spiegare come utilizzare l'API Aspose.Cells for Java per applicare la formattazione alle righe e alle colonne. 
### **Formattare Righe e Colonne**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una WorksheetCollection che consente l'accesso a ciascuna scheda nel file Excel. Una scheda è rappresentata dalla classe Worksheet. La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce la collezione Cells. La collezione Cells fornisce una collezione Rows.
#### **Formattazione di una riga**
Ogni elemento nella collezione Rows rappresenta un oggetto di tipo Row. L'oggetto Row offre il metodo applyStyle utilizzato per applicare la formattazione a una riga.

Per applicare la stessa formattazione a una riga, utilizzare l'oggetto Style:

1. Aggiungere un oggetto Style alla classe Workbook chiamando il suo metodo createStyle.
2. Impostare le proprietà dell'oggetto Style per applicare le impostazioni di formattazione.
3. Assegnare l'oggetto Style configurato al metodo applyStyle di un oggetto Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formattazione di una colonna**
La collezione Cells fornisce una collezione Columns. Ogni elemento nella collezione Columns rappresenta un oggetto di tipo Column. Similmente all'oggetto Row, l'oggetto Column offre il metodo applyStyle utilizzato per impostare la formattazione della colonna. Utilizzare il metodo applyStyle dell'oggetto Column per formattare una colonna allo stesso modo di una riga.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Impostazione del formato di visualizzazione dei numeri e delle date per righe e colonne**
Se il requisito è impostare il formato di visualizzazione di numeri e date per un'intera riga o colonna, il processo è più o meno lo stesso come discusso sopra, tuttavia, anziché impostare i parametri per i contenuti testuali, si imposterà la formattazione per numeri e date utilizzando Style.Number o Style.Custom. Si noti che la proprietà Style.Number è di tipo intero e si riferisce ai formati numerici e di data incorporati, mentre la proprietà Style.Custom è di tipo stringa e accetta i pattern validi.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

Si prega di consultare l'articolo dettagliato su [Impostazione dei formati di visualizzazione dei numeri e [Date](/cells/it/java/data-formatting/).

{{% /alert %}}
