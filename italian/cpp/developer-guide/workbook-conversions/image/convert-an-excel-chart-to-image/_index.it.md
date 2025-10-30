---
title: Convertire un grafico Excel in immagine con C++
linktitle: Convertire un grafico Excel in un immagine
type: docs
weight: 20
url: /it/cpp/convert-an-excel-chart-to-image/
description: Impara come convertire i grafici di Excel in immagini usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

I grafici sono visivamente attraenti e rendono facile per gli utenti vedere confronti, modelli e tendenze nei dati. Ad esempio, invece di analizzare colonne di numeri in un foglio di lavoro, un grafico mostra a colpo d'occhio se le vendite stanno diminuendo o aumentando, o come le vendite effettive si confrontano con quelle previste. Le persone vengono spesso invitate a presentare informazioni statistiche e grafiche in modo semplice da capire e facile da mantenere. Un'immagine aiuta.

A volte, i grafici sono necessari in un'applicazione o pagine web. Oppure potrebbero essere richiesti per un documento Word, un file PDF, una presentazione PowerPoint o qualche altra applicazione. In ogni caso, si desidera rendere il grafico come immagine affinché possa essere utilizzato altrove.

{{% /alert %}}

## **Conversione di grafici in immagini**

Negli esempi qui, un grafico a torta e un grafico a colonne vengono convertiti in immagini.

### **Conversione di un grafico a torta in un file immagine**

Innanzitutto, creare un grafico a torta in Microsoft Excel e quindi convertirlo in un file immagine con Aspose.Cells. Il codice in questo esempio crea un'immagine EMF basata sul grafico a torta nel file di modello di Microsoft Excel.

|**Output: immagine grafico a torta**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Crea un grafico a torta in Microsoft Excel:
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.
   1. Inserisci alcuni dati in un foglio di lavoro.
   1. Crea un grafico a torta in base ai dati.
   1. Salvare il file.

|**Il file di input.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. Installalo sul tuo computer di sviluppo.

Tutti i [componenti Aspose](http://www.aspose.com/) funzionano in modalità di valutazione quando vengono installati per la prima volta. La modalità di valutazione non ha limiti temporali e inserisce solo filigrane nei documenti di output.

1. Crea un progetto:
   1. Avvia il tuo ambiente di sviluppo C++ (ad esempio, Visual Studio).
   1. Crea una nuova applicazione console.
   1. Aggiungi un riferimento ad Aspose.Cells. Questo progetto utilizza Aspose.Cells, quindi aggiungi un riferimento alla libreria Aspose.Cells.
   1. Scrivi il codice che trova e converte il grafico. Qui di seguito c'è il codice utilizzato dal componente per completare il compito. Vengono utilizzate pochissime righe di codice.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Conversione di un grafico a colonne in un file immagine**

Per prima cosa, crea un grafico a colonne in Microsoft Excel e convertilo in un file immagine, come sopra. Dopo aver eseguito il codice di esempio, viene creato un file JPEG basato sul grafico a colonne nel file Excel di modello.

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

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
