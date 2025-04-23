---
title: Convertire un grafico Excel in un immagine
type: docs
weight: 20
url: /it/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

I grafici sono visivamente accattivanti e facilitano la visualizzazione di confronti, modelli e tendenze nei dati. Ad esempio, anziché analizzare colonne di numeri di fogli di lavoro, un grafico mostra in un colpo d'occhio se le vendite stanno aumentando o diminuendo, o come le vendite effettive si confrontano con le vendite previste. Spesso viene chiesto alle persone di presentare informazioni statistiche e grafiche in modo semplice da capire e da mantenere. Un'immagine aiuta.

A volte, sono necessari grafici in un'applicazione o pagine web. Oppure potrebbe essere necessario per un documento Word, un file PDF, una presentazione PowerPoint o un'altra applicazione. In ciascuno di questi casi, si desidera rendere il grafico come un'immagine in modo da poterlo utilizzare altrove.

{{% /alert %}}

## **Conversione di grafici in immagini**

Negli esempi qui, un grafico a torta e un grafico a colonne vengono convertiti in immagini.

### **Conversione di un grafico a torta in un file immagine**

Innanzitutto, creare un grafico a torta in Microsoft Excel e quindi convertirlo in un file immagine con Aspose.Cells. Il codice in questo esempio crea un'immagine EMF basata sul grafico a torta nel file di modello di Microsoft Excel.

|**Output: immagine grafico a torta**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Creare un grafico a torta in Microsoft Excel :
   1. Aperto un nuovo foglio di lavoro in Microsoft Excel.
   1. Inserisci alcuni dati in un foglio di lavoro.
   1. Creato un grafico a torta basato sui dati.
   1. Salvare il file.

|**Il file di input.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Installalo sul tuo computer di sviluppo.

Tutti i [componenti Aspose](http://www.aspose.com/) funzionano in modalità di valutazione quando vengono installati per la prima volta. La modalità di valutazione non ha limiti temporali e inserisce solo filigrane nei documenti di output.

1. Crea un progetto:
   1. Avviare Visual Studio.Net.
   1. Creare una nuova applicazione console. Questo esempio utilizza un'applicazione console C#, ma è possibile utilizzare anche VB.NET.
   1. Aggiungi un riferimento. Questo progetto utilizza Aspose.Cells, quindi aggiungi un riferimento a Aspose.Cells, ad esempio ...\Programmi\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
   1. Scrivi il codice che trova e converte il grafico. Qui di seguito c'è il codice utilizzato dal componente per completare il compito. Vengono utilizzate pochissime righe di codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Conversione di un grafico a colonne in un file immagine**

Prima crea un grafico a colonne in Microsoft Excel e convertilo in un file immagine, come sopra. Dopo l'esecuzione del codice di esempio, viene creato un file JPEG basato sul grafico a colonne nel file modello di Excel.

|**File di output: un'immagine del grafico a colonne.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Creare un grafico a colonne in Microsoft Excel:
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.
   1. Inserisci alcuni dati in un foglio di lavoro.
   1. Crea un grafico a colonne basato sui dati.
   1. Salvare il file.

|**File di input.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Impostare un progetto, con riferimenti, come descritto sopra.
1. Convertire il grafico in un'immagine in modo dinamico. Di seguito è riportato il codice utilizzato dal componente per portare a termine il compito. Il codice è simile a quello precedente:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
