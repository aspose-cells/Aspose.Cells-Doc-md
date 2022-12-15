---
title: Cells Formati
type: docs
weight: 100
url: /it/java/cells-formatting/
---
## **Aggiunta di bordi a Cells**
Microsoft Excel consente agli utenti di formattare le celle aggiungendo bordi.

**Impostazioni dei bordi in Microsoft Excel** 

![cose da fare:immagine_alt_testo](cells-formatting_1.png)

Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile e il colore della linea dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzare il loro aspetto nello stesso modo flessibile di Microsoft Excel.
### **Aggiunta di bordi a Cells**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Aspose.Cells fornisce il[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) metodo nel[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe utilizzata per impostare lo stile di formattazione di una cella. Inoltre, l'oggetto del[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style)viene utilizzata la classe e fornisce le proprietà per la configurazione delle impostazioni dei caratteri.
#### **Aggiunta di bordi a un numero Cell**
 Aggiungi bordi a una cella con il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style) dell'oggetto[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) metodo. Il tipo di bordo viene passato come parametro. Tutti i tipi di bordo sono predefiniti nel file[Tipo di bordo](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)enumerazione.

|**Tipi di bordo**|**Descrizione**|
|:- |:- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|La linea di confine inferiore|
|[DIAGONALE_GIÙ](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Una linea diagonale da sinistra in alto a destra in basso|
|[DIAGONALE_SU](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Una linea diagonale da sinistra in basso a destra in alto|
|[BORDO_SINISTRO](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|La linea di confine sinistra|
|[BORDO_DESTRO](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|La giusta linea di confine|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|La linea di confine superiore|
|[ORIZZONTALE](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Solo per lo stile dinamico, come la formattazione condizionale.|
|[VERTICALE](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Solo per lo stile dinamico, come la formattazione condizionale.|
 Per impostare il colore della linea, selezionare un colore utilizzando il[Colore](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enumerazione e passarlo al[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style) dell'oggetto[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) parametro Color del metodo. Gli stili di linea sono predefiniti nel file[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)enumerazione.

|**Stili di linea**|**Descrizione**|
|:- |:- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Rappresenta una sottile linea tratteggiata|
|[TRATTINO_PUNTO_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Rappresenta una sottile linea tratteggiata-punto-punteggiata|
|[TRATTATO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Rappresenta la linea tratteggiata|
|[PUNTEGGIATO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Rappresenta la linea tratteggiata|
|[DOPPIO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Rappresenta la doppia linea|
|[CAPELLI](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Rappresenta la linea dei capelli|
|[MEDIO_TRATTINO_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Rappresenta una linea tratteggiata media|
|[MEDIO_TRATTINO_PUNTO_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Rappresenta la linea tratteggiata-punto-punteggiata media|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Rappresenta la linea tratteggiata media|
|[NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Non rappresenta alcuna linea|
|[MEDIO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Rappresenta la linea media|
|[INCLINATO_TRATTINO_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Rappresenta una linea tratteggiata media obliqua|
|[SPESSO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Rappresenta la linea spessa|
|[SOTTILE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Rappresenta la linea sottile|
 Selezionare uno degli stili di linea di cui sopra e quindi assegnarlo a[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style)dell'oggetto[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) metodo.

Il seguente output viene generato durante l'esecuzione del codice seguente.

**Bordi applicati su tutti i lati di una cella** 

![cose da fare:immagine_alt_testo](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Aggiunta di bordi a un intervallo di Cells**
 È possibile aggiungere bordi a un intervallo di celle piuttosto che a una singola cella. Innanzitutto, crea un intervallo di celle chiamando il metodo[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), che accetta i seguenti parametri:

- **Prima riga**, la prima riga dell'intervallo.
- **Prima Colonna**, la prima colonna dell'intervallo.
- **Numero di righe**, il numero di righe nell'intervallo.
- **Numero di colonne**, il numero di colonne nell'intervallo.

 Il[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) metodo restituisce a[Gamma](https://reference.aspose.com/cells/java/com.aspose.cells/Range) oggetto, che contiene l'intervallo specificato. Il[Gamma](https://reference.aspose.com/cells/java/com.aspose.cells/Range) oggetto fornisce a[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) metodo che accetta i seguenti parametri:

- **CellBorderType**, lo stile della linea del bordo, selezionato da[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)enumerazione.
- **Colore**, il colore della linea del bordo, selezionato da[Colore](https://reference.aspose.com/cells/java/com.aspose.cells/Color)enumerazione.

Il seguente output viene generato durante l'esecuzione del codice seguente.

**Bordi applicati su un intervallo di celle** 

![cose da fare:immagine_alt_testo](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Colori e tavolozza**
Una tavolozza è il numero di colori disponibili per l'uso nella creazione di un'immagine. L'uso di una tavolozza standardizzata in una presentazione consente all'utente di creare un aspetto coerente. Ogni file di Microsoft Excel (97-2003) dispone di una tavolozza di 56 colori che possono essere applicati a celle, caratteri, griglie, oggetti grafici, riempimenti e linee in un grafico.

**Impostazioni della tavolozza in Microsoft Excel** 

![cose da fare:immagine_alt_testo](cells-formatting_4.png)

Con Aspose.Cells non solo è possibile utilizzare colori esistenti ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo alla tavolozza. Questo argomento spiega come aggiungere colori personalizzati alla tavolozza.
### **Aggiunta di colori personalizzati alla tavolozza**
Aspose.Cells supporta anche una tavolozza di 56 colori. Una tavolozza di colori standard è mostrata sopra. Se desideri utilizzare un colore personalizzato che non è definito nella tavolozza, dovrai aggiungere quel colore alla tavolozza prima dell'uso.

{{% alert color="primary" %}} 

La tavolozza contiene solo 56 colori. Quando aggiungi un colore personalizzato alla tavolozza, la tavolozza viene modificata e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando cambi la tavolozza, fai molta attenzione. Inoltre, questa è la limitazione solo nel formato di file XLS (Excel 97 - 2003) poiché non esiste tale limitazione per XLSX o altri formati di file avanzati MS Excel (2007/2010).

{{% /alert %}} 

Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. La classe fornisce il[changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) metodo che accetta i seguenti parametri per aggiungere un colore personalizzato per modificare la tavolozza:

- **Colore personalizzato**, il colore personalizzato da aggiungere alla tavolozza.
- **Indice**, l'indice del colore che verrà sostituito con il colore personalizzato. Dovrebbe essere compreso tra 0 e 55.

L'esempio seguente aggiunge un colore personalizzato alla tavolozza prima di applicarlo a un font.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Colori e motivi di sfondo**
Microsoft Excel può impostare i colori di primo piano (contorno) e di sfondo (riempimento) delle celle e dei motivi di sfondo come mostrato di seguito.

**Impostazione di colori e motivi di sfondo in Microsoft Excel** 

![cose da fare:immagine_alt_testo](cells-formatting_5.png)

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento, impariamo a utilizzare queste funzionalità utilizzando Aspose.Cells.
### **Impostazione di colori e motivi di sfondo**
Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

Aspose.Cells fornisce il[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) metodo nel[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe utilizzata per impostare la formattazione di una cella. Inoltre, l'oggetto del[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class può essere utilizzato per configurare le impostazioni dei caratteri.

{{% alert color="primary" %}} 

 Per impostare il colore di primo piano o di sfondo di una cella, utilizzare il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style) dell'oggetto[imposta Colore di sfondo](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) o[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) proprietà. Queste proprietà entrano in vigore solo se il file[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style) dell'oggetto[Impostare il modello](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) proprietà è configurata.

{{% /alert %}} 

Il[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)La proprietà imposta il colore dell'ombreggiatura della cella.

Il[Impostare il modello](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) La proprietà specifica il motivo di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce il[Tipo di sfondo](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)enumerazione che contiene una serie di tipi predefiniti di motivi di sfondo.

|**Tipo di motivo**|**Descrizione**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Rappresenta il modello di tratteggio incrociato diagonale|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Rappresenta il motivo a strisce diagonali|
|[GRIGIO_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Rappresenta il motivo grigio al 6,25%.|
|[GRIGIO_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Rappresenta il motivo grigio al 12,5%.|
|[GRIGIO_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Rappresenta il motivo grigio al 25%.|
|[GRIGIO_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Rappresenta il motivo grigio al 50%.|
|[GRIGIO_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Rappresenta il motivo grigio al 75%.|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Rappresenta il motivo a strisce orizzontali|
|[NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Non rappresenta alcuno sfondo|
|[INVERSIONE_DIAGONALE_BANDA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Rappresenta il motivo a strisce diagonali inverse|
|[SOLIDO](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Rappresenta un modello solido|
|[SPESSO_DIAGONALE_TRATTATURA INCROCIATA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Rappresenta un motivo a tratteggio incrociato diagonale spesso|
|[SOTTILE_DIAGONALE_TRATTATURA INCROCIATA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Rappresenta un motivo a tratteggio diagonale sottile|
|[SOTTILE_DIAGONALE_BANDA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Rappresenta il motivo a strisce diagonali sottili|
|[SOTTILE_ORIZZONTALE_TRATTATURA INCROCIATA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Rappresenta un motivo a tratteggio incrociato orizzontale sottile|
|[SOTTILE_ORIZZONTALE_BANDA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Rappresenta un motivo a strisce orizzontali sottili|
|[SOTTILE_INVERSIONE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Rappresenta un sottile motivo a strisce diagonali inverse|
|[SOTTILE_VERTICALE_BANDA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Rappresenta un motivo a strisce verticali sottili|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Rappresenta il motivo a strisce verticali|
Nell'esempio seguente, il colore di primo piano della cella A1 è impostato ma A2 è configurato per avere sia i colori di primo piano che di sfondo con un motivo di sfondo a strisce verticali.

Il seguente output viene generato durante l'esecuzione del codice.

**Colori di primo piano e di sfondo applicati alle celle con motivi di sfondo** 

![cose da fare:immagine_alt_testo](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Importante da sapere**
{{% alert color="primary" %}} 

-  Per impostare il colore di primo piano o di sfondo di una cella, utilizzare il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style) dell'oggetto[Colore di primo piano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) o[Colore di sfondo](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) proprietà. Entrambe le proprietà avranno effetto solo se il file[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/Style) dell'oggetto[Modello](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) proprietà è configurata.
-  Il[Colore di primo piano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) La proprietà imposta il colore dell'ombreggiatura della cella.
 Il[Modello](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) La proprietà specifica il tipo di motivo di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce un'enumerazione,[Tipo di sfondo](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)che contiene una serie di tipi predefiniti di motivi di sfondo.
-  Se selezioni[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) valore dal[Tipo di sfondo](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) enumerazione, il colore di primo piano non viene applicato.
 Allo stesso modo, il colore di sfondo non viene applicato se si seleziona il file[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) o[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) i valori.
-  Quando si recupera il colore di ombreggiatura/riempimento della cella, if[Stile.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) è[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) tornerà*Colore.Vuoto*.

{{% /alert %}} 
## **Formattazione dei caratteri selezionati in un Cell**
[Gestione delle impostazioni dei caratteri](/cells/it/java/dealing-with-font-settings/) spiegato come formattare le celle ma solo come formattare il contenuto di intere celle. Cosa succede se si desidera formattare solo i caratteri selezionati?

Aspose.Cells supporta questa funzione. Questo argomento spiega come utilizzare questa funzione.
### **Formattazione dei caratteri selezionati**
Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

Il[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) la classe fornisce[personaggi](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) metodo che accetta i seguenti parametri per selezionare un intervallo di caratteri in una cella:

- **Inizio indice**, l'indice del carattere da cui iniziare la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Nel file di output, nella cella A1", la parola 'Visit' è formattata con il carattere predefinito ma 'Aspose!' è in grassetto e blu.

**Formattazione dei caratteri selezionati** 

![cose da fare:immagine_alt_testo](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Se sei interessato a[formattare una porzione di Rich Text in una cella](/cells/it/java/access-and-update-the-portions-of-rich-text-of-cell/) , considera l'utilizzo di[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) & Cell.setCharacters metodi. Il[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) deve essere utilizzato per accedere alle parti del testo e quindi le modifiche possono essere apportate utilizzando il metodo Cell.setCharacters mentre il metodo**ottenere**metodo restituisce un array di[Impostazione carattere](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) oggetti che possono essere manipolati per impostare varie proprietà come nome del carattere, colore del carattere, grassetto, ecc**impostare** metodo può essere utilizzato per applicare le modifiche.

{{% /alert %}}

## **Argomenti avanzati**
- [Impostazioni di allineamento](/cells/it/java/cells-alignment-settings/)
- [Formattazione condizionale](/cells/it/java/conditional-formatting/)
- [Formattazione dei dati](/cells/it/java/data-formatting/)
- [Temi e colori di Excel](/cells/it/java/excel-2007-themes-and-colors/)
- [Gestione delle impostazioni dei caratteri](/cells/it/java/dealing-with-font-settings/)
- [Formattare il foglio di lavoro Cells in una cartella di lavoro](/cells/it/java/format-worksheet-cells-in-a-workbook/)
- [Implementare il sistema di data 1904](/cells/it/java/implement-1904-date-system/)
- [Fusione e Separazione Cells](/cells/it/java/merging-and-unmerging-cells/)
- [Impostazioni numero](/cells/it/java/cells-number-settings/)
- [Conserva il prefisso delle virgolette singole del valore o intervallo Cell](/cells/it/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Stile e formattazione dei dati](/cells/it/java/styling-and-data-formatting/)
