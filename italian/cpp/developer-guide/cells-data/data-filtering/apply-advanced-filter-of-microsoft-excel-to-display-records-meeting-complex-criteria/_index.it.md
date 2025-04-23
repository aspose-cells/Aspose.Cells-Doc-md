---
title: Applica il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi con C++
linktitle: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs
weight: 280
url: /it/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Impara come applicare il filtro avanzato di Microsoft Excel per visualizzare record che soddisfano criteri complessi usando l API Aspose.Cells for C++.
keywords: Applica Filtro Avanzato, Imposta Filtro Avanzato, Aggiungi Filtro Avanzato, Crea Filtro Avanzato, Come aggiungere Filtro Avanzato a un intervallo
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel ti permette di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. Puoi applicare il filtro avanzato con Microsoft Excel tramite il comando *Dati > Avanzate* come mostrato in questo screenshot.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells consente anche di applicare il filtro avanzato usando il metodo [**GetAdvancedFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getadvancedfilter/). Come Microsoft Excel, accetta i seguenti parametri.

**isFilter**

Indica se filtrare l'elenco sul posto.

**listRange**

L'intervallo dell'elenco.

**criteriaRange**

L'intervallo dei criteri.

**copyTo**

L'intervallo in cui copiare i dati.

**uniqueRecordOnly**

Mostra o copia solo le righe uniche.

## **Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi**

Il seguente esempio di codice applica il filtro avanzato sul [File Excel di esempio](48496692.xlsx) e genera il [File Excel di output](48496691.xlsx). Lo screenshot mostra entrambi i file per confronto. Come si può vedere nello screenshot, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook
    Workbook workbook(sourceDir + u"sampleAdvancedFilter.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Apply advanced filter on range A5:D19 and criteria range is A1:D2
    // Besides, we want to filter in place
    // And, we want all filtered records not just unique records
    ws.Advanced_Filter(true, u"A5:D19", u"A1:D2", u"", false);

    // Save the workbook in xlsx format
    workbook.Save(outputDir + u"outputAdvancedFilter.xlsx", SaveFormat::Xlsx);

    std::cout << "Advanced filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
