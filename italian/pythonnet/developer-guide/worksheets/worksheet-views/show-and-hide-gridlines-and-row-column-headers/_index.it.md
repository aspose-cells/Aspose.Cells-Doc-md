---
title: Mostra e nasconde le linee della griglia e gli intestazioni delle righe e delle colonne
type: docs
weight: 30
url: /it/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Questo articolo fornisce un codice di esempio per utilizzare l API Aspose.Cells per Python via .NET per nascondere o mostrare programmaticamente le griglie, gli header di riga e colonna di un foglio di lavoro di Excel.
keywords: Libreria Excel Python, Mostra e Nascondi Griglie, Come Mostrare e Nascondere Header di Riga e Colonna in Python, Come Mostrare e Nascondere Griglie e Header di Riga e Colonna in Python.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET supporta la visualizzazione e l'occultamento delle griglie del foglio di lavoro, visibili per impostazione predefinita. Fornisce inoltre il controllo sulla visibilità degli header di riga e colonna del foglio di lavoro.

{{% /alert %}}

## **Mostrare e nascondere le linee della griglia**

Tutti i fogli di lavoro di Excel hanno linee di griglia per impostazione predefinita. Aiutano a delimitare le celle in modo che sia facile inserire dati in celle specifiche. Le linee di griglia ci consentono di visualizzare un foglio di calcolo come una collezione di celle, in cui ogni cella è facilmente identificabile.

### **Controllo della visibilità delle linee della griglia**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente agli sviluppatori di accedere a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle griglie, utilizzare la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) è una proprietà booleana, il che significa che può memorizzare solo un valore **true** o **false**.

#### **Rendere Visibili le Linee della Griglia**

Rendi visibili le linee della griglia impostando la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**.

#### **Nascondere le Linee della Griglia**

Nascondi le linee della griglia impostando la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **false**.

Di seguito è riportato un esempio completo che dimostra l'uso della proprietà [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) aprendo un file excel (book1.xls), nascondendo le linee della griglia sul primo foglio di lavoro e salvando il file modificato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Mostra e nasconde gli intestazioni delle righe e delle colonne**

Tutti i fogli di lavoro in un file di Excel sono composti da celle disposte in righe e colonne. Tutte le righe e colonne hanno valori unici che vengono utilizzati per identificarli e per identificare le singole celle. Ad esempio, le righe sono numerate – 1, 2, 3, 4, ecc. – e le colonne sono ordinate alfabeticamente – A, B, C, D, ecc. I valori delle righe e delle colonne sono visualizzati negli header. Utilizzando Aspose.Cells per Python via .NET, gli sviluppatori possono controllare la visibilità di questi header di riga e colonna.

### **Controllo della visibilità dei fogli di lavoro**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente agli sviluppatori di accedere a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità degli header di riga e colonna, utilizzare la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) è una proprietà booleana, il che significa che può memorizzare solo un valore **true** o **false**.

#### **Rendere visibili le intestazioni di riga/colonna**

Rendi visibili le intestazioni di riga e colonna impostando la proprietà [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**.

#### **Nascondere le intestazioni di riga/colonna**

Nascondi le intestazioni di riga e colonna impostando la proprietà [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **false**.

Di seguito è riportato un esempio completo che mostra come utilizzare la proprietà [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) aprendo un file Excel (book1.xls), nascondendo le intestazioni di riga e colonna nel primo foglio di lavoro e salvando il file modificato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

È anche possibile utilizzare i metodi [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) e [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) della classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) per rendere visibili più righe e colonne.

{{% /alert %}}
