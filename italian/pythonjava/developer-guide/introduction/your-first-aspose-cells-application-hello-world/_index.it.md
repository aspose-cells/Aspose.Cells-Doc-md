---
title: La tua prima domanda Aspose.Cells - Hello World
type: docs
weight: 30
url: /it/python-java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Questo argomento per principianti mostra come gli sviluppatori possono creare una prima applicazione semplice (Hello World) utilizzando Aspose.Cells' semplice API. L'applicazione crea un file Excel Microsoft con le parole Hello World in una cella specificata di un foglio di lavoro.

{{% /alert %}}

### **Creazione dell'applicazione Hello World**

Per creare l'applicazione Hello World utilizzando Aspose.Cells API:

1.  Crea un'istanza di**[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**classe.
1. Applica la licenza:
1. Se hai acquistato una licenza, usa la licenza nella tua applicazione per ottenere l'accesso alla piena funzionalità di Aspose.Cells
 1. Se stai utilizzando la versione di valutazione del componente (se stai utilizzando Aspose.Cells senza licenza), salta questo passaggio.
1. Crea un nuovo file Excel Microsoft o apri un file esistente in cui desideri aggiungere/aggiornare del testo.
1. Accedi a qualsiasi cella di un foglio di lavoro nel file Excel Microsoft.
1.  Inserisci le parole**Hello World!** in una cella a cui si accede.
1. Genera il file Excel Microsoft modificato.

Gli esempi seguenti illustrano i passaggi precedenti.

#### **Creazione di una cartella di lavoro**

L'esempio seguente crea una nuova cartella di lavoro da zero, scrive le parole "Hello World!" nella cella A1 del primo foglio di lavoro e salva il file.

**Il foglio di calcolo generato** 

![cose da fare:immagine_alt_testo](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFile.py" >}}

#### **Apertura di un file esistente**

 L'esempio seguente apre un file modello Excel Microsoft esistente chiamato**libro1.xls**, scrive le parole "Hello World!" nella cella A1 nel primo foglio di lavoro e salva la cartella di lavoro come nuovo file.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpeningExistingFile.py" >}}
