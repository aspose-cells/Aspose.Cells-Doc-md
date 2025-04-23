---
title: Implementa il sistema di data 1904 con C++
linktitle: Implementa il sistema della data 1904
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Supporta l’implementazione del sistema di data 1904, consentendo agli utenti di calcolare e formattare basandosi sul sistema di data del 1 gennaio 1904. Questo articolo descrive come implementare il sistema di data 1904 usando la libreria Aspose.Cells.
keywords: Aspose.Cells, sistema della data 1904, foglio di calcolo, calcolo, formattazione
type: docs
weight: 7000
url: /it/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel supporta due sistemi di data: sistema della data 1900 (il sistema di data predefinito implementato in Excel per Windows) e sistema della data 1904. Il sistema della data 1904 è normalmente utilizzato per garantire la compatibilità con i file di Excel per Macintosh ed è il sistema predefinito se si utilizza Excel per Macintosh. È possibile impostare il sistema della data 1904 per i file di Excel utilizzando Aspose.Cells.

{{% /alert %}}

Per implementare il sistema della data 1904 in Microsoft Excel (ad esempio Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**, e selezionare la scheda **Calcolo**.
1. Selezionare l'opzione **sistema di data del 1904**.
1. Fai clic su **OK**.

|**Selezione del sistema di data del 1904 in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Vedere il seguente codice di esempio su come realizzare questo utilizzando le API di Aspose.Cells.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
