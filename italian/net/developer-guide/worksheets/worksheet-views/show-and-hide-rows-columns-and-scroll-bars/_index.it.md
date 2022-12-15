---
title: Mostra e nascondi righe, colonne e barre di scorrimento
type: docs
weight: 20
url: /it/net/show-and-hide-rows-columns-and-scroll-bars/
---
{{% alert color="primary" %}}

Aspose.Cells fornisce modi per controllare la visibilità di righe, colonne e barre di scorrimento di un foglio di lavoro.

{{% /alert %}}

## **Mostra e nascondi righe e colonne**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente agli sviluppatori di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) raccolta che rappresenta tutte le celle del foglio di lavoro. Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fornisce diversi metodi per la gestione di righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

### **Mostra righe e colonne**

 Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando il metodo[**ScopriRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) e[**Scopri colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)raccolta rispettivamente. Entrambi i metodi accettano due parametri:

- **Indice riga o colonna** - l'indice di una riga o di una colonna utilizzato per mostrare la riga o la colonna specifica.
- **Altezza riga o larghezza colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo l'apertura.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Mentre si rende visibile una colonna nascosta, se è necessario ripristinarla alla larghezza assegnata in precedenza o alla larghezza originale, mostrare la colonna con una larghezza negativa. Ad esempio: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Nascondi righe e colonne**

 Gli sviluppatori possono nascondere una riga o una colonna chiamando il metodo[**NascondiRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) e[**Nascondi colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)raccolta rispettivamente. Entrambi i metodi accettano l'indice di riga e colonna come parametro per nascondere la riga o la colonna specifica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

È anche possibile nascondere una riga o una colonna impostando rispettivamente l'altezza della riga o la larghezza della colonna su 0.

{{% /alert %}}

### **Nascondi più righe e colonne**

 Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando il metodo[**Nascondi righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) e[**Nascondi colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)raccolta rispettivamente. Entrambi i metodi prendono l'indice di riga o colonna iniziale e il numero di righe o colonne che devono essere nascoste come parametri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Mostra e nascondi le barre di scorrimento**

Le barre di scorrimento vengono utilizzate per navigare nel contenuto di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:

- Barre di scorrimento verticali
- Barre di scorrimento orizzontali

Microsoft Excel fornisce anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere il contenuto del foglio di lavoro. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.

### **Controllo della visibilità delle barre di scorrimento**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class fornisce un'ampia gamma di proprietà e metodi per la gestione di un file Excel. Per controllare la visibilità delle barre di scorrimento, utilizzare il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) e[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)proprietà.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) e[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sono proprietà booleane, il che significa che queste proprietà possono solo memorizzare**VERO** o**falso** i valori.

#### **Rendere visibili le barre di scorrimento**

 Rendere visibili le barre di scorrimento impostando il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) proprietà a**VERO**.

#### **Nascondere le barre di scorrimento**

 Nascondere le barre di scorrimento impostando il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) proprietà a**falso**.

**Codice di esempio**

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
