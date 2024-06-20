---
title: Estrarre oggetti OLE dal file di lavoro
type: docs
weight: 110
url: /it/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

A volte è necessario estrarre gli oggetti OLE da un file di lavoro. Aspose.Cells supporta l'estrazione e il salvataggio di quegli oggetti Ole.

Questo articolo mostra come creare un'applicazione console in Visual Studio.Net ed estrarre diversi oggetti OLE da un file di lavoro con poche righe di codice.

{{% /alert %}}

## **Estrarre oggetti OLE da un file di lavoro**

### **Creazione di un file di lavoro modello**

1. Creato un documento di lavoro in Microsoft Excel.
1. Aggiungi un documento di Microsoft Word, un libro di Excel e un documento in formato PDF come oggetti OLE nel primo foglio di lavoro.

|**Modello di documento con oggetti OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Successivamente estrai gli oggetti OLE e salvali sull'hard disk con i rispettivi tipi di file.

### **Scarica e installa Aspose.Cells**

1. [Scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installalo sul tuo computer di sviluppo.

Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.

### **Crea un Progetto**

Avvia **Visual Studio.Net** e crea un nuova applicazione console. Questo esempio mostrerà un'applicazione console C#, ma è possibile utilizzare anche VB.NET.

1. Aggiungi Riferimenti
   1. Aggiungi un riferimento al componente Aspose.Cells al tuo progetto, ad esempio aggiungi un riferimento a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Estrai oggetti OLE**

Il codice di seguito effettua il lavoro effettivo di individuare ed estrarre oggetti OLE. Gli oggetti OLE (file DOC, XLS e PDF) vengono salvati su disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
