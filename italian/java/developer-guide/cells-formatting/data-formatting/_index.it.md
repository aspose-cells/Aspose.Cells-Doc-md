---
title: Formattazione dei dati
type: docs
weight: 80
url: /it/java/data-formatting/
---
## **Si avvicina ai dati di formattazione in Cells**
È un fatto comune che se le celle del foglio di lavoro sono formattate correttamente, diventa più facile per gli utenti leggere i contenuti (dati) della cella. Esistono molti modi per formattare le celle e il loro contenuto. Il modo più semplice consiste nel formattare le celle utilizzando Microsoft Excel in un ambiente WYSIWYG durante la creazione di un foglio di calcolo Designer. Dopo aver creato il foglio di calcolo del designer, puoi aprire il foglio di calcolo utilizzando Aspose.Cells mantenendo tutte le impostazioni di formato salvate con il foglio di calcolo. Un altro modo per formattare le celle e il relativo contenuto consiste nell'usare Aspose.Cells API. In questo argomento, descriveremo due approcci per formattare le celle e il relativo contenuto con l'uso di Aspose.Cells API.
### **Formattazione Cells**
 Gli sviluppatori possono formattare le celle e il loro contenuto utilizzando il flessibile API di Aspose.Cells. Aspose.Cells fornisce una classe,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class fornisce una raccolta Cells. Ogni elemento del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)collezione rappresenta un oggetto di**Cell** classe.

 Aspose.Cells fornisce il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) proprietà nel[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class, utilizzato per impostare lo stile di formattazione di una cella. Inoltre, Aspose.Cells fornisce anche a[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) classe utilizzata per lo stesso scopo. Applica diversi tipi di stili di formattazione alle celle per impostare i colori di sfondo o di primo piano, i bordi, i caratteri, gli allineamenti orizzontali e verticali, il livello di rientro, la direzione del testo, l'angolo di rotazione e molto altro.
#### **Utilizzando il metodo setStyle**
 Quando si applicano diversi stili di formattazione a celle diverse, è meglio utilizzare il metodo setStyle di[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe. Di seguito viene fornito un esempio per dimostrare l'uso del metodo setStyle per applicare varie impostazioni di formattazione su una cella.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Utilizzo dell'oggetto stile**
 Quando si applica lo stesso stile di formattazione a celle diverse, utilizzare l'[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) oggetto.

1.  Aggiungere un[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) opporsi alla raccolta Styles del[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) chiamando il metodo createStyle della classe Workbook.
1. Accedi all'oggetto Style appena aggiunto dalla raccolta Styles.
1. Impostare le proprietà desiderate dell'oggetto Style per applicare le impostazioni di formattazione desiderate.
1. Assegna l'oggetto Style configurato alla proprietà Style di qualsiasi cella desiderata.

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare anche memoria.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Applicazione di effetti di riempimento sfumato**
Per applicare alla cella gli effetti di riempimento sfumatura desiderati, utilizzare di conseguenza il metodo setTwoColorGradient dell'oggetto Style.
#### **Esempio di codice**
 Il seguente output si ottiene eseguendo il codice seguente.

**Applicazione di effetti di riempimento sfumato** 

![cose da fare:immagine_alt_testo](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Configurazione delle impostazioni di allineamento**
Chiunque abbia utilizzato Microsoft Excel per formattare le celle avrà familiarità con le impostazioni di allineamento in Microsoft Excel.

**Impostazioni di allineamento in Microsoft Excel** 

![cose da fare:immagine_alt_testo](data-formatting_2.png)

Come puoi vedere dalla figura sopra, ci sono diversi tipi di opzioni di allineamento:

- [Allineamento del testo](/cells/it/java/data-formatting/) (orizzontale verticale)
- [Rientro](/cells/it/java/data-formatting/).
- [Orientamento](/cells/it/java/data-formatting/).
- [Controllo del testo](/cells/it/java/data-formatting/).
- [Direzione del testo](/cells/it/java/data-formatting/).

Tutte queste impostazioni di allineamento sono completamente supportate da Aspose.Cells e sono discusse più dettagliatamente di seguito.
### **Configurazione delle impostazioni di allineamento**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Worksheet fornisce una raccolta Cells. Ogni articolo della collezione Cells rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe.

Aspose.Cells fornisce il metodo setStyle nel file[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe utilizzata per la formattazione di una cella. Il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) class fornisce proprietà utili per la configurazione delle impostazioni dei caratteri.

Selezionare qualsiasi tipo di allineamento del testo utilizzando l'enumerazione TextAlignmentType. I tipi di allineamento del testo predefiniti nell'enumerazione TextAlignmentType sono:

|**Tipi di allineamento del testo**|**Descrizione**|
|:- |:- |
|Parte inferiore|Rappresenta l'allineamento del testo in basso|
|Centro|Rappresenta l'allineamento del testo al centro|
|CenterAcross|Rappresenta il centro rispetto all'allineamento del testo|
|Distribuito|Rappresenta l'allineamento del testo distribuito|
|Riempire|Rappresenta l'allineamento del testo di riempimento|
|Generale|Rappresenta l'allineamento generale del testo|
|Giustificare|Rappresenta giustifica l'allineamento del testo|
|Sono partiti|Rappresenta l'allineamento del testo a sinistra|
|Destra|Rappresenta l'allineamento del testo a destra|
|Superiore|Rappresenta l'allineamento del testo superiore|
{{% alert color="primary" %}} 

È inoltre possibile applicare l'impostazione di giustificazione distribuita utilizzando il metodo Style.setJustifyDistributed().

{{% /alert %}} 
#### **Allineamento orizzontale**
 Utilizzare il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) metodo setHorizontalAlignment dell'oggetto per allineare il testo orizzontalmente.

Il seguente output si ottiene eseguendo il codice di esempio riportato di seguito:

**Allineare il testo orizzontalmente** 

![cose da fare:immagine_alt_testo](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Allineamento verticale**
 Utilizzare il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) metodo setVerticalAlignment dell'oggetto per allineare il testo verticalmente.

L'output seguente viene ottenuto quando VerticalAlignment è impostato su center.

**Allineamento verticale del testo** 

![cose da fare:immagine_alt_testo](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Rientro**
 È possibile impostare il livello di indentazione del testo in una cella utilizzando il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) metodo setIndentLevel dell'oggetto.

Il seguente output viene ottenuto quando IndentLevel è impostato su 2.

**Livello di indentazione regolato a 2** 

![cose da fare:immagine_alt_testo](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientamento**
 Impostare l'orientamento (rotazione) del testo in una cella con il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) metodo setRotationAngle dell'oggetto.

L'output seguente si ottiene quando l'angolo di rotazione è impostato su 25.

**Angolo di rotazione impostato su 25** 

![cose da fare:immagine_alt_testo](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Controllo del testo**
La sezione seguente illustra come controllare il testo impostando il ritorno a capo del testo, la riduzione per adattare e altre opzioni di formattazione.
#### **Testo avvolgente**
Avvolgere il testo in una cella rende più facile la lettura: l'altezza della cella si adatta per adattarsi a tutto il testo, invece di tagliarlo o riversarsi nelle celle adiacenti.

 Attiva o disattiva la disposizione del testo con il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) metodo setTextWrapped dell'oggetto.

L'output seguente viene ottenuto quando è abilitato il ritorno a capo automatico.

**Testo avvolto all'interno della cella** 

![cose da fare:immagine_alt_testo](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Restringimento per adattarsi**
 Un'opzione per avvolgere il testo in un campo consiste nel ridurre le dimensioni del testo per adattarle alle dimensioni di una cella. Questo viene fatto impostando il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) proprietà IsTextWrapped dell'oggetto a**VERO**.

Il seguente output si ottiene quando il testo viene ridotto per adattarsi alla cella.

**Testo ridotto per adattarsi ai limiti della cella** 

![cose da fare:immagine_alt_testo](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Fusione Cells**
Come Microsoft Excel, Aspose.Cells supporta l'unione di più celle in una sola.

L'output seguente si ottiene se le tre celle nella prima riga vengono unite per creare un'unica grande cella.

**Tre celle unite per creare una grande cella** 

![cose da fare:immagine_alt_testo](data-formatting_9.png)

 Utilizzare il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) metodo Merge della raccolta per unire le celle. Il metodo Merge accetta i seguenti parametri:

- Prima riga, la prima riga da cui iniziare l'unione.
- Prima colonna, la prima colonna da cui iniziare l'unione.
- Numero di righe, il numero di righe da unire.
- Numero di colonne, il numero di colonne da unire.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Direzione del testo**
È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati caratteri, parole ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

 L'ordine di lettura è impostato con il[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) proprietà TextDirection dell'oggetto. Aspose.Cells fornisce tipi di direzione del testo predefiniti nell'enumerazione TextDirectionType.

|**Tipi di direzione del testo**|**Descrizione**|
|:- |:- |
|Contesto|L'ordine di lettura coerente con la lingua del primo carattere inserito|
|Da sinistra a destra|Ordine di lettura da sinistra a destra|
|Da destra a sinistra|Ordine di lettura da destra a sinistra|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Il seguente output si ottiene se l'ordine di lettura del testo è impostato da destra a sinistra.

**Impostazione dell'ordine di lettura del testo da destra a sinistra** 

![cose da fare:immagine_alt_testo](data-formatting_10.png)
## **Formattazione dei caratteri selezionati in un Cell**
[Gestione delle impostazioni dei caratteri](/cells/it/java/dealing-with-font-settings/)spiegato come formattare le celle ma solo come formattare il contenuto delle celle wintere. Cosa succede se si desidera formattare solo i caratteri selezionati?

Aspose.Cells supporta questa funzione. Questo argomento spiega come utilizzare questa funzione.
### **Formattazione dei caratteri selezionati**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. La classe Workbook contiene una raccolta di fogli di lavoro che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. La classe Worksheet fornisce una raccolta Cells. Ogni articolo della collezione Cells rappresenta un oggetto della[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe.

La classe Cell fornisce il metodo characters che accetta i seguenti parametri per selezionare un intervallo di caratteri in una cella:

- **Inizio indice**, l'indice del carattere da cui iniziare la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Nel file di output, nella cella A1", la parola 'Visit' è formattata con il carattere predefinito ma 'Aspose!' è in grassetto e blu.

**Formattazione dei caratteri selezionati** 

![cose da fare:immagine_alt_testo](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Se sei interessato a[formattare una porzione di Rich Text in una [cella]](/cells/it/java/access-and-update-the-portions-of-rich-text-of-cell/) , prendere in considerazione l'utilizzo dei metodi Cell.getCharacters e Cell.setCharacters. Il metodo Cell.getCharacters deve essere utilizzato per accedere alle porzioni di testo e quindi le modifiche possono essere apportate utilizzando il metodo Cell.setCharacters mentre il**ottenere** metodo restituisce un array di oggetti FontSetting che possono essere manipolati per impostare varie proprietà nome carattere, colore carattere, grassetto ecc. e**impostare** metodo può essere utilizzato per applicare le modifiche.

{{% /alert %}} 
## **Attivazione di fogli e creazione di un Cell attivo o selezione di un intervallo di Cells nel foglio di lavoro**
volte, potrebbe essere necessario attivare un foglio di lavoro specifico in modo che sia il primo visualizzato quando qualcuno apre il file in Microsoft Excel. Potrebbe anche essere necessario attivare una cella specifica in modo tale che le barre di scorrimento scorrano fino alla cella attiva in modo che sia chiaramente visibile. Aspose.Cells è in grado di svolgere tutte le attività sopra menzionate.

Un foglio attivo è il foglio su cui stai lavorando in una cartella di lavoro. Il nome sulla scheda del foglio attivo è in grassetto per impostazione predefinita. Una cella attiva, nel frattempo, è la cella selezionata e in cui vengono inseriti i dati quando inizi a digitare. È attiva solo una cella alla volta. La cella attiva è circondata da un bordo spesso per farla risaltare rispetto alle altre celle. Aspose.Cells consente inoltre di selezionare un intervallo di celle nel foglio di lavoro.
### **Attivare un foglio e rendere attivo uno Cell**
Aspose.Cells fornisce uno specifico API per questi compiti. Ad esempio, il metodo WorksheetCollection.setActiveSheetIndex è utile per impostare un foglio attivo. Allo stesso modo, il metodo Worksheet.setActiveCell viene utilizzato per impostare e ottenere una cella attiva in un foglio di lavoro.

Se si desidera che le barre di scorrimento orizzontale e verticale scorrano fino alla posizione dell'indice di riga e colonna per offrire una buona visualizzazione dei dati selezionati quando il file viene aperto in Microsoft Excel, utilizzare le proprietà Worksheet.setFirstVisibleRow e Worksheet.setFirstVisibleColumn.

L'esempio seguente mostra come attivare un foglio di lavoro e rendere attiva una cella al suo interno. Le barre di scorrimento vengono fatte scorrere per rendere la seconda riga e la seconda colonna come prima riga e colonna visibili.

**Impostazione della cella B2 come cella attiva** 

![cose da fare:immagine_alt_testo](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Selezionando un intervallo di Cells nel foglio di lavoro**
Aspose.Cells fornisce il metodo Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Utilizzando l'ultimo parametro, removeOthers, su true, le altre selezioni di celle o intervalli di celle nel foglio vengono rimosse.

L'esempio seguente mostra come selezionare un intervallo di celle nel foglio di lavoro attivo.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Tutte le classi e i metodi di cui sopra sono disponibili con la versione con licenza di Aspose.Cells.

{{% /alert %}} 
## **Formattazione di righe e colonne**
La formattazione delle righe e delle colonne in un foglio di calcolo per dare un aspetto al report è probabilmente la funzionalità più utilizzata dell'applicazione Excel. Aspose.Cells Le API forniscono anche questa funzionalità attraverso il suo modello di dati esponendo la classe Style che gestisce principalmente tutte le funzionalità relative allo stile come carattere e suoi attributi, allineamento del testo, colori di sfondo/primo piano, bordi, formato di visualizzazione per numeri e data letterali e così via . Un'altra classe utile fornita dalle API Aspose.Cells è la StyleFlag che consente la riutilizzabilità dell'oggetto Style.

In questo articolo, proveremo a spiegare come utilizzare Aspose.Cells for Java API per applicare la formattazione a righe e colonne.
### **Formattazione di righe e colonne**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe Worksheet. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class fornisce la raccolta Cells. La raccolta Cells fornisce una raccolta Righe.
#### **Formattazione di una riga**
Ogni elemento nella raccolta Rows rappresenta un oggetto Row. L'oggetto Row offre il metodo applyStyle utilizzato per applicare la formattazione a una riga.

Per applicare la stessa formattazione a una riga, utilizza l'oggetto Style:

1. Aggiungi un oggetto Style alla classe Workbook chiamando il relativo metodo createStyle.
1. Impostare le proprietà dell'oggetto Stile per applicare le impostazioni di formattazione.
1. Assegna l'oggetto Style configurato al metodo applyStyle di un oggetto Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formattazione di una colonna**
La raccolta Cells fornisce una raccolta Colonne. Ogni elemento nell'insieme Columns rappresenta un oggetto Column. Simile all'oggetto Row, l'oggetto Column offre il metodo applyStyle utilizzato per impostare la formattazione della colonna. Utilizzare il metodo applyStyle dell'oggetto Column per formattare una colonna allo stesso modo di una riga.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Impostazione del formato di visualizzazione di numeri e date per righe e colonne**
Se il requisito è impostare il formato di visualizzazione di numeri e date per una riga o colonna completa, il processo è più o meno lo stesso discusso sopra, tuttavia, invece di impostare i parametri per i contenuti testuali, imposterai la formattazione per i numeri e le date utilizzando Style.Number o Style.Custom. Si noti che la proprietà Style.Number è di tipo integer e fa riferimento ai formati numerici e data incorporati, mentre la proprietà Style.Custom è di tipo stringa e accetta i modelli validi.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Impostazione dei formati di visualizzazione dei numeri e delle [date]](/cells/it/java/data-formatting/).

{{% /alert %}}
