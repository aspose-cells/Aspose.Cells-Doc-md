---
title: Konvertera Excel till CSV, TSV och Txt med C++
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/cpp/convert-excel-to-csv-tsv-and-txt/
description: Konvertera enkelt Excel filer till CSV , TSV och TXT format med Aspose.Cells med C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att konvertera Excel, ODS, JSON och andra formatfiler till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil som CSV. Som standard är [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) ett komma, så specificera inte en separator om du sparar till CSV-format.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="cpp" >}}
