---
title: Impostazioni del bordo
description: Come utilizzare la libreria Aspose.Cells in C# per impostare lo stile del bordo e il colore delle celle. Regolando la larghezza, lo stile e il colore del bordo, hai un maggiore controllo sull'aspetto e sulla visualizzazione delle celle.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /it/net/cells-border-settings/
---
##  **Aggiunta di bordi a Cells**

Microsoft Excel consente agli utenti di formattare le celle aggiungendo bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile e il colore della linea dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzarne l'aspetto con la stessa flessibilità di Microsoft Excel.

###  **Aggiunta di bordi a Cells**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce il file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fornisce il[**Ottieni Stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)metodo nel[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe. IL[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)viene utilizzato per impostare lo stile di formattazione di una cella. IL[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fornisce proprietà per aggiungere bordi alle celle.

####  **Aggiunta di bordi a Cell**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collezione. Il tipo di bordo viene passato come indice al file[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collezione. Tutti i tipi di bordo sono predefiniti nel file[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumerazione.

**Enumerazione dei confini**

|**Tipi di confine**|**Descrizione**|
| :- | :- |
|BottomBorder|Una linea di confine inferiore|
|Diagonale verso il basso|Una linea diagonale dall'alto a sinistra al basso a destra|
|Diagonale su|Una linea diagonale dal basso a sinistra verso l'alto a destra|
|LeftBorder|Una linea di confine sinistra|
|Bordo destro|Una linea di confine destra|
|TopBorder|Una linea di confine superiore|

IL[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)la raccolta memorizza tutti i confini. Ogni confine nel[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) la raccolta è rappresentata da a[**Confine**](https://reference.aspose.com/cells/net/aspose.cells/border) oggetto che fornisce due proprietà,[**Colore**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) E[**Stile linea**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)per impostare rispettivamente il colore e lo stile della linea del bordo.

Per impostare il colore della linea di un bordo, seleziona un colore utilizzando l'enumerazione Color (parte del Framework .NET) e assegnalo alla proprietà Color dell'oggetto Border.

 Lo stile della linea del bordo viene impostato selezionando uno stile di linea dal file[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumerazione.

**Enumerazione CellBorderType**

|**Stili di linea**|**Descrizione**|
| :- | :- |
|DashDot|Linea tratteggiata sottile|
|DashDotDot|Linea sottile tratteggiata|
|Tratteggiato|Linea tratteggiata|
|Punteggiato|Linea tratteggiata|
|Doppio|Doppia linea|
|Capelli|Attaccatura dei capelli|
|MediumDashDot|Linea tratteggiata media|
|MedioDashDotDot|Linea tratteggiata-punto-punteggiata media|
|Medio Tratteggiato|Linea tratteggiata media|
|Nessuno|Nessuna linea|
|medio|Linea media|
|SlantedDashDot|Linea tratteggiata media obliqua|
|Spesso|Linea spessa|
|Magro|Linea sottile|
Seleziona uno degli stili di linea e assegnalo a[**Confine**](https://reference.aspose.com/cells/net/aspose.cells/border) dell'oggetto[**Stile linea**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Dovresti impostare sia lo stile della linea che il colore contemporaneamente. Le due linee di bordo diagonali dovrebbero avere lo stesso stile e colore della linea.

{{% /alert %}}

####  **Aggiunta di bordi a un intervallo di Cells**

 È anche possibile aggiungere bordi a un intervallo di celle anziché a una singola cella. Per fare ciò, crea prima un intervallo di celle chiamando il file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione[**Creaintervallo**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) metodo. Richiede i seguenti parametri:

- Prima riga, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

 IL[**Creaintervallo**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) il metodo restituisce a[**Allineare**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto, che contiene l'intervallo di celle specificato. IL[**Allineare**](https://reference.aspose.com/cells/net/aspose.cells/range) l'oggetto fornisce a[**Imposta bordo contorno**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) metodo che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

-  *Tipo bordo**, il tipo di bordo, selezionato da[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)enumerazione.
-  *Stile linea**, lo stile della linea del bordo, selezionato da[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumerazione.
- *Color**, il colore della linea, selezionato dall'enumerazione Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
