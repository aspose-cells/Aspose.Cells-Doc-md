---
title: Formattare le celle
description: Scopri come formattare e definire lo stile delle celle in Aspose.Cells for .NET, inclusa la formattazione dei numeri, la formattazione della data, gli stili dei caratteri e altre opzioni di stile delle celle. La nostra guida ti aiuterà a creare fogli di calcolo accattivanti e dall'aspetto professionale.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Formattare le celle
type: docs
weight: 120
url: /it/net/cells-formatting/
---
##  **introduzione**

{{% alert color="primary" %}}

 Aspose.Cells fornisce il[**Ottieni Stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) E[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodi del[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) classe, utilizzata per ottenere/impostare lo stile di formattazione di una cella. Aspose.Cells fornisce anche a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)classe.

{{% /alert %}}

##  **Come formattare Cells utilizzando i metodi GetStyle e SetStyle**

Applica diversi tipi di stili di formattazione sulle celle per impostare colori di sfondo o di primo piano, bordi, caratteri, allineamenti orizzontali e verticali, livello di rientro, direzione del testo, angolo di rotazione e molto altro.

###  **Come utilizzare i metodi GetStyle e SetStyle**

 Se gli sviluppatori devono applicare stili di formattazione diversi a celle diverse, è meglio ottenere il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) della cella utilizzando[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) metodo, specificare gli attributi di stile e quindi applicare la formattazione utilizzando[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)metodo. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare varie formattazioni su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **Come utilizzare l'oggetto stile per formattare diversamente Cells**

 Se gli sviluppatori devono applicare lo stesso stile di formattazione a celle diverse, possono utilizzare[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto. Si prega di seguire i passaggi seguenti per utilizzare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto:

1.  Aggiungere un[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto chiamando il[**Crea stile**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) metodo del[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe
1.  Accedi a quelli appena aggiunti[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  Imposta le proprietà/attributi desiderati del file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto per applicare le impostazioni di formattazione desiderate
1.  Assegnare il configurato[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)opporsi alle celle desiderate

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e anche risparmiare memoria.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **Come utilizzare gli stili predefiniti di Excel 2007 Microsoft**

Se è necessario applicare stili di formattazione diversi per Microsoft Excel 2007, applicare gli stili utilizzando Aspose.Cells API. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare uno stile predefinito su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **Come formattare i caratteri selezionati in Cell**

Gestire le impostazioni dei caratteri spiega come formattare il testo nelle celle, ma spiega solo come formattare tutto il contenuto della cella. Cosa succede se vuoi formattare solo i caratteri selezionati?

Aspose.Cells supporta anche questa funzione. Questo argomento spiega come utilizzare questa funzionalità in modo efficace.

###  **Come formattare i caratteri selezionati**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene il file[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 IL[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) la classe fornisce il file[**Caratteri**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)metodo che accetta i seguenti parametri per selezionare un intervallo di caratteri all'interno di una cella:

- *Indice iniziale**, l'indice del carattere da cui inizia la selezione.
- *Numero di caratteri**, il numero di caratteri da selezionare.

 IL[**Caratteri**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) Il metodo restituisce un'istanza del metodo[**Impostazione carattere**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)classe che consente agli sviluppatori di formattare i caratteri nello stesso modo in cui farebbero una cella, come mostrato di seguito nell'esempio di codice. Nel file di output, nella cella A1, la parola 'Visita' verrà formattata con il carattere predefinito ma 'Aspose!' è audace e blu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Se sei interessato a formattare una porzione di Rich Text in una cella, considera l'utilizzo di[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodi. IL[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) è necessario utilizzare il metodo per accedere alle parti del testo e quindi è possibile apportare modifiche utilizzando il metodo[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodo mentre il**Ottenere** Il metodo restituisce un array di[**Impostazione carattere**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) oggetti che possono essere manipolati per impostare varie proprietà come nome del carattere, colore del carattere, grassetto, ecc. e**Impostato** metodo può essere utilizzato per applicare le modifiche.

{{% /alert %}}

##  **Come formattare righe e colonne**

A volte gli sviluppatori devono applicare la stessa formattazione su righe o colonne. Applicare la formattazione alle celle una per una spesso richiede più tempo e non è una buona soluzione.
Per risolvere questo problema, Aspose.Cells fornisce un modo semplice e veloce discusso in dettaglio in questo articolo.

###  **Formattazione di righe e colonne**

 Aspose.Cells mette a disposizione una classe, la[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. IL[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta fornisce a[**Righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)collezione.

###  **Come formattare una riga**

 Ogni elemento in[**Righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) la raccolta rappresenta a[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row) oggetto. IL[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row)l'oggetto offre il[**Applica stile**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metodo utilizzato per impostare la formattazione della riga. Per applicare la stessa formattazione a una riga, utilizzare il comando[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto. I passaggi seguenti mostrano come usarlo.

1.  Aggiungere un[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) opporsi al[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe chiamando its[**Crea stile**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)metodo.
1.  Impostare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)le proprietà dell'oggetto per applicare le impostazioni di formattazione.
1.  Attiva gli attributi rilevanti per il[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)oggetto.
1.  Assegnare il configurato[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) opporsi al[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row)oggetto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **Come formattare una colonna**

 IL[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta fornisce anche a[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) collezione. Ogni elemento in[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) la raccolta rappresenta a[**Colonna**](https://reference.aspose.com/cells/net/aspose.cells/column) oggetto. Simile ad a[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row) oggetto, il[**Colonna**](https://reference.aspose.com/cells/net/aspose.cells/column) l'oggetto offre anche il[**Applica stile**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)metodo per formattare una colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **Argomenti avanzati**
- [Impostazioni di allineamento](/cells/it/net/cells-alignment-settings/)
- [Impostazioni del bordo](/cells/it/net/cells-border-settings/)
- [Imposta i formati condizionali dei file Excel e ODS.](/cells/it/net/conditional-formatting/)
- [Temi e colori di Excel](/cells/it/net/excel-themes-and-colors/)
- [Impostazioni di riempimento](/cells/it/net/cells-fill-settings/)
- [Impostazioni dei caratteri](/cells/it/net/cells-font-settings/)
- [Formatta il foglio di lavoro Cells in una cartella di lavoro](/cells/it/net/format-worksheet-cells-in-a-workbook/)
- [Implementare il sistema di data 1904](/cells/it/net/implement-1904-date-system/)
- [Unire e separare Cells](/cells/it/net/merging-and-unmerging-cells/)
- [Impostazioni numero](/cells/it/net/cells-number-settings/)
- [Ottieni e imposta lo stile per le celle](/cells/it/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

