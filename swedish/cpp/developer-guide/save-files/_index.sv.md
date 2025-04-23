---
title: Olika sätt att spara filer med C++
linktitle: Spara filer
type: docs
weight: 40
url: /sv/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ kan spara filer i olika format. Spara filer som PDF. Spara filer som HTML. Spara filer som DOCX. Spara filer som PPTX. Spara filer som JSON. Spara filer som MHTML.
keywords: Aspose.Cells sparar Excel till PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML och liknande med C++, spara eller konvertera arbetsbok till PDF, HTML, JSON, TXT, SQL i C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att skapa och spara filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}}

## **Olika sätt att spara filer**

Aspose.Cells tillhandahåller [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil och tillhandahåller de egenskaper och metoder som krävs för att arbeta med Excel-filer. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) tillhandahåller metoden [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) som används för att spara Excel-filer. Metoden [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) har många överbelastningar som används för att spara filer på olika sätt.

Filen format som filen sparas till bestäms av [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) uppräkningen

|**Filtyp**|**Beskrivning**|
| :- | :- |
|CSV|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007 XLSX-fil|
|Xlsm|Representerar en Excel 2007 XLSM-fil|
|Xltx|Representerar en Excel 2007-mall XLTX-fil|
|Xltm|Representerar en Excel 2007 med makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007 binär XLSB-fil|
|SpreadsheetML|Representerar en kalkyl XML-fil|
|TSV|Representerar en tab-separated values-fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|ODS|Representerar en ODS-fil|
|Html|Representerar HTML-fil(er)|
|MHtml|Representerar MHTML-fil(er)|
|Pdf|Representerar en PDF-fil|
|XPS|Representerar ett XPS-dokument|
|TIFF|Representerar Tagged Image File Format (TIFF)|

## **Så här sparar du filen i olika format**

För att spara filer till en lagringsplats, ange filnamnet (komplett med lagringsväg) och önskat filformat (från [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) uppräkningen) vid anrop av [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektets [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod.

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

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Så här sparar du arbetsbok till Pdf**
Portable Document Format (PDF) är en typ av dokument som skapades av Adobe på 1990-talet. Syftet med detta filformat var att införa en standard för representation av dokument och annat referensmaterial i ett format som är oberoende av applikationsprogramvara, hårdvara samt operativsystem. PDF-filformatet har full kapacitet att innehålla information som text, bilder, hyperlänkar, formulärfält, rika medier, digitala signaturer, bilagor, metadata, geospatiala funktioner och 3D-objekt som kan bli en del av käll-dokumentet.

Följande koder visar hur man sparar arbetsbok som Pdf-fil med Aspose.Cells:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Så här sparar du arbetsboken till Text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil till CSV. Som standard är [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) komma, så specificera inte en separator om du sparar i CSV-format. Observera: Om du använder utvärderingsversionen och till och med egenskapen [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) är inställd på true, kommer programmet fortfarande bara att exportera ett kalkylblad.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Så här sparar du filen till textfiler med anpassad avskiljare**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Så här sparar du filen till en ström**

För att spara filer till en ström, skapa en *MemoryStream* eller *FileStream* objekt och spara filen till det strömobjektet genom att anropa [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektets [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metod. Ange önskat filformat med hjälp av [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) uppräkningen vid anrop av [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)metoden.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **Så här sparar du Excel-filen till HTML- och MHT-filer**
Aspose.Cells kan enkelt spara en Excel-fil, JSON, CSV eller andra filer som kan laddas av Aspose.Cells som .html och .mht-filer.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Så här sparar du Excel-filen till OpenOffice (ODS, SXC, FODS, OTS)**
Vi kan spara filerna i öppet offce-format: ODS, SXC, FODS, OTS osv.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Så här sparar du Excel-filen till JSON eller XML**

JSON (JavaScript Object Notation) är ett öppet standardfilformat för att dela data som använder mänskligt läsbar text för att lagra och överföra data. JSON-filer lagras med filändelsen .json. JSON kräver mindre formatering och är ett bra alternativ till XML. JSON härstammar från JavaScript men är ett språkoberoende dataformat. Generering och tolkning av JSON stöds av många moderna programmeringsspråk. application/json är mediatypen som används för JSON.

Aspose.Cells stöder att spara filer i JSON eller XML.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Fortsatta ämnen**
- [Justera arbetsbokens kompressionsnivå](/cells/sv/cpp/adjust-workbook-compression-level/)
- [Spara arbetsbok i strikt öppet XML-kalkylbladsformat](/cells/sv/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Spara fil till responsobjekt](/cells/sv/cpp/saving-file-to-response-object/)
