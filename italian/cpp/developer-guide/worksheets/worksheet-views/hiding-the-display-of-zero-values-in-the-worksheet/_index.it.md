---
title: Nascondere la visualizzazione di valori zero nel foglio di lavoro con C++
linktitle: Nascondere la Visualizzazione dei Valori Zero nel Foglio di Lavoro
type: docs
weight: 50
url: /it/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Questo articolo ti mostrerà un esempio di codice che spiega come nascondere programmaticamente i valori zero in un foglio di calcolo Excel usando la libreria o API C++.
keywords: nascondere i valori zero del foglio di lavoro Excel in C++
---

{{% alert color="primary" %}} 

A volte è necessario nascondere i valori zero in un foglio di calcolo. Potrebbe essere una preferenza personale o uno standard di formattazione.

{{% /alert %}} 

Per nascondere i valori zero in un foglio di lavoro in Microsoft Excel (ad esempio Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**, e quindi selezionare la scheda **Visualizza**.
1. Deselezionare l'opzione **Valori zero**.
1. Fai clic su **OK**.

Si prega di vedere il seguente codice di esempio che dimostra come nascondere gli zeri utilizzando Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
