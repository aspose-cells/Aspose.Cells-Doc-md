---
title: Applica la Formattazione Condizionale nei fogli di lavoro con C++
linktitle: Applica la Formattazione Condizionale
description: Come usare la libreria Aspose.Cells in C++ per applicare la formattazione condizionale nei fogli di lavoro. Modificando questi criteri, hai un maggiore controllo sull aspetto delle celle.
keywords: Aspose.Cells, Formattazione Condizionale, C++, Foglio di lavoro, Formattazione
type: docs
weight: 130
url: /it/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Questo articolo è progettato per fornire una comprensione dettagliata di come aggiungere la formattazione condizionale a un intervallo di celle in un foglio di lavoro.

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a un intervallo di celle e di far sì che la formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, lo sfondo di una cella può essere rosso per evidenziare un valore negativo, o il colore del testo potrebbe essere verde per un valore positivo. Quando il valore della cella soddisfa la condizione di formattazione, la formattazione viene applicata. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella.

È possibile applicare la formattazione condizionale con la Automazione di Office di Microsoft ma ciò comporta alcuni svantaggi. Sono coinvolte diverse ragioni e problemi: ad esempio, sicurezza, stabilità, scalabilità e velocità. Il motivo principale per trovare un'altra soluzione è che Microsoft stessa sconsiglia vivamente l'Automazione di Office per le soluzioni software.

Questo articolo mostra come creare un'applicazione console, aggiungere la formattazione condizionale alle celle con poche semplici righe di codice utilizzando l'API di Aspose.Cells.

{{% /alert %}}

## **Utilizzare Aspose.Cells per Applicare la Formattazione Condizionale in Base al Valore della Cella**

1. **Scarica e installa Aspose.Cells**.
   1. Scarica Aspose.Cells for C++.
1. Installalo sul tuo computer di sviluppo.
   Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. **Crea un progetto**.
   Avvia il tuo ambiente di sviluppo C++ e crea una nuova applicazione console.
1. **Aggiungi riferimenti**.
   Aggiungi un riferimento a Aspose.Cells al tuo progetto, ad esempio aggiungi un riferimento a ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. **Applicare formattazione condizionale basata sul valore della cella**.
   Di seguito il codice usato per completare il compito. Applica la formattazione condizionale a una cella.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Quando viene eseguito il codice sopra, viene applicata una formattazione condizionale alla cella "A1" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata ad A1 dipende dal valore della cella. Se il valore di A1 è tra 50 e 100, lo sfondo diventa rosso grazie alla formattazione condizionale applicata.

## **Utilizzare Aspose.Cells per Applicare la Formattazione Condizionale in Base a una Formula**

1. **Applicare la formattazione condizionale in base a una formula (segmento di codice)**
   Di seguito è riportato il codice per completare il compito. Si applica la formattazione condizionale su B3.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Quando viene eseguito il codice sopra, la formattazione condizionale viene applicata alla cella "B3" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale dipende dalla formula che calcola il valore di "B3" come somma di B1 e B2.
{{< app/cells/assistant language="cpp" >}}
