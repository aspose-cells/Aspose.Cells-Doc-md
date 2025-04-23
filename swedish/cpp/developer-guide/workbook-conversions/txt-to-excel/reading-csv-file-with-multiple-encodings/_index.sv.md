---
title: Läsning av CSV fil med flera kodningar med C++
linktitle: Läsning av CSV fil med flera kodningar
type: docs
weight: 200
url: /sv/cpp/reading-csv-file-with-multiple-encodings/
description: Lär dig hur man läser CSV filer med flera kodningar med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera kodningar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells tillåter dig att ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

Aspose.Cells ger egenskapen [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/), som du behöver ställa in på **true** för att ladda din CSV-fil med flera kodningar korrekt.

Följande skärmbild visar en exempel CSV-fil som innehåller två rader. Den första raden är i **ANSI**-kodning och den andra raden är i **Unicode**-kodning.

|**Ingående fil**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Följande skärmbild visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/)-egenskapen till **true**. Som du ser, tolkades Unicode-texten inte korrekt.

|**Utgående fil 1: ingen anpassning gjord för flera krypteringar**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Följande skärmbild visar XLSX-filen konverterad från ovanstående CSV-fil efter att ha ställt in [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/)-egenskapen till **true**. Som du ser, konverteras Unicode-texten nu på rätt sätt.

|**Utgående fil 2: IsMultiEncoded är satt till true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är det exempelkod som konverterar ovanstående CSV-fil till XLSX-format korrekt.

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

## Relaterade artiklar

- [Öppning av CSV-filer](/cells/sv/cpp/opening-files-with-different-formats/#opening-csv-files)
