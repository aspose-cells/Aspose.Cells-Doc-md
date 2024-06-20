---
title: La tua prima applicazione Aspose.Cells  Ciao mondo
type: docs
weight: 30
url: /it/net/your-first-aspose-cells-application-hello-world/
description: Crea, modifica e salva il tuo primo file excel in qualsiasi formato supportato usando Aspose.Cells for .NET per sperimentarne la semplicità e la potenza in C#.
keywords: C# Ciao Mondo, Aspose.Cells for .NET Ciao Mondo, La prima applicazione usando Aspose.Cells for .NET, Il primo programma tramite Aspose.Cells for .NET.
---

{{% alert color="primary" %}}

Questo tutorial mostra come creare una prima applicazione (Ciao Mondo) utilizzando la semplice API di Aspose.Cells. Questa semplice applicazione crea un file Microsoft Excel con il testo 'Ciao Mondo' in una cella di un foglio di lavoro specificato.

{{% /alert %}}

## **Come Creare l'Applicazione Ciao Mondo**

I passi seguenti creano l'applicazione Hello World utilizzando l'API Aspose.Cells:

1. Crea un'istanza della classe [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Se hai una licenza, quindi [applicala](/cells/it/net/licensing/).
   Se stai utilizzando la versione di valutazione, salta le righe di codice relative alla licenza.
1. Crea un nuovo file Excel, oppure apri un file Excel esistente.
1. Accedi a qualsiasi cella desiderata di un foglio di lavoro nel file di Excel.
1. Inserisci le parole **Hello World!** in una cella accessibile.
1. Genera il file modificato di Microsoft Excel.

L'implementazione dei passaggi sopra è dimostrata negli esempi seguenti.

### **Come Creare un Nuovo Workbook**

Nell'esempio seguente viene creato un nuovo workbook da zero, viene scritto Hello World! nella cella A1 del primo foglio di lavoro e viene salvato il file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Come Aprire un File Esistente**

Nell'esempio seguente viene aperto un file di modello Microsoft Excel esistente chiamato "Sample.xlsx", viene inserito il testo "Hello World!" nella cella A1 del primo foglio di lavoro e viene salvato il workbook.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
