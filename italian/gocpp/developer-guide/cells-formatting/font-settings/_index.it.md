---
title: Impostazioni del carattere con Golang via C++
linktitle: Impostazioni del carattere
type: docs
weight: 30
url: /it/go-cpp/cells-font-settings/
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Supporta la configurazione delle impostazioni dei font delle celle, consentendo agli utenti di personalizzare lo stile e le proprietà del font delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per impostare le impostazioni dei font delle celle.
keywords: Aspose.Cells, Celle, Impostazioni del Carattere, Stili, Proprietà
---

{{% alert color="primary" %}}

L'aspetto e la sensazione di un testo possono essere controllati modificando le impostazioni del font. Le impostazioni del font possono includere nome, stile, dimensione, colore ed effetti degli font. Proprio come Microsoft Excel, anche Aspose.Cells supporta la configurazione delle impostazioni del font delle celle.

{{% /alert %}}

## **Configurazione delle Impostazioni del Carattere**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una collezione [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Ciascun elemento nella collezione [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fornisce i metodi [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) e [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/) della classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) utilizzati per ottenere e impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fornisce proprietà per configurare le impostazioni del carattere.

### **Impostazione del nome del carattere**

Gli sviluppatori possono applicare qualsiasi font al testo all’interno di una cella usando la proprietà [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) dell’oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Impostare lo stile del carattere su Grassetto**

Gli sviluppatori possono rendere il testo in grassetto impostando la proprietà [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) su **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Impostazione della dimensione del carattere**

Imposta la dimensione del carattere con la proprietà [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Impostazione del colore del carattere**

Usa la proprietà [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) dell’oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) per impostare il colore del font. Seleziona un colore dall’enumerazione Colore (parte del framework C++) e assegnalo alla proprietà [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Impostazione del tipo sottolineato del carattere**

Utilizzare la proprietà [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) per sottolineare il testo. Aspose.Cells offre vari tipi predefiniti di sottolineatura nel'enumerazione [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Tipi di sottolineatura del carattere**|**Descrizione**|
| :- | :- |
|Accounting|Un solo sottolineatura contabile|
|Double|Doppia sottolineatura|
|DoubleAccounting|Doppia sottolineatura contabile|
|None|Nessuna sottolineatura|
|Single|Una singola sottolineatura|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Impostazione dell'effetto barrato**

Applicare il barrato impostando la proprietà [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) su **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Impostazione dell'effetto pedice**

Applica il pedice impostando la proprietà [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) su **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Impostazione dell'effetto esponente sulla font**

I programmatori possono applicare l'effetto esponente sulla font impostando la proprietà [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) dell'oggetto [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) su **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Argomenti avanzati**
- [Applica gli effetti esponente e pedice sulle font](/cells/it/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
