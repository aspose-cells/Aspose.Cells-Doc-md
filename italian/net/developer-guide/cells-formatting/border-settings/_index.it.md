---
title: Impostazioni del bordo
type: docs
weight: 40
url: /it/net/cells-border-settings/
---
## **Aggiunta di bordi a Cells**

Microsoft Excel consente agli utenti di formattare le celle aggiungendo bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile e il colore della linea dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzare il loro aspetto nello stesso modo flessibile di Microsoft Excel.

### **Aggiunta di bordi a Cells**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la classe fornisce il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Ogni elemento del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione rappresenta un oggetto della[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fornisce il[**Ottieni stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)metodo nel[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe. Il[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)Il metodo viene utilizzato per impostare lo stile di formattazione di una cella. Il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)class fornisce proprietà per l'aggiunta di bordi alle celle.

#### **Aggiunta di bordi a un numero Cell**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collezione. Il tipo di bordo viene passato come indice al file[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collezione. Tutti i tipi di bordo sono predefiniti nel file[**Tipo di bordo**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumerazione.

**Enumerazione dei confini**

|**Tipi di bordo**|**Descrizione**|
|:- |:- |
|Bordo inferiore|Una linea di confine inferiore|
|Diagonale giù|Una linea diagonale da sinistra in alto a destra in basso|
|DiagonalUp|Una linea diagonale da sinistra in basso a destra in alto|
|Bordo Sinistro|Una linea di confine sinistra|
|Bordo destro|Una linea di confine destra|
|TopBorder|Una linea di confine superiore|

Il[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)la collezione memorizza tutti i bordi. Ogni bordo in[**frontiere**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) la raccolta è rappresentata da a[**Confine**](https://reference.aspose.com/cells/net/aspose.cells/border) oggetto che fornisce due proprietà,[**Colore**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) e[**Stile linea**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)per impostare rispettivamente il colore e lo stile della linea di un bordo.

Per impostare il colore della linea di un bordo, selezionare un colore utilizzando l'enumerazione Color (parte del Framework .NET) e assegnarlo alla proprietà Color dell'oggetto Border.

 Lo stile della linea del bordo viene impostato selezionando uno stile della linea da[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumerazione.

**Enumerazione CellBorderType**

|**Stili di linea**|**Descrizione**|
|:- |:- |
|DashDot|Sottile linea tratteggiata|
|DashDotDot|Sottile linea tratteggiata|
|Tratteggiato|Linea tratteggiata|
|Punteggiato|Linea tratteggiata|
|Doppio|Doppia linea|
|Capelli|Attaccatura dei capelli|
|MediumDashDot|Linea tratteggiata media|
|MedioTrattinoPuntoPunto|Linea tratteggiata media|
|MedioTratteggiato|Linea tratteggiata media|
|Nessuno|Nessuna linea|
|medio|Linea media|
|SlantedDashDot|Linea tratteggiata media obliqua|
|Spesso|Linea spessa|
|Sottile|Linea sottile|
Selezionare uno degli stili di linea e quindi assegnarlo a[**Confine**](https://reference.aspose.com/cells/net/aspose.cells/border) dell'oggetto[**Stile linea**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

È necessario impostare contemporaneamente lo stile e il colore della linea. Le due linee di confine diagonali dovrebbero avere lo stesso stile e colore della linea.

{{% /alert %}}

#### **Aggiunta di bordi a un intervallo di Cells**

È anche possibile aggiungere bordi a un intervallo di celle anziché solo a una singola cella. Per fare ciò, prima crea un intervallo di celle chiamando il metodo[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) della collezione[**Crea intervallo**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) metodo. Richiede i seguenti parametri:

- First Row, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

 Il[**Crea intervallo**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) metodo restituisce a[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto, che contiene l'intervallo di celle specificato. Il[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto fornisce a[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) metodo che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- **Tipo di bordo** , il tipo di bordo, selezionato da[**Tipo di bordo**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)enumerazione.
- **Stile linea** , lo stile della linea del bordo, selezionato da[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumerazione.
- **Colore**, il colore della linea, selezionato dall'enumerazione Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **Colori e tavolozza**

Una tavolozza è il numero di colori disponibili per l'uso nella creazione di un'immagine. L'uso di una tavolozza standardizzata in una presentazione consente all'utente di creare un aspetto coerente. Ogni file Excel Microsoft (97-2003) ha una tavolozza di 56 colori che possono essere applicati a celle, caratteri, griglie, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile non solo utilizzare i colori esistenti della tavolozza ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla tavolozza.

Questo argomento illustra come aggiungere colori personalizzati alla tavolozza.

### **Aggiunta di colori personalizzati alla tavolozza**

Aspose.Cells supporta la tavolozza dei 56 colori di Microsoft di Excel. Per utilizzare un colore personalizzato non definito nella tavolozza, aggiungi il colore alla tavolozza.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe fornisce a[**Cambia tavolozza**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) metodo che accetta i seguenti parametri per aggiungere un colore personalizzato per modificare la tavolozza:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella tavolozza che verrà sostituito dal colore personalizzato. Dovrebbe essere compreso tra 0 e 55.

L'esempio seguente aggiunge un colore personalizzato (Orchidea) alla tavolozza prima di applicarlo a un font.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La tavolozza contiene solo 56 colori. Quando aggiungi un colore personalizzato alla tavolozza, la tavolozza viene modificata e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando cambi la tavolozza, fai molta attenzione. Inoltre, questa è la limitazione solo nel formato di file XLS (Excel 97 - 2003) in quanto non esiste tale limitazione per XLSX o altri formati di file MS Excel avanzati (2007/2010 o 2013).

{{% /alert %}}


