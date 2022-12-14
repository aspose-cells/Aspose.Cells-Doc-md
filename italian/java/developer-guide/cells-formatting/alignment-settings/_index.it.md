---
title: Impostazioni di allineamento
type: docs
weight: 20
url: /it/java/cells-alignment-settings/
---
## **Configurazione delle impostazioni di allineamento**

## **Impostazioni di allineamento in Microsoft Excel**

Chiunque abbia utilizzato Microsoft Excel per formattare le celle avrà familiarità con le impostazioni di allineamento in Microsoft Excel.

Come puoi vedere dalla figura sopra, ci sono diversi tipi di opzioni di allineamento:

- Allineamento del testo (orizzontale e verticale)
- Rientro.
- Orientamento.
- Controllo del testo.
- Direzione del testo.

Tutte queste impostazioni di allineamento sono completamente supportate da Aspose.Cells e sono discusse più dettagliatamente di seguito.

## **Impostazioni di allineamento in Aspose.Cells**

 Aspose.Cells fornisce[**Ottieni stile**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) e[**Imposta stile**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) metodi per il[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class che vengono utilizzate per ottenere e impostare la formattazione di una cella. Il[**Stile**](https://reference.aspose.com/cells/java/com.aspose.cells/style)class fornisce proprietà utili per la configurazione delle impostazioni di allineamento.

 Selezionare qualsiasi tipo di allineamento del testo utilizzando il[**TipoAllineamentoTesto**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) enumerazione. I tipi di allineamento del testo predefiniti nel file[**TipoAllineamentoTesto**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)enumerazione sono:

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
|Giustificato Basso|Allinea il testo con una lunghezza kashida regolata per il testo arabo.|
|ThaiDistributed|Distribuisce soprattutto il testo tailandese, perché ogni carattere viene trattato come una parola.|

{{% alert color="primary" %}}

 È inoltre possibile applicare l'impostazione di giustificazione distribuita utilizzando il file[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) proprietà.

{{% /alert %}}

## **Allineamento orizzontale, verticale e rientro**

 Utilizzare il[**Allineamento orizzontale**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) proprietà per allineare il testo orizzontalmente e[**Allineamento verticale**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)proprietà per allineare il testo verticalmente.
 È possibile impostare il livello di indentazione del testo in una cella con il[**Livello rientro**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) proprietà
e ha effetto solo quando l'allineamento orizzontale è a sinistra oa destra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientamento**

 Impostare l'orientamento (rotazione) del testo in una cella con il[**Angolo di rotazione**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Controllo del testo**

La sezione seguente illustra come controllare il testo impostando il ritorno a capo del testo, la riduzione per adattare e altre opzioni di formattazione.

### **Testo avvolgente**

 Avvolgere il testo in una cella rende più facile la lettura: l'altezza della cella si adatta per adattarsi a tutto il testo, invece di tagliarlo o riversarsi nelle celle adiacenti. Attiva o disattiva la disposizione del testo con il[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Restringimento per adattarsi**

 Un'opzione per avvolgere il testo in un campo consiste nel ridurre le dimensioni del testo per adattarle alle dimensioni di una cella. Questo viene fatto impostando il[**Rimpicciolirsi per starci dentro**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) proprietà. a**VERO**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Fusione Cells**

 Come Microsoft Excel, Aspose.Cells supporta l'unione di più celle in una sola. Aspose.Cells fornisce due approcci a questo compito. Un modo è chiamare il[**Unisci**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) metodo. Il metodo accetta i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare l'unione.
- Prima colonna: la prima colonna da cui iniziare l'unione.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati caratteri, parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

 L'ordine di lettura è impostato con il[**Direzione del testo**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) proprietà. Aspose.Cells fornisce tipi di direzione del testo predefiniti nel file[**TipoDirezioneTesto**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)enumerazione.

|**Tipi di direzione del testo**|**Descrizione**|
|:- |:- |
|Contesto|L'ordine di lettura coerente con la lingua del primo carattere inserito|
|Da sinistra a destra|Ordine di lettura da sinistra a destra|
|Da destra a sinistra|Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Argomenti avanzati**
- [Modificare l'allineamento Cells e mantenere la formattazione esistente](/cells/it/java/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e ritorno a capo del testo](/cells/it/java/line-breaks-and-text-wrapping/)
