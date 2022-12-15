---
title: Formatta le celle
linktitle: Formatta le celle
type: docs
weight: 120
url: /it/net/cells-formatting/
description: Imposta il formato numerico, il bordo e il colore di sfondo per i file Excel su piattaforme .NET Framework, .NET Core, Mono o Xamarin.
---
## **introduzione**

{{% alert color="primary" %}}

 Aspose.Cells fornisce il[**Ottieni stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) e[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodi del[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) class, usata per ottenere/impostare lo stile di formattazione di una cella. Aspose.Cells fornisce anche a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)classe.

{{% /alert %}}

## **Formattare Cells utilizzando i metodi GetStyle e SetStyle**

Applica diversi tipi di stili di formattazione alle celle per impostare colori di sfondo o di primo piano, bordi, caratteri, allineamenti orizzontali e verticali, livello di rientro, direzione del testo, angolo di rotazione e molto altro.

### **Utilizzo dei metodi GetStyle e SetStyle**

 Se gli sviluppatori devono applicare diversi stili di formattazione a celle diverse, è meglio ottenere il formato[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) della cella utilizzando[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) metodo, specificare gli attributi di stile e quindi applicare la formattazione utilizzando[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)metodo. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare varie formattazioni su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Utilizzo dell'oggetto stile per formattare diversamente Cells**

 Se gli sviluppatori devono applicare lo stesso stile di formattazione a celle diverse, possono utilizzare[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto. Si prega di seguire i passaggi seguenti per utilizzare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto:

1.  Aggiungere un[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto chiamando il[**Crea stile**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) metodo del[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe
1.  Accedi ai nuovi aggiunti[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto
1.  Impostare le proprietà/attributi desiderati del file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto per applicare le impostazioni di formattazione desiderate
1. Assegna il configurato[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)opporsi alle celle desiderate

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare anche memoria.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Utilizzo degli stili predefiniti di Microsoft Excel 2007**

Se devi applicare stili di formattazione diversi per Microsoft Excel 2007, applica gli stili utilizzando l'API Aspose.Cells. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare uno stile predefinito su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Formattazione dei caratteri selezionati in un Cell**

La gestione delle impostazioni dei caratteri spiega come formattare il testo nelle celle, ma spiega solo come formattare tutto il contenuto della cella. Cosa succede se si desidera formattare solo i caratteri selezionati?

Aspose.Cells supporta anche questa funzione. Questo argomento spiega come utilizzare questa funzione in modo efficace.

### **Formattazione dei caratteri selezionati**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contiene il[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione rappresenta un oggetto della[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) la classe fornisce il[**Personaggi**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)metodo che accetta i seguenti parametri per selezionare un intervallo di caratteri all'interno di una cella:

- **Inizio indice**, l'indice del carattere da cui inizia la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

 Il[**Personaggi**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) Il metodo restituisce un'istanza di[**Impostazione carattere**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)class che consente agli sviluppatori di formattare i caratteri nello stesso modo in cui farebbero con una cella, come mostrato di seguito nell'esempio di codice. Nel file di output, nella cella A1, la parola 'Visit' sarà formattata con il font predefinito ma 'Aspose!' è in grassetto e blu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Se sei interessato a formattare una parte di Rich Text in una cella, prendi in considerazione l'utilizzo di[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodi. Il[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) metodo deve essere utilizzato per accedere alle parti del testo e quindi è possibile apportare modifiche utilizzando il[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodo mentre il**Ottenere**metodo restituisce un array di[**Impostazione carattere**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) oggetti che possono essere manipolati per impostare varie proprietà come nome del carattere, colore del carattere, grassetto, ecc. e**Impostare** metodo può essere utilizzato per applicare le modifiche.

{{% /alert %}}

## **Formattazione di righe e colonne**

A volte, gli sviluppatori devono applicare la stessa formattazione a righe o colonne. L'applicazione della formattazione alle celle una per una spesso richiede più tempo e non è una buona soluzione.
Per risolvere questo problema, Aspose.Cells fornisce un modo semplice e veloce discusso in dettaglio in questo articolo.

### **Formattazione di righe e colonne**

 Aspose.Cells mette a disposizione un corso, il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)la raccolta fornisce a[**Righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)collezione.

### **Formattazione di una riga**

 Ogni elemento del[**Righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) collezione rappresenta a[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row) oggetto. Il[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row)oggetto offre il[**Applica stile**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metodo utilizzato per impostare la formattazione della riga. Per applicare la stessa formattazione a una riga, utilizzare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto. I passaggi seguenti mostrano come usarlo.

1.  Aggiungere un[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) opporsi al[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class chiamando its[**Crea stile**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)metodo.
1.  Impostare il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)proprietà dell'oggetto per applicare le impostazioni di formattazione.
1.  Attiva gli attributi rilevanti per il file[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)oggetto.
1. Assegna il configurato[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) opporsi al[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row)oggetto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Formattazione di una colonna**

 Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) raccolta fornisce anche a[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) collezione. Ogni elemento del[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) collezione rappresenta a[**Colonna**](https://reference.aspose.com/cells/net/aspose.cells/column) oggetto. Simile all'a[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row) oggetto, il[**Colonna**](https://reference.aspose.com/cells/net/aspose.cells/column) oggetto offre anche il[**Applica stile**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)metodo per la formattazione di una colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Argomenti avanzati**
- [Impostazioni di allineamento](/cells/it/net/cells-alignment-settings/)
- [Impostazioni del bordo](/cells/it/net/cells-border-settings/)
- [Imposta i formati condizionali dei file Excel e ODS.](/cells/it/net/conditional-formatting/)
- [Temi e colori di Excel](/cells/it/net/excel-themes-and-colors/)
- [Impostazioni di riempimento](/cells/it/net/cells-fill-settings/)
- [Impostazioni carattere](/cells/it/net/cells-font-settings/)
- [Formattare il foglio di lavoro Cells in una cartella di lavoro](/cells/it/net/format-worksheet-cells-in-a-workbook/)
- [Implementare il sistema di data 1904](/cells/it/net/implement-1904-date-system/)
- [Fusione e Separazione Cells](/cells/it/net/merging-and-unmerging-cells/)
- [Impostazioni numero](/cells/it/net/cells-number-settings/)
- [Ottieni e imposta stile per le celle](/cells/it/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

