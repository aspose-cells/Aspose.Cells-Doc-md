---
title: La tua prima applicazione Aspose.Cells  Ciao mondo
type: docs
weight: 30
url: /it/java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

Questo argomento per principianti mostra come gli sviluppatori possono creare una semplice prima applicazione (Ciao mondo) utilizzando la semplice API di Aspose.Cells. L'applicazione crea un file Microsoft Excel con la scritta Ciao mondo in una cella specificata di un foglio di lavoro.

{{% /alert %}}

### **Creazione dell'applicazione Hello World**

Per creare l'applicazione Hello World utilizzando l'API di Aspose.Cells:

1. Creare un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).
1. Applicare la licenza:
   1. Se hai acquistato una licenza, utilizza la licenza nella tua applicazione per accedere a tutte le funzionalità complete di Aspose.Cells
   1. Se stai utilizzando la versione di valutazione del componente (se stai usando Aspose.Cells senza licenza), salta questo passaggio.
1. Creare un nuovo file Microsoft Excel o aprire un file esistente in cui desideri aggiungere/aggiornare del testo.
1. Accedere a qualsiasi cella di un foglio di lavoro nel file Microsoft Excel.
1. Inserisci le parole **Hello World!** in una cella accessibile.
1. Genera il file modificato di Microsoft Excel.

Gli esempi seguenti dimostrano i passaggi sopra indicati.

#### **Creazione di un'organizzazione**

Nell'esempio seguente viene creata una nuova organizzazione da zero, vengono scritte le parole "Ciao mondo!" nella cella A1 del primo foglio di lavoro e il file viene salvato.

**Il foglio di calcolo generato** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Apertura di un file esistente**

Nell'esempio seguente viene aperto un file modello Microsoft Excel esistente chiamato **book1.xls**, si scrive la frase "Ciao Mondo!" nella cella A1 nel primo foglio di lavoro, e si salva il foglio di lavoro come un nuovo file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
{{< app/cells/assistant language="java" >}}
