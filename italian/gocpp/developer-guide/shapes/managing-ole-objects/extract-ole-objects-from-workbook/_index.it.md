---
title: Estrai oggetti OLE dal workbook con Golang tramite C++
linktitle: Estrarre oggetti OLE dal file di lavoro
type: docs
weight: 110
url: /it/go-cpp/extract-ole-objects-from-workbook/
description: Impara come estrarre oggetti OLE da un workbook usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

A volte, è necessario estrarre oggetti OLE da un workbook. Aspose.Cells supporta l'estrazione e il salvataggio di tali oggetti OLE.

Questo articolo mostra come creare un'applicazione console in Visual Studio ed estrarre diversi oggetti OLE da un workbook con poche semplici righe di codice.

{{% /alert %}}

## **Estrarre oggetti OLE da un file di lavoro**

### **Creazione di un file di lavoro modello**

1. Crea un workbook in Microsoft Excel.
1. Aggiungi un documento Microsoft Word, un workbook Excel e un documento PDF come oggetti OLE sul primo foglio di lavoro.

|**Modello di documento con oggetti OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Successivamente, estrai gli oggetti OLE e salvali sul disco rigido con i rispettivi tipi di file.

### **Scarica e installa Aspose.Cells**

1. [Scarica Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
1. Installalo sul tuo computer di sviluppo.

Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.

### **Crea un Progetto**

Avvia **Visual Studio** e crea una nuova applicazione console. Questo esempio mostrerà un'applicazione console C++.

1. Aggiungi Riferimenti
   1. Aggiungi un riferimento al componente Aspose.Cells nel tuo progetto, ad esempio, aggiungi un riferimento a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Estrai oggetti OLE**

Il codice sotto fa il vero lavoro di trovare ed estrarre oggetti OLE. Gli oggetti OLE (file DOC, XLS e PDF) vengono salvati su disco.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
