---
title: Formattare celle
description: Scopri come formattare e stilizzare le celle in Aspose.Cells for .NET, inclusa la formattazione dei numeri, la formattazione delle date, i tipi di carattere e altre opzioni di stile delle celle. La nostra guida ti aiuterà a creare fogli di calcolo attraenti e professionali.
keywords: Aspose.Cells for .NET, formattazione celle, stile, formattazione numeri, formattazione date, stile carattere, opzioni stile celle, foglio di calcolo, creare, aspetto professionale, formattare righe e colonne.
linktitle: Formattare celle
type: docs
weight: 120
url: /it/net/cells-formatting/
---

## **Introduzione**

{{% alert color="primary" %}}

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) e [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) della classe [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell), utilizzati per ottenere/impostare lo stile di formattazione di una cella. Aspose.Cells fornisce anche una classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{% /alert %}}

## **Come formattare le celle utilizzando i metodi GetStyle e SetStyle**

Applicare diversi tipi di stili di formattazione alle celle per impostare colori di sfondo o primo piano, bordi, caratteri, allineamenti orizzontali e verticali, livello di rientro, direzione del testo, angolo di rotazione e molto altro.

### **Come utilizzare i metodi GetStyle e SetStyle**

Se gli sviluppatori devono applicare stili di formattazione diversi a celle diverse, è meglio ottenere il [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) della cella utilizzando il metodo [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle), specificare gli attributi dello stile e quindi applicare la formattazione utilizzando il metodo [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle). Di seguito è riportato un esempio per dimostrare questo approccio per applicare varie formattazioni a una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Come utilizzare l'oggetto stile per formattare celle diverse**

Se gli sviluppatori hanno bisogno di applicare lo stesso stile di formattazione a diverse celle, possono utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Seguire i passaggi seguenti per utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style):

1. Aggiungi un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) richiamando il metodo [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)
1. Accedere al nuovo oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) aggiunto
1. Imposta le proprietà/attributi desiderati dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) per applicare le impostazioni di formattazione desiderate
1. Assegna l'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) configurato alle celle desiderate

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare memoria anche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Come utilizzare gli stili predefiniti di Microsoft Excel 2007**

Se è necessario applicare stili di formattazione diversi per Microsoft Excel 2007, applicare gli stili utilizzando l'API Aspose.Cells. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare uno stile predefinito su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Come formattare i caratteri selezionati in una cella**

Il trattamento delle impostazioni del carattere spiega come formattare il testo nelle celle, ma spiega solo come formattare tutto il contenuto della cella. E se si vuole formattare solo alcuni caratteri?

Aspose.Cells supporta anche questa funzione. Questo argomento spiega come utilizzare questa funzione in modo efficace.

### **Come formattare caratteri selezionati**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene la raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ogni elemento nella raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) fornisce il metodo [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) che riceve i seguenti parametri per selezionare una gamma di caratteri all'interno di una cella:

- **Indice di inizio**, l'indice del carattere da cui inizia la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Il metodo [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) restituisce un'istanza della classe [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) che consente agli sviluppatori di formattare i caratteri allo stesso modo in cui farebbero con una cella come mostrato di seguito nell'esempio di codice. Nel file di output, nella cella A1, la parola 'Visit' verrà formattata con il carattere predefinito ma 'Aspose!' è in grassetto e blu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Se sei interessato a formattare una porzione di testo ricco in una cella, considera di utilizzare i metodi [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) e [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). Il metodo [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) è da utilizzare per accedere alle porzioni del testo e quindi le modifiche possono essere apportate utilizzando il metodo [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) mentre il **Get** restituisce un array di oggetti [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) che possono essere manipolati per impostare varie proprietà come il nome del font, il colore del font, la grassetto, ecc. e il metodo **Set** può essere utilizzato per applicare le modifiche.

{{% /alert %}}

## **Come formattare righe e colonne**

A volte i developer devono applicare la stessa formattazione su righe o colonne. Applicare la formattazione alle celle una per una richiede spesso più tempo e non è una buona soluzione.
Per affrontare questo problema, Aspose.Cells fornisce un modo semplice e veloce discusso dettagliatamente in questo articolo.

### **Formattare Righe e Colonne**

Aspose.Cells fornisce una classe, la [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fornisce una raccolta [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows).

### **Come formattare una riga**

Ogni elemento nella raccolta [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) rappresenta un oggetto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row). L'oggetto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) offre il metodo [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) utilizzato per impostare la formattazione della riga. Per applicare la stessa formattazione a una riga, utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). I passaggi seguenti mostrano come utilizzarlo.

1. Aggiungi un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) alla classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) chiamando il suo metodo [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle).
1. Imposta le proprietà dell'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) per applicare le impostazioni di formattazione.
1. Attiva gli attributi rilevanti per l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).
1. Assegna l'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) configurato all'oggetto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Come formattare una colonna**

Anche la raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fornisce una raccolta [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns). Ciascun elemento nella raccolta [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) rappresenta un oggetto [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column). Similmente a un oggetto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), l'oggetto [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) offre anche il metodo [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) per formattare una colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Argomenti avanzati**
- [Impostazioni di Allineamento](/cells/it/net/cells-alignment-settings/)
- [Impostazioni dei Bordi](/cells/it/net/cells-border-settings/)
- [Imposta Formati Condizionali di file Excel e ODS.](/cells/it/net/conditional-formatting/)
- [Temi e Colori di Excel](/cells/it/net/excel-themes-and-colors/)
- [Impostazioni di Riempimento](/cells/it/net/cells-fill-settings/)
- [Impostazioni dei Caratteri](/cells/it/net/cells-font-settings/)
- [Formattare le Celle di un Foglio di Lavoro in un Documento di Lavoro](/cells/it/net/format-worksheet-cells-in-a-workbook/)
- [Implementare il Sistema di Data 1904](/cells/it/net/implement-1904-date-system/)
- [Unione e separazione di celle](/cells/it/net/merging-and-unmerging-cells/)
- [Impostazioni dei numeri](/cells/it/net/cells-number-settings/)
- [Ottenere e impostare lo stile delle celle](/cells/it/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="csharp" >}}
