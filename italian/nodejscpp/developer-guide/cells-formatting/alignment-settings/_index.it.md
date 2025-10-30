---
title: Impostazioni di Allineamento
linktitle: Impostazioni di Allineamento
description: Nella libreria Aspose.Cells, puoi usare le impostazioni di allineamento della cella per regolare il layout e la visualizzazione del testo usando Node.js via C++. Questo documento fornisce passaggi dettagliati e codice esempio per usare Aspose.Cells per le impostazioni di allineamento della cella.
keywords: Aspose.Cells, allineamento della cella, allineamento orizzontale, allineamento verticale, testo a capo Node.js via C++
type: docs
weight: 20
url: /it/nodejs-cpp/cells-alignment-settings/
---

## **Configurazione delle impostazioni di allineamento**

### **Impostazioni di allineamento in Microsoft Excel**

Chiunque abbia usato Microsoft Excel per formattare le celle sarà familiare con le impostazioni di allineamento in Microsoft Excel.

Come si può vedere dalla figura sopra, ci sono diversi tipi di opzioni di allineamento:

- Allineamento del testo (orizzontale e verticale)
- Rientro.
- Orientamento.
- Controllo del testo.
- Direzione del testo.

Tutte queste impostazioni di allineamento sono completamente supportate da Aspose.Cells e sono discusse in modo più dettagliato di seguito.

### **Impostazioni di allineamento in Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells fornisce i metodi [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) e [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) per la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) che vengono usati per ottenere e impostare il formato di una cella. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) fornisce proprietà utili per configurare le impostazioni di allineamento.

Seleziona qualsiasi tipo di allineamento del testo usando l'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype). I tipi di allineamento del testo predefiniti nell'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) sono:

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

Puoi anche applicare l'impostazione di giustificazione distribuita usando il metodo [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-).

{{% /alert %}}

#### **Allineamento Orizzontale**

Usa il metodo [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) per allineare orizzontalmente il testo.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Allineamento Verticale**

Simile all'allineamento orizzontale, utilizza il metodo [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) per allineare verticalmente il testo.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Rientro**

È possibile impostare il livello di indentazione del testo in una cella con il metodo [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Orientamento**

Imposta l'orientamento (rotazione) del testo in una cella con il metodo [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Controllo del Testo**

La seguente sezione discute come controllare il testo impostando il rientro del testo, adattamento alla cella e altre opzioni di formattazione.

##### **Testo a Capo**

L'andamento del testo in una cella facilita la lettura: l'altezza della cella si adatta per contenere tutto il testo, invece di tagliarlo o fuoriuscire nelle celle adiacenti. Attiva o disattiva l'impacchettamento del testo con il metodo [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Ridimensionamento per adattarsi**

Un'opzione per l'impacchettamento del testo in un campo è ridurre la dimensione del testo per adattarsi alle dimensioni della cella. Ciò si ottiene impostando il metodo [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) su **true**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Unione di celle**

Come Microsoft Excel, Aspose.Cells supporta l'unione di più celle in una sola. Aspose.Cells offre due approcci per questo compito. Un modo è chiamare il metodo [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Il metodo [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) accetta i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare a unire.
- Prima colonna: la prima colonna da cui iniziare a unire.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


L'altro modo è chiamare prima il metodo [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) per creare un intervallo di celle da unire. Il metodo [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) prende gli stessi parametri del sopra menzionato metodo [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) e restituisce un oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). L'oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) fornisce anche un metodo [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) che unisce l'intervallo specificato nell'oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).

##### **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati i caratteri, le parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

L'ordine di lettura si imposta con la proprietà [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Aspose.Cells offre tipi di direzione del testo predefiniti nell'enumerazione [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype).

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|Context| L'ordine di lettura coerente con la lingua del primo carattere inserito|
|LeftToRight| Ordine di lettura da sinistra a destra|
|RightToLeft| Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Argomenti avanzati**
- [Modifica dell'allineamento delle celle e mantenimento della formattazione esistente](/cells/it/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e interruzioni di testo](/cells/it/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}
