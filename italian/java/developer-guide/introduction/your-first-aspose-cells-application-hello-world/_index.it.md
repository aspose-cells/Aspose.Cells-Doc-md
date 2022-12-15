---
title: La tua prima domanda Aspose.Cells - Hello World
type: docs
weight: 30
url: /it/java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Questo argomento per principianti mostra come gli sviluppatori possono creare una semplice prima applicazione (Hello World) utilizzando la semplice API Aspose.Cells. L'applicazione crea un file Microsoft Excel con le parole Hello World in una cella specificata di un foglio di lavoro.

{{% /alert %}}

### **Creazione dell'applicazione Hello World**

Per creare l'applicazione Hello World utilizzando l'API Aspose.Cells:

1.  Crea un'istanza di**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)**classe.
1. Applica la licenza:
 1. Se hai acquistato una licenza, usa la licenza nella tua applicazione per ottenere l'accesso alla piena funzionalità di Aspose.Cells
1. Se stai utilizzando la versione di valutazione del componente (se stai utilizzando Aspose.Cells senza licenza), salta questo passaggio.
1. Crea un nuovo file Microsoft Excel o apri un file esistente in cui desideri aggiungere/aggiornare del testo.
1. Accedi a qualsiasi cella di un foglio di lavoro nel file Microsoft Excel.
1.  Inserisci le parole**Hello World!** in una cella a cui si accede.
1. Genera il file Microsoft Excel modificato.

Gli esempi seguenti illustrano i passaggi precedenti.

#### **Creazione di una cartella di lavoro**

L'esempio seguente crea una nuova cartella di lavoro da zero, scrive le parole "Hello World!" nella cella A1 del primo foglio di lavoro e salva il file.

**Il foglio di calcolo generato** 

![cose da fare:immagine_alt_testo](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Apertura di un file esistente**

 L'esempio seguente apre un file modello di Microsoft Excel esistente denominato**libro1.xls**, scrive le parole "Hello World!" nella cella A1 nel primo foglio di lavoro e salva la cartella di lavoro come nuovo file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
