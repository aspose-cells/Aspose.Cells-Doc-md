---
title: Formati delle celle
type: docs
weight: 100
url: /it/java/cells-formatting/
---

## **Aggiungere Bordi alle Celle**
Microsoft Excel consente agli utenti di formattare le celle aggiungendo dei bordi.

**Impostazioni dei bordi in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore è quello aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile della linea e il colore dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzarne l'aspetto nello stesso modo flessibile con cui si può fare in Microsoft Excel.
### **Aggiungere Bordi alle Celle**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ciascun elemento nella raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).

Aspose.Cells fornisce il metodo [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#setStyle\(com.aspose.cells.Style\)) nella classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) utilizzato per impostare lo stile di formattazione di una cella. Inoltre, viene utilizzato l'oggetto della classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) che fornisce proprietà per configurare le impostazioni del carattere.
#### **Aggiunta di bordi a una cella**
Aggiungere bordi a una cella con il metodo [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Il tipo di bordo viene passato come parametro. Tutti i tipi di bordo sono predefiniti nell'enumerazione [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**Tipi di bordi**|**Descrizione**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|La linea inferiore dello stesso bordo|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Una linea diagonale dall'angolo in alto a sinistra all'angolo in basso a destra|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Una linea diagonale dall'angolo in basso a sinistra all'angolo in alto a destra|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|La linea del bordo sinistro|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|La linea del bordo destro|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|La linea del bordo superiore|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Solo per lo stile dinamico, come la formattazione condizionale.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Solo per lo stile dinamico, come la formattazione condizionale.|
Per impostare il colore della linea, selezionare un colore utilizzando l'enumerazione [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) e passarlo al parametro Color del metodo [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder(int,%20int,%20com.aspose.cells.Color)) dell'oggetto Style. I tipi di linea sono predefiniti nell'enumerazione [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**Stili di linea**|**Descrizione**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Rappresenta una linea sottile tratteggiata e puntata|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Rappresenta una linea sottile tratteggiata, punteggiata e puntata|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Rappresenta una linea tratteggiata|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Rappresenta una linea punteggiata|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Rappresenta una doppia linea|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Rappresenta una linea sottile|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Rappresenta una linea media tratteggiata e puntata|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Rappresenta una linea media tratteggiata, punteggiata e puntata|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Rappresenta una linea tratteggiata media|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Rappresenta nessuna linea|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Rappresenta una linea media|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Rappresenta una linea tratteggiata inclinata di media grandezza|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Rappresenta una linea spessa|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Rappresenta una linea sottile|
Seleziona uno dei sopracitati stili di linea e poi assegnalo al metodo [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style).

La seguente uscita viene generata eseguendo il codice sottostante.

**Bordi applicati su tutti i lati di una cella** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Aggiunta di bordi a un intervallo di celle**
È possibile aggiungere bordi a un intervallo di celle anziché a una singola cella. Prima, crea un intervallo di celle chiamando il metodo [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), che richiede i seguenti parametri:

- **Prima riga**, la prima riga dell'intervallo.
- **Prima colonna**, la prima colonna dell'intervallo.
- **Numero di righe**, il numero di righe nell'intervallo.
- **Numero di colonne**, il numero di colonne nell'intervallo.

Il metodo [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) restituisce un oggetto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range), che contiene l'intervallo specificato. L'oggetto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) fornisce un metodo [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) che richiede i seguenti parametri:

- **Tipo di bordo cella**, lo stile di linea del bordo, selezionato dall'enumerazione [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- **Colore**, il colore della linea del bordo, selezionato dall'enumerazione [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

La seguente uscita viene generata eseguendo il codice sottostante.

**Bordi applicati su un intervallo di celle** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Colori e Palette**
Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.

**Impostazioni della palette in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

Con Aspose.Cells non è solo possibile utilizzare i colori esistenti ma anche i colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo alla tavolozza. Questo argomento spiega come aggiungere colori personalizzati alla tavolozza.
### **Aggiunta colori personalizzati alla palette**
Aspose.Cells supporta anche una tavolozza di 56 colori. Una tavolozza di colori standard è mostrata sopra. Se si desidera utilizzare un colore personalizzato non definito nella tavolozza, sarà necessario aggiungere tale colore alla tavolozza prima dell'uso.

{{% alert color="primary" %}} 

La tavolozza può contenere solo 56 colori. Quando si aggiunge un colore personalizzato alla tavolozza, questa viene modificata e ogni elemento del file formattato con il colore precedente viene modificato. Quindi, quando si modifica la tavolozza, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato del file XLS (Excel 97 - 2003) poiché non vi è alcuna tale limitazione per i formati di file XLSX o altri formati avanzati di MS Excel (2007/2010).

{{% /alert %}} 

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. La classe fornisce il metodo [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) che prende i seguenti parametri per aggiungere un colore personalizzato per modificare la tavolozza:

- **Colore personalizzato**, il colore personalizzato da aggiungere alla tavolozza.
- **Indice**, l'indice del colore che verrà sostituito con il colore personalizzato. Dovrebbe essere compreso tra 0 e 55.

Nell'esempio seguente viene aggiunto un colore personalizzato alla tavolozza prima di applicarlo a un carattere.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Colori e motivi di sfondo**
Microsoft Excel può impostare i colori di primo piano (contorno) e di sfondo (riempimento) delle celle e i modelli di sfondo come mostrato di seguito.

**Impostazione dei colori e dei Modelli di Sfondo in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento, impariamo ad utilizzare queste funzionalità utilizzando Aspose.Cells.
### **Impostazione di Colori e Modelli di Sfondo**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che permette l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una collezione di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ogni elemento nella collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).

Aspose.Cells fornisce il metodo [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) nella classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) che viene utilizzato per impostare la formattazione di una cella. Inoltre, l'oggetto della classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) può essere utilizzato per configurare le impostazioni del carattere.

{{% alert color="primary" %}} 

Per impostare il colore di primo piano o di sfondo di una cella, utilizzare le proprietà [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) o [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Queste proprietà entrano in vigore solo se la proprietà [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) è configurata.

{{% /alert %}} 

La proprietà [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) imposta il colore dell'ombreggiatura della cella.

La proprietà [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) specifica il modello di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce l'enumerazione [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) che contiene una serie di tipi predefiniti di modelli di sfondo.

|**Tipo di Modello**|**Descrizione**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Rappresenta un modello di incroci diagonali|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Rappresenta un motivo a strisce diagonali|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Rappresenta un motivo grigio al 6,25%|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Rappresenta un motivo grigio al 12,5%|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Rappresenta un motivo grigio al 25%|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Rappresenta un motivo grigio al 50%|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Rappresenta un motivo grigio al 75%|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Rappresenta un motivo a strisce orizzontali|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Rappresenta nessun sfondo|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Rappresenta un motivo a strisce diagonali invertite|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Rappresenta un motivo solido|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Rappresenta un motivo a incroci diagonali spessi|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Rappresenta un motivo a incroci diagonali sottili|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Rappresenta un motivo a strisce diagonali sottili|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Rappresenta un motivo a incroci orizzontali sottili|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Rappresenta un motivo a strisce orizzontali sottili|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Rappresenta un motivo a strisce diagonali invertite sottili|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Rappresenta un motivo a strisce verticali sottili|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Rappresenta un motivo a strisce verticali|
Nell'esempio seguente, il colore dell'oggetto A1 è impostato ma A2 è configurato per avere sia colori di primo piano sia di sfondo con un modello di sfondo a strisce verticali.

L'output seguente viene generato durante l'esecuzione del codice.

**Colori del primo piano e dello sfondo applicati alle celle con pattern di sfondo** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Importante sapere**
{{% alert color="primary" %}} 

- Per impostare il colore del primo piano o lo sfondo di una cella, utilizzare le proprietà [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) o [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Entrambe le proprietà avranno effetto solo se la proprietà [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) dell'oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) è configurata.
- La proprietà [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) imposta il colore della sfumatura della cella.
  La proprietà [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) specifica il tipo di pattern di sfondo utilizzato per il colore del primo piano o dello sfondo. Aspose.Cells fornisce un'enumerazione, [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) che contiene un insieme di tipi predefiniti di pattern di sfondo.
- Se si seleziona il valore [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) dall'enumerazione [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), il colore del primo piano non viene applicato.
  Allo stesso modo, il colore di sfondo non viene applicato se si selezionano i valori [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) o [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID).
- Quando si recupera il colore di riempimento di una cella, se [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) è [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) restituirà *Color.Empty*.

{{% /alert %}} 
## **Formattazione dei caratteri selezionati in una cella**
[Gestione delle impostazioni del carattere](/cells/it/java/gestione-delle-impostazioni-del-carattere/) ha spiegato come formattare le celle ma solo come formattare il contenuto delle intere celle. Cosa fare se si desidera formattare solo alcuni caratteri?

Aspose.Cells supporta questa funzione. Questo argomento spiega come utilizzare questa funzione.
### **Formattazione dei caratteri selezionati**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che permette l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una collezione di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ogni elemento nella collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).

La classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) fornisce un metodo [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) che prende i seguenti parametri per selezionare un intervallo di caratteri in una cella:

- **Indice di inizio**, l'indice del carattere da cui iniziare la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Nel file di output, nella cella A1, la parola 'Visita' è formattata con il carattere predefinito ma 'Aspose!' è in grassetto e blu.

**Formattazione dei caratteri selezionati** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Se sei interessato a [formattare una parte del testo ricco in una cella](/cells/it/java/access-and-update-the-portions-of-rich-text-of-cell/), considera l'utilizzo dei metodi [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) e Cell.setCharacters. Il metodo [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) deve essere utilizzato per accedere alle porzioni di testo e quindi possono essere apportate modifiche utilizzando il metodo Cell.setCharacters, mentre il metodo **get** restituisce un array di oggetti [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) che possono essere manipolati per impostare diverse proprietà come il nome del carattere, il colore del carattere, il grassetto, ecc. e il metodo **set** può essere utilizzato per applicare le modifiche.

{{% /alert %}}

## **Argomenti avanzati**
- [Impostazioni di Allineamento](/cells/it/java/cells-alignment-settings/)
- [Formattazione condizionale](/cells/it/java/conditional-formatting/)
- [Formattazione dei dati](/cells/it/java/data-formatting/)
- [Temi e Colori di Excel](/cells/it/java/excel-2007-themes-and-colors/)
- [Gestione delle impostazioni del carattere](/cells/it/java/dealing-with-font-settings/)
- [Formattare le Celle di un Foglio di Lavoro in un Documento di Lavoro](/cells/it/java/format-worksheet-cells-in-a-workbook/)
- [Implementare il Sistema di Data 1904](/cells/it/java/implement-1904-date-system/)
- [Unione e separazione di celle](/cells/it/java/merging-and-unmerging-cells/)
- [Impostazioni dei numeri](/cells/it/java/cells-number-settings/)
- [Conserva il prefisso apice singolo del valore della cella o dell'intervallo](/cells/it/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Stile e formattazione dei dati](/cells/it/java/styling-and-data-formatting/)
