---
title: Lettura di file CSV con più encodings con C++
linktitle: Lettura di file CSV con codifiche multiple
type: docs
weight: 200
url: /it/cpp/reading-csv-file-with-multiple-encodings/
description: Impara come leggere file CSV con più encodings usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte, il tuo file CSV contiene più encodings (Unicode, ANSI, UTF8, UTF7, ecc). Aspose.Cells ti permette di caricare tali file CSV e convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/), che devi impostare su **true** per caricare correttamente il tuo file CSV con più encodings.

Lo screenshot seguente mostra un esempio di file CSV che contiene due righe. La prima riga è codificata in **ANSI** e la seconda riga in **Unicode**.

|**File di input**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Lo screenshot seguente mostra il file XLSX convertito dal file CSV sopra senza impostare la proprietà [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) su **true**. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna modifica per la codifica multipla**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Lo screenshot seguente mostra il file XLSX convertito dal file CSV sopra dopo aver impostato la proprietà [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) su **true**. Come puoi vedere, il testo Unicode ora è stato convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte il precedente file CSV nel formato XLSX correttamente.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articoli correlati

- [Apertura dei file CSV](/cells/it/cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="cpp" >}}
