---
title: Formattare celle
description: Impara come formattare e stilizzare le celle in Aspose.Cells for Python via .NET, includendo la formattazione dei numeri, la formattazione delle date, gli stili di carattere e altre opzioni di stile delle celle. La nostra guida ti aiuterà a creare fogli di calcolo attraenti e professionali.
keywords: Aspose.Cells for Python via .NET, formattazione celle, styling, formattazione numeri, formattazione date, stile carattere, opzioni di stile celle, foglio di calcolo, creare, aspetto professionale, formattare righe e colonne.
linktitle: Formattare celle
type: docs
weight: 120
url: /it/python-net/cells-formatting/
---

## **Introduzione**

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fornisce i metodi [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) e [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) della classe [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell), usati per ottenere/impostare lo stile di formattazione di una cella. Aspose.Cells for Python via .NET fornisce anche una classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{% /alert %}}

## **Come formattare le celle utilizzando i metodi GetStyle e SetStyle**

Applicare diversi tipi di stili di formattazione alle celle per impostare colori di sfondo o primo piano, bordi, caratteri, allineamenti orizzontali e verticali, livello di rientro, direzione del testo, angolo di rotazione e molto altro.

### **Come utilizzare i metodi GetStyle e SetStyle**

Se gli sviluppatori devono applicare stili di formattazione diversi a celle diverse, è meglio ottenere il [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) della cella utilizzando il metodo [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style), specificare gli attributi dello stile e quindi applicare la formattazione utilizzando il metodo [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style). Di seguito è riportato un esempio per dimostrare questo approccio per applicare varie formattazioni a una cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Come utilizzare l'oggetto stile per formattare celle diverse**

Se gli sviluppatori hanno bisogno di applicare lo stesso stile di formattazione a diverse celle, possono utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Seguire i passaggi seguenti per utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style):

1. Aggiungi un oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) richiamando il metodo [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)
1. Accedere al nuovo oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) aggiunto
1. Imposta le proprietà/attributi desiderati dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) per applicare le impostazioni di formattazione desiderate
1. Assegna l'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) configurato alle celle desiderate

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare memoria anche.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Come utilizzare gli stili predefiniti di Microsoft Excel 2007**

Se devi applicare stili di formattazione diversi per Microsoft Excel 2007, applica gli stili usando l'API di Aspose.Cells for Python via .NET. Un esempio viene fornito di seguito per dimostrare questo approccio nell'applicare uno stile predefinito su una cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Come formattare i caratteri selezionati in una cella**

Il trattamento delle impostazioni del carattere spiega come formattare il testo nelle celle, ma spiega solo come formattare tutto il contenuto della cella. E se si vuole formattare solo alcuni caratteri?

Aspose.Cells per Python via .NET supporta anche questa funzionalità. Questo argomento spiega come utilizzare efficacemente questa funzione.

### **Come formattare caratteri selezionati**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene la collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Ogni elemento nella collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) fornisce il metodo [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) che riceve i seguenti parametri per selezionare una gamma di caratteri all'interno di una cella:

- **Indice di inizio**, l'indice del carattere da cui inizia la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Il metodo [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) restituisce un'istanza della classe [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) che consente agli sviluppatori di formattare i caratteri allo stesso modo in cui farebbero con una cella come mostrato di seguito nell'esempio di codice. Nel file di output, nella cella A1, la parola 'Visit' verrà formattata con il carattere predefinito ma 'Aspose!' è in grassetto e blu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Se sei interessato a formattare una parte del testo ricco in una cella, considera di usare i metodi [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) e [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters). Il metodo [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) serve per accedere alle parti del testo e quindi apportare modifiche utilizzando il metodo [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters), mentre il metodo **Get** restituisce un array di oggetti [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) che possono essere manipolati per impostare varie proprietà come il nome del font, il colore del font, il grassetto, ecc. e il metodo **Set** può essere usato per applicare le modifiche.

{{% /alert %}}

## **Come formattare righe e colonne**

A volte i developer devono applicare la stessa formattazione su righe o colonne. Applicare la formattazione alle celle una per una richiede spesso più tempo e non è una buona soluzione.
Per risolvere questo problema, Aspose.Cells per Python via .NET offre un modo semplice e veloce, discusso in dettaglio in questo articolo.

### **Formattare Righe e Colonne**

Aspose.Cells per Python via .NET fornisce una classe, la [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fornisce una collezione [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows).

### **Come formattare una riga**

Ogni elemento nella raccolta [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) rappresenta un oggetto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row). L'oggetto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) offre il metodo [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) utilizzato per impostare la formattazione della riga. Per applicare la stessa formattazione a una riga, utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). I passaggi seguenti mostrano come utilizzarlo.

1. Aggiungi un oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) alla classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) chiamando il suo metodo [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style).
1. Imposta le proprietà dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) per applicare le impostazioni di formattazione.
1. Attiva gli attributi rilevanti per l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).
1. Assegna l'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) configurato all'oggetto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Come formattare una colonna**

Anche la raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fornisce una raccolta [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns). Ciascun elemento nella raccolta [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) rappresenta un oggetto [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column). Similmente a un oggetto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row), l'oggetto [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) offre anche il metodo [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) per formattare una colonna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Argomenti avanzati**
- [Impostazioni di Allineamento](/cells/it/python-net/cells-alignment-settings/)
- [Impostazioni dei Bordi](/cells/it/python-net/cells-border-settings/)
- [Imposta Formati Condizionali di file Excel e ODS.](/cells/it/python-net/conditional-formatting/)
- [Temi e Colori di Excel](/cells/it/python-net/excel-themes-and-colors/)
- [Impostazioni di Riempimento](/cells/it/python-net/cells-fill-settings/)
- [Impostazioni dei Caratteri](/cells/it/python-net/cells-font-settings/)
- [Formattare le Celle di un Foglio di Lavoro in un Documento di Lavoro](/cells/it/python-net/format-worksheet-cells-in-a-workbook/)
- [Implementare il Sistema di Data 1904](/cells/it/python-net/implement-1904-date-system/)
- [Unione e separazione di celle](/cells/it/python-net/merging-and-unmerging-cells/)
- [Impostazioni dei numeri](/cells/it/python-net/cells-number-settings/)
- [Ottenere e impostare lo stile delle celle](/cells/it/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="python-net" >}}
