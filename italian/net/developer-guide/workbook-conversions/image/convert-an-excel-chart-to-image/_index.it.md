---
title: Converti un grafico Excel in immagine
type: docs
weight: 20
url: /it/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

I grafici sono visivamente accattivanti e consentono agli utenti di vedere facilmente confronti, modelli e tendenze nei dati. Ad esempio, anziché analizzare le colonne dei numeri del foglio di lavoro, un grafico mostra a colpo d'occhio se le vendite sono in calo o in aumento o il confronto tra le vendite effettive e quelle previste. Alle persone viene spesso chiesto di presentare informazioni statistiche e grafiche in modo facile da capire e da mantenere. Una foto aiuta.

A volte, i grafici sono necessari in un'applicazione o nelle pagine web. Oppure potrebbe essere necessario per un documento Word, un file PDF, una presentazione PowerPoint o qualche altra applicazione. In ogni caso, si desidera eseguire il rendering del grafico come immagine in modo da poterlo utilizzare altrove.

{{% /alert %}}

## **Conversione di grafici in immagini**

Negli esempi qui riportati, un grafico a torta e un carattere di colonna vengono convertiti in immagini.

### **Conversione di un grafico a torta in un file immagine**

Innanzitutto, crea un grafico a torta in Excel Microsoft e quindi convertilo in un file immagine con Aspose.Cells. Il codice in questo esempio crea un'immagine EMF basata sul grafico a torta nel file Excel modello Microsoft.

|**Output: immagine del grafico a torta**|
|:- |
|![cose da fare:immagine_alt_testo](convert-an-excel-chart-to-image_1.png)|

1. Crea un grafico a torta in Microsoft Excel:
 1. Ha aperto una nuova cartella di lavoro in Microsoft Excel.
 1. Inserisci alcuni dati in un foglio di lavoro.
 1. Creato un grafico a torta basato sui dati.
 1. Salva il file.

|**Il file di input.**|
|:- |
|![cose da fare:immagine_alt_testo](convert-an-excel-chart-to-image_2.png)|

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Installalo sul tuo computer di sviluppo.

 Tutto[Aspose](http://www.aspose.com/) i componenti funzionano in modalità di valutazione quando vengono installati per la prima volta. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti di output.

1. Crea un progetto:
 1. Avviare Visual Studio.Net.
 1. Creare una nuova applicazione console. Questo esempio utilizza un'applicazione console C#, ma è possibile utilizzare anche VB.NET.
 1. Aggiungi un riferimento. Questo progetto utilizza Aspose.Cells, quindi aggiungi un riferimento a Aspose.Cells, ad esempio ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Scrivi il codice che trova e converte il grafico. Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. Vengono utilizzate pochissime righe di codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Conversione di un istogramma in un file immagine**

Per prima cosa crea un istogramma in Microsoft Excel e convertilo in un file immagine, come sopra. Dopo aver eseguito il codice di esempio, viene creato un file JPEG basato sull'istogramma nel file Excel modello.

|**File di output: un'immagine del grafico a colonne.**|
|:- |
|![cose da fare:immagine_alt_testo](convert-an-excel-chart-to-image_3.png)|

1. Crea un istogramma in Microsoft Excel:
 1. Apri una nuova cartella di lavoro in Microsoft Excel.
 1. Inserisci alcuni dati in un foglio di lavoro.
 1. Creare un istogramma basato sui dati.
 1. Salva il file.

|**File di input.**|
|:- |
|![cose da fare:immagine_alt_testo](convert-an-excel-chart-to-image_4.png)|

1. Impostare un progetto, con riferimenti, come descritto sopra.
1. Converti dinamicamente il grafico in un'immagine. Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. Il codice è simile al precedente:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
