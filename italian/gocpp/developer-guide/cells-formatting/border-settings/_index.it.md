---
title: Impostazioni del bordo con Golang via C++
linktitle: Impostazioni bordo
description: Come usare la libreria Aspose.Cells in C++ per impostare lo stile e il colore del bordo delle celle. Regolando larghezza, stile e colore del bordo, si ha un maggiore controllo sull aspetto delle celle.
keywords: Aspose.Cells, Impostazioni del bordo della cella, C++, Larghezza del bordo, Stile del bordo, Colore del bordo
type: docs
weight: 40
url: /it/go-cpp/cells-border-settings/
---

## **Aggiungere Bordi alle Celle**

Microsoft Excel permette agli utenti di formattare le celle aggiungendo i bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile di linea e il colore dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzarne l'aspetto in modo flessibile come in Microsoft Excel.

### **Aggiungere Bordi alle Celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ogni foglio di calcolo nel file Excel. Un foglio di calcolo viene rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce la collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fornisce il metodo [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) nella classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Il metodo [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) viene utilizzato per impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) offre proprietà per aggiungere bordi alle celle.

#### **Aggiunta di bordi a una cella**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando la raccolta [**Style**](https://reference.aspose.com/cells/go-cpp/style/) dell'oggetto [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/). Il tipo di bordo viene passato come indice alla raccolta [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/). Tutti i tipi di bordo sono predefiniti nell'enumerazione [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

**Enumerazione Border**

| **Tipi di bordo** | **Descrizione** |
|------------------|-----------------|
| BottomBorder     | Una linea di bordo inferiore |
| DiagonaleInGiù | Una linea diagonale dall'angolo superiore sinistro a quello inferiore destro |
| DiagonaleSu | Una linea diagonale dall'angolo inferiore sinistro a quello superiore destro |
| BordoSinistro | Una linea del bordo sinistro |
| BordoDestro | Una linea del bordo destro |
| BordoSuperiore | Una linea del bordo superiore |

La raccolta [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) memorizza tutti i bordi. Ogni bordo nella raccolta [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) è rappresentato da un oggetto [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) che fornisce due proprietà, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) e [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/), per impostare rispettivamente colore e stile della linea del bordo.

Per impostare il colore della linea di un bordo, seleziona un colore utilizzando l'enumerazione Colore e assegnalo alla proprietà Colore dell'oggetto Border.

Lo stile della linea del bordo viene impostato selezionando uno stile di linea dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).

**Enumerazione CellBorderType**

| **Stili di Linea** | **Descrizione** |
|------------------------|-------------------------------|
| TrattoPunto | Linea sottile tratteggiata |
| TrattoPuntoPunto | Linea sottile trattino-punto |
| Tratteggiata | Linea tratteggiata |
| Punteggiata | Linea punteggiata |
| Doppia | Linea doppia |
| Capelli |Linea sottile di capelli |
| TrattoPuntoPuntoMedio | Linea tratto-punto di spessore medio |
| TrattoPuntoPuntoMedio | Linea trattino-punto di spessore medio |
| TrattoTratteggiatoMedio | Linea tratteggiata di spessore medio |
| Nessuno | Nessuna linea |
| Medio | Linea di spessore medio |
| TrattoInclinatoPunto | Linea tratto-punto inclinata di medio spessore |
| Spesso | Linea spessa |
| Sottile | Linea sottile |

Seleziona uno degli stili di linea e assegnalo alla proprietà [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) dell'oggetto [**Border**](https://reference.aspose.com/cells/go-cpp/border/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Dovresti impostare sia lo stile di linea che il colore contemporaneamente. Le due linee diagonali del bordo dovrebbero avere lo stesso stile e colore.

{{% /alert %}}

#### **Aggiunta di bordi a un intervallo di celle**

È anche possibile aggiungere bordi a un intervallo di celle piuttosto che a una singola cella. Per farlo, prima crea un intervallo di celle chiamando il metodo [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) della raccolta [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/). Accetta i seguenti parametri:

- Prima riga, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

Il metodo [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), che contiene l'intervallo di celle specificato. L'oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fornisce un metodo [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) che prende i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- **Tipo di Bordi**, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/).
- **Stile di Linea**, lo stile della linea del bordo, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).
- **Colore**, il colore della linea, selezionato dall'enumerazione Colore.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
