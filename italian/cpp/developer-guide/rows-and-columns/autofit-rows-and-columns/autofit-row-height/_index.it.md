---
title: Adatta automaticamente l altezza delle righe durante il caricamento del file con C++
linktitle: Adattamento automatico dell altezza della riga in modo automatico durante il caricamento del file
type: docs
weight: 120
url: /it/cpp/autofit-row-height/
description: Impara come adattare le righe con altezza non personalizzata usando Aspose.Cells con C++.
keywords: Adattamento automatico dell altezza della riga durante il caricamento del file, regola automaticamente l altezza della riga all apertura del file di Excel.
---

## **Possibili Scenari di Utilizzo**
L'altezza della riga si adatta automaticamente al font del contenuto, ma quando l'altezza della riga memorizzata non corrisponde all'altezza del contenuto nel file, MS Excel regola automaticamente l'altezza della riga durante il caricamento del file, mentre Aspose.Cells non la regola automaticamente per migliorare le prestazioni. Se hai bisogno di usare il programma Aspose.Cells per adattare automaticamente le altezze delle linee durante il caricamento dei file, puoi ottenere questo obiettivo tramite il parametro [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Si prega di fare riferimento ai seguenti dati dell'immagine. Possiamo osservare che l'altezza della riga memorizzata nella riga 11 è 15, ma Excel ha regolato automaticamente l'altezza della riga durante il caricamento del file.
<br>
<img src="1.png" width=70% />

## **Regolare l'altezza della riga utilizzando Aspose.Cells**
Se carichi direttamente il file e lo salvi in PDF, i dati non verranno completamente visualizzati in PDF perché l'altezza della riga della cache è solo 15.
<br>
<img src="2.png" width=70% />
<br>
Se imposti il parametro [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) su true durante il caricamento del file, Aspose.Cells regolerà automaticamente l'altezza della riga. L'altezza della linea regolata può soddisfare efficacemente i requisiti di visualizzazione del testo.
<br>
<img src="3.png" width=70% />

## **Codice di esempio C++**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
