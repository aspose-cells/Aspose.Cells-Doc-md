---
title: Filtra il progetto VBA durante il caricamento di un workbook con C++
linktitle: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 140
url: /it/cpp/filter-vba-project-while-loading-a-workbook/
description: Impara come filtrare i progetti VBA durante il caricamento di un file Excel usando Aspose.Cells con C++.
---

## **Filtra il progetto VBA durante il caricamento di un file Excel in C++**

Alcuni file .xlsm/.xslb contengono un numero estremamente elevato di macro (o macro molto, molto lunghe). Aspose.Cells caricherà incondizionatamente questi dati durante l'apertura di tali workbook. Potrebbe essere necessario controllare questo tramite [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) quando si desidera estrarre solo i nomi dei fogli da un gran numero di workbook, ignorando contenuti non necessari. Questo filtro viene fornito introducendo una nuova opzione, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **Codice di Esempio**

Il seguente codice di esempio carica un documento di lavoro in modo che solo il VBA venga filtrato. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
