---
title: Mostra e nasconde le linee della griglia e gli intestazioni delle righe e delle colonne
type: docs
weight: 30
url: /it/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Questo articolo fornisce codice di esempio per usare l API Aspose.Cells per Python via .NET per nascondere o mostrare programmaticamente le linee della griglia, le intestazioni di riga e colonna di un foglio di lavoro Excel.
keywords: Biblioteca Python Excel, mostra e nascondi le linee della griglia in Python, Come mostrare e nascondere le intestazioni di riga e colonna in Python, Come mostrare e nascondere le linee della griglia e le intestazioni di riga e colonna in Python.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET supporta la possibilità di nascondere e mostrare le linee della griglia del foglio di lavoro, che sono visibili di default. Offre anche il controllo sulla visibilità delle intestazioni di riga e colonna del foglio di lavoro.

{{% /alert %}}

## **Mostrare e nascondere le linee della griglia**

Tutti i fogli di lavoro di Excel hanno linee di griglia per impostazione predefinita. Aiutano a delimitare le celle in modo che sia facile inserire dati in celle specifiche. Le linee di griglia ci consentono di visualizzare un foglio di calcolo come una collezione di celle, in cui ogni cella è facilmente identificabile.

### **Controllo della visibilità delle linee della griglia**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) offre un ampio insieme di proprietà e metodi per gestire un foglio di lavoro. Per controllare la visibilità delle linee della griglia, usa la proprietà [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) della classe [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) è una proprietà Booleana, il che significa che può memorizzare solo un valore **true** o **false**.

#### **Rendere Visibili le Linee della Griglia**

Rendi visibili le linee della griglia impostando la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**.

#### **Nascondere le Linee della Griglia**

Nascondi le linee della griglia impostando la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **false**.

Di seguito è riportato un esempio completo che dimostra l'uso della proprietà [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) aprendo un file excel (book1.xls), nascondendo le linee della griglia sul primo foglio di lavoro e salvando il file modificato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Mostra e nasconde gli intestazioni delle righe e delle colonne**

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e le colonne hanno valori unici utilizzati per identificarli e per riconoscere le singole celle. Per esempio, le righe sono numerate – 1, 2, 3, 4, ecc. – e le colonne sono ordinate alfabeticamente – A, B, C, D, ecc. I valori di riga e colonna sono visualizzati nelle intestazioni. Usando Aspose.Cells per Python via .NET, gli sviluppatori possono controllare la visibilità di queste intestazioni di riga e colonna.

### **Controllo della visibilità dei fogli di lavoro**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) offre un ampio insieme di proprietà e metodi per gestire un foglio di lavoro. Per controllare la visibilità delle intestazioni di riga e colonna, usa la proprietà [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) della classe [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) è una proprietà Booleana, che significa che può memorizzare solo un valore **true** o **false**.

#### **Rendere visibili le intestazioni di riga/colonna**

Rendi visibili le intestazioni di riga e colonna impostando la proprietà [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**.

#### **Nascondere le intestazioni di riga/colonna**

Nascondi le intestazioni di riga e colonna impostando la proprietà [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **false**.

Di seguito è riportato un esempio completo che mostra come utilizzare la proprietà [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) aprendo un file Excel (book1.xls), nascondendo le intestazioni di riga e colonna nel primo foglio di lavoro e salvando il file modificato come output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

È anche possibile utilizzare i metodi [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) e [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) della classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) per rendere visibili più righe e colonne.

{{% /alert %}}
