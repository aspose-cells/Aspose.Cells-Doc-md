---
title: Mostra e Nascondi Righe Colonne e Barre di Scorrimento
type: docs
weight: 20
url: /it/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Questo articolo dimostra come visualizzare e nascondere programmaticamente le righe e le colonne di un foglio di lavoro Excel usando l API Aspose.Cells per Python via .NET. La visibilità delle barre di scorrimento può essere regolata, e diverse righe e colonne possono essere nascoste.
keywords: Biblioteca Python Excel, mostra righe e colonne in Python, nascondi righe e colonne in Python, mostra la barra di scorrimento verticale, mostra la barra di scorrimento orizzontale, nascondi la barra di scorrimento verticale, nascondi la barra di scorrimento orizzontale, mostra e nascondi righe, colonne e barre di scorrimento.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET offre modalità per controllare la visibilità delle righe, delle colonne e delle barre di scorrimento di un foglio di lavoro.

{{% /alert %}}

## **Mostra e nascondi righe e colonne**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) contiene una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) che rappresenta tutte le celle nel foglio di lavoro. La collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono illustrati di seguito.

### **Mostra Righe e Colonne**

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) e [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Entrambi i metodi prendono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Mentre si rende visibile una colonna nascosta, se è necessario ripristinarla alla larghezza assegnata in precedenza o alla larghezza originale, si prega di mostrare la colonna con larghezza negativa. Ad esempio: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Nascondi Righe e Colonne**

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) e [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Entrambi i metodi prendono l'indice della riga e della colonna come parametro per nascondere la riga o colonna specifica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.

{{% /alert %}}

### **Nascondi Più Righe e Colonne**

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando rispettivamente i metodi [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) e [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Entrambi i metodi prendono l'indice di partenza della riga o colonna e il numero di righe o colonne che devono essere nascoste come parametri.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Mostra e nascondi le barre di scorrimento**

Le barre di scorrimento vengono utilizzate per navigare nei contenuti di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:

- Barre di scorrimento verticali
- Barre di scorrimento orizzontali

Microsoft Excel offre anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere i contenuti del foglio di lavoro. Usando Aspose.Cells per Python via .NET, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.

### **Controllare la visibilità delle barre di scorrimento**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) offre molte proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle barre di scorrimento, usa le proprietà [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) e [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) della classe. [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) e [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) sono proprietà Booleane, il che significa che queste proprietà possono memorizzare solo valori **true** o **false**.

#### **Rendere visibili le barre di scorrimento**

Rendere le barre di scorrimento visibili impostando la proprietà [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) o [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) su **true**.

#### **Nascondere le barre di scorrimento**

Nascondere le barre di scorrimento impostando la proprietà [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) o [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) su **false**.

**Codice di Esempio**

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
