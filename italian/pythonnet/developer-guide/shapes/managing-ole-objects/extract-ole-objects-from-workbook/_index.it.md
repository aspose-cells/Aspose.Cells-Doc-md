---
title: Estrarre oggetti OLE dal file di lavoro
type: docs
weight: 110
url: /it/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

A volte, è necessario estrarre oggetti OLE da un foglio di lavoro. Aspose.Cells for Python via .NET supporta l'estrazione e il salvataggio di questi oggetti Ole.

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

### **Estrazione di oggetti OLE usando Aspose.Cells per libreria Excel Python**

Il codice di seguito effettua il lavoro effettivo di individuare ed estrarre oggetti OLE. Gli oggetti OLE (file DOC, XLS e PDF) vengono salvati su disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
