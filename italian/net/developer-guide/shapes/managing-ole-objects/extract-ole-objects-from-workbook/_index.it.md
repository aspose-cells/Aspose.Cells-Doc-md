---
title: Estrai oggetti OLE dalla cartella di lavoro
type: docs
weight: 110
url: /it/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

A volte, è necessario estrarre oggetti OLE da una cartella di lavoro. Aspose.Cells supporta l'estrazione e il salvataggio di quegli oggetti Ole.

Questo articolo mostra come creare un'applicazione console in Visual Studio.Net ed estrarre diversi oggetti OLE da una cartella di lavoro con poche semplici righe di codice.

{{% /alert %}}

## **Estrai oggetti OLE da una cartella di lavoro**

### **Creazione di una cartella di lavoro modello**

1. Creato una cartella di lavoro in Microsoft Excel.
1. Aggiungi un documento Microsoft Word, una cartella di lavoro Excel e un documento PDF come oggetti OLE nel primo foglio di lavoro.

|**Documento modello con oggetti OLE (OleFile.xls)**|
|:- |
|![cose da fare:immagine_alt_testo](extract-ole-objects-from-workbook_1.png)|

Quindi estrarre gli oggetti OLE e salvarli sul disco rigido con i rispettivi tipi di file.

### **Scarica e installa Aspose.Cells**

1. [Scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installalo sul tuo computer di sviluppo.

Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.

### **Crea un progetto**

 Inizio**Visual Studio.Net** e creare una nuova applicazione console. Questo esempio mostrerà un'applicazione console C#, ma puoi usare anche VB.NET.

1. Aggiungi riferimenti
 1. Aggiungi un riferimento al componente Aspose.Cells al tuo progetto, ad esempio aggiungi un riferimento a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Estrai oggetti OLE**

Il codice seguente esegue il lavoro effettivo di ricerca ed estrazione di oggetti OLE. Gli oggetti OLE (file DOC, XLS e PDF) vengono salvati su disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
