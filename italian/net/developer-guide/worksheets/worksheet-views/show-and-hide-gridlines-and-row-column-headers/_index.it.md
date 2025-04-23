---
title: Mostra e nasconde le linee della griglia e gli intestazioni delle righe e delle colonne
type: docs
weight: 30
url: /it/net/show-and-hide-gridlines-and-row-column-headers/
description: Questo articolo fornisce esempi di codice per utilizzare l API C# o la libreria .NET per nascondere o mostrare in modo programmato le linee della griglia, le intestazioni delle righe e delle colonne di un foglio di calcolo Excel.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la visualizzazione e la modifica delle linee della griglia del foglio di calcolo che sono visibili per impostazione predefinita. Fornisce anche il controllo della visibilità delle intestazioni delle righe e delle colonne del foglio di calcolo.

{{% /alert %}}

## **Mostrare e nascondere le linee della griglia**

Tutti i fogli di lavoro di Excel hanno linee di griglia per impostazione predefinita. Aiutano a delimitare le celle in modo che sia facile inserire dati in celle specifiche. Le linee di griglia ci consentono di visualizzare un foglio di calcolo come una collezione di celle, in cui ogni cella è facilmente identificabile.

### **Controllo della visibilità delle linee della griglia**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente agli sviluppatori di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire un foglio di lavoro. Per controllare la visibilità delle linee della griglia, utilizzare la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) è una proprietà Booleana, il che significa che può solo memorizzare un valore **true** o **false**.

#### **Rendere Visibili le Linee della Griglia**

Rendi visibili le linee della griglia impostando la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **true**.

#### **Nascondere le Linee della Griglia**

Nascondi le linee della griglia impostando la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **false**.

Di seguito è riportato un esempio completo che dimostra l'uso della proprietà [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) aprendo un file excel (book1.xls), nascondendo le linee della griglia sul primo foglio di lavoro e salvando il file modificato come output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Mostra e nasconde gli intestazioni delle righe e delle colonne**

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e colonne hanno valori univoci che vengono utilizzati per identificarle e per identificare singole celle. Ad esempio, le righe sono numerate – 1, 2, 3, 4, ecc. – e le colonne sono ordinate in modo alfabetico – A, B, C, D, ecc. I valori delle righe e delle colonne sono visualizzati negli intestazioni. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di queste intestazioni delle righe e delle colonne.

### **Controllo della visibilità dei fogli di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente agli sviluppatori di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire un foglio di lavoro. Per controllare la visibilità degli intestazioni di riga e colonna, utilizzare la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) è una proprietà booleana, il che significa che può solo memorizzare un valore **true** o **false**.

#### **Rendere visibili le intestazioni di riga/colonna**

Rendi visibili le intestazioni di riga e colonna impostando la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **true**.

#### **Nascondere le intestazioni di riga/colonna**

Nascondi le intestazioni di riga e colonna impostando la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **false**.

Di seguito è riportato un esempio completo che mostra come utilizzare la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) aprendo un file Excel (book1.xls), nascondendo le intestazioni di riga e colonna nel primo foglio di lavoro e salvando il file modificato come output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

È anche possibile utilizzare i metodi [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) e [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) per rendere visibili più righe e colonne.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
