---
title: Applica una formattazione condizionale avanzata con C++
linktitle: Applicare la formattazione condizionale avanzata
description: Come usare la libreria Aspose.Cells in C++ per applicare una formattazione condizionale avanzata. Modificando questi criteri, hai un maggiore controllo sull aspetto e la presentazione delle celle.
keywords: Aspose.Cells, Formattazione Condizionale Avanzata, C++, Condizionale, Formattazione
type: docs
weight: 70
url: /it/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 e versioni successive (2010/2013/2016) fornisce alcune funzionalità avanzate per la formattazione condizionale. Ad esempio, consente di applicare sfumature di celle, bordi, icone colorate, frecce, bandiere e formattazione del testo, ecc. che è diventata piuttosto sofisticata.

{{% /alert %}}

## **Applicare la formattazione condizionale avanzata ai file Microsoft Excel**
La formattazione condizionale può:

- Aggiungere barre di dati sfumate per migliorare graficamente i numeri sottostanti incorporando un semplice grafico a barre nelle celle.
- Sfumare automaticamente le celle con scale di colori in base alla loro relazione con i valori in altre celle nel range. Le impostazioni predefinite sfumano il valore più basso in rosso fino al valore più alto in verde.
- Usare set di icone in modo simile alle scale di colori, ma anziché sfumare le celle aggiunge piccole icone, come frecce e semafori, alle celle.

Aspose.Cells supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle in fase di esecuzione. Questo esempio dimostra un esercizio per tipi avanzati di formattazione condizionale, tra cui IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom e altre regole con diversi insiemi di attributi.

### **Calcola il colore scelto da Microsoft Excel per la formattazione condizionale delle scale di colore**
Aspose.Cells ti permette di calcolare il colore selezionato da Microsoft Excel quando viene utilizzata la formattazione condizionale delle scale di colore in un file modello. Vedere il codice di esempio di seguito per imparare come calcolare il colore selezionato da Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
