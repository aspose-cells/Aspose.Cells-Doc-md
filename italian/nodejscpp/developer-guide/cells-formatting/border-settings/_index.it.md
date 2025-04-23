---  
title: Impostazioni bordo
linktitle: Impostazioni bordo  
description: Come utilizzare la libreria Aspose.Cells in Node.js tramite C++ per impostare lo stile e il colore del bordo delle celle. Regolando larghezza, stile e colore del bordo, hai un maggiore controllo sull aspetto e la visualizzazione delle celle.  
keywords: Aspose.Cells, Impostazioni bordo cella, Node.js tramite C++, Larghezza bordo, Stile bordo, Colore bordo  
type: docs  
weight: 40  
url: /it/nodejs-cpp/cells-border-settings/  
---  

## **Aggiungere Bordi alle Celle**  

Microsoft Excel permette agli utenti di formattare le celle aggiungendo i bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile di linea e il colore dei bordi.  

Con Aspose.Cells for Node.js via C++, gli sviluppatori possono aggiungere bordi e personalizzarli come fanno in modo flessibile in Microsoft Excel.  

### **Aggiungere Bordi alle Celle**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ogni foglio di calcolo nel file Excel. Un foglio di calcolo viene rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce la collezione [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ogni elemento nella collezione [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells fornisce il metodo [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) nella classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Il metodo [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) viene utilizzato per impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) offre proprietà per aggiungere bordi alle celle.  

#### **Aggiunta di bordi a una cella**  

Gli sviluppatori possono aggiungere bordi a una cella utilizzando la raccolta [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) dell'oggetto [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--). Il tipo di bordo viene passato come indice alla raccolta [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--). Tutti i tipi di bordo sono predefiniti nell'enumerazione [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  

**Enumerazione Border**  

|**Tipi di bordi**|**Descrizione**|  
| :- | :- |  
|BottomBorder|Una linea di bordo inferiore|  
|DiagonalDown|Una linea diagonale dall'angolo in alto a sinistra all'angolo in basso a destra|  
|DiagonalUp|Una linea diagonale dall'angolo in basso a sinistra all'angolo in alto a destra|  
|LeftBorder|Una linea di bordo sinistro|  
|RightBorder|Una linea di bordo destro|  
|TopBorder|Una linea di bordo superiore|  

La raccolta [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) memorizza tutti i bordi. Ogni bordo nella raccolta [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) è rappresentato da un oggetto [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) che fornisce due proprietà, [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) e [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-), per impostare rispettivamente colore e stile della linea del bordo.  

Per impostare il colore della linea del bordo, seleziona un colore usando l'enumerazione Color (parte di Node.js) e assegnalo alla proprietà color dell'oggetto Border.  

Lo stile della linea del bordo viene impostato selezionando uno stile di linea dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  

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
Seleziona uno degli stili di linea e assegnalo alla proprietà [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) dell'oggetto [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Dovresti impostare sia lo stile di linea che il colore contemporaneamente. Le due linee diagonali del bordo dovrebbero avere lo stesso stile e colore.  
{{% /alert %}}  

#### **Aggiunta di bordi a un intervallo di celle**  

È anche possibile aggiungere bordi a un intervallo di celle piuttosto che a una singola cella. Per farlo, prima crea un intervallo di celle chiamando il metodo [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) della raccolta [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Accetta i seguenti parametri:  

- Prima riga, la prima riga dell'intervallo.  
- Prima colonna, rappresenta la prima colonna dell'intervallo.  
- Numero di righe, il numero di righe nell'intervallo.  
- Numero di colonne, il numero di colonne nell'intervallo.  

Il metodo [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range), che contiene l'intervallo di celle specificato. L'oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) fornisce un metodo [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) che prende i seguenti parametri per aggiungere un bordo all'intervallo di celle:  

- **Tipo di Bordi**, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  
- **Stile di Linea**, lo stile della linea del bordo, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  
- **Colore**, il colore della linea, selezionato dall'enumerazione Colore.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


