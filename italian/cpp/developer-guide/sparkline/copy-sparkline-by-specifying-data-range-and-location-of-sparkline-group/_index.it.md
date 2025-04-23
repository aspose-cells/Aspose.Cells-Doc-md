---
title: Copia Sparkline specificando l intervallo di dati e la posizione del gruppo di Sparkline con C++
linktitle: Copia Sparkline specificando l intervallo di dati e la posizione
type: docs
weight: 300
url: /it/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Impara come copiare sparklines specificando l intervallo di dati e la posizione usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel consente di copiare una linea di tendenza specificando l'intervallo di dati e la posizione di un gruppo di linee di tendenza. Aspose.Cells supporta questa funzionalità

{{% /alert %}}

Per copiare una linea di tendenza in altre celle in Microsoft Excel

1. Selezionare la cella contenente la linea di tendenza
1. Selezionare **Modifica dati** dalla sezione **Linee di tendenza** della scheda **Progettazione**
1. Selezionare **Modifica posizione gruppo e dati**
1. Specificare l'intervallo di dati e la posizione
1. Fai clic su **OK**.

Aspose.Cells fornisce il metodo `SparklineCollection.Add(dataRange, row, column)` per specificare l'intervallo di dati e la posizione di un gruppo di sparklines. Il codice di esempio carica il file Excel di origine come mostrato nello screenshot sopra, quindi accede al primo gruppo di sparklines e aggiunge intervalli di dati e posizioni nel gruppo. Infine, scrive il file Excel di output su disco, visualizzato anche nello screenshot sopra.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
