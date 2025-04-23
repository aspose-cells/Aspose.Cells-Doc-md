---
title: Impostazioni di Allineamento
type: docs
weight: 20
url: /it/java/cells-alignment-settings/
---

## **Configurazione delle impostazioni di allineamento**

## **Impostazioni di allineamento in Microsoft Excel**

Chiunque abbia usato Microsoft Excel per formattare le celle sarà familiare con le impostazioni di allineamento in Microsoft Excel.

Come si può vedere dalla figura sopra, ci sono diversi tipi di opzioni di allineamento:

- Allineamento del testo (orizzontale e verticale)
- Rientro.
- Orientamento.
- Controllo del testo.
- Direzione del testo.

Tutte queste impostazioni di allineamento sono completamente supportate da Aspose.Cells e sono discusse in modo più dettagliato di seguito.

## **Impostazioni di allineamento in Aspose.Cells**

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) e [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) per la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) che vengono utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) fornisce proprietà utili per la configurazione delle impostazioni di allineamento.

Seleziona qualsiasi tipo di allineamento del testo utilizzando l'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype). I tipi di allineamento del testo predefiniti nell'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) sono:

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
|JustifiedLow|Allinea il testo con una lunghezza kashida regolata per il testo in arabo.|
|ThaiDistributed|Distribuisce il testo thailandese in particolare, poiché ciascun carattere è trattato come una parola.|

{{% alert color="primary" %}}

È anche possibile applicare l'impostazione giustifica distribuita utilizzando la proprietà [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed).

{{% /alert %}}

## **Allineamento orizzontale, verticale e rientro**

Usa la proprietà [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) per allineare il testo in orizzontale e la proprietà [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) per allineare il testo in verticale.
È possibile impostare il livello di rientro del testo in una cella con la proprietà [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel). 
e influisce solo quando l'allineamento orizzontale è a sinistra o a destra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientamento**

Imposta l'orientamento (rotazione) del testo in una cella con la proprietà [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Controllo del Testo**

La seguente sezione discute come controllare il testo impostando il rientro del testo, adattamento alla cella e altre opzioni di formattazione.

### **Testo a Capo**

Il ritorno a capo del testo in una cella rende più facile la lettura: l'altezza della cella si adatta per contenere tutto il testo anziché tagliarlo o farlo traboccare nelle celle adiacenti. Imposta il ritorno a capo del testo su on o off con la proprietà [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Ridimensionamento per adattarsi**

Una opzione per il ritorno a capo del testo in un campo è ridurre le dimensioni del testo per adattarlo alle dimensioni di una cella. Questo viene fatto impostando la proprietà [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) su **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Unione di celle**

Come Microsoft Excel, Aspose.Cells supporta l'unione di diverse celle in una. Aspose.Cells fornisce due approcci per questo compito. Un modo è chiamare il metodo [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-). Il metodo richiede i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare a unire.
- Prima colonna: la prima colonna da cui iniziare a unire.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati i caratteri, le parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

L'ordine di lettura è impostato con la proprietà [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection). Aspose.Cells fornisce tipi di direzione del testo predefiniti nell'enumerazione [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection).

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|Context| L'ordine di lettura coerente con la lingua del primo carattere inserito|
|LeftToRight| Ordine di lettura da sinistra a destra|
|RightToLeft| Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Argomenti avanzati**
- [Modifica dell'allineamento delle celle e mantenimento della formattazione esistente](/cells/it/java/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e interruzioni di testo](/cells/it/java/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="java" >}}
