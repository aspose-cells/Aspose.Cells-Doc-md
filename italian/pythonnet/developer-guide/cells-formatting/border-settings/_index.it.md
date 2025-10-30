---
title: Impostazioni bordo
description: Come utilizzare la libreria Aspose.Cells per Python via .NET in Python per impostare lo stile e il colore del bordo delle celle. Modificando la larghezza, lo stile e il colore del bordo, hai un controllo maggiore sull aspetto e sulla visualizzazione delle celle.
keywords: Aspose.Cells per Python via .NET, Impostazioni del bordo delle celle, Larghezza del bordo, Stile del bordo, Colore del bordo
type: docs
weight: 40
url: /it/python-net/cells-border-settings/
---

## **Aggiungere Bordi alle Celle**

Microsoft Excel consente agli utenti di formattare le celle aggiungendo dei bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore è quello aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile della linea e il colore dei bordi.

Con Aspose.Cells per Python via .NET, gli sviluppatori possono aggiungere bordi e personalizzarli nello stesso modo flessibile di Microsoft Excel.

### **Aggiungere Bordi alle Celle**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce la collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells per Python via .NET fornisce il metodo [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) nella classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Il metodo [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) viene usato per impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fornisce proprietà per aggiungere bordi alle celle.

#### **Aggiunta di bordi a una cella**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando la collezione [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) dell'oggetto [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). Il tipo di bordo viene passato come indice alla collezione [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). Tutti i tipi di bordi sono predefiniti nell'enumerazione [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).

**Enumerazione Border**

|**Tipi di bordi**|**Descrizione**|
| :- | :- |
|BOTTOM_BORDER|Una linea di bordo inferiore|
|DIAGONAL_DOWN|Una linea diagonale dalla parte superiore sinistra a quella inferiore destra|
|DIAGONAL_UP|Una linea diagonale dalla parte inferiore sinistra a quella superiore destra|
|LEFT_BORDER|Una linea di bordo sinistra|
|RIGHT_BORDER|Una linea di bordo destra|
|TOP_BORDER|Una linea di bordo superiore|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

Per impostare il colore della linea del bordo, selezionare un colore utilizzando l'enumerazione Colore (parte del Framework .NET) e assegnarlo alla proprietà Colore dell'oggetto Bordo.

Lo stile della linea del bordo viene impostato selezionando uno stile di linea dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).

**Enumerazione CellBorderType**

|**Stili di linea**|**Descrizione**|
| :- | :- |
|DASH_DOT|Linea sottile tratteggiata-puntinata|
|DASH_DOT_DOT|Linea sottile tratteggiata-puntinata doppia|
|DASHED|Linea tratteggiata|
|DOTTED|Linea punteggiata|
|DOUBLE|Linea doppia|
|HAIR|Linea sottile|
|MEDIUM_DASH_DOT|Linea tratteggiata media|
|MEDIUM_DASH_DOT_DOT|Linea tratteggiata-doppia media|
|MEDIUM_DASHED|Linea tratteggiata media|
|NONE|Nessuna linea|
|MEDIUM|Linea media|
|SLANTED_DASH_DOT|Linea tratteggiata obliqua media|
|THICK|Linea spessa|
|THIN|Linea sottile|
Seleziona uno degli stili di linea e poi assegnalo alla proprietà [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) dell'oggetto [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Dovresti impostare contemporaneamente lo stile di linea e il colore. Le due linee di bordo diagonali dovrebbero avere lo stesso stile di linea e colore.

{{% /alert %}}

#### **Aggiunta di bordi a un intervallo di celle**

È anche possibile aggiungere bordi a un intervallo di celle anziché a una singola cella. Per farlo, prima crea un intervallo di celle chiamando il metodo [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Richiede i seguenti parametri:

- Prima riga, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

Il metodo [**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range), che contiene l'intervallo specificato di celle. L'oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) fornisce un metodo [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- **Tipo di bordo**, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- **Stile di linea**, lo stile di linea del bordo, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- **Colore**, il colore della linea, selezionato dall'enumerazione Colore.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
