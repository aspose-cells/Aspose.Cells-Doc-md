---
title: Impostazioni di allineamento con Golang via C++
linktitle: Impostazioni di Allineamento
description: Nella libreria Aspose.Cells, puoi utilizzare le impostazioni di allineamento delle celle per regolare il layout e la visualizzazione del testo. Regolando le impostazioni come allineamento orizzontale, allineamento verticale e ritorno a capo del testo, hai maggior controllo su come il testo fluisce nelle celle. Questo documento ti fornirà dettagliati passaggi e codice di esempio per aiutarti a capire rapidamente come utilizzare Aspose.Cells per le impostazioni di allineamento delle celle.
keywords: Aspose.Cells, allineamento delle celle, allineamento orizzontale, allineamento verticale, ritorno a capo del testo
type: docs
weight: 20
url: /it/go-cpp/cells-alignment-settings/
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

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una collezione [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Ogni elemento nella collezione [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) e [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) per la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) che vengono utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fornisce proprietà utili per la configurazione delle impostazioni di allineamento.

Seleziona qualsiasi tipo di allineamento del testo utilizzando l'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/). I tipi di allineamento del testo predefiniti nell'enumerazione [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) sono:

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

È anche possibile applicare l'impostazione giustifica distribuita utilizzando la proprietà [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/).

{{% /alert %}}

#### **Allineamento Orizzontale**

Utilizzare la proprietà [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) per allineare il testo orizzontalmente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **Allineamento Verticale**

Similmente all'allineamento orizzontale, utilizzare la proprietà [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) per allineare il testo verticalmente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **Rientro**

È possibile impostare il livello di rientro del testo in una cella con la proprietà [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **Orientamento**

Imposta l'orientamento (rotazione) del testo in una cella con la proprietà [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **Controllo del Testo**

La seguente sezione discute come controllare il testo impostando il rientro del testo, adattamento alla cella e altre opzioni di formattazione.

##### **Testo a Capo**

Il testo a capo in una cella rende più facile leggerlo: l'altezza della cella si adatta per contenere tutto il testo, invece di tagliarlo o farlo fuoriuscire nelle celle adiacenti. Imposta il testo a capo on o off con la proprietà [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **Ridimensionamento per adattarsi**

Un'opzione per avvolgere il testo in un campo è ridurre le dimensioni del testo per adattarlo alle dimensioni di una cella. Questo viene fatto impostando la proprietà [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) su **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **Unione di celle**

Come Microsoft Excel, Aspose.Cells supporta l'unione di diverse celle in una. Aspose.Cells fornisce due approcci a questo compito. Un modo è chiamare il metodo [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) della raccolta [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/). Il metodo [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) richiede i seguenti parametri per unire le celle:

- Prima riga: la prima riga da cui iniziare a unire.
- Prima colonna: la prima colonna da cui iniziare a unire.
- Numero di righe: il numero di righe da unire.
- Numero di colonne: il numero di colonne da unire.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
L'altro modo è chiamare prima il metodo [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) della raccolta [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) per creare un intervallo di celle da unire. Il metodo [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) richiede lo stesso set di parametri di quello del metodo [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) discusso sopra e restituisce un oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). L'oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fornisce anche un metodo [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) che unisce l'intervallo specificato nell'oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **Direzione del testo**

È possibile impostare l'ordine di lettura del testo nelle celle. L'ordine di lettura è l'ordine visivo in cui vengono visualizzati i caratteri, le parole, ecc. Ad esempio, l'inglese è una lingua da sinistra a destra mentre l'arabo è una lingua da destra a sinistra.

L'ordine di lettura è impostato con la proprietà [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) dell'oggetto [**Style**](https://reference.aspose.com/cells/go-cpp/style/). Aspose.Cells fornisce tipi di direzione del testo predefiniti nell'enumerazione [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|**Tipi di direzione del testo**|**Descrizione**|
| :- | :- |
|Context| L'ordine di lettura coerente con la lingua del primo carattere inserito|
|LeftToRight| Ordine di lettura da sinistra a destra|
|RightToLeft| Ordine di lettura da destra a sinistra|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **Argomenti avanzati**
- [Modifica dell'allineamento delle celle e mantenimento della formattazione esistente](/cells/it/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Interruzioni di riga e interruzioni di testo](/cells/it/cpp/line-breaks-and-text-wrapping/)
