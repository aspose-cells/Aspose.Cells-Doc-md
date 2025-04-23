---
title: Impostazioni di Allineamento
description: Nella libreria Aspose.Cells, puoi utilizzare le impostazioni di allineamento delle celle per regolare il layout e la visualizzazione del testo. Regolando le impostazioni come allineamento orizzontale, allineamento verticale e ritorno a capo del testo, hai maggior controllo su come il testo fluisce nelle celle. Questo documento ti fornirà dettagliati passaggi e codice di esempio per aiutarti a capire rapidamente come utilizzare Aspose.Cells per le impostazioni di allineamento delle celle.
keywords: Aspose.Cells, allineamento delle celle, allineamento orizzontale, allineamento verticale, ritorno a capo del testo
type: docs
weight: 20
url: /it/net/cells-alignment-settings/
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

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) e [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) per la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) che vengono utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fornisce proprietà utili per la configurazione delle impostazioni di allineamento.

Seleziona qualsiasi tipo di allineamento del testo utilizzando l'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype). I tipi di allineamento del testo predefiniti nell'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) sono:

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

È anche possibile applicare l'impostazione giustifica distribuita utilizzando la proprietà [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed).

{{% /alert %}}

#### **Allineamento Orizzontale**

Utilizzare la proprietà [**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) per allineare il testo orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Allineamento Verticale**

Similmente all'allineamento orizzontale, utilizzare la proprietà [**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) per allineare il testo verticalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Rientro**

È possibile impostare il livello di rientro del testo in una cella con la proprietà [**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientamento**

Imposta l'orientamento (rotazione) del testo in una cella con la proprietà [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Controllo del Testo**

La seguente sezione discute come controllare il testo impostando il rientro del testo, adattamento alla cella e altre opzioni di formattazione.

##### **Testo a Capo**

Il testo a capo in una cella rende più facile leggerlo: l'altezza della cella si adatta per contenere tutto il testo, invece di tagliarlo o farlo fuoriuscire nelle celle adiacenti. Imposta il testo a capo on o off con la proprietà [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Ridimensionamento per adattarsi**

Un'opzione per avvolgere il testo in un campo è ridurre le dimensioni del testo per adattarlo alle dimensioni di una cella. Questo viene fatto impostando la proprietà [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) su **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Unione di celle**

Come Microsoft Excel, Aspose.Cells supporta l'unione di diverse celle in una. Aspose.Cells fornisce due approcci a questo compito. Un modo è chiamare il metodo [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) richiede i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare a unire.
- Prima colonna: la prima colonna da cui iniziare a unire.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

L'altro modo è chiamare prima il metodo [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) per creare un intervallo di celle da unire. Il metodo [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) richiede lo stesso set di parametri di quello del metodo [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) discusso sopra e restituisce un oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). L'oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) fornisce anche un metodo [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) che unisce l'intervallo specificato nell'oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

##### **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati i caratteri, le parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

L'ordine di lettura è impostato con la proprietà [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Aspose.Cells fornisce tipi di direzione del testo predefiniti nell'enumerazione [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype).

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|Context| L'ordine di lettura coerente con la lingua del primo carattere inserito|
|LeftToRight| Ordine di lettura da sinistra a destra|
|RightToLeft| Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Argomenti avanzati**
- [Modifica dell'allineamento delle celle e mantenimento della formattazione esistente](/cells/it/net/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e interruzioni di testo](/cells/it/net/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="csharp" >}}
