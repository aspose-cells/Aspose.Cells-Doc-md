---
title: Impostazioni di Allineamento
description: Nella libreria Aspose.Cells per Python via .NET, puoi usare le impostazioni di allineamento delle celle per regolare il layout e la visualizzazione del testo. Regolando impostazioni come l’allineamento orizzontale, l’allineamento verticale e l’avvolgimento del testo, hai un controllo maggiore su come il testo scorre nelle celle. Questo documento ti fornirà passaggi dettagliati e codice di esempio per aiutarti a comprendere come usare Aspose.Cells per Python via .NET per le impostazioni di allineamento delle celle.
keywords: Aspose.Cells per Python via .NET, allineamento celle, allineamento orizzontale, allineamento verticale, avvolgimento del testo
type: docs
weight: 20
url: /it/python-net/cells-alignment-settings/
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

Tutte queste impostazioni di allineamento sono pienamente supportate da Aspose.Cells per Python via .NET e sono discusse più in dettaglio sotto.

### **Impostazioni di allineamento in Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). Ogni elemento nella raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells per Python via .NET fornisce i metodi [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) e [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) per la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) che vengono usati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fornisce proprietà utili per configurare le impostazioni di allineamento.

Seleziona qualsiasi tipo di allineamento del testo utilizzando l'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype). I tipi di allineamento del testo predefiniti nell'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) sono:

|**Tipi di Allineamento del Testo**|**Descrizione**|
| :- | :- |
|GENERAL|Rappresenta l'allineamento generale del testo|
|BOTTOM|Rappresenta l'allineamento del testo in basso|
|CENTER|Rappresenta l'allineamento del testo al centro|
|CENTER_ACROSS|Rappresenta l'allineamento del testo centrato attraverso|
|DISTRIBUTED|Rappresenta l'allineamento distribuito del testo|
|FILL|Rappresenta l'allineamento del testo di riempimento|
|JUSTIFY|Rappresenta l’allineamento del testo giustificato|
|LEFT|Rappresenta l'allineamento del testo a sinistra|
|RIGHT|Rappresenta l'allineamento del testo a destra|
|TOP|Rappresenta l'allineamento del testo in alto|
|JUSTIFIED_LOW|Allinea il testo con una lunghezza di kashida regolata per il testo arabo|
|THAI_DISTRIBUTED|Distribuisce il testo tailandese in modo speciale, poiché ogni carattere è trattato come una parola|

{{% alert color="primary" %}}

È anche possibile applicare l'impostazione giustifica distribuita utilizzando la proprietà [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed).

{{% /alert %}}

#### **Allineamento Orizzontale**

Utilizzare la proprietà [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) per allineare il testo orizzontalmente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Allineamento Verticale**

Similmente all'allineamento orizzontale, utilizzare la proprietà [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) per allineare il testo verticalmente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Rientro**

È possibile impostare il livello di rientro del testo in una cella con la proprietà [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Orientamento**

Imposta l'orientamento (rotazione) del testo in una cella con la proprietà [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Controllo del Testo**

La seguente sezione discute come controllare il testo impostando il rientro del testo, adattamento alla cella e altre opzioni di formattazione.

##### **Testo a Capo**

Il testo a capo in una cella rende più facile leggerlo: l'altezza della cella si adatta per contenere tutto il testo, invece di tagliarlo o farlo fuoriuscire nelle celle adiacenti. Imposta il testo a capo on o off con la proprietà [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Ridimensionamento per adattarsi**

Un'opzione per avvolgere il testo in un campo è ridurre le dimensioni del testo per adattarlo alle dimensioni di una cella. Questo viene fatto impostando la proprietà [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) su **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Unione di celle**

Come Microsoft Excel, Aspose.Cells per Python via .NET supporta la fusione di più celle in una. Aspose.Cells per Python via .NET fornisce due approcci per questo compito. Un modo è chiamare il metodo [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) della raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). Il metodo [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) prende i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare a unire.
- Prima colonna: la prima colonna da cui iniziare a unire.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

L'altro modo è chiamare prima il metodo [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) della raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) per creare un intervallo di celle da unire. Il metodo [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) richiede lo stesso set di parametri di quello del metodo [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) discusso sopra e restituisce un oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). L'oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) fornisce anche un metodo [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) che unisce l'intervallo specificato nell'oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

##### **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati i caratteri, le parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

L’ordine di lettura è impostato con la proprietà [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) dell’oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Aspose.Cells per Python via .NET fornisce tipi di direzione del testo predefiniti nella enumerazione [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype).

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|CONTEXT|L’ordine di lettura coerente con la lingua del primo carattere inserito|
|LEFT_TO_RIGHT|Ordine di lettura da sinistra a destra|
|RIGHT_TO_LEFT|Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Argomenti avanzati**
- [Modifica dell'allineamento delle celle e mantenimento della formattazione esistente](/cells/it/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e interruzioni di testo](/cells/it/python-net/line-breaks-and-text-wrapping/)


{{< app/cells/assistant language="python-net" >}}
