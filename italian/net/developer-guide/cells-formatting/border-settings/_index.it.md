---
title: Impostazioni bordo
description: Come utilizzare la libreria Aspose.Cells in C# per impostare lo stile e il colore del bordo delle celle. Regolando la larghezza, lo stile e il colore del bordo, si ha maggiore controllo su come appaiono e appaiono le celle.
keywords: Aspose.Cells, Impostazioni di bordo della cella, C#, Larghezza del bordo, Stile del bordo, Colore del bordo
type: docs
weight: 40
url: /it/net/cells-border-settings/
---

## **Aggiungere Bordi alle Celle**

Microsoft Excel consente agli utenti di formattare le celle aggiungendo dei bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore è quello aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile della linea e il colore dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzarne l'aspetto in modo flessibile come in Microsoft Excel.

### **Aggiungere Bordi alle Celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce la collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells fornisce il metodo [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) nella classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Il metodo [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) viene utilizzato per impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fornisce proprietà per aggiungere bordi alle celle.

#### **Aggiunta di bordi a una cella**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando la collezione [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). Il tipo di bordo viene passato come indice alla collezione [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). Tutti i tipi di bordi sono predefiniti nell'enumerazione [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).

**Enumerazione Border**

|**Tipi di bordi**|**Descrizione**|
| :- | :- |
|BottomBorder|Una linea di bordo inferiore|
|DiagonalDown|Una linea diagonale dall'angolo in alto a sinistra all'angolo in basso a destra|
|DiagonalUp|Una linea diagonale dall'angolo in basso a sinistra all'angolo in alto a destra|
|LeftBorder|Una linea di bordo sinistro|
|RightBorder|Una linea di bordo destro|
|TopBorder|Una linea di bordo superiore|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

Per impostare il colore della linea del bordo, selezionare un colore utilizzando l'enumerazione Colore (parte del Framework .NET) e assegnarlo alla proprietà Colore dell'oggetto Bordo.

Lo stile della linea del bordo viene impostato selezionando uno stile di linea dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).

**Enumerazione CellBorderType**

|**Stili di linea**|**Descrizione**|
| :- | :- |
|DashDot|Linea tratteggiata sottile a punti|
|DashDotDot|Linea sottile a punti e trattini|
|Dashed|Linea tratteggiata|
|Dotted|Linea a punti|
|Double|Linea doppia|
|Hair|Linea sottilissima|
|MediumDashDot|Linea media tratteggiata a punti|
|MediumDashDotDot|Linea media a punti e trattini|
|MediumDashed|Linea tratteggiata media|
|None|Nessuna linea|
|Medium|Linea media|
|SlantedDashDot|Linea tratteggiata sottile a punti inclinata|
|Thick|Linea spessa|
|Thin|Linea sottile|
Seleziona uno degli stili di linea e poi assegnalo alla proprietà [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) dell'oggetto [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Dovresti impostare contemporaneamente lo stile di linea e il colore. Le due linee di bordo diagonali dovrebbero avere lo stesso stile di linea e colore.

{{% /alert %}}

#### **Aggiunta di bordi a un intervallo di celle**

È anche possibile aggiungere bordi a un intervallo di celle anziché a una singola cella. Per farlo, prima crea un intervallo di celle chiamando il metodo [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Richiede i seguenti parametri:

- Prima riga, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

Il metodo [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range), che contiene l'intervallo specificato di celle. L'oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) fornisce un metodo [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- **Tipo di bordo**, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- **Stile di linea**, lo stile di linea del bordo, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- **Colore**, il colore della linea, selezionato dall'enumerazione Colore.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
