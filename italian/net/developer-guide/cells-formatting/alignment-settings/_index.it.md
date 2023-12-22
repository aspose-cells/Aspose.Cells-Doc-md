---
title: Impostazioni di allineamento
description: Nella libreria Aspose.Cells è possibile utilizzare le impostazioni di allineamento delle celle per regolare il layout e la visualizzazione del testo. Regolando impostazioni quali l'allineamento orizzontale, l'allineamento verticale e la disposizione del testo, hai un maggiore controllo sul modo in cui il testo scorre nelle celle. Questo documento ti fornirà passaggi dettagliati e codice di esempio per aiutarti a comprendere rapidamente come utilizzare Aspose.Cells per le impostazioni di allineamento delle celle.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /it/net/cells-alignment-settings/
---
##  **Configurazione delle impostazioni di allineamento**

###  **Impostazioni di allineamento in Microsoft Excel**

Chiunque abbia utilizzato Microsoft Excel per formattare le celle avrà familiarità con le impostazioni di allineamento in Microsoft Excel.

Come puoi vedere dalla figura sopra, ci sono diversi tipi di opzioni di allineamento:

- Allineamento del testo (orizzontale e verticale)
- Rientro.
- Orientamento.
- Controllo del testo.
- Direzione del testo.

Tutte queste impostazioni di allineamento sono completamente supportate da Aspose.Cells e sono discusse più dettagliatamente di seguito.

###  **Impostazioni di allineamento allo Aspose.Cells**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fornisce[**Ottieni Stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) E[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodi per il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe utilizzata per ottenere e impostare la formattazione di una cella. IL[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fornisce proprietà utili per configurare le impostazioni di allineamento.

 Seleziona qualsiasi tipo di allineamento del testo utilizzando[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) enumerazione. I tipi di allineamento del testo predefiniti nel file[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)enumerazione sono:

|**Tipi di allineamento del testo**|**Descrizione**|
| :- | :- |
|Metter il fondo a|Rappresenta l'allineamento del testo in basso|
|Centro|Rappresenta l'allineamento centrale del testo|
|CenterAcross|Rappresenta il centro nell'allineamento del testo|
|Distribuito|Rappresenta l'allineamento del testo distribuito|
|Riempire|Rappresenta l'allineamento del testo di riempimento|
|Generale|Rappresenta l'allineamento generale del testo|
|Giustificare|Rappresenta giustificare l'allineamento del testo|
|Sinistra|Rappresenta l'allineamento del testo a sinistra|
|Giusto|Rappresenta l'allineamento corretto del testo|
|Superiore|Rappresenta l'allineamento del testo superiore|
|GiustificatoBasso|Allinea il testo con una lunghezza kashida modificata per il testo arabo.|
|ThaiDistributed|Distribuisce soprattutto il testo tailandese, perché ogni carattere viene trattato come una parola.|

{{% alert color="primary" %}}

 Puoi anche applicare l'impostazione di giustificazione distribuita utilizzando il comando[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) proprietà.

{{% /alert %}}

####  **Allineamento orizzontale**

 Usa il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Allineamento orizzontale**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)proprietà per allineare il testo orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **Allineamento verticale**

 Simile all'allineamento orizzontale, utilizzare il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Allineamento verticale**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)proprietà per allineare il testo verticalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **Rientro**

 È possibile impostare il livello di rientro del testo in una cella con[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Livello di rientro**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **Orientamento**

 Imposta l'orientamento (rotazione) del testo in una cella con[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Angolo di rotazione**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **Controllo del testo**

La sezione seguente illustra come controllare il testo impostando il ritorno a capo, la riduzione per adattarlo e altre opzioni di formattazione.

#####  **Testo a capo**

 Avvolgere il testo in una cella ne facilita la lettura: l'altezza della cella si adatta per adattarsi a tutto il testo, invece di tagliarlo o riversarlo nelle celle adiacenti. Attiva o disattiva il ritorno a capo del testo con[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **Rimpicciolirsi per adattarsi**

 Un'opzione per mandare a capo il testo in un campo consiste nel ridurre la dimensione del testo per adattarla alle dimensioni di una cella. Questo viene fatto impostando il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)proprietà su *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **Unire Cells**

 Come Microsoft Excel, Aspose.Cells supporta l'unione di più celle in una sola. Aspose.Cells fornisce due approcci a questo compito. Un modo è chiamare il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**Unisci**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metodo. IL[**Unisci**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)Il metodo accetta i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare l'unione.
- Prima colonna: la prima colonna da cui iniziare l'unione.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

L'altro modo è chiamare prima il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**Creaintervallo**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metodo per creare un intervallo di celle da unire. IL[**Creaintervallo**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) accetta lo stesso insieme di parametri di quello di[**Unisci**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metodo discusso sopra e restituisce a[**Allineare**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto. IL[**Allineare**](https://reference.aspose.com/cells/net/aspose.cells/range) l'oggetto fornisce anche a[**Unisci**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) metodo che unisce l'intervallo specificato nel file[**Allineare**](https://reference.aspose.com/cells/net/aspose.cells/range)oggetto.

#####  **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati caratteri, parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

 L'ordine di lettura viene impostato con[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**DirezioneTesto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) proprietà. Aspose.Cells fornisce tipi di direzione del testo predefiniti nel file[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)enumerazione.

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|Contesto|L'ordine di lettura coerente con la lingua del primo carattere immesso|
|Da sinistra a destra|Ordine di lettura da sinistra a destra|
|Da destra a sinistra|Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **Argomenti avanzati**
- [Modifica l'allineamento Cells e mantieni la formattazione esistente](/cells/it/net/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e ritorno a capo del testo](/cells/it/net/line-breaks-and-text-wrapping/)

